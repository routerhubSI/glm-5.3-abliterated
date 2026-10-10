# Connect to the GLM 5.3 API

RouterHub's documented base URL is `https://routerhub.si/v1`. The GLM entries
covered here use `/chat/completions` with bearer-token authentication.
Running the examples spends prepaid credits; checking their syntax does not.

## Account and key

[Create an account](https://routerhub.si/register?next=onboarding&utm_source=github&utm_medium=docs&utm_campaign=glm-5.3-abliterated), add prepaid credits, and create an API key.
Set the key locally as `ROUTERHUB_API_KEY`. Do not commit its value to a file
or put it into a public issue. Consult [models.json](https://routerhub.si/models.json)
for the exact current model ID and required protocol.

## Python SDK

Install with `pip install openai`. The following is a complete short request:

```python
import os
from openai import OpenAI

api = OpenAI(
    api_key=os.environ["ROUTERHUB_API_KEY"],
    base_url="https://routerhub.si/v1",
)
completion = api.chat.completions.create(
    model="glm-5.3-abliterated",
    messages=[{"role": "user", "content": "Reply with OK."}],
)
print(completion.choices[0].message.content)
```

Prefer a standard-library-only example? Use [examples/chat.py](../examples/chat.py).
Its `--help` option does not make a request:

```bash
python examples/chat.py --help
python examples/chat.py --model glm-5.3-abliterated --prompt "Reply with OK."
```

## JavaScript SDK

Install with `npm install openai`, then save this as an ES module such as
`request.mjs`. Run it only after setting your private key in the environment.

```javascript
import OpenAI from "openai";

const api = new OpenAI({
  baseURL: "https://routerhub.si/v1",
  apiKey: process.env.ROUTERHUB_API_KEY,
});
const completion = await api.chat.completions.create({
  model: "glm-5.3-abliterated",
  messages: [{ role: "user", content: "Reply with OK." }],
});
console.log(completion.choices[0].message.content);
```

## cURL

The repository includes a small [request body](../examples/request.json):

```bash
curl https://routerhub.si/v1/chat/completions \
  -H "Authorization: Bearer $ROUTERHUB_API_KEY" \
  -H "Content-Type: application/json" \
  --data @examples/request.json
```

Run that command from the repository root so the relative path resolves.

## Streaming text with Python

Use the same `api` instance from the Python SDK example:

```python
chunks = api.chat.completions.create(
    model="glm-5.3-abliterated",
    messages=[{"role": "user", "content": "Explain an API gateway in one paragraph."}],
    stream=True,
)
for chunk in chunks:
    if chunk.choices:
        part = chunk.choices[0].delta.content
        if part:
            print(part, end="", flush=True)
```

Some streaming events contain metadata instead of text. Do not assume every
event has a nonempty `choices` list. Check streaming support separately if
you select another model.

## Verify the result

- Confirm the response is for your requested model entry.
- Inspect the recorded cost in your RouterHub account.
- Check whether your input was ordinary chat, a persona request, or an
  instruction-sensitive workflow. Personas can replace system messages.
- Keep a redacted timestamp and request ID when diagnosing failures.

## Common failures

| Failure | First check |
|---|---|
| Authentication error | Environment key is present, current, and sent as a bearer token |
| Model unavailable | Exact ID and availability in the public catalogue |
| Incorrect endpoint | GLM request is going to Chat Completions rather than Messages or Responses |
| Invalid request | JSON syntax, message roles, supported fields, and model limits |
| Rate limit | Error details, concurrency, and bounded retry policy |
| Billing restriction | Account balance and checkout/usage information |

Do not repeatedly retry a billing or authentication failure. If you contact
support, redact credentials and private prompt text first.

[Model variants](./model-variants.md) · [Client compatibility](./tool-compatibility.md) · [RouterHub GLM pricing](https://routerhub.si/guides/glm?utm_source=github&utm_medium=docs&utm_campaign=glm-5.3-abliterated)
