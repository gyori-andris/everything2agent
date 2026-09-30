# Synthetic infrastructure experiment

Question: **Why is the bathroom Shelly unavailable?**

The directory below is all the supervisor initially needs. Each worker receives
only its own OBJECT.md, personality, relevant context, and scenario packet. The supervisor
can ask follow-ups and receive excerpts. These files describe fictional observations
based on an illustrative homelab layout, not measurements of the user's systems or
a backend required by the Agent Objects convention.

| ID | Semantic object | Document |
| --- | --- | --- |
| home-assistant | Entity state, integration configuration, application observations | [OBJECT.md](home-assistant/OBJECT.md) |
| mosquitto | Broker behavior, MQTT clients, broker configuration and telemetry | [OBJECT.md](mosquitto/OBJECT.md) |
| network | Device reachability and observed network attachment | [OBJECT.md](network/OBJECT.md) |

Three cases exercise different stopping behavior:

- `device-unreachable`: current observations narrow the fault to the device or its attachment; power versus Wi-Fi remains unknown.
- `stale-telemetry`: an old successful collection cannot establish present broker health. The investigation must remain unresolved.
- `topic-mismatch`: both services appear healthy, but their shared topic contract disagrees. Looking only inside one boundary misses the cause.

The [scenario files](scenarios/) contain separate packets plus evaluator-only
expectations. Do not give entire scenario files to workers or the supervisor in
the bounded trial. The packet reader separates them for manual use, but is not a
security sandbox. Use separate sessions with pasted packets for a blind trial.

Run `python3 scripts/rehearse.py start topic-mismatch` from the repository root.
Then use `packet` for the selected workers. Consult `reveal` only after saving the
supervisor's final answer. See [the evaluation plan](../../evals/README.md).
