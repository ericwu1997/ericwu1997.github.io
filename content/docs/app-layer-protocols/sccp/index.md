---
title: SCCP
description: SCCP (Skinny)
permalink: /docs/app-layer-protocols/sccp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-18
updateTime: 2026-09-18
tags: [Markdown, Writing]
---

## Overview
The **Skinny Client Control Protocol** (SCCP), also known as Skinny, is a
proprietary, application-layer signaling protocol developed by Cisco for
VoIP call control and device management. It operates in a client–server
architecture over **TCP port 2000**, between IP phones (SCCP clients) and a
call agent — most commonly Cisco Unified Communications Manager (CUCM).
Supported protocol versions run up to **version 20**. Use cases: device
registration, call setup/teardown, feature control (hold, transfer,
conferencing), and media session negotiation — voice/video transport itself
is carried separately over RTP.

## Protocol Stacks
```
 ------------------------------------     IP Telephony Endpoint
|      Call Control Application      | <= CUCM / SCCP Call Agent
|------------------------------------|
|     Skinny (SCCP) Signaling        | <= Call control & device control
|------------------------------------|
|              TCP                   |
|------------------------------------|
|              IP                    |
 ------------------------------------
```

## Protocol Structure
The Skinny Client Control Protocol (SCCP) uses a binary protocol design
featuring a fixed 12-byte header consisting of three 32-bit fields: data
length, header version, and message ID, followed by message-specific
parameters.

<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse; border:1px solid #333; background:transparent;">
  <colgroup>
    <col style="width:20%"><col style="width:20%"><col style="width:20%"><col style="width:40%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:6px; background:transparent;"><i>Data Length</i><br>(4 byte)</td>
      <td style="border:1px solid #333; padding:6px; background:transparent;"><i>Header Version</i><br>(4 byte)</td>
      <td style="border:1px solid #333; padding:6px; background:transparent;"><i>Message ID</i><br>(4 byte)</td>
      <td style="border:1px solid #333; padding:6px; background:transparent;"><i>payload</i> ....</td>
    </tr>
  </tbody>
</table>

<!-- ```
 --------------------------
|   Data Length  (32 bit)  |
|--------------------------|
| Header Version (32 bit)  |
|--------------------------|
|    Message ID  (32 bit)  |
|--------------------------|
|       payload  ....      |
 --------------------------
``` -->

The 32-bit header field after the message length was historically reserved
and set to zero, but starting with SCCP version 18 Cisco repurposed it to
carry the protocol version number. As a result, older phones and CUCM
versions always use 0, while newer implementations may send a non-zero
value, which legacy receivers typically ignore for compatibility.

## RegisterReq Payload — Identification fields
| **Field** | **Size (bytes)** | **Example** |
|---|---|---|
| Device Name | 16 | `SEP00192FXXXXXX` |
| Reserved for future use | 4 | |
| Instance | 4 | |
| Device Type | 4 | `0x00000073` (7941G) |
| MAC Address | 6 | `00:19:2f:XX:XX:XX` |
| Firmware Load Name | 32 | `SCCP41.9-0-3S` |

## RegisterReq Payload — Network fields
| **Field** | **Size (bytes)** | **Example** |
|---|---|---|
| Station IPv4 Address | 4 | |
| IPv4 Address Scope | 4 | |
| Station IPv6 Address | 16 | Empty for IPv4-only phones |
| IPv6 Address Scope | 4 | |

## RegisterReq Payload — Capability/capacity fields
| **Field** | **Size (bytes)** | **Example** |
|---|---|---|
| Max Concurrent RTP Streams | 4 | |
| Active RTP Streams | 4 | |
| Max Concurrent Conferences | 4 | |
| Active Conferences | 4 | |
| Max Number of Lines | 4 | |

## RegisterReq Payload — Protocol/feature fields
| **Field** | **Size (bytes)** | **Example** |
|---|---|---|
| Protocol Version | 1 | |
| Unknown / Reserved | 1 | 0 |
| Phone Features | 2 | |

## Common Message ID
Station → CallManager (Client → CUCM)

|                                  |                                         |                                          |                                   |
|----------------------------------|-----------------------------------------|--------------------------------------------|-----------------------------------|
| (1) KeepAlive (0x0000)          | (2) RegisterMessage (0x0001)           | (3) IpPortMessage (0x0002)              | (4) StimulusMessage (0x0005)   |
| (5) OffHookMessage (0x0006)     | (6) OnHookMessage (0x0007)             | (7) HookFlashMessage (0x0008)           | (8) SoftKeyEventMessage (0x0026) |
| (9) UnregisterMessage (0x0027)  | (10) DeviceToUserDataMessage (0x002E)  | (11) MediaTransmissionFailure (0x002A)  | (12) RegisterTokenReq (0x0029) |

CallManager → Station (CUCM → Client)

|                                      |                                        |                                     |                                    |
|---------------------------------------|------------------------------------------|---------------------------------------|--------------------------------------|
| (1) RegisterAckMessage (0x0081)      | (2) KeepAliveAckMessage (0x0100)         | (3) StartToneMessage (0x0082)         | (4) StopToneMessage (0x0083)        |
| (5) SetRingerMessage (0x0085)        | (6) StartMediaTransmission (0x008A)      | (7) StopMediaTransmission (0x008B)    | (8) OpenReceiveChannel (0x0105)     |
| (9) OpenReceiveChannelAck (0x0022)   | (10) CallInfoMessage (0x008F)            | (11) DisplayTextMessage (0x0099)      | (12) VersionMessage (0x0098)        |

## Sample Hex Dump + Dissector View (RegisterReq)
```
Skinny Client Control Protocol
    Data length: 128
    Header version: Basic (0x00000000)
    Message ID: RegisterReq (1)
    sid
    stationIpAddr: 192.168.6.50
    Device Type: 7941G (0x00000073)
    Maximum Number of Concurrent RTP Streams: 5
    Active RTP Streams: 0
    Protocol Version: 19
    unknown: 0
    phoneFeatures
    Maximum Number of Concurrent Conferences: 1
    Active Conferences: 0
    Mac Address: Cisco_XX:XX:XX (00:19:2f:XX:XX:XX)
    ipV4AddressScope: 3
    maxNumberOfLines: 2
    stationIpV6Addr: ::
    ipV6AddressScope: 0
    firmwareLoadName: SCCP41.9-0-3S
    [Response In: 10]

0000   80 00 00 00 00 00 00 00 01 00 00 00 53 45 50 30   ............SEP0
0010   30 31 39 32 46 XX XX XX XX XX XX 00 00 00 00 00   0192FXXXXXX.....
0020   00 00 00 00 c0 a8 06 32 73 00 00 00 05 00 00 00   .......2s.......
0030   00 00 00 00 13 00 72 85 01 00 00 00 00 00 00 00   ......r.........
0040   00 19 2f XX XX XX 00 00 00 00 00 00 03 00 00 00   ../.!...........
0050   02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0060   00 00 00 00 00 00 00 00 53 43 43 50 34 31 2e 39   ........SCCP41.9
0070   2d 30 2d 33 53 00 00 00 00 00 00 00 00 00 00 00   -0-3S...........
0080   00 00 00 00 00 00 00 00                           ........
```

## Reference
[VoIP - Excerpt (SCCP).pdf](https://www.technologeeks.com/Courses/VoIP%20-%20Excerpt%20(SCCP).pdf)<br>
[Wireshark Github SCCP Dissector - packet-skinny.c](https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-skinny.c)<br>
[Github staskobzar - Provisioning files for Cisco phones SCCP firmware](https://github.com/staskobzar/cisco_prov/tree/master/sccp)<br>
