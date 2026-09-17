---
type: Agent Object
title: Home Assistant in CT111
resource: homelab://ct111/home-assistant
agent_object:
  version: "0.1"
  id: home-assistant
  roots:
    - source: services/home-automation/home-assistant
    - runtime: ct111/home-assistant
  personality: ./PERSONALITY.md
  related:
    - ../mosquitto/OBJECT.md
---

This object is the Home Assistant deployment in CT111. Its personality describes
how an agent represents and works within the object. The fixture supplies synthetic,
read-only observations; it does not connect to the roots above.
