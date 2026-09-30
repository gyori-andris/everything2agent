---
type: Agent Object
title: IoT network
resource: homelab://network/iot
agent_object:
  version: "0.2"
  id: network
  roots:
    - network: iot
  personality: ./PERSONALITY.md
  related:
    - ../mosquitto/OBJECT.md
---

This object represents the IoT network as a semantic whole: its addressing,
attachment, routing, transport behavior, and network-specific documentation. It does
not represent device power, firmware, or application semantics. The fixture supplies
synthetic observations and no live runtime.
