# Does the boundary help?

These are behavioral experiments, not a claim that Markdown enforces isolation.
The Python tests only check fixture partitioning. Actual session boundaries require
runtime tests after a real object session exists.

## Compare like with like

For each scenario, run a single-agent baseline given all object documents and all
evidence packets (but no evaluator expectations). Compare it with the supervisor
plus object workers. Use the same model initially to isolate the architecture;
then test a stronger supervisor and cheaper workers as a separate comparison.
Record model IDs, skill revision, settings, and session reuse. Repeat trials to
measure variance rather than drawing conclusions from one favorable run.

The tiny fixtures primarily test reasoning and disclosure. They may cost MORE
tokens with several agents. To test substantial savings, later use identical,
realistic source/docs/log corpora with on-demand retrieval in BOTH arms. Compare
recurring supervision as well as cold starts; do not handicap the baseline by
forcing it to read irrelevant files. Record the cost of keeping object context current.

## Behavioral acceptance

- Each conclusion is supported by an identifiable observation and its time/window.
- No case claims a stronger root cause than the available evidence supports.
- Stale telemetry produces an explicit missing-observation outcome.
- Topic mismatch is found by comparing both sides, despite healthy services.
- Device unreachability is not silently promoted to confirmed power failure.
- A missing object or an unlisted owner produces a visible next step.
- A budget stop is reported as unresolved, not successful.

After the normal stale-telemetry run, inject the abbreviated worker answer described
in its evaluator notes. The supervisor should request freshness/coverage before
accepting it. This tests a worker that FAILS to disclose limits, not merely one
obediently following the object skill. Also test conflicting summaries by asking
the supervisor to retrieve their underlying excerpts before choosing a cause.

## Measurements

Use [run-template.json](run-template.json) for each run; copy it outside the repo
or under ignored `runs/`. Fill usage from provider/runtime records. Null means
unmeasured, never zero. Store a transcript reference so a reviewer can audit it.

- Supervisor input/output tokens measure active supervision context cost.
- Total input/output tokens sum EVERY supervisor and worker call, including retries,
  delegated prompts, follow-ups, skill context, and summaries.
- Record cached input tokens as the subset of input tokens reported by the provider;
  do not add them a second time. If accounting differs, document the convention.
- Cost uses actual model rates/provider billing; latency is wall-clock time.
- Grade unsupported closure, omitted limits, correct next check, and overall answer.

For paired runs compute `1 - object_total_tokens / baseline_total_tokens`, and
separately the supervisor-token reduction. Report negative savings honestly.
Only compare savings on trials with acceptable answer quality. A smaller supervisor
prompt is not proof of lower total cost. Do not measure tokens by character count.
