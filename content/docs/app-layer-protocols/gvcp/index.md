---
title: GVCP
description: GVCP (GigE Vision Control Protocol)
permalink: /docs/app-layer-protocols/gvcp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-19
updateTime: 2026-09-19
tags: [Markdown, Writing]
---

# Overview
**GVCP** (**GigE Vision Control Protocol**) is the control-plane protocol of the **GigE Vision** standard, maintained by the **Automated Imaging Association (AIA)**, for configuring and commanding machine-vision cameras and frame grabbers over Gigabit Ethernet. It runs over **UDP**, on the IANA-registered **port 3956**, in a client-server model where a host application (controller) discovers, reads/writes bootstrap registers on, and issues commands to one or more camera devices (servers); the companion protocol **GVSP** (GigE Vision Streaming Protocol) carries the actual image data on a separate, dynamically negotiated channel.

Every GVCP command and acknowledgment opens with a fixed 8-byte header: a **magic byte `0x42`**, a 1-byte flag field, a 2-byte command ID (e.g. `0x0002` for `DISCOVERY_CMD`, acknowledgments OR the command with `0x8000`), a 2-byte payload length, and a 2-byte request ID — all in cleartext with no authentication or encryption by default. A `DISCOVERY_ACK` response carries the camera's manufacturer name, model name, device version, serial number, user-defined name, current IP configuration, and MAC address directly on the wire, making GVCP discovery traffic a strong device-identification source for industrial camera fingerprinting.

# Protocol Structure / Field Type

## DISCOVERY_CMD

<table style="width:100%; text-align:center; table-layout:fixed; border-collapse:collapse;">
  <colgroup>
    <col style="width:25%"><col style="width:25%"><col style="width:25%"><col style="width:25%">
  </colgroup>
  <tbody>
    <tr>
      <td>0x42 (1 byte)</td>
      <td>flag (1 byte)</td>
      <td colspan="2">command (2 bytes)</td>
    </tr>
    <tr>
      <td colspan="2">length (2 bytes)</td>
      <td colspan="2">req_id (2 bytes)</td>
    </tr>
  </tbody>
</table>

<!--
| Field   | Size    |
| ------- | ------- |
| 0x42    | 1 byte  |
| flag    | 1 byte  |
| command | 2 bytes |
| length  | 2 bytes |
| req_id  | 2 bytes |
-->

# Reference
[GigE Vision Wireshark Dissector GitHub](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-gvcp.c)<br>
[IANA search=gvcp](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=gvcp)<br>
