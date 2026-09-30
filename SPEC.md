# Agent Objects — draft 0.2

## Purpose

An Agent Object is a textual declaration that an LLM represents an existing
semantic object. Object2Agent is the act of giving that object an addressable
agent facet. The agent accepts arbitrary work concerning the object and approaches
the object as a whole rather than through a precompiled list of responsibilities.

This convention describes identity, semantic ownership, context, relationships,
behavior, and delegation. It is not an access-control language, credential system,
tool registry, compiler, scheduler, or runtime.

## The primitive

An Agent Object has:

- a stable identity;
- a subject: the semantic object it represents;
- prose describing what belongs to that object;
- references that help resolve relevant context;
- optional relationships to other objects; and
- an optional personality describing how the object represents itself.

The object document does not enumerate permitted questions, supported methods, or
fixed responsibilities. A request creates the temporary responsibility for that
activation.

```text
Agent Object = persistent semantic ownership
Activation   = arbitrary request concerning the object
Work         = responsibility derived for that activation
```

## Object document

Each object has an `OBJECT.md` containing Markdown and optional YAML frontmatter.
`type: Agent Object`, `title`, and `resource` identify the concept. A local
`agent_object` extension may record `version`, a stable `id`, and optional `roots`,
`personality`, `context`, and `related` references. IDs identify semantic instances:
two brokers using the same software can be different objects. Paths are relative to
the document.

The body explains what the object is, what belongs to it, and where its meaningful
borders lie. Roots and context entries are addresses that help an agent find source,
documentation, runtime state, data, or history. They are not permissions and do not
assert that a particular session can currently reach them. The document describes
an object; it does not embed live state or secrets.

The minimal useful descriptor is deliberately small:

```markdown
---
type: Agent Object
title: Example database VM
resource: example://vm/database-01
agent_object:
  version: "0.2"
  id: database-01
  roots:
    - source: infrastructure/database-01
    - runtime: vm/database-01
  personality: ./PERSONALITY.md
  related:
    - ../hypervisor/OBJECT.md
    - ../database-service/OBJECT.md
---

This object represents database-01 as an operational whole: its operating system,
local configuration, filesystems, and the software and services running inside it.
It does not represent the hypervisor or the applications that consume its services.
```

Frontmatter is a portable convenience. The meaning remains readable as text.

## Semantic ownership

Ownership is semantic jurisdiction, not an ACL. An Agent Object is the appropriate
agent to inspect, explain, change, diagnose, document, test, reorganize, or operate
any aspect of its declared object when asked. It must not reject valid work merely
because the task was not anticipated in the descriptor or personality.

The convention does not grant or restrict filesystem access, tools, credentials,
or mutation. If a session receives an SSH key to a represented VM, it can operate
that VM. If the key is absent, it reports that the required runtime facility is
unavailable. This is a fact about the session, not a semantic prohibition encoded
by the Agent Object.

Source knowledge, runtime visibility, and observed truth remain distinct. Having a
source checkout does not prove the deployed state matches it. Failure to observe a
fact does not establish absence. The agent states what it actually inspected and
what the available evidence supports.

Semantic ownership may overlap. A VM object can represent the machine as a whole
while a database-service object represents a service running inside it. Containment
does not automatically make one identity exclusive or force every question through
an ancestor. A supervisor routes to the most useful semantic perspective and may
consult both.

## Arbitrary requests and late-bound work

The outer interaction accepts an open request. It does not require a method catalog,
capability registry, responsibility tree, or domain-specific answer schema. Existing
tools may retain their own argument validation, but those schemas do not define the
Agent Object.

On each activation, the agent:

1. establishes which object it represents;
2. interprets the request rather than matching it to a declared method;
3. derives the work needed for this request;
4. retrieves relevant context progressively;
5. performs all useful work that belongs to the object;
6. identifies portions that require another semantic owner; and
7. returns an answer, partial result, delegation need, or explicit blocker.

