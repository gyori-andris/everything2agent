# Milestones

## v0.1 — Object identity, open requests, visible limits

Deliver a small object-document convention, generic object/supervisor skills, and
a Hermes example. Test normal diagnosis, missing observations, and a shared contract
failure. Establish whether progressive disclosure preserves answer quality and
reduces supervisor context. Measure total cost separately. The initial repository
provides the manual rehearsal; live Hermes evaluation remains to be done.

## v0.2 — Attach Agent Objects to deployment definitions

Make deploying or updating a service also attach or update its agent facet. The
user maintains the existing infrastructure declaration; an adapter discovers the
object's location, source roots, documentation pointers, and known relationships.
Its personality remains authored with the object. Hermes is the first deployment
target.

Start with one adapter for the homelab's actual service registry and deployment
layout, once supplied. Do not invent a replacement catalog or treat this fixture's
fields as the real registry schema. The expected path is:

```text
existing deployment declarations + object personality + small agent opt-in
    -> discover object roots and relationships
    -> validate references and preview attachment
    -> deployment starts a scoped object session when addressed
    -> session probe records what the current environment exposes
```

Separate what can be discovered from what must be authored. Container location,
image, mounts, repository paths, and declared dependencies can often be extracted.
The personality and meaningful diagnostic boundary remain authored. A model may
suggest prose/docs, with provenance; it must not turn a guess into a known dependency.

Preserve human-authored personality/runbooks as source files beside the object.
Discovery should report unknowns rather than filling them with guesses. Persist a
source revision and adapter version; never copy secrets into object context.

Acceptance cases:

1. Adding an opted-in service makes its authored personality addressable through a
   Hermes object session without manually assembling a new profile.
2. Moving a service to another container updates discovered roots while preserving
   its logical identity. Recreating a resource with a different meaning is explicit.
3. Re-running discovery on unchanged inputs produces no changes; invalid or missing
   roots fail validation rather than creating a seemingly functional object.
4. Removing a service retires its address through the deployment lifecycle;
   in-flight work receives an explicit unavailable/retired result.
5. Shared dependencies produce relationship references without granting their access.
6. Missing telemetry or failed session probes are visible to the supervisor.
7. A dry run shows the exact diff and respects existing reviewed deployment flow.

The first v0.2 result should attach and run one Mosquitto object end to end. Broader
discovery, multiple deployment backends, and A2A publication follow only after that
adapter works. v0.2 removes manual setup around the established v0.1 convention;
it does not turn the project's primitive into a compiler.
