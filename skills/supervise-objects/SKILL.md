---
name: supervise-objects
description: Delegate open infrastructure questions to Agent Objects, probe incomplete evidence, and synthesize an answer while tracking context and investigation cost.
---

# Supervise Agent Objects

Start from the user's question and a small directory of object identities and
responsibilities. Select the most relevant objects directly; infrastructure nesting
does not require calling every ancestor. Pass a bounded question and enough task
context. Use the same object identity on follow-up; fresh sessions may need the
earlier finding and evidence references supplied explicitly.

For every result ask: does this explain the symptom, or only establish that one
component appears healthy? What evidence supports it? Does that evidence cover the
incident window and failure mode? Is actual collection working? Are there conflicting
observations? Does the worker's current session actually cover the claim?

Probe when the answer is partial, freshness or coverage is unclear, a causal claim
exceeds the evidence, or multiple observations disagree. Ask a discriminating
question such as “Was collection functioning during that interval?” or “Which
dependency contract did each side actually use?” Retrieve a narrow evidence excerpt
when summaries conflict. Do not route automatically to networking just because a
device is missing from MQTT.

For a causal conclusion based on absent events, require the relevant time window
and collection status even if the worker omitted that caveat. For a proposed fix,
verify the claimed cause against at least one relevant observation beyond a generic
health indicator. These checks reduce, but cannot eliminate, hidden blind spots.

Keep routing under one supervisor in the initial experiment. Track questions already
asked and evidence already obtained. A new agent repeating the same stale source
is not independent corroboration. Related-object links are hints; an unlisted owner
or missing object is a valid unresolved outcome.

Default trial budget: six worker calls including follow-ups. A budget limit is a
reason to report unresolved work, never a reason to fabricate closure. Record worker
and supervisor usage separately. Summarize the answer, evidence, remaining limits,
and any next step. Keep changes as proposals in this example.
