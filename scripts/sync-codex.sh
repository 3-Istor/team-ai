#!/usr/bin/env bash
# Expose team-ai skills to Codex (and any agent that reads .agents/skills).
#
# Usage:
#   scripts/sync-codex.sh                 # links into ~/.agents/skills
#   scripts/sync-codex.sh path/to/project # links into that project's .agents/skills
#   scripts/sync-codex.sh --copy [target] # copies instead of linking (CI, Windows)
#
# Re-run after `git pull` to pick up new skills. Existing entries with the same
# name are replaced only if they are links or copies made by this script.
set -euo pipefail

mode=link
if [[ "${1:-}" == "--copy" ]]; then
  mode=copy
  shift
fi

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [[ $# -ge 1 ]]; then
  target="$(cd "$1" && pwd)/.agents/skills"
else
  target="${HOME}/.agents/skills"
fi
mkdir -p "$target"

count=0
for skill in "$repo_root"/plugins/*/skills/*/; do
  [[ -f "$skill/SKILL.md" ]] || continue
  name="$(basename "$skill")"
  dest="$target/$name"
  if [[ -e "$dest" || -L "$dest" ]]; then
    if [[ -L "$dest" || -f "$dest/.team-ai" ]]; then
      rm -rf "$dest"
    else
      echo "skip  $name: $dest exists and was not made by this script" >&2
      continue
    fi
  fi
  if [[ "$mode" == link ]]; then
    ln -s "${skill%/}" "$dest"
  else
    cp -R "${skill%/}" "$dest"
    touch "$dest/.team-ai"
  fi
  echo "$mode  $name -> $dest"
  count=$((count + 1))
done
echo "$count skills synced into $target"
