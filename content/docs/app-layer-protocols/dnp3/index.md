---
title: DNP3
description: DNP3 (Distributed Network Protocol 3)
permalink: /docs/app-layer-protocols/dnp3/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-10-09
updateTime: 2026-10-09
tags: [Markdown, Writing]
---

### Overview

**DNP3 (Distributed Network Protocol 3)**, standardized as **IEEE 1815** and maintained by the DNP Users Group, is a SCADA protocol used mainly in electric and water utilities for communication between a control-center **master** and field **outstations** (RTUs, IEDs, protection relays). It runs over serial links or IP. IANA registers **port 20000** (`dnp`) for **TCP** and **UDP**, with TCP the common deployment, and **port 19999** (`dnp-sec`) for secure DNP3. The master polls outstations for static and event data and issues control commands, and outstations can also send unsolicited responses.

Each DNP3 frame starts with a **data-link header**: fixed start bytes **`05 64`**, a 1-byte length, a 1-byte control field, 2-byte destination and source addresses (little-endian), and a 16-bit CRC. User data follows in blocks of up to 16 bytes, each followed by its own CRC. A 1-byte transport header (FIN/FIR/sequence) precedes the application layer, whose header carries an application-control byte and a function code (e.g. `0x01` Read, `0x81` Response, `0x82` Unsolicited Response). Responses add 2 bytes of Internal Indications (IIN). When the master reads object group 0, outstations can return **device attributes** such as manufacturer name (g0v252), product model, software and hardware version, and serial number; which attributes a device supports is listed in its Device Profile. DNP3 traffic is **cleartext** by default. Secure Authentication (SAv5, IEEE 1815-2012) adds HMAC challenge-response authentication of critical requests without encrypting the payload, and encryption is provided by running DNP3 over TLS.
