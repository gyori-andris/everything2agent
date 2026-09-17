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

## Attaching a real object session later

The session starts at the object's source and documentation roots and receives the
runtime tools appropriate to that object. Scope credentials and mounts there. Access
to one container should not silently expose a host-wide container socket. Full
knowledge of the relevant source and docs is compatible with a small prompt: retain
access and retrieve what the question needs.

Pin resource revisions and record observation timestamps. Keep model/provider
selection in runtime configuration so the object identity stays portable. Runtime
state and secrets stay outside the object document and repository.

See [v0.2 object attachment](../../docs/roadmap.md) for the next milestone.
