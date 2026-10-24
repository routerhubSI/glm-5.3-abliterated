# GLM 5.3 API Troubleshooting

Start with a short request and a known catalogue entry. Check recorded usage
before retrying a failed request repeatedly, because attempts can consume credits.

## Authentication fails

Confirm that the process making the request has `ROUTERHUB_API_KEY` set to a
current private key. GLM Chat Completions requests use
`Authorization: Bearer <API_KEY>`. Never publish the real header in an issue.

## A model or endpoint cannot be found

Check the exact model ID in [models.json](https://routerhub.si/models.json).
The published GLM endpoint is `https://routerhub.si/v1/chat/completions`.
Do not send a GLM Chat ID to Messages or Responses just because the account
supports other models on those protocols.

## The request body is rejected

Reduce it to the short example in the [quickstart](./03-glm-5.3-api-quickstart.md).
Check JSON syntax, role names, supported fields, and model-specific limits.
Add optional settings back one at a time so you can identify the incompatibility.

## Streaming produces empty events

Some stream events contain metadata rather than text. Do not assume every event
has a populated choices list or text delta. Use the [streaming example](./api-quickstart.md)
and verify the selected model's current streaming support separately.

## Instructions or tools behave unexpectedly

Check whether a persona changes customer system/developer instructions. Verify
required tool calling and structured-output features individually; a successful
chat response is not a certification of every agent feature.

## Billing or rate limits block the request

Inspect the account balance, error details, and concurrency. For transient
rate limits, use bounded retries and respect server retry guidance. Repeated
authentication or billing errors need a configuration or account fix, not a
faster retry loop.

## Contacting support

Save the timestamp, exact API ID, request path, redacted error, and request ID
if returned. Use the support options in your RouterHub account for account
problems. Documentation corrections can go in this repository's issues.
Follow [SECURITY.md](../SECURITY.md) for private or sensitive reports.

[Client setup](./04-glm-5.3-claude-code-cursor-opencode-codex.md) · [FAQ](./08-faq.md) · [Overview](../README.md)
