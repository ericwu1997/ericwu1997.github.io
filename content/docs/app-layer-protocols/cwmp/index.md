---
title: CWMP
description: CWMP
permalink: /docs/app-layer-protocols/cwmp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-23
updateTime: 2026-09-23
tags: [Markdown, Writing]
---

## Overview
**CWMP** (CPE WAN Management Protocol), commonly known by its Broadband Forum specification number **TR-069**, is a bidirectional **SOAP-over-HTTP** application-layer protocol for remote management of customer-premises equipment (CPE). It runs over **TCP**, on the IANA-assigned port **7547**, and follows a client-server model between the managed CPE (routers, cable/DSL modems, VoIP ATAs, and increasingly cameras and other IoT devices) and an ISP-operated Auto Configuration Server (ACS), which uses it to provision configuration, push firmware updates, and run remote diagnostics without a truck roll.

The CPE-initiated `Inform` RPC — sent in a SOAP envelope under the XML namespace `urn:dslforum-org:cwmp-1-x` (version-dependent) — carries a `DeviceId` structure with **Manufacturer**, **OUI**, **ProductClass**, and **SerialNumber** fields in cleartext XML, making it a direct device fingerprint whenever the exchange isn't wrapped in TLS. The ACS can also issue an unsolicited **Connection Request** back to the CPE on port 7547 (typically HTTP Basic/Digest authenticated) to trigger an immediate session. CWMP traffic is plaintext HTTP by default unless the HTTPS variant is negotiated, and internet-exposed port 7547 endpoints have been a recurring target for CPE-hijacking botnets (e.g., the 2016 Mirai/Annie attacks).

## Reference
[IANA search=cwmp](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=cwmp)<br>
[Broadband Forum TR-069 CPE WAN Management Protocol](https://www.broadband-forum.org/technical/download/TR-069.pdf)<br>
