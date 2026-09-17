---
type: Agent Object
title: IoT network
resource: homelab://network/iot
agent_object:
  version: "0.1"
  id: network
  roots:
    - network: iot
  personality: ./PERSONALITY.md
  related:
    - ../mosquitto/OBJECT.md
---

This object is the IoT network. Its personality describes how an agent represents
and works within the object. The fixture supplies synthetic, read-only observations;
it does not connect to the roots above.
