# Connect ProcessHub

## Codex and Claude Code plugins

Install the package for your client following README.md. Authenticate using the client's
MCP connection interface. Sign into ProcessHub in your browser, verify the account and
organization, select projects, and decide whether future projects should be added.
Return to the AI application when authorization completes. A plain local callback page
belongs to that AI client and cannot be styled by the ProcessHub plugin.

Start with: “Check my ProcessHub connection and list the projects I allowed.”
For my work, ask for your tasks or overdue deadlines across permitted projects. Context tools require a new explicit consent including `tasks:context:read`; existing grants never gain discussion/file access automatically. Reconnect with tasks:write to create/update tasks and save reports directly from chat. The consent screen explicitly states that no additional ProcessHub confirmation is required.

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
- Read works, writes unavailable: reconnect with the new read-and-write permission. Older grants never gain direct writes automatically.
- Expired request: start a fresh connection from the AI client, not an old browser URL.
- Claude Code callback failure: ensure port 39847 is free and the server release includes
  the `processhub-claude-code` client (server v0.5.35 or later). It is registered automatically,
  including with older deployment settings. An operator can explicitly disable registration
  with `CONNECT_CLAUDE_CODE_ENABLED=false`.
- Legacy report awaiting approval: decide using the old link. The AI must not approve it for you. Reconnecting enables direct writes for future requests; it does not execute old pending reports.

Support: hello@prgm.kz. Include client/version and the error text, not credentials or
OAuth callback URLs containing authorization codes.
