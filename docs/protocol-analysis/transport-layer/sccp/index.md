---
title: (TCP 2000) SCCP
parent: Transport Layer
---

# SKINNY Client Control Protocol
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
The <b>Skinny Client Control Protocol</b> (SCCP), also known as Skinny, is a proprietary signaling protocol developed by Cisco Systems for use in Voice over IP (VoIP) communications. It enables the exchange of call control and device management messages between IP phones (SCCP clients) and a centralized call agent, most commonly Cisco Unified Communications Manager (CUCM). Operating in a client–server architecture over TCP, typically on port 2000, SCCP provides lightweight binary signaling for functions such as device registration, call setup and teardown, feature control, and media session management, while RTP is used separately for voice and video transport.

SCCP originated from technology developed by Selsius Systems, which Cisco acquired in 1998, and evolved into the primary line-side signaling protocol within Cisco IP telephony environments. It supports multiple protocol versions (up to version 17) and includes mechanisms for firewall traversal, dynamic media channel negotiation, and supplementary services such as hold, transfer, and conferencing. SCCP is commonly deployed alongside other Cisco signaling protocols such as MGCP for gateway control, and while its use has declined in favor of SIP in modern deployments, SCCP remains widely encountered in legacy and enterprise Cisco IP Phone installations due to its efficiency and tight integration with CUCM.

### Protocol Stacks
The Skinny Client Control Protocol (SCCP) primarily utilizes the Transmission Control Protocol (TCP) over port 2000
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

### Protocol Structure
The Skinny Client Control Protocol (SCCP) uses a binary protocol design featuring a fixed 12-byte header consisting of three 32-bit fields: data length, reserved (typically set to 0), and message ID, followed by message-specific parameters 

```
 --------------------------
|   Data Length  (32 bit)  |
|--------------------------|
| Header Version (32 bit)  |
|--------------------------|
|    Message ID  (32 bit)  |
|--------------------------|  
|       payload  ....      |
 --------------------------
```
In SCCP, the 32-bit header field after the message length was historically reserved and set to zero, but starting with SCCP version 18 Cisco repurposed it to carry the protocol version number. As a result, older phones and CUCM versions always use 0, while newer implementations may send a non-zero value, which legacy receivers typically ignore for compatibility.

### Common Message ID 
Station → CallManager (Client → CUCM)

| **#**                          | **#**                                 | **#**                                  | **#**                            |
|--------------------------------|---------------------------------------|----------------------------------------|----------------------------------|
| (1) KeepAlive (0x0000)         | (2) RegisterMessage (0x0001)          | (3) IpPortMessage (0x0002)             | (4) StimulusMessage (0x0005)     |
| (5) OffHookMessage (0x0006)    | (6) OnHookMessage (0x0007)            | (7) HookFlashMessage (0x0008)          | (8) SoftKeyEventMessage (0x0026) |
| (9) UnregisterMessage (0x0027) | (10) DeviceToUserDataMessage (0x002E) | (11) MediaTransmissionFailure (0x002A) | (12) RegisterTokenReq (0x0029)   |

CallManager → Station (CUCM → Client)

| **#**                              | **#**                               | **#**                              | **#**                           |
|------------------------------------|-------------------------------------|------------------------------------|---------------------------------|
| (1) RegisterAckMessage (0x0081)    | (2) KeepAliveAckMessage (0x0100)    | (3) StartToneMessage (0x0082)      | (4) StopToneMessage (0x0083)    |
| (5) SetRingerMessage (0x0085)      | (6) StartMediaTransmission (0x008A) | (7) StopMediaTransmission (0x008B) | (8) OpenReceiveChannel (0x0105) |
| (9) OpenReceiveChannelAck (0x0022) | (10) CallInfoMessage (0x008F)       | (11) DisplayTextMessage (0x0099)   | (12) VersionMessage (0x0098)    |


### RegisterReq Payload

| **Field**                      | **Size (bytes)** | **Example**        | **Detail**                               |
|--------------------------------|------------------|--------------------|------------------------------------------|
| Data Length                    | 4                |                    | Total message length including header    |
| Header Version                 | 4                | 0                  | Reserved / Basic (0 for pre-v18)         |
| Message ID                     | 4                | 1 (RegisterReq)    | SCCP message type                        |
| Device Name                    | 16               | SEP00192FXXXXXX    | MAC-based identifier of the phone        |
| Reserved for future use        | 4                |                    | Padding / reserved                       |
| Instance                       | 4                |                    | Instance ID (typically 0)                |
| Station IPv4 Address           | 4                |                    | Phone IP address                         |
| Device Type                    | 4                | 0x00000073 (7941G) | Maps to phone model                      |
| Max Concurrent RTP Streams     | 4                |                    | Maximum active RTP streams supported     | 
| Active RTP Streams             | 4                |                    | Currently active RTP streams             |
| Protocol Version               | 1                |                    | SCCP protocol version supported by phone |
| Unknown / Reserved             | 1                | 0                  | Reserved / unknown                       |
| Phone Features                 | 2                |                    | Phone Features                           |
| Max Concurrent Conferences     | 4                |                    | Maximum simultaneous conferences         |
| Active Conferences             | 4                |                    | Currently active conferences             |
| MAC Address                    | 6                | 00:19:2f:XX:XX:XX  | Hardware MAC of the phone                |
| IPv4 Address Scope             | 4                |                    | Scope / type of IP address               |
| Max Number of Lines            | 4                |                    | Maximum phone lines supported            |
| Station IPv6 Address           | 16               |                    | Empty for IPv4-only phones               |
| IPv6 Address Scope             | 4                |                    | Scope / type of IPv6 address             |
| Firmware Load Name             | 32               | SCCP41.9-0-3S      | Firmware ID / loadInformation            |

### Sample Hex Dump + Dissector View (RegisterReq)
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
    Mac Address: Cisco_19:21:b0 (00:19:2f:XX:XX:XX)
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
[Grokipedia - Skinny Client Control Protocol](https://grokipedia.com/page/Skinny_Client_Control_Protocol)<br>