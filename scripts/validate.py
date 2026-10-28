#!/usr/bin/env python3
"""Validate the team-ai marketplace: manifests, skills and the catalog.

Exit code 0 when everything is valid, 1 when at least one error is found.
Warnings never fail the run.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
MAX_DESCRIPTION = 1024
SOFT_MAX_BODY_LINES = 150
HARD_MAX_BODY_LINES = 500
# Skills never depend on each other, so a file two skills need is copied into
# both; each group here must stay byte-identical.
SHARED_COPIES = [
    [
        "plugins/team/skills/deck/references/tokens.md",
        "plugins/team/skills/design-web/references/tokens.md",
    ],
]

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        err(f"{path.relative_to(ROOT)}: missing")
    except json.JSONDecodeError as exc:
        err(f"{path.relative_to(ROOT)}: invalid JSON ({exc})")
    return None


def parse_front_matter(text: str) -> tuple[dict[str, str], str] | None:
    """Return (fields, body) for a '---' delimited front matter, else None.

    Only flat `key: value` pairs are read; that is all SKILL.md needs.
    """
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith((" ", "\t", "#")):
            continue
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().strip('"').strip("'")
    body = text[end + 4 :].lstrip("\n")
    return fields, body


def check_skill(skill_dir: Path) -> str | None:
    rel = skill_dir.relative_to(ROOT)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        err(f"{rel}: no SKILL.md")
        return None
    parsed = parse_front_matter(skill_md.read_text(encoding="utf-8"))
    if parsed is None:
        err(f"{rel}/SKILL.md: missing '---' front matter")
        return None
    fields, body = parsed

    name = fields.get("name", "")
    if not name:
        err(f"{rel}/SKILL.md: front matter has no 'name'")
    elif name != skill_dir.name:
        err(f"{rel}/SKILL.md: name '{name}' differs from folder '{skill_dir.name}'")
    elif not NAME_RE.match(name) or len(name) > 64:
        err(f"{rel}/SKILL.md: name '{name}' must be lowercase words joined by '-', 64 chars max")

    description = fields.get("description", "")
    if not description:
        err(f"{rel}/SKILL.md: front matter has no 'description'")
    elif len(description) > MAX_DESCRIPTION:
        err(f"{rel}/SKILL.md: description is {len(description)} chars (max {MAX_DESCRIPTION})")
    elif "use when" not in description.lower() and "use it when" not in description.lower():
        warn(f"{rel}/SKILL.md: description does not say when to use the skill ('Use when …')")

    lines = body.count("\n") + 1
    if lines > HARD_MAX_BODY_LINES:
        err(f"{rel}/SKILL.md: body is {lines} lines (max {HARD_MAX_BODY_LINES}); move detail to references/")
    elif lines > SOFT_MAX_BODY_LINES:
        warn(f"{rel}/SKILL.md: body is {lines} lines (aim for {SOFT_MAX_BODY_LINES}); consider references/")

    for target in LINK_RE.findall(body):
        if "://" in target or target.startswith("mailto:"):
            continue
        if not (skill_dir / target).exists():
            err(f"{rel}/SKILL.md: link to '{target}' but the file does not exist")
    return name or skill_dir.name


def check_plugin(entry: dict, index: int) -> list[str]:
    source = entry.get("source")
    name = entry.get("name", f"plugins[{index}]")
    if not isinstance(source, str):
        return []  # remote source: checked when installed
    if ".." in source:
        err(f"marketplace plugin '{name}': source must not contain '..'")
        return []
    plugin_dir = (ROOT / source).resolve()
    if not plugin_dir.is_dir():
        err(f"marketplace plugin '{name}': source {source} does not exist")
        return []
    manifest = load_json(plugin_dir / ".claude-plugin" / "plugin.json")
    if manifest and manifest.get("name") != name:
        err(f"marketplace plugin '{name}': plugin.json name is '{manifest.get('name')}' (must match)")
    skills = []
    skills_dir = plugin_dir / "skills"
    if skills_dir.is_dir():
        for skill_dir in sorted(p for p in skills_dir.iterdir() if p.is_dir()):
            skill = check_skill(skill_dir)
            if skill:
                skills.append(skill)
    return skills


def main() -> int:
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    all_skills: list[str] = []
    if marketplace:
        for key in ("name", "owner", "plugins"):
            if key not in marketplace:
                err(f"marketplace.json: missing '{key}'")
        names = [p.get("name") for p in marketplace.get("plugins", [])]
        if len(names) != len(set(names)):
            err("marketplace.json: two plugins share a name")
        for i, entry in enumerate(marketplace.get("plugins", [])):
            for key in ("name", "source"):
                if key not in entry:
                    err(f"marketplace.json plugins[{i}]: missing '{key}'")
            all_skills += check_plugin(entry, i)

    dupes = {s for s in all_skills if all_skills.count(s) > 1}
    for skill in sorted(dupes):
        err(f"skill name '{skill}' is used by more than one plugin")

    catalog = ROOT / "CATALOG.md"
    catalog_text = catalog.read_text(encoding="utf-8") if catalog.is_file() else ""
    if not catalog_text:
        err("CATALOG.md: missing")
    for skill in all_skills:
        if f"`{skill}`" not in catalog_text:
            err(f"CATALOG.md: skill '{skill}' is not listed (add a row with `{skill}`)")

    for group in SHARED_COPIES:
        contents = {path: (ROOT / path).read_bytes() for path in group if (ROOT / path).is_file()}
        missing = [path for path in group if path not in contents]
        for path in missing:
            err(f"{path}: missing (shared copy of {group[0]})")
        if len(set(contents.values())) > 1:
            err(f"shared copies differ, keep them identical: {', '.join(group)}")

    for msg in warnings:
        print(f"warning: {msg}")
    for msg in errors:
        print(f"error: {msg}")
    print(f"{len(all_skills)} skills checked · {len(errors)} errors · {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