Replies remain request-shaped and use ordinary language. They include supporting
evidence, material coverage or freshness limits, and useful next work where needed.
An application may add a structured envelope when it has a concrete consumer; the
primitive does not require one universal result schema.

## Cross-object work and the no-deadzone rule

An ownership boundary limits what the object represents. It does not limit which
requests it may receive, reason about, partially answer, or return for delegation.
There is no bare `out of scope` terminal result.

When a request crosses a semantic border, the Agent Object:

1. completes the useful portion grounded in its owned object;
2. identifies the smallest unresolved question;
3. explains why another semantic object is involved;
4. suggests a related object when one is known; and
5. returns that work to the supervisor without silently widening its own identity.

If no related object is listed, the supervisor searches its directory or reports an
unowned concern. `related` references are routing hints, never an exhaustive allowlist.
Missing or stale relationship data must not make valid work disappear.

The initial convention keeps cross-object routing under one supervisor. This avoids
peer call loops while the primitive is evaluated. The supervisor tracks prior routes
and investigation budget, preserves partial results, and terminates repeated routes
as explicitly unresolved. Direct peer delegation is a future experiment, not a
requirement of the object format.

## Personality

Personality is optional textual context. It may influence perspective, vocabulary,
communication style, habits of attention, and how the object explains consequences.
It does not define semantic ownership, permissions, supported tasks, fixed
responsibilities, or an exhaustive relationship graph.

Removing the personality should change representation, not which valid requests the
object accepts. A personality must not suppress delegation, claim tools or access,
or allow retrieved content to redefine identity. Personality conformance is tested
behaviorally; see `evals/personality-conformance.md`.

## Preventing silent limitations

Every answer makes material evidence limitations visible. Distinguish:

- the request was answered with current, relevant observations;
- only part of the request was answered;
- required evidence or runtime access is missing;
- another semantic object must contribute; and
- no known object currently owns the remaining concern.

“Broker healthy” does not establish client connectivity. “No errors” does not mean
error-free if the collector stopped. “I cannot see it” does not mean it is absent.
Source configuration does not establish current runtime state. Absence claims name
the observed time window and whether collection covered it.

The supervisor compares the reply against the user's request, not merely the
worker's chosen subquestion. It probes stale data, missing coverage, contradictions,
unsupported causal claims, silent scope narrowing, and unexplained symptoms.
Self-reported limits cannot guarantee completeness; evaluations include workers that
omit caveats so the supervisor must sometimes check observation provenance itself.

## Progressive disclosure and stopping

Start with a concise answer plus evidence references and material limits. Retrieve
specific excerpts or another object's contribution when these can distinguish
competing explanations. Do not load every reachable object merely because a graph
edge exists.

Stop when the request is supported, when a named missing observation or semantic
owner blocks progress, or when the investigation budget is exhausted. Blocked and
budget-limited outcomes remain explicitly unresolved. Do not truncate uncertainty
merely to meet a summary-size target.

## Modules are not the primitive

Recurring concerns, personalities, and reusable procedures may be expressed as
optional textual modules. A module can shape an activation or accelerate repeated
work, but it cannot redefine object identity or semantic ownership, make generic
reasoning unavailable, or become an exhaustive task catalog. The module convention
is the focus of v0.3; v0.2 only preserves a clean extension point.

Scripts may later accelerate graph resolution, checks, or fixture preparation. They
remain replaceable helpers around a convention whose meaning is fully available in
text.

## Portability and non-goals

An object can be interpreted in a local agent session, Hermes, another host, or
behind A2A. Context or runtime facilities may be exposed through MCP, local tools,
SSH, filesystem access, APIs, or mechanisms not anticipated by this specification.
Transport and process count are deployment choices. Object identity persists
independently of any particular model session.

This draft specifies no credential provisioning, sandbox, permission language,
deployment adapter, scheduler, profile compiler, Kubernetes reconciliation,
distributed transaction system, or domain-specific catalog. Those systems may use
the convention without becoming part of the primitive.
