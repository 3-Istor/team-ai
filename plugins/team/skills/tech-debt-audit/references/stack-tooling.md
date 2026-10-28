# Stack-specific tooling

Detect the stack from the manifest and run the relevant tools. Run them in parallel when possible.

- **TypeScript / JavaScript** — `npm audit`, `npx knip` (dead exports), `npx madge --circular` (circular deps), `npx depcheck` (unused deps), `tsc --noEmit` for type drift.
- **Python** — `pip-audit`, `ruff check`, `vulture` (dead code), `pydeps --show-cycles`, `mypy --strict` for type drift.
- **Rust** — `cargo audit`, `cargo udeps`, `cargo machete`, `cargo clippy -- -W clippy::pedantic`.
- **Go** — `govulncheck`, `go vet`, `staticcheck`, `golangci-lint run`.

If a tool isn't installed, note it in the audit and move on rather than blocking. Do not install dev tools globally without permission.
