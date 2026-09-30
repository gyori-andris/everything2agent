#!/usr/bin/env python3
"""Prepare object-specific synthetic packets; never invokes a model or infrastructure."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "homelab"
DIRECTORY = {
    "home-assistant": "Entity state, integration configuration, application observations",
    "mosquitto": "Broker behavior, MQTT clients, configuration and telemetry",
    "network": "Device reachability and observed network attachment",
}


def scenarios():
    return sorted(path.stem for path in (EXAMPLE / "scenarios").glob("*.json"))


def scenario_data(name):
    if name not in scenarios():
        raise ValueError(f"Unknown scenario: {name}")
    return json.loads((EXAMPLE / "scenarios" / f"{name}.json").read_text())


def render_start(name):
    data = scenario_data(name)
    directory = "\n".join(f"- {key}: {value}" for key, value in DIRECTORY.items())
    return f"SYNTHETIC TRIAL\n\n{data['question']}\n\nObject directory:\n{directory}"


def render_packet(name, object_id):
    if object_id not in DIRECTORY:
        raise ValueError(f"Unknown object: {object_id}")
    data = scenario_data(name)
    document = (EXAMPLE / object_id / "OBJECT.md").read_text()
    personality = (EXAMPLE / object_id / "PERSONALITY.md").read_text()
    # Context is explicitly limited to the example's authored local knowledge file.
    context_path = EXAMPLE / object_id / "knowledge.md"
    context = context_path.read_text() if context_path.exists() else "No additional fixture context."
    return (
        f"SYNTHETIC WORKER PACKET — {object_id}\n\n{document}\n"
        f"Personality:\n{personality}\n\nContext:\n{context}\n\n"
        f"Evidence:\n{data['packets'][object_id]}\n\n"
        "Handle the supervisor's separately supplied request for this semantic object. "
        "Use the evidence where relevant. Preserve useful owned work and return the "
        "smallest unresolved external question for delegation. Further unavailable "
        "observations must be reported as unavailable."
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    for command in ("start", "packet", "reveal"):
        sub = commands.add_parser(command)
        sub.add_argument("scenario", choices=scenarios())
        if command == "packet":
            sub.add_argument("object", choices=list(DIRECTORY))
    args = parser.parse_args()
    if args.command == "list":
        print("\n".join(scenarios()))
    elif args.command == "start":
        print(render_start(args.scenario))
    elif args.command == "packet":
        print(render_packet(args.scenario, args.object))
    else:
        print("EVALUATOR ONLY — reveal after recording the final answer")
        print(json.dumps(scenario_data(args.scenario)["evaluation"], indent=2))


if __name__ == "__main__":
    main()
