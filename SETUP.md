# Connect ProcessHub

## Codex and Claude Code plugins

Install the package for your client following README.md. Authenticate using the client's
MCP connection interface. Sign into ProcessHub in your browser, verify the account and
organization, select projects, and decide whether future projects should be added.
Return to the AI application when authorization completes. A plain local callback page
belongs to that AI client and cannot be styled by the ProcessHub plugin.

Start with: “Check my ProcessHub connection and list the projects I allowed.”
Reports require write permission and a separate approval inside ProcessHub.

## Claude web / Desktop connector

Add a custom remote connector with URL `https://processhub.kz/mcp`.
For a pre-registered OAuth client use client ID `processhub-claude`, with no client secret.
Its registered callback is `https://claude.ai/api/mcp/auth_callback`.
The server does not provide dynamic client registration. If the client interface cannot
accept a pre-registered client ID, do not substitute an API key: use the supported
connection UI or contact support. Official directory onboarding is a separate review.

## Troubleshooting

- Authorization unavailable: check that your organization permits AI connections.
- No projects: select projects in a new consent flow and check membership/permissions.
- New projects absent: reconnect with automatic new-project access enabled if desired.
- Read works, report missing: reconnect with the report permission; status changes are
  not supported by this integration.
- Expired request: start a fresh connection from the AI client, not an old browser URL.
- Claude Code callback failure: ensure port 39847 is free and the server release includes
  the `processhub-claude-code` client (server v0.5.35 or later). It is registered automatically,
  including with older deployment settings. An operator can explicitly disable registration
  with `CONNECT_CLAUDE_CODE_ENABLED=false`.
- Report awaiting approval: use the link shown in chat, review the exact text, and decide
  inside ProcessHub. The AI must never approve the report for you.

Support: hello@prgm.kz. Include client/version and the error text, not credentials or
OAuth callback URLs containing authorization codes.
