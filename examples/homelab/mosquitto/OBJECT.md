---
type: Agent Object
title: Mosquitto in CT111
resource: homelab://ct111/mosquitto
agent_object:
  version: "0.1"
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

This object is the Mosquitto deployment in CT111. Its personality describes how an
agent represents and works within the object. The fixture supplies synthetic,
read-only observations; it does not connect to the roots above.
