# Evaluate the task, not just the refusal

A response that avoids saying "no" can still be incorrect, unusable, or
incompatible with your application. Evaluate engagement and usefulness as
separate outcomes.

## Choose a baseline

Pick the standard model and one research variant. Run both against the same
legitimate task set with comparable settings. The [local sample prompts](../examples/benign-eval-prompts.json)
are RouterHub-authored starting points, not a validated benchmark or a harmful
prompt suite.

Do not assume that a fixed-prompt persona isolates a weight-level change:
replacing system instructions changes the experiment itself.

## Record enough information to reproduce a run

- Exact API ID, date, endpoint, and advertised availability.
- Full non-sensitive prompt set and its revision.
- Sampling and output settings, including omitted defaults.
- Number of repetitions and any retried or failed requests.
- Request IDs where returned, measured latency, and reported token usage.
- Your rubric and whether a human reviewed the labels.

Model IDs can remain stable while hosted behavior changes. A dated run is
more informative than a model name without test conditions.

Keep raw responses separate from scoring notes so you can review disputed
labels without rerunning paid requests. Redact private information before
sharing either artifact.

## Use more than one score

| Dimension | Example question |
|---|---|
| Task completion | Did the response solve the requested legitimate task? |
| Unnecessary refusal | Did it decline a request that should be answerable under the test's defined policy? |
| Quality | Was it correct, well supported, and appropriately uncertain? |
| Instruction following | Did it follow the required format and system instructions? |
| Integration | Did streaming and any required function calls match the client contract? |
| Latency | How long did the task take, including retries? |
| Cost | What did all attempted requests cost per accepted result? |

Document ambiguity rather than forcing every output into a binary win/loss.
Use human review where the scoring affects important product or safety decisions.

## Keep result claims proportional

Publish the number of test cases, failures, and repeats along with averages.
Do not cherry-pick one successful response and call a model refusal-free.
If you share examples publicly, remove secrets and personal information.

This repository ships evaluation guidance and sample inputs. It does not
publish live benchmark scores or independently verify hosted weights.

[Choose a variant](./model-variants.md) · [Run a request](./api-quickstart.md) · [Overview](../README.md)
