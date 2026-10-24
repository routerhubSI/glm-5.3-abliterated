# GLM 5.3 and AI API Glossary

| Term | Meaning in this guide |
|---|---|
| Abliteration | A family of weight-level interventions intended to reduce refusal-related behavior |
| Uncensored model | A broad product or behavior label; the actual implementation must be checked |
| Jailbreak prompt | An input or instruction experiment intended to change how a model applies its instruction boundaries |
| Persona | Instructions that establish a role or behavioral style; not evidence of changed model weights |
| Refusal | An output that declines a request; evaluating whether it was unnecessary requires a defined rubric |
| Model ID | The exact identifier sent in an API request, such as `glm-5.3-abliterated` |
| API base URL | The service prefix used by a compatible client: `https://routerhub.si/v1` |
| Chat Completions | The protocol used by the GLM entries documented here |
| Messages | The protocol used by supported Claude entries and Claude Code |
| Responses | The protocol required by Codex and supported GPT entries |
| Token | A unit used to represent model input or output and calculate published usage charges |
| Cached input | Input usage reported as a cache hit and billed according to an applicable published rate |
| Context limit | The model-specific input/output capacity; do not infer it from another entry |
| Streaming | Incremental response delivery; event structure and support must match your client |
| Tool calling | Structured model output requesting a tool action; support is separate from basic chat compatibility |
| Preview | A catalogue availability label that should be checked before depending on an entry |
| Baseline | A comparison condition, usually a standard model tested with the same task set |
| Cost per accepted result | Total attempted-request cost divided by results meeting the task's success criteria |

The terminology describes methods and integration choices, not universal
performance or privacy guarantees. For concrete setup steps, open the
[API quickstart](./03-glm-5.3-api-quickstart.md).

[Variant comparison](./02-abliterated-vs-uncensored.md) · [Documentation index](./README.md) · [Overview](../README.md)
