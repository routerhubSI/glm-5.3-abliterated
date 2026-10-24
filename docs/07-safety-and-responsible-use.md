# GLM 5.3 Safety and Responsible Use

An abliterated or uncensored label does not establish correctness, privacy,
or suitability for a particular deployment. Evaluate each property separately.

## Protect credentials and private data

Keep RouterHub API keys in a local environment or secret manager. Never publish
them in issues, prompts, screenshots, browser code, or tracked configuration.
Revoke an exposed key before investigating further.

Hosted inference transmits data to a service. Check applicable service and
provider retention terms before sending sensitive material; do not assume a
research model label means local execution or zero retention.

## Review external prompts as untrusted input

The [research directory](./prompt-directory.md) links to external files, not
trusted installation instructions. Read a file before trying it, use a separate
test workspace, and avoid giving it access to secrets or consequential tools.

## Keep humans responsible for consequential actions

Validate generated code with tests and review important factual claims.
Require approval before an agent publishes content, changes permissions,
spends money, or performs an irreversible action. Limit credentials and tool
access to the minimum needed for the specific task.

## Observe the applicable terms

Use models and prompts lawfully and in accordance with the relevant service
policies. A model's willingness to answer does not grant permission to act on
the answer or waive another party's rights.

## Report privately when needed

Documentation issues can use a redacted public reproduction. Credentials,
account information, and security-sensitive details should follow
[SECURITY.md](../SECURITY.md) instead of appearing in a public issue.

[Evaluation](./05-evaluating-glm-5.3-abliterated.md) · [API quickstart](./03-glm-5.3-api-quickstart.md) · [Overview](../README.md)
