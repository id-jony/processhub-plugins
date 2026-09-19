# ProcessHub plugins

Connect [ProcessHub](https://processhub.kz/welcome) projects and tasks to Codex and Claude Code.
Published by **ИП Pragma** · [Support](mailto:hello@prgm.kz).

This repository contains plugin packages and workflow instructions. The hosted service
and its source code are separate. Directory review and marketplace distribution are
separate steps: this repository alone does not mean an official listing is approved.

## What you can do

- **Task brief** — understand a task, its requirements and missing information.
- **Implementation plan** — turn a task into steps and verification criteria.
- **Work report** — propose a report; publish it only after confirmation in ProcessHub.

Examples (Russian and English work):

> Разбери задачу в моём проекте ProcessHub и уточни, чего не хватает для начала.
>
> Prepare an implementation plan for this ProcessHub task.
>
> Предложи отчёт о выполненной работе для подтверждения в ProcessHub.

The integration does not create/delete tasks or change their status. It does not read
comments or attachments. Task descriptions are limited to 6,000 characters per response.

## Install in Codex

From a local clone of this public repository:

```sh
codex plugin marketplace add /absolute/path/to/processhub-plugins
codex plugin add processhub@personal
```

The bundled Codex marketplace is named `personal`. If your setup already uses that name
for another marketplace, resolve the name conflict before adding this one. Open a new
Codex task after installing. Complete ProcessHub OAuth when prompted. Existing manual
MCP connections can coexist; avoid invoking two copies of the same tool by mistake.

## Install in Claude Code

```sh
claude plugin marketplace add id-jony/processhub-plugins
claude plugin install processhub@processhub
```

Use `/mcp` to authenticate the plugin's ProcessHub server. The package uses a public
OAuth client and a local callback on port 39847. Keep that port available. Never paste a
client secret or access token into the plugin. Use the current stable Claude Code release.

Claude web/Desktop **Connectors** use the separate remote MCP connection described in
[SETUP.md](SETUP.md). Cowork installation and OAuth need a separate product smoke test;
CLI validation is not proof of Cowork compatibility.

## Permissions and privacy

A ProcessHub account, enabled organization access and project permissions are required.
Select projects during consent; automatic access to newly created projects is opt-in.
The server rechecks your current rights for each operation. Revoke access under
Profile → AI connections; organization policy lives in organization settings.

The host AI provider receives the content it requests. Revoking access does not erase
copies already held by that provider. See [Privacy](https://processhub.kz/privacy) and
[Terms](https://processhub.kz/terms), plus your AI provider's policies.

## Development and submission

- `python3 scripts/validate.py` checks packages, mirrored skills and release boundaries.
- `claude plugin validate --strict claude/processhub` validates the Claude package.
- [Submission checklist](submission/README.md) records release and review requirements.
- [Reviewer scenarios](submission/test-cases.json) includes five positive and three negative cases.

No credentials, private customer fixtures or application source belong in this repository.
MIT-licensed plugin files; hosted service usage is governed by its terms.
