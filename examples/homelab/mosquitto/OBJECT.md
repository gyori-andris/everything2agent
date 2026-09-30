---
type: Agent Object
title: Mosquitto in CT111
resource: homelab://ct111/mosquitto
agent_object:
  version: "0.2"
  id: mosquitto
  roots:
    - source: services/home-automation/mosquitto
    - runtime: ct111/mosquitto
  personality: ./PERSONALITY.md
  context:
    - ./knowledge.md
  related:
    - ../home-assistant/OBJECT.md
    - ../network/OBJECT.md
---

This object represents the Mosquitto deployment in CT111 as a semantic whole: its
broker software, configuration, local documentation, clients as observed by the
broker, and runtime behavior. It does not represent client internals, the network,
or physical devices. The fixture supplies synthetic observations and no live runtime.
