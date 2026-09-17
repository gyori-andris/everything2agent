# Agent Objects

Give an existing resource an agent facet: a scoped personality, responsibility,
and context. Ask it open questions. Let a supervisor coordinate across objects
without loading every object's internals into its own context.

`everything2agent` is an early, portable convention and a Hermes reference
experiment. **Status: runnable fixture rehearsal and draft skills; live Hermes
integration and token savings are not yet validated.**

## The primitive

An **Agent Object** represents a particular resource: a containerized service,
repository, dataset, or tool within a biology pipeline. `OBJECT.md` describes its
identity, roots, personality, context, and related objects. The resource stays
where it is. Its agent can be instantiated when needed.

Identity and object roots are explicit. Questions and reasoning remain open-ended.
There is no mandatory method catalog, capability registry, or domain-specific
answer schema.
An agent must explain the scope and limits of its answer, in ordinary language.

```text
Supervisor ── open question ──> Agent Object
                                 ├── scoped personality
                                 ├── source, documentation, runtime roots
                                 └── session observations
Supervisor <── finding + evidence + limits + useful next check
```

The intended benefit is both bounded responsibility and substantially less
context in the supervisor. Whether total tokens, latency, and correctness improve
is an experimental question. A short answer that hides missing evidence is a failure.

## Start here

- [SPEC.md](SPEC.md): the small, draft convention and boundary philosophy.
- [Agent skill](skills/agent-object/SKILL.md): how to act as an object.
- [Supervisor skill](skills/supervise-objects/SKILL.md): when to accept, probe, or escalate.
- [Homelab example](examples/homelab/README.md): three objects and a Shelly incident.
- [Evaluation plan](evals/README.md): blind spots, progressive disclosure, and token accounting.
- [Hermes recipe](integrations/hermes/README.md): how to conduct the first manual trial.

## Run the fixture rehearsal

Requires Python 3.11+; no dependencies, credentials, network, or model calls.

```sh
python3 scripts/rehearse.py list
python3 scripts/rehearse.py start stale-telemetry
python3 scripts/rehearse.py packet stale-telemetry mosquitto
python3 scripts/rehearse.py reveal stale-telemetry
python3 -m unittest discover -s tests
```

`start` prints only the supervisor's question and object directory. `packet`
prints one object's instructions and scoped evidence for a worker. `reveal`
prints evaluator-only expectations **after** an investigation. This prepares a
manual experiment; it does not run agents or prove isolation.

## Repository shape

```text
SPEC.md                    Draft convention
skills/                    Object and supervisor behaviors
examples/homelab/           Object documents, context, synthetic scenarios
integrations/hermes/       Reference experiment recipe
evals/                     Evaluation and usage-record template
scripts/rehearse.py        Role-specific fixture packet reader
tests/                     Checks for packet leakage and fixture integrity
```

## Relationship to existing work

[OKF](https://github.com/GoogleCloudPlatform/open-knowledge-format) inspires the
Markdown-first format and separation of convention from reference implementation.
Our object frontmatter uses its extensible concept-document style; this is a
draft local extension, not an upstream OKF standard.
[MCP](https://modelcontextprotocol.io/docs/learn/architecture) can supply tools
and resources. [A2A](https://a2a-protocol.org/latest/topics/key-concepts/) can
transport requests between separately served agents. Neither is required for a
local rehearsal. Hermes is the first intended host.

[Paper2Agent](https://github.com/jmiao24/Paper2Agent) and
[NVIDIA OO Agents](https://github.com/NVIDIA-NeMo/labs-OO-Agents) are inspirations
for turning existing artifacts and functional units into agent-accessible objects.

## Next milestones

v0.1 tests the three scenarios through Hermes, comparing answer quality and usage
against one agent with the same evidence and session access.

**v0.2 focuses on automatically attaching Agent Objects to deployed resources.**
It discovers roots and relationships from existing deployment data, while keeping
the personality authored with the object. See the [roadmap and acceptance
cases](docs/roadmap.md).
