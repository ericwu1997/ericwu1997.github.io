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

### Overview
The **Skinny Client Control Protocol** (SCCP), also known as Skinny, is a
proprietary, application-layer signaling protocol developed by Cisco for
VoIP call control and device management. It operates in a client–server
architecture over **TCP port 2000**, between IP phones (SCCP clients) and a
call agent — most commonly Cisco Unified Communications Manager (CUCM).
Supported protocol versions run up to **version 20**. Use cases: device
registration, call setup/teardown, feature control (hold, transfer,
conferencing), and media session negotiation — voice/video transport itself
is carried separately over RTP.

### Protocol Stacks
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
The Skinny Client Control Protocol (SCCP) uses a binary protocol design
featuring a fixed 12-byte header consisting of three 32-bit fields: data
length, header version, and message ID, followed by message-specific
parameters. Below example structure is for RegisterReq

#### RegisterReq
<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse;">
  <colgroup>
    <col style="width:6%">
    <col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%">
    <col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%">
    <col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%">
    <col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%"><col style="width:5.875%">
  </colgroup>
  <tbody>
    <!-- Ruler: top row only -->
    <tr>
      <td style="border:1px solid #333; padding:2px 4px;"></td>
      <td colspan="16" style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>0</span><span>7</span><span>15</span></div>
      </td>
    </tr>
    <!-- Offset 0 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">0</td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Data Length</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Header Version</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Message ID</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Device Name</i></td>
    </tr>
    <!-- Offset 16 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">16</td>
      <td colspan="12" style="border:1px solid #333; padding:6px;"><i>Device Name</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Reserved</i></td>
    </tr>
    <!-- Offset 32 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">32</td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Instance</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Station IPv4 Address</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Device Type</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Max Concurrent RTP Streams</i></td>
    </tr>
    <!-- Offset 48 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">48</td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Active RTP Streams</i></td>
      <td colspan="1" style="border:1px solid #333; padding:6px;"><i>Proto Ver</i></td>
      <td colspan="1" style="border:1px solid #333; padding:6px;"><i>Reserved</i></td>
      <td colspan="2" style="border:1px solid #333; padding:6px;"><i>Phone Features</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Max Concurrent Conferences</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Active Conferences</i></td>
    </tr>
    <!-- Offset 64 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">64</td>
      <td colspan="6" style="border:1px solid #333; padding:6px;"><i>MAC Address</i></td>
      <td colspan="6" style="border:1px solid #333; padding:6px;"><i>Reserved / Padding</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>IPv4 Address Scope</i></td>
    </tr>
    <!-- Offset 80 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">80</td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Max Number of Lines</i></td>
      <td colspan="12" style="border:1px solid #333; padding:6px;"><i>Station IPv6 Address</i></td>
    </tr>
    <!-- Offset 96 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">96</td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>Station IPv6 Address</i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>IPv6 Address Scope</i></td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>Firmware Load Name</i></td>
    </tr>
    <!-- Offset 112 -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">112</td>
      <td colspan="16" style="border:1px solid #333; padding:6px;"><i>Firmware Load Name</i></td>
    </tr>
    <!-- Offset 128 (partial row, only 8 of 16 bytes remain) -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">128</td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>Firmware Load Name</i></td>
      <td colspan="8" style="border:1px solid #333; padding:6px; opacity:0.4;"></td>
    </tr>
  </tbody>
</table>

### Common Message ID
Station → CallManager (Client → CUCM)

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:8%"><col style="width:29%"><col style="width:13%">
    <col style="width:8%"><col style="width:29%"><col style="width:13%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">No.</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Message Name</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Value</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">No.</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Message Name</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">1</td>
      <td style="border:1px solid #333; padding:8px 12px;">KeepAlive</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0000</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">7</td>
      <td style="border:1px solid #333; padding:8px 12px;">HookFlashMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0008</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">2</td>
      <td style="border:1px solid #333; padding:8px 12px;">RegisterMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0001</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">8</td>
      <td style="border:1px solid #333; padding:8px 12px;">SoftKeyEventMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0026</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">3</td>
      <td style="border:1px solid #333; padding:8px 12px;">IpPortMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0002</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">9</td>
      <td style="border:1px solid #333; padding:8px 12px;">UnregisterMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0027</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">4</td>
      <td style="border:1px solid #333; padding:8px 12px;">StimulusMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0005</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">10</td>
      <td style="border:1px solid #333; padding:8px 12px;">DeviceToUserDataMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x002E</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">5</td>
      <td style="border:1px solid #333; padding:8px 12px;">OffHookMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0006</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">11</td>
      <td style="border:1px solid #333; padding:8px 12px;">MediaTransmissionFailure</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x002A</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">6</td>
      <td style="border:1px solid #333; padding:8px 12px;">OnHookMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0007</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">12</td>
      <td style="border:1px solid #333; padding:8px 12px;">RegisterTokenReq</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0029</code></td>
    </tr>
  </tbody>
</table>

CallManager → Station (CUCM → Client)

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:8%"><col style="width:29%"><col style="width:13%">
    <col style="width:8%"><col style="width:29%"><col style="width:13%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">No.</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Message Name</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Value</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">No.</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Message Name</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">1</td>
      <td style="border:1px solid #333; padding:8px 12px;">RegisterAckMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0081</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">7</td>
      <td style="border:1px solid #333; padding:8px 12px;">StopMediaTransmission</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x008B</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">2</td>
      <td style="border:1px solid #333; padding:8px 12px;">KeepAliveAckMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0100</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">8</td>
      <td style="border:1px solid #333; padding:8px 12px;">OpenReceiveChannel</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0105</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">3</td>
      <td style="border:1px solid #333; padding:8px 12px;">StartToneMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0082</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">9</td>
      <td style="border:1px solid #333; padding:8px 12px;">OpenReceiveChannelAck</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0022</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">4</td>
      <td style="border:1px solid #333; padding:8px 12px;">StopToneMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0083</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">10</td>
      <td style="border:1px solid #333; padding:8px 12px;">CallInfoMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x008F</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">5</td>
      <td style="border:1px solid #333; padding:8px 12px;">SetRingerMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0085</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">11</td>
      <td style="border:1px solid #333; padding:8px 12px;">DisplayTextMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0099</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">6</td>
      <td style="border:1px solid #333; padding:8px 12px;">StartMediaTransmission</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x008A</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">12</td>
      <td style="border:1px solid #333; padding:8px 12px;">VersionMessage</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0x0098</code></td>
    </tr>
  </tbody>
</table>

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
