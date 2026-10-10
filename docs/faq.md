# RouterHub GLM API FAQ

## Which ID selects the abliterated research entry?

The catalogue lists `glm-5.3-abliterated`. Use the exact ID with Chat
Completions and check [current availability](https://routerhub.si/models.json)
before depending on it.

## Is "uncensored" the same as "abliterated"?

No. One is a broad product label; the other describes a family of weight-level
methods. RouterHub's `glm-5.3-uncensored` entry is a fixed-prompt persona, not
a separately verified uncensored fine-tune. Read [model variants](./model-variants.md)
for the instruction-handling difference.

## Will an abliterated model answer every request?

No such guarantee is made here. Hosted behavior depends on the model,
instructions, implementation, and applicable service policies. Test your
legitimate tasks rather than relying on a label.

## Do all models use the same API protocol?

No. One account can include models supporting Chat Completions, Messages,
or Responses. Match your client to the entry's supported protocol using the
[compatibility guide](./tool-compatibility.md).

## Are the prompt files copied into this repository?

No. The [prompt directory](./prompt-directory.md) links to externally hosted
community files. They retain their own terms and can change independently.
The small [local evaluation sample](../examples/benign-eval-prompts.json) is
separate, original RouterHub material.

## How is model usage paid for?

RouterHub offers prepaid, per-token usage. Add credits, create a key, and
review consumption in your account. Card and crypto options are shown at
checkout. The [GLM guide](https://routerhub.si/guides/glm) publishes token rates;
cached-input pricing applies only where supported and reported.

## Is hosted use equivalent to running a model privately on my computer?

No. Requests are transmitted to a hosted service. The research entries state
that provider retention terms apply. Check those terms before sending private
data and do not assume zero retention.

## Does this repository prove which model weights are served?

No. It explains published catalogue entries and how to send requests. It does
not independently inspect the hosted weights or claim a live benchmark result.

## Where should I report a problem?

For a documentation problem, open a redacted issue. For credentials, account
data, or a security concern, follow [SECURITY.md](../SECURITY.md) rather than
posting private information publicly.

[RouterHub](https://routerhub.si/?utm_source=github&utm_medium=docs&utm_campaign=glm-5.3-abliterated) · [Quickstart](./api-quickstart.md)
