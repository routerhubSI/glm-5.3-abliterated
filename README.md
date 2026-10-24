<div align="center">

<a href="https://routerhub.si/?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=glm-5.3-abliterated">
  <img src="./assets/routerhub-banner.png" width="100%" alt="RouterHub — One key. All your models.">
</a>

<p>
  <a href="https://routerhub.si/?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=glm-5.3-abliterated"><img src="./assets/visit-website.svg" width="208" height="74" alt="Visit RouterHub website"></a>
  <a href="https://t.me/routerhubsi"><img src="./assets/telegram-channel.svg" width="216" height="74" alt="Join the RouterHub Telegram channel"></a>
  <a href="https://routerhub.si/register?next=onboarding&amp;utm_source=github&amp;utm_medium=readme&amp;utm_campaign=glm-5.3-abliterated"><img src="./assets/get-api-key.svg" width="183" height="74" alt="Get a RouterHub API key"></a>
</p>

**GLM is your starting point. One RouterHub API key also connects you to GPT, Claude, DeepSeek, Qwen, and Grok, with research variants listed in the model catalogue.**

# GLM 5.3 Abliterated or Uncensored — Jailbreak Prompts, Model Guide & API Access

**Find a GLM 5.3 abliterated API, compare GLM 5.3 uncensored models, and explore 35 community research prompt files.** This RouterHub guide connects model terminology, jailbreak prompt research, API examples, and coding-tool setup in one place.

Searching for a **GLM 5.3 uncensored AI model**, a **GLM 5.3 abliterated model**, or a **GLM 5.3 no-refusal model**? Learn what each label tells you, choose an API ID, and evaluate the behavior you actually need. The gateway offers OpenAI-compatible Chat Completions for GLM and Anthropic-compatible Messages for supported Claude entries.

