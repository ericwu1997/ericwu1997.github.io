---
title: AMQP
description: AMQP
permalink: /docs/app-layer-protocols/amqp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-22
updateTime: 2026-09-22
tags: [Markdown, Writing]
---

## Overview
**AMQP** (Advanced Message Queuing Protocol) is an open, binary wire-level messaging protocol, originally developed at JPMorgan Chase and later standardized by OASIS and ISO/IEC. It runs over **TCP**, on IANA-assigned port **5672** for cleartext traffic and **5671** for TLS-secured **AMQPS**, with SASL negotiation on 5672 also able to upgrade a connection to TLS in place. AMQP is broker-centric messaging middleware: producers publish messages to a broker (RabbitMQ, ActiveMQ, Azure Service Bus, etc.) that routes them via exchanges and queues (0-9-1) or link/node addressing (1.0) to consumers, making it common in enterprise messaging, IoT telemetry, and financial transaction systems.

Two incompatible wire formats circulate under the same protocol name and are readily distinguished on the wire: both open a connection with the fixed 8-byte ASCII preamble **`AMQP`** followed by a protocol-ID byte and three version bytes — `41 4D 51 50 00 00 09 01` for **AMQP 0-9-1** (the format used by RabbitMQ) versus `41 4D 51 50 00 01 00 00` for **AMQP 1.0** (the OASIS/ISO standard) — giving a reliable version fingerprint independent of payload. Traffic is cleartext by default unless the AMQPS/TLS variant or a SASL security layer is negotiated, and frames carry broker-, exchange-, and queue-name strings in plaintext that can further identify the messaging backend in use.

## Reference
[AMQP Wireshark Wiki](https://wiki.wireshark.org/AMQP)<br>
[IANA search=amqp](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=amqp)<br>
[RabbitMQ: Inspecting AMQP 0-9-1 Traffic using Wireshark](https://www.rabbitmq.com/amqp-wireshark)<br>
