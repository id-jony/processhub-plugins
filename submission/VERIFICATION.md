# Verification — 2026-09-19

## Completed

- Codex 0.153.4: local marketplace and plugin installation in a clean temporary profile.
- Codex 0.153.4: public GitHub marketplace and plugin installation in a second clean profile.
- Claude Code 2.1.228: strict plugin and marketplace validation; local marketplace and
  plugin installation in a clean temporary profile.
- Codex plugin schema validator and all three skill validators passed.
- Dependency-free release checks passed: both OAuth configurations, mirrored skills,
  icon assets, marketplace paths and five positive / three negative reviewer cases.
- Public ProcessHub OAuth discovery advertises issuer-bound authorization responses,
  ProcessHub scopes, and no dynamic client registration.
- Application regressions: 47 tests passed, including callback host/path restrictions,
  default client upgrade without key rotation, custom allowlist preservation, public legal
  routes and consent UI. TypeScript and targeted ESLint passed.
- Legal pages rendered in a browser at desktop and phone widths, without a session.

## Still requires a live product test

- Complete OAuth from the installed plugin, read a synthetic task, propose a report and
  approve it inside ProcessHub in each target product after deploying the new server client.
- Execute all eight reviewer scenarios with synthetic fixtures and record results.
- Claude web connector and Cowork are separate targets; Claude CLI installation does not
  establish their OAuth compatibility. The owner will test Claude authorization.
- Publisher/legal review, domain verification, private reviewer access and portal submission.

This record does not claim a vendor listing is approved or that unexecuted end-to-end
scenarios passed. No production credentials or customer fixtures are included.

## Registration regression - 2026-09-20

Server v0.5.35 passed 28 focused tests, including HTTP authorization with an old
allowlist and both native callback hosts, custom metadata preservation, unchanged
persistent keys and explicit disable. Production health confirmed v0.5.35 on
2026-09-20. Authorization-start probes for Claude Code (localhost and 127.0.0.1)
and Codex each returned HTTP 303 to the ProcessHub consent page; invalid_client
was absent. Public legal pages were verified without a session on 2026-09-19.
Full user OAuth and report approval remain separate from this unauthenticated
authorization-start check and have not been newly claimed as completed.

## Context tools - 2026-09-20

Local server regression: 142 Connect tests passed, including cross-project filters,
canonical and legacy assignments, timezone-aware deadline bounds, text/comment paging,
related-task scope, context consent and revocation during file extraction. Existing
grants do not gain tasks:context:read automatically. The consent UI was inspected
in the local browser with synthetic fixtures. Full installed-plugin OAuth and human
report approval remain unverified; these tests do not imply marketplace approval.

## Direct writes (server v0.5.37)

The new write-consent profile executes tasks and reports directly, with no ProcessHub
approval hop. Legacy report grants retain their original approval semantics. Packages
now include task-changes; installed-client OAuth and human review scenarios must be
rerun against this release before marketplace submission. Repository validators and
local synthetic tests do not certify a full Codex/Claude client session.
