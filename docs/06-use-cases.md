# GLM 5.3 Abliterated and Uncensored Use Cases

Use cases are candidates for evaluation, not guarantees of model capability.
Compare GLM 5.3 variants on the tasks and acceptance criteria that matter to you.

## Coding and repository work

Try code explanation, small refactors, unit-test suggestions, and migration
planning. Validate generated code with the project's real tests. A confident
answer is not evidence that the code compiles or preserves behavior.

For agent workflows, verify protocol support and instruction handling before
granting tool access. See the [client guide](./04-glm-5.3-claude-code-cursor-opencode-codex.md).

## Bilingual assistance

Compare English and Chinese explanations, translations, and terminology choices
using a reviewer who can assess both languages. Include factual and formatting
requirements rather than scoring only fluency.

## Creative writing and analysis

Evaluate fictional dialogue, alternative viewpoints, and discussion of sensitive
but legitimate topics. Track whether the model meaningfully completes the task,
whether the tone is appropriate, and whether claims are supported.

## Prompt and model research

Study differences between a request with ordinary instructions and one with a
reviewed research prompt. Separately compare standard, abliterated, and
uncensored model entries so input changes are not confused with model changes.
Prompt files are indexed in the [prompt directory](./prompt-directory.md).

## Cost-sensitive repeated work

Measure short and long tasks separately. Include input, output, retries, and
failed requests when estimating the cost per accepted result. Standard and
Flash variants have separate listings and rates; do not assume the cheaper
token rate always produces the cheaper successful task.

[Evaluation guide](./05-evaluating-glm-5.3-abliterated.md) · [GLM API pricing](https://routerhub.si/guides/glm?utm_source=github&utm_medium=docs&utm_campaign=glm-5.3-abliterated) · [Overview](../README.md)
