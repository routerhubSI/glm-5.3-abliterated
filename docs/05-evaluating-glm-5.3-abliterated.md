# Evaluating GLM 5.3 Abliterated

A GLM 5.3 abliterated evaluation should show whether the model improves your
legitimate tasks, not merely whether it produces text. Keep a standard GLM
baseline and score correctness separately from unnecessary refusal.

## Build the task set

Choose representative tasks from your application: code explanation, writing,
bilingual assistance, or instruction-following checks. Include clear success
criteria before collecting responses so favorable examples do not redefine
the benchmark after the fact.

The [benign evaluation samples](../examples/benign-eval-prompts.json) are original
RouterHub starting points. They are not a validated benchmark and do not
establish a model's behavior outside those tasks.

## Record the run

Save the model ID, endpoint, date, prompt revision, settings, and number of
attempts. Record latency, reported token usage, retries, and failures.
Keep redacted responses so disputed scores can be reviewed without paying
to regenerate the request.

## Score multiple outcomes

| Measure | What it tells you |
|---|---|
| Accepted task results | How often the output satisfies the task's requirements |
| Unnecessary refusals | How often an answerable task is declined under your rubric |
| Correctness | Whether factual claims or generated code survive independent checks |
| Instruction following | Whether required format and instruction boundaries are preserved |
| Integration reliability | Whether the response and events satisfy your client contract |
| Time and cost per accepted result | What retries and unsuccessful attempts add to deployment cost |

## Compare variants fairly

Use the same task set for standard, abliterated, and uncensored entries. Note
when a persona changes system-instruction handling, because that is a different
condition rather than an isolated weight-level comparison.

Publish sample counts and failures alongside averages. A narrow task set cannot
justify a claim that a model never refuses or is universally better.

[Expanded evaluation checklist](./evaluation.md) · [Variant comparison](./02-abliterated-vs-uncensored.md) · [Overview](../README.md)
