# GLM 5.3 abliterated, uncensored, or standard?

Decide which intervention you want to study before choosing an API ID. A
change to weights, a fixed system persona, and a normal model request are
different experiments even when their outputs look similar.

## The three categories

**Standard model:** a useful baseline for task quality and instruction
following. Keep the request and evaluation conditions consistent when
comparing it with another entry.

**Abliterated model:** a label generally used for weight-level interventions
intended to reduce refusal-related behavior. It does not by itself prove
which weights a hosted endpoint serves, how the change was performed, or
whether unrelated capabilities were affected.

**Uncensored model:** a broad product label rather than a single technical
method. It can refer to training, weight edits, or prompt changes. Read the
entry's implementation notes instead of treating the label as a guarantee.

## How RouterHub lists GLM

| ID | Published category | Important implementation detail |
|---|---|---|
| `glm-5.3` | Standard | Baseline GLM entry |
| `glm-5.3-flash` | Standard Flash | A separate model selection with its own rates |
| `glm-5.3-abliterated` | Research variant | Catalogue advertises abliteration and streaming |
| `glm-5.3-uncensored` | Fixed-prompt persona | Server-owned instructions replace customer system/developer messages |
| `glm-5.3-flash-uncensored` | Fixed-prompt Flash persona | The same instruction-replacement distinction applies |

The catalogue does not turn the persona entries into independently verified
fine-tunes. Persona adherence is not guaranteed. If your app relies on a
carefully designed system message, replacing that message is a significant
behavioral difference, not a minor naming detail.

Check [the live catalogue](https://routerhub.si/models.json) for changes.
This page records published descriptions; it does not independently inspect
the hosted weights or report measured performance.

## Questions to answer with a test

1. Does the model answer the legitimate tasks you care about?
2. Is the answer correct and useful, rather than merely non-refusing?
3. Does the endpoint preserve the instructions your application requires?
4. Do required streaming, tool, and structured-output behaviors actually work?
5. What is the total cost after retries and failed attempts?
6. Are the data-retention terms acceptable for the information you send?

Do not infer privacy from the word "uncensored," and do not infer capability
from the word "abliterated." Those are separate properties to verify.

[API setup](./api-quickstart.md) · [Evaluation checklist](./evaluation.md) · [Back to RouterHub guide](../README.md)
