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
- Verify public legal URLs and the new Claude Code client after the application deploy.
- Publisher/legal review, domain verification, private reviewer access and portal submission.

This record does not claim a vendor listing is approved or that unexecuted end-to-end
scenarios passed. No production credentials or customer fixtures are included.
