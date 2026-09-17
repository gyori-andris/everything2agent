---
type: Agent Object
title: Home Assistant in CT111
resource: homelab://ct111/home-assistant
agent_object:
  version: "0.1"
  id: home-assistant
  bindings:
    source: home-assistant-source
    runtime: home-assistant-container
    telemetry: home-assistant-observations
  related:
    - ../mosquitto/OBJECT.md
---

# Responsibility

Represent entity availability, integration configuration, application logs, and
runtime subscription behavior. Understand the relevant source and documentation.
An unavailable entity is a symptom, not proof that a device or broker is offline.
An accepted configuration is not proof it matches the publisher's configuration.

Compare expected inputs with actual observations. Broker and network internals
are related responsibilities. The fixture bindings supply read-only observations;
no live container or source checkout is connected.
