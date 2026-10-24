# GLM 5.3 Abliterated vs. Uncensored

If you are comparing a GLM 5.3 abliterated model with a GLM 5.3 uncensored model,
separate the advertised technique from the behavior you want to measure.

## Weight changes and behavior labels

**Abliteration** normally describes interventions in model weights aimed at
refusal-related behavior. **Uncensored** is a less precise label: it can describe
a model's training, a weight edit, or an instruction-driven persona. A request
that receives an answer does not reveal which mechanism produced it.

**Jailbreak prompts** are another layer. They change the input or instruction
context of a request rather than directly modifying the hosted weights.

## Questions for each variant

| Property | What to establish |
|---|---|
| Method | What intervention is actually described for this entry? |
| Provenance | Is there evidence for the claimed weights or training recipe? |
| Instructions | Are customer system/developer messages preserved or replaced? |
| Capability | Does the model solve your real tasks accurately? |
| Refusals | Does it unnecessarily decline tasks in your defined evaluation? |
| Integration | Does the exact entry support your protocol and required features? |
| Privacy | Which service and provider terms govern transmitted data? |

## RouterHub GLM entries

The catalogue lists `glm-5.3-abliterated`, `glm-5.3-uncensored`, and
`glm-5.3-flash-uncensored`, with `glm-5.3` and `glm-5.3-flash` available as
separate comparison entries. The published protocol for these entries is Chat.

Pay particular attention to persona implementations: replacing system instructions
can change the experiment and conflict with an application's own requirements.
The [implementation notes](./model-variants.md) explain that distinction. Check
current service documentation for changes rather than assuming a name specifies
the complete runtime behavior.

## Choosing between them

For a research comparison, keep a standard-model baseline and record the exact
settings used for each entry. For application work, prioritize task success,
instruction handling, latency, and total cost over the stronger-sounding label.

[Run an API request](./03-glm-5.3-api-quickstart.md) · [Evaluation checklist](./05-evaluating-glm-5.3-abliterated.md) · [Overview](../README.md)
