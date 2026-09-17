# Agent Objects — draft 0.1

## Purpose

An Agent Object is an existing resource represented by an agent with a scoped
personality, explicit responsibility, and relevant context. Object2Agent is the
act of attaching that agent facet to an object. This draft describes documents and
behavior, not a compiler or a new runtime.

## Object document

Each object has an `OBJECT.md` containing YAML frontmatter and Markdown prose.
`type: Agent Object`, `title`, and `resource` describe the concept. A local
`agent_object` extension records `version`, a stable `id`, and optional `roots`,
`personality`, `context`, and `related` references. IDs identify deployed instances:
two brokers using the same software are different objects. Paths are relative to
the document.

The personality explains how the agent represents this object: its responsibility,
way of working, external dependencies, and known limitations. It may link source,
runbooks, API descriptions, or OKF knowledge. Context references are retrieved as
needed, not all inserted into every prompt. The document describes a resource; it
does not embed live state.

Roots identify the source, documentation, runtime, or data that make up the object.
They are addresses and context anchors, not an access-control language. A Hermes
session supplies its actual working directory and tools. A skill alone cannot
isolate filesystem or container access, and this convention does not attempt to do so.

## Where typing stops

Identity, roots, references, and the underlying tools' arguments need stable
structure. The outer interaction accepts an open question or request. It does not
require enumerating every question the object can answer. Existing tool schemas
keep their own validation; this convention does not replace them.

Responsibility and related-object prose help route work; they are neither exhaustive
method lists nor evidence of available access. On each request, the agent checks
what it can actually inspect in its current session. Unsupported work gets an
explicit limit, not an invented result.

Replies use ordinary language. They convey an answer, supporting observations,
their coverage and freshness, remaining uncertainty, and a useful next check when
needed. No numeric confidence score or mandatory JSON finding is required.
Structured results may be added by an application that has a concrete consumer.

## Responsibility and access

An object session may have deep access to its own source, documentation, and runtime.
Source knowledge, runtime visibility, and mutation authority are separate: having
the source does not mean the running configuration matches it. The session's tools
and host policy determine what it can change. The example permits inspection only.

Containment, dependency, and delegation differ. Being located in CT111 does not
force every question through a CT111 agent. Related objects form useful navigation
links; they need not cover every real dependency. A supervisor may discover that
the directory is incomplete and report that explicitly.

## Preventing silent limitations

Every answer must make material evidence limitations visible. Distinguish:

- The question was answered with current, relevant observations.
- Only part of the question was answered.
- Required evidence or access is missing.
- The question belongs partly or entirely to another object.

“Broker healthy” does not establish client connectivity. “No errors” does not mean
error-free if the collector stopped. “I cannot see it” does not mean it is absent.
Source configuration does not establish current runtime state. Absence claims
must name the observed time window and whether collection covered it.

The supervisor compares the reply against the user's question, not just the
worker's chosen subquestion. It follows up on stale data, missing coverage,
contradictions, unsupported causal claims, or an unexplained symptom. It asks a
discriminating next question instead of automatically requesting all raw logs.

Self-reported limits cannot guarantee completeness. Evaluation includes workers
that omit a caveat; the supervisor must sometimes request the observation source,
timestamp, and collection status independently. Periodic audits of apparently
healthy results test this behavior. Independent observations help detect shared
blind spots; repeated summaries from the same source do not.

## Progressive disclosure and stopping

Start with a concise answer plus evidence references and material limits. Retrieve
specific excerpts, configuration, or another object's observations when these can
distinguish competing explanations. Direct shared telemetry access is allowed
when the deployment grants it. An investigator is an optional role, not a primitive.

One supervisor initially owns cross-object routing, avoiding peer call loops.
Use a per-investigation call/token budget. Stop when the question is supported,
when a named missing observation blocks progress, or when the budget is exhausted.
The latter two outcomes are explicitly unresolved and name the next useful check.
Do not truncate uncertainty merely to meet a summary-size target.

## Portability

An object can run in a Hermes session, another agent host, or behind A2A. Its tools
may come from MCP or local adapters. Transport and process count are deployment
choices. Object identity persists independently of any particular model session.
No new scheduling, profile compiler, Kubernetes reconciliation, or distributed
transaction system is specified here.
