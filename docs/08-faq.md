# GLM 5.3 Abliterated and Uncensored FAQ

## What is the GLM 5.3 abliterated API ID?

RouterHub lists `glm-5.3-abliterated`. Check its current availability and rates
in [models.json](https://routerhub.si/models.json), then use Chat Completions.

## Which uncensored GLM variants are listed?

The catalogue includes `glm-5.3-uncensored` and `glm-5.3-flash-uncensored`.
The implementation matters: an uncensored label is not proof of separately
fine-tuned weights or of preserved customer system instructions.

## How does GLM 5.3 abliterated differ from uncensored?

Abliteration describes a family of weight-level interventions. Uncensored
can refer to a wider range of training, weight, or prompt changes. See the
[comparison guide](./02-abliterated-vs-uncensored.md).

## Are GLM 5.3 jailbreak prompts the same as abliterated weights?

No. A prompt changes a request's instructions or context; a weight-level
intervention changes the model. The [prompt directory](./prompt-directory.md)
is a separate research resource from the hosted API entries.

## Will a no-refusal model always answer correctly?

Neither refusal-free output nor correctness is guaranteed. Measure task
completion, factual quality, and unnecessary refusals independently.

## Can I use the OpenAI SDK?

Yes: configure the RouterHub base URL and key, then call Chat Completions with
the exact GLM model ID. See the [SDK examples](./api-quickstart.md).

## Can I use GLM directly in Claude Code or Codex?

The GLM entries documented here list Chat Completions. Claude Code requires
Messages and Codex requires Responses. Choose an appropriate model from the
same RouterHub account, or use a Chat-compatible client when you need GLM.

## Does RouterHub support Cursor and OpenCode workflows?

RouterHub publishes an OpenCode setup guide. Cursor users should check custom
endpoint support for their version and intended feature. Review the
[client matrix](./04-glm-5.3-claude-code-cursor-opencode-codex.md) before configuring either.

## How do pricing and payment work?

API usage is prepaid, with published input, output, and eligible cached-input
rates per million tokens. RouterHub advertises card and crypto top-ups; check
the checkout screen for current payment options. See [GLM pricing](https://routerhub.si/guides/glm).

## Are these local models or guaranteed private endpoints?

These examples use hosted inference. Review data-handling and retention terms
before transmitting private information. A research label does not establish
zero retention.

## Where should I start if a request fails?

Check the key, exact model ID, account balance, endpoint, and request fields.
Keep a redacted request ID and timestamp for support. The
[troubleshooting guide](./10-troubleshooting.md) organizes those checks.

[Additional API FAQ](./faq.md) · [Documentation index](./README.md) · [Overview](../README.md)
