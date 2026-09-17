# MQTT investigation context

Mosquitto serves Home Assistant in CT111. Device publishers and application
subscribers share a topic contract. Compare actual published and subscribed topics
when the broker works but an entity remains unavailable. Do not assume a topic
convention from a device name.

A collector timestamp measures the evidence, not necessarily the incident. Check
collection continuity before treating absent publications or errors as significant.
Prefer current runtime observations over assumptions from source configuration.
