# Match the model to your tool

API keys authenticate requests; they do not translate one API protocol into
another. Start by identifying the request format your tool actually sends.

## Protocol selection

| Tool or interface | Protocol to check | Where to start |
|---|---|---|
| Chat Completions SDK or custom chat client | `chat` | [GLM request examples](./api-quickstart.md) |
| OpenCode | Depends on the selected provider runtime | [RouterHub setup guide](https://routerhub.si/guides/opencode) |
| Claude Code | `messages` | [RouterHub setup guide](https://routerhub.si/guides/claude-code) |
| Codex | `responses` | [RouterHub setup guide](https://routerhub.si/guides/codex) |
| Other editor or agent integrations | Check the client's documentation | [RouterHub setup index](https://routerhub.si/docs) |

The GLM variants in this repository are listed for Chat Completions. Do not
select one in a Messages-only or Responses-only client unless the live
catalogue explicitly adds that support or you have a separately verified adapter.

## Before using a coding agent

Chat support alone does not prove that function tools, structured output,
reasoning fields, or multimodal inputs behave as your agent expects. Verify
the required behavior using an innocuous test before enabling external actions.

Check that the endpoint preserves the instruction surface your app uses.
The fixed-prompt uncensored GLM personas replace customer system/developer
messages, which can conflict with an agent's own operating instructions.

## Deployment checks

- Use the published API base rather than an inferred dashboard URL.
- Make the key available to the process sending requests, not only your editor.
- Keep credentials out of tracked configuration files.
- Confirm the exact model ID and the protocol in [models.json](https://routerhub.si/models.json).
- Send a short request and review usage before running a long agent session.
- Require human approval for actions with irreversible effects.

This page is a protocol-selection guide, not a claim of live certification
for every client or model combination. Follow the current linked setup guide
for your client version.

[Overview](../README.md) · [Model variants](./model-variants.md) · [FAQ](./faq.md)
