<div align="center">

<a href="https://routerhub.si/?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=glm-5.3-abliterated">
  <img src="./assets/routerhub-banner.png" width="100%" alt="RouterHub — One key. All your models.">
</a>

# GLM 5.3 Abliterated & Uncensored API

**Research prompt directory, model selection, and working API examples from RouterHub.**

[Get an API key](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) · [Models & pricing](https://routerhub.si/models?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) · [Prompt directory](./docs/prompt-directory.md) · [Quickstart](./docs/api-quickstart.md)

</div>

## Start with the model, not the label

Looking for a **GLM 5.3 abliterated API**, an **uncensored GLM model**, or a place to study **LLM jailbreak prompts**? This guide separates those three topics so you can choose the right interface and understand what you are testing.

RouterHub provides prepaid access to 30+ listed AI models through one account and API key. Available model families include GPT, Claude, DeepSeek, GLM, Qwen, and Grok. A model's supported protocol determines which tools can use it.

- **Explore prompts:** browse the [external research prompt directory](./docs/prompt-directory.md).
- **Connect a model:** follow the [Chat Completions quickstart](./docs/api-quickstart.md).
- **Compare variants:** read [abliterated vs. uncensored vs. standard GLM](./docs/model-variants.md).
- **Measure behavior:** start with the [evaluation checklist](./docs/evaluation.md) and [original benign test prompts](./examples/benign-eval-prompts.json).

The external prompt files are not bundled here. The API documentation, examples, and evaluation prompts in this repository are RouterHub-authored material.

## GLM model IDs

The following IDs were listed in RouterHub's public catalogue on October 24, 2026. Verify the current [model catalogue](https://routerhub.si/models.json) before sending requests: availability, rates, and capabilities can change.

| Model | API ID | Selection notes |
|---|---|---|
| GLM 5.3 Abliterated | `glm-5.3-abliterated` | Listed as an abliterated research variant with streaming |
| GLM 5.3 | `glm-5.3` | Standard comparison baseline |
| GLM 5.3 Flash | `glm-5.3-flash` | Separate catalogue entry and token rates |
| GLM 5.3 Uncensored | `glm-5.3-uncensored` | Fixed-prompt persona; not a separately verified uncensored fine-tune |
| GLM 5.3 Flash Uncensored | `glm-5.3-flash-uncensored` | Fixed-prompt persona over the Flash entry |

These GLM entries are listed for **Chat Completions**. The uncensored personas replace customer system/developer messages with server-owned instructions. That behavior matters if your app depends on its own system prompt.

**Abliterated is not a guarantee of zero refusals.** This repository does not independently inspect hosted model weights or claim measured refusal rates. See [model variants](./docs/model-variants.md).

## Quickstart

1. [Create a RouterHub account](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated).
2. Add prepaid credits and create a private API key.
3. Set `ROUTERHUB_API_KEY` in your local environment.
4. Send a short request, then check the recorded cost in your account.

Requests below use paid credits. Do not put your actual key into a public repository or paste it into an issue.

### cURL

```bash
curl https://routerhub.si/v1/chat/completions \
  -H "Authorization: Bearer $ROUTERHUB_API_KEY" \
  -H "Content-Type: application/json" \
  --data '{"model":"glm-5.3-abliterated","messages":[{"role":"user","content":"Reply with OK."}]}'
```

### Python

Install the SDK with `pip install openai`.

```python
import os
from openai import OpenAI

api = OpenAI(
    base_url="https://routerhub.si/v1",
    api_key=os.environ["ROUTERHUB_API_KEY"],
)
result = api.chat.completions.create(
    model="glm-5.3-abliterated",
    messages=[{"role": "user", "content": "Reply with OK."}],
)
print(result.choices[0].message.content)
```

For Node.js, streaming, and a dependency-free Python example, see the [full API quickstart](./docs/api-quickstart.md).

## Why the API protocol matters

One key does not mean every model supports every endpoint.

| Your client sends | Choose a catalogue entry listing | Relevant guide |
|---|---|---|
| Chat Completions | `chat` | [GLM API quickstart](./docs/api-quickstart.md) |
| Messages | `messages` | [RouterHub tool setup](https://routerhub.si/docs) |
| Responses | `responses` | [RouterHub tool setup](https://routerhub.si/docs) |

Check tool calling, streaming, input types, and context limits separately for the exact model. See [tool compatibility](./docs/tool-compatibility.md).

## Pricing and data handling

RouterHub uses prepaid, per-token billing. Card and crypto funding options are shown at checkout. Current input, output, and published cached-input rates are available on the [GLM pricing page](https://routerhub.si/guides/glm?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated).

Hosted inference is not local inference. Provider retention terms apply to the listed research variants; do not assume zero retention. Avoid sending private material until you have checked the applicable terms.

## Documentation

| Resource | What you can do |
|---|---|
| [Research prompt directory](./docs/prompt-directory.md) | Follow links to community-hosted model and agent prompt files |
| [Model variants](./docs/model-variants.md) | Distinguish weight-level methods from prompt-level personas |
| [API quickstart](./docs/api-quickstart.md) | Send requests using Python, Node.js, or cURL |
| [Tool compatibility](./docs/tool-compatibility.md) | Match the model protocol to your application |
| [Evaluation](./docs/evaluation.md) | Compare quality, unnecessary refusals, latency, and cost |
| [FAQ](./docs/faq.md) | Resolve common setup and billing questions |

## Contribute

Found a broken link or a setup mistake? Include the affected page, exact model ID, and a redacted reproduction in an issue. Read [CONTRIBUTING.md](./CONTRIBUTING.md) before submitting content and [SECURITY.md](./SECURITY.md) before reporting sensitive information.

Run `python tools/check.py` from the repository root to check local links,
example data, and code syntax. This check makes no API calls and spends no credits.

This is a RouterHub-maintained research and integration resource. External prompt links do not establish compatibility or effectiveness on RouterHub. Follow applicable laws and the terms for your chosen model and service.

[RouterHub](https://routerhub.si/?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) · [API catalogue](https://routerhub.si/models.json) · [MIT license](./LICENSE)
