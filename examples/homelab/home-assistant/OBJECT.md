---
type: Agent Object
title: Home Assistant in CT111
resource: homelab://ct111/home-assistant
agent_object:
  version: "0.2"
  id: home-assistant
  roots:
    - source: services/home-automation/home-assistant
    - runtime: ct111/home-assistant
  personality: ./PERSONALITY.md
  related:
    - ../mosquitto/OBJECT.md
---

This object represents the Home Assistant deployment in CT111 as a semantic whole:
its application, configuration, integrations, local documentation, and observed
runtime behavior. It does not represent the broker, network, or physical devices.
The fixture supplies synthetic observations and no live runtime.
