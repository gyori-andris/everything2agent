# Hermes reference trial

This is a manual integration recipe. No Hermes profiles, remote peers, tools, or
credentials are installed by this repository. Validate your deployed Hermes version's
skill-loading and delegation features before automating this flow. The skill files
use the conventional SKILL.md name/description frontmatter and Markdown instructions.

## Conduct one trial

1. Start an isolated supervisor session with `skills/supervise-objects/SKILL.md`
   and the output of `python3 scripts/rehearse.py start <scenario>`.
2. When it asks an object a question, start a separate worker session with
   `skills/agent-object/SKILL.md`, that question, and the corresponding `packet`
   output. Sessions must not receive the entire repo or evaluator expectations.
3. Return the worker's response to the supervisor. Relay follow-ups to the same
   worker session where possible. The fixture has no hidden live tools: unavailable
   evidence stays unavailable.
4. Stop after resolution or six worker calls. Save the final answer and usage for
   every session before running `reveal`.
5. Grade using `evals/README.md`, then repeat as a single-agent baseline.

Manual relaying is sufficient to test the convention. A later Hermes adapter can
perform the same handoffs using the supported delegation mechanism of a pinned
Hermes version. A2A is optional if objects are served independently. Do not invent
A2A cards or Hermes configuration and label them compatible without testing them.

## Hosting a real object session later

The session resolves the object's source and documentation references and receives
whatever runtime environment the host supplies. These facilities are not declared or
granted by OBJECT.md. A host may still enforce security around credentials, mounts,
or sockets, but that mechanism remains outside the semantic Agent Object convention.
Full availability of relevant source and documentation is compatible with a small
prompt: retain context addresses and retrieve what the request needs.

Pin resource revisions and record observation timestamps. Keep model/provider
selection in runtime configuration so the object identity stays portable. Runtime
state and secrets stay outside the object document and repository.

See the [generic roadmap](../../docs/roadmap.md). Hermes is one possible runtime
experiment, not the deployment model of the primitive.
