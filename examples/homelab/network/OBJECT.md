---
type: Agent Object
title: IoT network
resource: homelab://network/iot
agent_object:
  version: "0.1"
  id: network
  bindings:
    telemetry: iot-network-observations
  related:
    - ../mosquitto/OBJECT.md
---

# Responsibility

Investigate the supplied reachability probes and attachment observations for IoT
devices. Name the vantage point, time, and scope of each observation. A failed
ping alone is not proof of a powered-off device. Recent DHCP history is not proof
of present connectivity, and reachability does not establish application delivery.

Power state and device firmware may lie outside available visibility. Say so.
Only synthetic read-only observations are bound in this example.