[![Model](https://img.shields.io/badge/model-GLM%205.3-a9ff6b?style=flat)](#what-is-glm-53)
[![Prompts](https://img.shields.io/badge/research%20prompts-35-a9ff6b?style=flat)](#glm-53-jailbreak-collection-35-prompts)
[![Variants](https://img.shields.io/badge/variants-abliterated%20%C2%B7%20uncensored-a9ff6b?style=flat)](#abliterated-vs-uncensored)
[![API](https://img.shields.io/badge/API-OpenAI%20%2B%20Anthropic-0ea5e9?style=flat)](#quickstart)
[![Billing](https://img.shields.io/badge/billing-pay%20per%20token-a9ff6b?style=flat)](#pricing-and-access)

[**Get an API key →**](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) · [Quickstart](#quickstart) · [Docs](#documentation) · [Telegram](https://t.me/routerhubsi)

</div>

---

## GLM 5.3 Abliterated or Uncensored?

These searches describe related goals, but the labels answer different questions:

- **GLM 5.3 abliterated** names a research variant associated with interventions in model weights intended to reduce refusal-related behavior.
- **GLM 5.3 uncensored** describes a broader product category. The implementation might involve training, weight changes, or a prompt-level persona; the name alone does not tell you which.

If your goal is a **GLM 5.3 uncensored API**, start with the exact catalogue entry rather than assuming every variant behaves alike. RouterHub lists both `glm-5.3-abliterated` and `glm-5.3-uncensored`, along with standard and Flash alternatives.

Reduced refusal is something to measure, not a promise of unrestricted output. Compare the variants in the [abliterated vs. uncensored guide](./docs/02-abliterated-vs-uncensored.md).

## Not just GLM

RouterHub connects **GLM, GPT, Claude, DeepSeek, Qwen, and Grok** through a prepaid account and API key. Use this repository for GLM 5.3 abliterated and uncensored research; explore the [full model catalogue](https://routerhub.si/models?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) when you need another family or protocol.

There are 30+ published model entries. Chat Completions, Messages, and Responses are supported across the catalogue, but each entry has its own supported protocol. Choosing a model and choosing a client go together.

<a href="https://routerhub.si/models?utm_source=github&amp;utm_medium=readme&amp;utm_campaign=glm-5.3-abliterated">
  <img src="./assets/routerhub-banner.png" width="600" alt="GLM 5.3 abliterated and uncensored API access with RouterHub">
</a>

## GLM 5.3 jailbreak collection (35 prompts)

Explore **35 community-hosted jailbreak prompts and agent instruction files**, organized by model family. This directory links to the original files rather than redistributing their text. Open a file to inspect its current contents and terms; a listing is not a compatibility or effectiveness guarantee.

The collection is a starting point for **LLM jailbreak research**, prompt-injection analysis, and instruction-following experiments. It is separate from RouterHub's hosted abliterated and uncensored model entries.

### Collection

### OpenCode Zen — Free Stealth Models

| Model | Research file | Instruction format |
|---|---|---|
| **Big Pickle** | [BigPickle-opencode.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/BigPickle-opencode.md) | Persona-oriented agent instructions |
| **Space Bunny** | [spacebunny-agents.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/spacebunny-agents.md) | Persistent assistant instructions |
| **LongCat 2.5** | [longcat-agents.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/longcat-agents.md) | Persistent assistant instructions |
| **MiMo V2.6** | [mimo-2.6-agents.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/mimo-2.6-agents.md) | Persistent assistant instructions |
| **Step 5 Preview** | [Step-5-preview.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Step-5-preview.md) | Workspace-level instructions |
| **Muse Spark 1.3** | [Muse spark 1.3.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Muse%20spark%201.3.md) | Agent behavior profile |
| **Muse Spark 1.3 v2** | [Muse-spark-1-3-v2.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Muse-spark-1-3-v2.md) | Alternate agent behavior profile |
| **Muse.ai** | [muse-ai-AGENTS.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/muse-ai-AGENTS.md) | Project instruction file |

### Anthropic — Claude

| Model | Research file | Instruction format |
|---|---|---|
| **Opus** | [opus v1.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/opus%20v1.md) · [opus v2.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/opus%20v2.md) | Two persona-prompt revisions |
| **Sonnet** | [sonnet v1.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/sonnet%20v1.md) · [Sonnet v2.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Sonnet%20v2.md) | Two creative-writing prompt revisions |

### Zhipu — GLM / ZCode

| Model | Research file | Instruction format |
|---|---|---|
| **GLM 5.2** | [glm-5.2.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/glm-5.2.md) | System-level instructions |
| **GLM ZCode 5.2** | [glm-zcode-5.2.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/glm-zcode-5.2.md) | System-level instructions |
| **GLM ZCode 5.3** | [glm-zcode-5.3.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/glm-zcode-5.3.md) · [glm-zcode-5.3-AGENTS.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/glm-zcode-5.3-AGENTS.md) | Chat and project-level variants |
| **GLM 5.3 Flash** | [glm-5-3-flash.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/glm-5-3-flash.md) | Assistant behavior profile |
| **GLM 5.3 (OpenCode)** | [glm5-3opencode.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/glm5-3opencode.md) | Agent behavior profile |

### DeepSeek

| Model | Research file | Instruction format |
|---|---|---|
| **DeepSeek V3** | [deepseek v3.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/deepseek%20v3.md) | System-level instructions |
| **DeepSeek V4** | [deepseek v4.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/deepseek%20v4.md) | System-level instructions |
| **DeepSeek 4.1** | [deepseek-4-1.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/deepseek-4-1.md) | Assistant behavior profile |

### Moonshot — Kimi

| Model | Research file | Instruction format |
|---|---|---|
| **Kimi K2** | [kimi-k2.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/kimi-k2.md) | System-level instructions |
| **Kimi K3** | [kimi-k3-agents.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/kimi-k3-agents.md) | Workspace-level instructions |

### xAI — Grok

| Model | Research file | Instruction format |
|---|---|---|
| **Grok Build** | [Grok build.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Grok%20build.md) | Agent-level instructions |
| **Grok 4.7** | [grok-4.7.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/grok-4.7.md) | Application workspace instructions |
| **Grok Config** | [grok-config.txt](https://github.com/togg53192-cmd/jailbreaks/blob/main/grok-config.txt) | Harness configuration |

### Google / Mistral / Alibaba

| Model | Research file | Instruction format |
|---|---|---|
| **Gemini 4 Argon** | [Gemini-4-Argon.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Gemini-4-Argon.md) | Model behavior profile |
| **Mistral Large 4** | [Mistral-Large-4.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Mistral-Large-4.md) | Agent-level instructions |
| **Qwen 3.7** | [qwen-3.7.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/qwen-3.7.md) | System-level instructions |

### Ollama Modelfiles

| Model | Research file | Instruction format |
|---|---|---|
| **Gemma 4** | [gemma4.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/gemma4.md) | Local model definition |
| **GPT-OSS 20B** | [gpt-oss-20b.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/gpt-oss-20b.md) | Local model definition |

### Unfiled Files

Additional community experiments are available as [Beam.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Beam.md), [Muse-wonder.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Muse-wonder.md), [qwen-preferences.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/qwen-preferences.md), and [Unified.md](https://github.com/togg53192-cmd/jailbreaks/blob/main/Unified.md).

### How to use these prompts

#### System Prompts

Review the selected file before testing it in your client's system-message or custom-instructions field. Keep a copy of your original configuration so you can compare behavior and restore it afterward.

#### AGENTS.md Files

A compatible coding agent may load a project-level `AGENTS.md`. Use a disposable workspace to inspect unfamiliar instructions before adding them to a real project, and follow your client's documented instruction-loading rules.

#### Workspace Policies

Some entries are intended for persistent agent instructions rather than ordinary chat messages. Confirm the scope in your client: global configuration can affect unrelated projects, so prefer an isolated test profile.

#### Ollama Modelfiles

The local-model entries use Ollama's model-definition format. Review the referenced base model and configuration, then follow the [Ollama documentation](https://docs.ollama.com/modelfile). Local Ollama execution and hosted RouterHub API requests are separate integration paths.

#### Grok Configuration

The Grok configuration file targets a harness-specific settings surface. Check that the receiving application understands the format; a chat endpoint does not automatically interpret it as configuration.

For source-link details and additional entries, open the [research prompt directory](./docs/prompt-directory.md). Linking a file does not establish that its target model is offered by RouterHub.

## If a jailbreak gets patched

An upstream update can change how a model interprets a persona, system message, or agent instruction file. Keep the model version and prompt revision with your test results so you can identify what changed.

You can then choose between two research paths:

1. **Revise the prompt experiment.** Compare the new behavior with a saved baseline and document the legitimate task that regressed.
2. **Evaluate a different model entry.** Test a **GLM 5.3 abliterated or uncensored model** against the same task set instead of depending on a particular prompt technique.

Ready to compare hosted variants? [Run the GLM 5.3 API quickstart](./docs/03-glm-5.3-api-quickstart.md) or [create your RouterHub API key](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated).

## What is GLM 5.3?

**GLM 5.3** belongs to the GLM model family associated with Z.ai / Zhipu. This guide focuses on API access, variant selection, and evaluation for developers considering GLM for coding, agent tasks, analysis, and Chinese/English workflows.

Useful evaluation scenarios include:

- code explanation, refactoring suggestions, and test generation;
- project instructions and multi-step agent work;
- bilingual drafting and translation;
- repeated tasks where token cost affects deployment choices;
- comparing standard, Flash, abliterated, and uncensored entries on the same inputs.

Choose on measured task quality, latency, and cost rather than a product label alone. The [GLM 5.3 model guide](./docs/01-what-is-glm-5.3-abliterated.md) explains where to start.

## Abliterated vs. uncensored

| Question | GLM 5.3 Abliterated | GLM 5.3 Uncensored |
|---|---|---|
| **What does the label describe?** | A research category associated with weight-level intervention | A broad behavior or product category |
| **What implementation should you verify?** | The advertised method and hosted model provenance | Whether the entry uses training changes, weight changes, or a fixed persona |
| **Which API ID is listed?** | `glm-5.3-abliterated` | `glm-5.3-uncensored` |
| **Which protocol is listed?** | Chat Completions | Chat Completions |
| **What needs testing?** | Task quality, refusals, instruction following, and integration | The same measures, plus how customer system instructions are handled |
| **Does it guarantee no refusals?** | No | No |

The [full abliterated vs. uncensored comparison](./docs/02-abliterated-vs-uncensored.md) separates weight-level methods from prompt-level changes. This repository does not independently inspect hosted model weights or publish a refusal-rate benchmark.

## Why use GLM 5.3 abliterated or uncensored?

- **Research model behavior:** compare variant responses on legitimate requests where the standard model was unnecessarily restrictive.
- **Develop coding workflows:** evaluate explanation, code generation, and agent instruction following with your own acceptance tests.
- **Explore creative and bilingual tasks:** assess tone, useful engagement, and Chinese/English output separately from correctness.
- **Compare cost per result:** include retries, failures, and output length instead of looking only at token rates.
- **Keep one integration account:** use RouterHub for GLM and other listed families without maintaining a separate account for each model.
- **Reuse familiar clients:** connect through a Chat Completions SDK or a tool supporting a custom compatible endpoint.

See [GLM 5.3 use cases](./docs/06-use-cases.md) for practical evaluation tasks, or [get an API key](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) to begin a paid test.

## Quickstart

### 1. Get the key and base URL

[Register with RouterHub](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated), add prepaid credits, and create a private API key. The published API base is `https://routerhub.si/v1`.

```bash
export ROUTERHUB_API_KEY="<your-private-key>"
export ROUTERHUB_API_BASE_URL="https://routerhub.si/v1"
```

Set these values only in your local environment or secret manager. Running an inference example consumes credits; do not commit a real key.

### 2. Confirm the GLM 5.3 model ID

These entries were listed in the [public catalogue](https://routerhub.si/models.json) on October 24, 2026. All five list Chat Completions and preview availability; recheck availability and rates before use.

| Variant | Exact API ID |
|---|---|
| **GLM 5.3 Abliterated** | `glm-5.3-abliterated` |
| **GLM 5.3** | `glm-5.3` |
| **GLM 5.3 Flash** | `glm-5.3-flash` |
| **GLM 5.3 Uncensored** | `glm-5.3-uncensored` |
| **GLM 5.3 Flash Uncensored** | `glm-5.3-flash-uncensored` |

### 3. OpenAI-compatible request

Install `openai` with pip, then run a short Chat Completions request:

```python
import os
from openai import OpenAI

api = OpenAI(
    base_url=os.environ["ROUTERHUB_API_BASE_URL"],
    api_key=os.environ["ROUTERHUB_API_KEY"],
)
result = api.chat.completions.create(
    model="glm-5.3-abliterated",
    messages=[{"role": "user", "content": "Explain what an API gateway does in two sentences."}],
)
print(result.choices[0].message.content)
```

### 4. Anthropic-compatible request

The same RouterHub account also serves supported Claude models through Messages. **This is a Claude example, not an alternate GLM endpoint:** the listed GLM variants use Chat Completions. Install `anthropic` with pip to try it.

```python
import os
from anthropic import Anthropic

api = Anthropic(
    base_url=os.environ["ROUTERHUB_API_BASE_URL"],
    api_key=os.environ["ROUTERHUB_API_KEY"],
)
result = api.messages.create(
    model="claude-opus-5-5",
    max_tokens=64,
    messages=[{"role": "user", "content": "Explain what an API gateway does in two sentences."}],
)
for part in result.content:
    if part.type == "text":
        print(part.text)
```

For cURL, JavaScript, streaming, and a standard-library Python client, continue with the [GLM 5.3 API quickstart](./docs/03-glm-5.3-api-quickstart.md).

## Works with your stack

| Tool | Connection path |
|---|---|
| **OpenCode** | Select a Chat Completions provider configuration for the listed GLM model ID |
| **Cursor** | Check whether your version supports a custom Chat Completions endpoint and the required model features |
| **Continue / Cline** | Follow the compatible Chat Completions setup for GLM |
| **OpenAI SDK** | Supply the RouterHub base URL, key, and exact GLM API ID |
| **Claude Code / Anthropic SDK** | Use a catalogue entry supporting Messages, such as Claude; the listed GLM entries do not |
| **Codex CLI** | Select a Responses model from the same account rather than a Chat-only GLM entry |
| **LangChain / LlamaIndex** | Choose a compatible Chat Completions integration and verify the features your application uses |

Client setup and protocol selection: [Claude Code, Cursor, OpenCode, Codex](./docs/04-glm-5.3-claude-code-cursor-opencode-codex.md).

## Evaluating GLM 5.3 abliterated

A useful **GLM 5.3 abliterated benchmark** needs more than a single permissive answer. Compare standard and research variants using the same legitimate tasks, then record:

1. **Unnecessary refusals:** requests declined despite being answerable under your defined test policy.
2. **Task quality:** correctness, useful detail, code tests, and appropriate uncertainty.
3. **Instruction behavior:** formatting, system-message handling, and required tool integration.
4. **Repeatability:** prompt revision, API ID, settings, repetitions, and test date.
5. **Total task cost:** token use, failed attempts, retries, and end-to-end latency.

Use the [evaluation guide](./docs/05-evaluating-glm-5.3-abliterated.md) and [original benign sample tasks](./examples/benign-eval-prompts.json) to design your run. No live benchmark scores are claimed in this repository.

## Pricing and access

- **Prepaid token billing:** add credits and pay for usage at the selected model's rates.
- **Input and output pricing:** compare the published USD-per-million-token rates for your exact GLM variant.
- **Cache-aware charges:** use a published cached-input rate only where supported and reported.
- **Card or crypto funding:** review available payment methods and terms at checkout.
- **Usage tracking:** check charges in your account after a short initial request.

[View GLM API pricing](https://routerhub.si/guides/glm?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) · [Browse models](https://routerhub.si/models?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated) · [Get your API key](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated)

For cost estimation and model limits, see [pricing and limits](./docs/03-glm-5.3-api-quickstart.md#pricing-and-limits).

## Honest limits

- **A no-refusal label is not a guarantee.** Evaluate the actual model instead of assuming every request will receive a useful answer.
- **Hosted behavior can change.** Recheck availability and rerun important evaluations after updates.
- **Protocols are model-specific.** A shared API key does not make a Chat-only model compatible with Messages or Responses.
- **Instruction handling matters.** In particular, confirm whether a persona replaces your system/developer instructions.
- **Hosted inference is not local inference.** Review applicable provider terms and retention policies before transmitting private data.

Read [safety and responsible use](./docs/07-safety-and-responsible-use.md) for practical deployment checks.

## FAQ

**Is GLM 5.3 abliterated the same as GLM 5.3 uncensored?**

No. Abliteration identifies a family of weight-level methods, while uncensored is a broader label that can also cover prompt-level changes. Compare the implementation notes in the [variant guide](./docs/02-abliterated-vs-uncensored.md).

**How do I access GLM 5.3 abliterated through an API?**

Create a RouterHub account, fund it, create a key, and send a Chat Completions request using `glm-5.3-abliterated`. Follow the [API quickstart](./docs/03-glm-5.3-api-quickstart.md) and check the live catalogue first.

**Does RouterHub have a GLM 5.3 uncensored model?**

The public catalogue lists `glm-5.3-uncensored` and `glm-5.3-flash-uncensored` alongside the abliterated entry. Verify availability and how the entry handles system instructions before integrating it.

**Can I use GLM 5.3 with Claude Code or Cursor?**

GLM currently requires Chat Completions. Claude Code requires Messages, so use a supported Claude entry there. For Cursor, check that your version supports the needed custom endpoint. See the [client guide](./docs/04-glm-5.3-claude-code-cursor-opencode-codex.md).

**Is GLM 5.3 abliterated safe?**

Suitability depends on the task, data, model behavior, and controls around your application. Review outputs and approve consequential actions; see the [deployment checklist](./docs/07-safety-and-responsible-use.md).

**Will a GLM 5.3 no-refusal model never refuse?**

No. The phrase is a search label, not evidence of refusal-free behavior or correct answers.

**Is there a subscription?**

RouterHub describes its API billing as prepaid and usage-based. Review current account terms and token prices before funding a run.

**Can I pay with crypto?**

RouterHub advertises card and crypto top-ups. The checkout screen shows the payment methods currently available.

**What is the difference between GLM 5.3 and GLM 5.3 Flash?**

They are separate catalogue entries with separate rates and capabilities to verify. Benchmark both against your latency, quality, and cost requirements.

**Where can I compare GLM 5.3 with Claude, GPT, and DeepSeek?**

Start with [RouterHub's model catalogue](https://routerhub.si/models?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated), then apply the same task rubric while accounting for protocol and instruction differences. More answers are in the [GLM 5.3 FAQ](./docs/08-faq.md).

## Documentation

| Guide | Coverage |
|---|---|
| [What is GLM 5.3 Abliterated?](./docs/01-what-is-glm-5.3-abliterated.md) | Model terminology and a starting checklist |
| [Abliterated vs. uncensored](./docs/02-abliterated-vs-uncensored.md) | Weight changes, personas, and variant selection |
| [GLM 5.3 API quickstart](./docs/03-glm-5.3-api-quickstart.md) | Account, model IDs, requests, and billing |
| [Claude Code, Cursor, OpenCode, Codex](./docs/04-glm-5.3-claude-code-cursor-opencode-codex.md) | Matching clients to supported protocols |
| [Evaluating GLM 5.3 abliterated](./docs/05-evaluating-glm-5.3-abliterated.md) | Test design and task-based scoring |
| [Use cases](./docs/06-use-cases.md) | Coding, agent, writing, and bilingual tasks |
| [Safety and responsible use](./docs/07-safety-and-responsible-use.md) | Secrets, privacy, permissions, and deployment checks |
| [FAQ](./docs/08-faq.md) | Common GLM API and model-selection questions |
| [Glossary](./docs/09-glossary.md) | Model, prompt, protocol, and billing terms |
| [Troubleshooting](./docs/10-troubleshooting.md) | Authentication, model IDs, streaming, and request failures |

## Related

- **[RouterHub models](https://routerhub.si/models?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated):** compare model families, protocols, and published prices.
- **[Research prompt directory](./docs/prompt-directory.md):** community-hosted prompt links and source-version guidance.
- **[RouterHub](https://routerhub.si/?utm_source=github&utm_medium=readme&utm_campaign=glm-5.3-abliterated):** account access, prepaid credits, and API keys.
- **[Telegram](https://t.me/routerhubsi):** RouterHub's community channel.

Documentation fixes and redacted reproductions are welcome: [contributing](./CONTRIBUTING.md) · [security](./SECURITY.md) · [MIT license](./LICENSE). Run `python tools/check.py` for offline link and syntax checks without spending credits.

---

<div align="center">

**Found a useful GLM 5.3 abliterated or uncensored resource? Star the repository and share your documentation improvements.**

<sub>Maintained by RouterHub. Model names and trademarks belong to their respective owners; this repository does not imply endorsement by model providers. External research files retain their own terms. Use the APIs in accordance with applicable laws and service policies.</sub>

</div>
