# Agent Objects

Give an existing resource a general-purpose agent facet with stable semantic
ownership and relevant context. Ask it arbitrary questions or request work. Let a
supervisor coordinate across objects without loading every object's internals into
its own context.

`everything2agent` is an early, portable convention and a Hermes reference
experiment. **Status: runnable fixture rehearsal and draft skills; live Hermes
integration and token savings are not yet validated.**

## The primitive

An **Agent Object** represents a particular semantic object: a containerized
service, repository, dataset, paper, experiment, or tool within a pipeline.
`OBJECT.md` describes its identity, ownership, context references, and related
objects. The resource stays where it is. Its agent can be instantiated when needed.

Identity and semantic ownership are persistent. Responsibility is derived from each
request. There is no mandatory method catalog, capability registry, permissions
model, or domain-specific answer schema. An agent must explain the evidence and
limits of its answer in ordinary language.

```text
Supervisor ── arbitrary request ──> Agent Object
                                    ├── semantic ownership
                                    ├── optional personality
                                    ├── context references
                                    └── session observations
Supervisor <── result + evidence + limits + delegation need
```

The intended benefit is coherent object-local work and substantially less context
in the supervisor. Semantic borders must not create work deadzones: an object does
its useful portion and returns cross-object work to the supervisor. Whether total
tokens, latency, and correctness improve is an experimental question. A short answer
that hides missing evidence is a failure.

## Start here

- [SPEC.md](SPEC.md): the v0.2 semantic-ownership convention.
- [Agent skill](skills/agent-object/SKILL.md): how to act as an object.
- [Supervisor skill](skills/supervise-objects/SKILL.md): when to accept, probe, or escalate.
- [Homelab example](examples/homelab/README.md): three objects and a Shelly incident.
- [Evaluation plan](evals/README.md): novel work, delegation, blind spots, and token accounting.
- [Personality conformance](evals/personality-conformance.md): prove that personality does not narrow ownership.
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
scripts/rehearse.py        Object-specific fixture packet reader
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
local rehearsal. Hermes is the first reference hosting experiment, not part of
the primitive.

[Paper2Agent](https://github.com/jmiao24/Paper2Agent) and
[NVIDIA OO Agents](https://github.com/NVIDIA-NeMo/labs-OO-Agents) are inspirations
for turning existing artifacts and functional units into agent-accessible objects.

## Roadmap

V0.1 introduced object identity, open questions, and visible evidence limits.

**V0.2 defines semantic ownership, late-bound work, no-deadzone delegation, and
personality conformance.** V0.3 explores optional textual modules for recurring
concerns and procedures. Later ideas remain an uncommitted concept collection until
experiments justify an order. See the [roadmap and acceptance cases](docs/roadmap.md).

The synthetic homelab scenario is one testing ground, not an architectural backend.
Infrastructure, SWE, and research objects should all be able to use the same textual
primitive.
