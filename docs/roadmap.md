# Milestones

## v0.1 — Object identity, open requests, visible limits

Deliver a small object-document convention, generic object/supervisor skills, and
a Hermes example. Test normal diagnosis, missing observations, and a shared contract
failure. Establish whether progressive disclosure preserves answer quality and
reduces supervisor context. Measure total cost separately. The initial repository
provides the manual rehearsal; live Hermes evaluation remains to be done.

## v0.2 — Generate Agent Objects from deployment definitions

Make deploying or updating a service also produce/update its agent representation.
The user maintains the existing infrastructure declaration; a generator derives the
object's identity, location, source references, documentation pointers, runtime
bindings, and known relationships. Hermes is the first deployment target.

Start with one adapter for the homelab's actual service registry and deployment
layout, once supplied. Do not invent a replacement catalog or treat this fixture's
fields as the real registry schema. The expected path is:

```text
service registry + deployment declarations + small agent opt-in
    -> inspect and derive an object draft
    -> validate references and preview changes
    -> deployment installs object context and scoped runtime bindings
    -> capability probe verifies what the object can actually inspect
```

Separate what can be derived from what must be authored. Container location, image,
mounts, repository paths, and declared dependencies can often be extracted.
Responsibility, meaningful diagnostic boundaries, and approved mutation authority
may need an explicit annotation. A model may suggest prose/docs, with provenance;
it must not invent access grants or silently turn a guess into a known dependency.

Preserve human-authored responsibility/runbooks in separate inputs or stable sections.
Generation should be deterministic for structured deployment data and report unknowns.
Persist a source revision and generator version; never copy secrets into output.

Acceptance cases:

1. Adding an opted-in service produces a usable object document and runtime binding
   plan without manually assembling a Hermes identity.
2. Moving a service to another container changes location/bindings while preserving
   its logical identity. Recreating a resource with a different meaning is explicit.
3. Re-running generation on unchanged inputs produces no changes; invalid or missing
   references fail validation rather than emitting a seemingly functional object.
4. Removing a service retires its route and access through the deployment lifecycle;
   in-flight work receives an explicit unavailable/retired result.
5. Shared dependencies produce relationship references without granting their access.
6. Missing telemetry or failed capability probes are visible to the supervisor.
7. A dry run shows the exact diff and respects existing reviewed deployment flow.

The first v0.2 result should generate and deploy one Mosquitto object end to end.
Broader discovery, multiple deployment backends, and A2A publication follow only
after that adapter works. v0.2 generation automates the established v0.1 convention;
it does not redefine the project's primitive as a compiler.
