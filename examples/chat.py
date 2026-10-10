"""Send one paid RouterHub chat request using the Python standard library."""

import argparse
import json
import os
import sys
from urllib import error, request


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="glm-5.3-abliterated")
    parser.add_argument("--prompt", default="Reply with OK.")
    args = parser.parse_args()
    key = os.environ.get("ROUTERHUB_API_KEY")
    if not key:
        parser.error("Set ROUTERHUB_API_KEY locally before sending a request.")

    payload = {
        "model": args.model,
        "messages": [{"role": "user", "content": args.prompt}],
    }
    call = request.Request(
        "https://routerhub.si/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with request.urlopen(call, timeout=120) as response:
            result = json.load(response)
    except error.HTTPError as exc:
        print(f"Request failed with HTTP {exc.code}; check the model, account, and API documentation.", file=sys.stderr)
        return 1
    except (error.URLError, TimeoutError, ValueError) as exc:
        print(f"Request could not be completed ({type(exc).__name__}).", file=sys.stderr)
        return 1

    choices = result.get("choices") if isinstance(result, dict) else None
    if not choices:
        print("No text choice was returned; inspect the model's supported response format.", file=sys.stderr)
        return 1
    print(choices[0].get("message", {}).get("content") or "")
    if result.get("usage"):
        print(json.dumps({"usage": result["usage"]}), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
