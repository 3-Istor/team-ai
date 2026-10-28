# Security pass (high tier)

Check each item against the diff. Report only what you can point to in the
code; a checklist item is not a finding by itself.

- **Access control.** Who can call this? Is ownership checked server-side, on
  every path (list, read, update, delete, export)?
- **Injection.** User input reaching SQL, shell, templates, file paths,
  regexes or URLs without parameterising or validating.
- **Server-side requests.** URLs built from input (SSRF), redirects to
  arbitrary hosts.
- **Secrets.** Keys, tokens or passwords in code, config, logs, error messages
  or test fixtures. New env vars documented in `.env.example`, never with a
  real value.
- **Data exposure.** Personal data in logs, responses returning more fields
  than needed, debug endpoints left on.
- **Dependencies.** New packages: maintained, expected name (typosquatting),
  pinned version.
- **CI and infra.** Workflows triggered by untrusted PRs with secrets
  (`pull_request_target`), unpinned third-party actions, widened IAM or
  network rules, public buckets.
- **AI features.** Text the app reads (user input, documents, web pages, tool
  output) treated as instructions; a model with private data, untrusted input
  and an outbound channel at once.
