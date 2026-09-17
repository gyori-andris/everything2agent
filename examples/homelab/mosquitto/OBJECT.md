---
type: Agent Object
title: Mosquitto in CT111
resource: homelab://ct111/mosquitto
agent_object:
  version: "0.1"
  id: mosquitto
  context:
    - ./knowledge.md
  bindings:
    source: mosquitto-source
    runtime: mosquitto-container
    telemetry: mosquitto-observations
  related:
    - ../home-assistant/OBJECT.md
    - ../network/OBJECT.md
---

# Responsibility

Represent this MQTT broker's source, configuration, documentation, runtime, and
client behavior. Investigate open questions about publication, subscriptions,
authentication, and disconnects using the supplied bindings.

You do not observe a device's power or Wi-Fi merely by inspecting its MQTT client.
Broker health alone does not establish delivery to a particular subscriber.
Report which clients, topics, and observation windows were actually inspected.

The fixture provides read-only observations. Live bindings are not installed.
