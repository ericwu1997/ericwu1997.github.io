---
title: CoLa-B
description: CoLa-B (Command Language Binary)
permalink: /docs/app-layer-protocols/cola-b/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-10-09
updateTime: 2026-10-09
tags: [Markdown, Writing]
---

### Overview

**CoLa-B (Command Language Binary)** is the binary variant of SICK AG's **CoLa** command protocol, part of the **SOPAS** device-communication framework used by SICK industrial sensors such as LiDAR/laser scanners, radar sensors and other detection devices. It runs over **TCP**, typically on **port 2112**. On some devices (e.g. SICK RMS radar sensors) this port defaults to the ASCII variant CoLa-A and can be switched to CoLa-B, while **port 2111** carries CoLa-A. Both are vendor defaults, not IANA assignments: IANA registers 2111 to `dsatp` and 2112 to `idonix-metanet`. CoLa-B follows a **client-server** model: a host (PLC, PC, or the SOPAS ET configuration tool) sends command telegrams to the sensor to read and write variables, invoke methods, and subscribe to events such as scan-data streams.

Every CoLa-B telegram begins with a fixed **4-byte start sequence `02 02 02 02`**, followed by a **4-byte big-endian length** field, the payload, and a **1-byte XOR checksum** over the payload bytes. The payload opens with a 3-byte ASCII command type: `sRN`/`sRI` (read by name/index), `sWN` (write by name), `sMN` (method), `sEN` (event), with matching replies `sRA`, `sWA`, `sAN`/`sMA`, `sEA`. The variable or method is addressed either by name (e.g. `DeviceIdent`) or by a 2-byte index. A **DeviceIdent** read returns length-prefixed ASCII strings for the device name and firmware version (e.g. `ML20` / `1.110`), and related variables expose the serial number and order number. CoLa-B traffic is sent in **cleartext**. Write and method access is gated by a `SetAccessMode` login that sends a user level and a password hash, with no transport encryption. The newer CoLa-2 variant (port 2122) uses a different session-based framing.

### Protocol Stacks
```
  ------------------------------------
|     Sensor/Host Application        |  <= Client (e.g., PLC, PC, SOPAS ET software)
|------------------------------------|
|          CoLa-B Telegrams          |  <= Binary command/data framing (SOPAS commands)
|------------------------------------|
|               TCP                  |  <= Reliable, connection-oriented transport
|------------------------------------|
|              TCP/IP                |
 ------------------------------------
```

### CoLa-B Dataframe
technical_information_ml20_en_im0059796.pdf#page=8&zoom=100

<table style="border-collapse: collapse; font-family: Arial, sans-serif; font-size: 14px;">
  <thead>
    <tr>
      <th style="border: 1px solid #000; padding: 4px 10px; text-align: center;">Request by client<br>(PC)</th>
      <th style="border: 1px solid #000; padding: 4px 10px; text-align: center;">Response by server<br>(ML20)</th>
      <th style="border: 1px solid #000; padding: 4px 10px; text-align: center;">Command</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; padding: 4px 10px;">sRI{SVIdx}</td>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; padding: 4px 10px;">sRA{SVIdx}{variable value}</td>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; padding: 4px 10px;">Read variable identified by index <em>SVIdx</em></td>
    </tr>
    <tr>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; padding: 4px 10px;">sWI{SVIdx}</td>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; padding: 4px 10px;">sWA{SVIdx}</td>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; padding: 4px 10px;">Write variable identified by index <em>SVIdx</em></td>
    </tr>
    <tr>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; border-bottom: 1px solid #000; padding: 4px 10px;">sMI{MIdx}{parameters}</td>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; border-bottom: 1px solid #000; padding: 4px 10px;">sMA{MIdx}{return values}</td>
      <td style="border-left: 1px solid #000; border-right: 1px solid #000; border-bottom: 1px solid #000; padding: 4px 10px;">Invoke method identified by index <em>MIdx</em></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 4px 10px;"></td>
      <td style="border: 1px solid #000; padding: 4px 10px;">sFA{error code}</td>
      <td style="border: 1px solid #000; padding: 4px 10px;">Alternatively, the device can respond to every command with an error code.</td>
    </tr>
  </tbody>
</table>

#### Request Frame
<table style="display:table; width:100%; text-align:left; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:12%">
    <col style="width:6.286%"><col style="width:6.286%"><col style="width:6.286%"><col style="width:6.286%">
    <col style="width:6.286%"><col style="width:6.286%"><col style="width:6.286%"><col style="width:6.286%">
    <col style="width:6.286%"><col style="width:6.286%"><col style="width:6.286%"><col style="width:6.286%">
    <col style="width:6.286%"><col style="width:6.284%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Byte Index</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">1</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">2</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">3</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">4</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">5</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">6</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">7</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">8</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">9</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">10</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">11</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">12</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">13</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">14</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Content<br>(as hex-Value)</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">05</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">73</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">52</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">49</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">04</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">6c</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Description</td>
      <td colspan="4" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">STx<br><i>framing start</i></td>
      <td colspan="4" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Length = 5 bytes<br><i>Length of CoLa-B data (without checksum byte)</i></td>
      <td colspan="3" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">„sRI“<br>ASCII-command<br><i>read Variable</i></td>
      <td colspan="2" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Var.-Idx = 4</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Checksum = 6c</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Layer</td>
      <td colspan="8" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa framing start</td>
      <td colspan="5" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa-B command<br><i>Valid indices see following chapters.</i></td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa framing end</td>
    </tr>
  </tbody>
</table>

#### Response Frame
<table style="display:table; width:100%; text-align:left; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:12%">
    <col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%">
    <col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%">
    <col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%">
    <col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%">
    <col style="width:5.184%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Byte Index</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">1</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">2</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">3</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">4</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">5</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">6</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">7</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">8</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">9</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">10</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">11</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">12</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">13</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">14</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">15</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">16</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">17</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Content<br>(as hex-Value)</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">02</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">15</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">73</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">52</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">41</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">04</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">00</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">0e</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">44</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">35</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Description</td>
      <td colspan="4" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">STx<br><i>Framing Start</i></td>
      <td colspan="4" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Length = 21 bytes<br><i>Length of CoLa-B data (without checksum byte)</i></td>
      <td colspan="3" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">„sRA“<br>ASCII-answer<br><i>read acknowledge</i></td>
      <td colspan="2" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Var.-Idx = 4</td>
      <td colspan="2" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Flexstring-length = 14</td>
      <td colspan="2" style="border:1px solid #333; padding:4px 6px; vertical-align:top;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Layer</td>
      <td colspan="8" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa framing start</td>
      <td colspan="5" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa-B command<br><i>Valid indices see following chapters.</i></td>
      <td colspan="4" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa-B value</td>
    </tr>
  </tbody>
</table>

<br>

<table style="display:table; width:100%; text-align:left; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:12%">
    <col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%">
    <col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%">
    <col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%"><col style="width:5.176%">
    <col style="width:25.888%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Byte Index</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">18</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">19</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">20</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">21</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">22</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">23</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">24</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">25</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">26</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">27</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">28</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">29</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">30</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Content<br>(as hex-Value)</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">2e</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">31</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">33</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">2e</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">30</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">30</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">38</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">2e</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">32</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">37</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">32</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">32</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">0a</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Description</td>
      <td colspan="12" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Variable content, here: Flexstring, ascii:<br>„D5.13.008.2722“</td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Checksum = 0a</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">Layer</td>
      <td colspan="12" style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa-B value <i>(continued)</i></td>
      <td style="border:1px solid #333; padding:4px 6px; vertical-align:top;">CoLa framing end</td>
    </tr>
  </tbody>
</table>

checksum = XOR all bytes 9 to 13

### CoLa-A Dataframe
telegram_listing_nav210_en_im0084703.pdf#page=5&zoom=100,97,700

<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:15.5%"><col style="width:11.5%"><col style="width:15.5%"><col style="width:18%"><col style="width:25.5%"><col style="width:14%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">Byte index</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">frame start</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">Command Type</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">Command</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">Parameter</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">frame end</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">In ASCII</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">&lt;STX&gt;</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">sMN</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">SetAccessMode</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">3 F4724744</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">&lt;ETX&gt;</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">In Hex</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">02</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">same</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">same</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">same</td>
      <td style="border:1px solid #333; padding:6px; vertical-align:middle;">03</td>
    </tr>
  </tbody>
</table>

There has to be a space in between the command and the parameters and also in between each parameter.<br>
In HEX the command start with 02 and ends with 03. The spaces are marked as 20. Single numbers that are converted to ASCII always get a 3 in front.

below two are the hex and ascii format equivalent
```
<STX>sMN SetAccessMode 3 F4724744<ETX>
02 73 4D 4E 20 53 65 74 41 63 63 65 73 73 4D 6F 64 65 20 33 20 46 34 37 32 34 37 34 34 03
```

### Known Command Type/Command

| **Description** | **Value ASCII** | **Value Hex** | **Request/Response** |
|-----------------|-----------------|---------------|----------------------|
| Read by name    | sRN             | 73 52 4E      | request              |
| Write by name   | sWN             | 73 57 4E      | request              |
| Method          | sMN             | 73 4D 4E      | request              |
| Read by name    | sRA             | 73 52 41      | response             |
| Method          | sAN             | 73 41 4E      | response             |

### Telegram Example

<table style="display:table; width:100%; text-align:left; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:15.2%"><col style="width:25.1%"><col style="width:9.9%"><col style="width:11.9%"><col style="width:37.9%">
  </colgroup>
  <tbody>
    <tr>
      <td colspan="5" style="border:1px solid #333; padding:2px 6px;"><b>Read Variable:</b></td>
    </tr>
    <tr>
      <td colspan="5" style="border:1px solid #333; padding:2px 6px 14px; font-family:'Courier New', monospace;">sRI 0</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Telegram Part</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Telegram</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Type</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Length [Byte]</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Description</b></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;">Command Type</td>
      <td style="border:1px solid #333; padding:2px 6px;">sRI</td>
      <td style="border:1px solid #333; padding:2px 6px;">String</td>
      <td style="border:1px solid #333; padding:2px 6px;">3</td>
      <td style="border:1px solid #333; padding:2px 6px;">Read SOPAS Variable by Name</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;">Command</td>
      <td style="border:1px solid #333; padding:2px 6px;">0</td>
      <td style="border:1px solid #333; padding:2px 6px;">String</td>
      <td style="border:1px solid #333; padding:2px 6px;">1</td>
      <td style="border:1px solid #333; padding:2px 6px;">Unique Identification of device</td>
    </tr>
  </tbody>
</table>

<br>

<table style="display:table; width:100%; text-align:left; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:15.2%"><col style="width:25.1%"><col style="width:9.9%"><col style="width:11.9%"><col style="width:37.9%">
  </colgroup>
  <tbody>
    <tr>
      <td colspan="5" style="border:1px solid #333; padding:2px 6px;"><b>Read Variable Response:</b></td>
    </tr>
    <tr>
      <td colspan="5" style="border:1px solid #333; padding:2px 6px 14px; font-family:'Courier New', monospace;">sRA 0 &lt;Name&gt; &lt;Version&gt;</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Telegram Part</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Telegram</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Type</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Length [Byte]</b></td>
      <td style="border:1px solid #333; padding:2px 6px;"><b>Description</b></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;">Command Type</td>
      <td style="border:1px solid #333; padding:2px 6px;">sRA</td>
      <td style="border:1px solid #333; padding:2px 6px;">String</td>
      <td style="border:1px solid #333; padding:2px 6px;">3</td>
      <td style="border:1px solid #333; padding:2px 6px;">SOPAS Variable Read Acknowledge</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;">Command</td>
      <td style="border:1px solid #333; padding:2px 6px;">0</td>
      <td style="border:1px solid #333; padding:2px 6px;">String</td>
      <td style="border:1px solid #333; padding:2px 6px;">1</td>
      <td style="border:1px solid #333; padding:2px 6px;">Unique Identification of device</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;">Variable Data 1</td>
      <td style="border:1px solid #333; padding:2px 6px;">Name</td>
      <td style="border:1px solid #333; padding:2px 6px;">FlexString</td>
      <td style="border:1px solid #333; padding:2px 6px;">4</td>
      <td style="border:1px solid #333; padding:2px 6px;"></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:2px 6px;">Variable Data 2</td>
      <td style="border:1px solid #333; padding:2px 6px;">Version</td>
      <td style="border:1px solid #333; padding:2px 6px;">FlexString</td>
      <td style="border:1px solid #333; padding:2px 6px;">5</td>
      <td style="border:1px solid #333; padding:2px 6px;"></td>
    </tr>
  </tbody>
</table>

CoLa-B (DeviceIdent)

```
Read Variable:          02 02 02 02 00 00 00 05 73 52 49 00 00 68         ········sRI··h

Read Variable Response: 02 02 02 02 00 00 00 12 73 52 41 00 00 00 04 4D   ········sRA····M
                        4C 32 30 00 05 31 2E 31 31 30 4D                  L20··1.110M
```

CoLa-A (DeviceIdent)

```
Read Variable:          02 02 02 02 00 00 00 0f 73 52 4E 20 44 65 76 69   .......-sRN Devi
                        63 65 49 64 65 6E 25 

Read Variable Response: 02 02 02 02 00 00 00 2d 73 52 41 20 44 65 76 69   .......-sRA Devi
                        63 65 49 64 65 6e 74 20 00 0f 54 72 69 53 70 65   ceIdent ..TriSpe
                        63 74 6f 72 20 31 30 36 30 00 0a 34 2e 33 2e 31   ctor 1060..4.3.1
                        2e 32 34 32 52 55                                 .242RU
```

### Client / Server Script

Reconstruct from TCP payload. For instance

```
0000   02 02 02 02 00 00 00 2d 73 52 41 20 44 65 76 69   .......-sRA Devi
0010   63 65 49 64 65 6e 74 20 00 0f 54 72 69 53 70 65   ceIdent ..TriSpe
0020   63 74 6f 72 20 31 30 36 30 00 0a 34 2e 33 2e 31   ctor 1060..4.3.1
0030   2e 32 34 32 52 55                                 .242RU
```

The scripts below extract TCP payload, save to "payloads.hex", iterate through to next line on each response.

```bash
tshark -r sick_cola-b_evaluated.pcap -Y "tcp.srcport == 2112" -T fields -e tcp.payload > payloads.hex

PORT=2112
FILE=payloads.hex

while read line; do
  echo "Serving: $line"
  echo -n "$line" | xxd -r -p | nc -l $PORT
done < "$FILE"
```

```bash
while echo -n "0202020200000005735249000068" | xxd -r -p | nc -w 2 10.119.24.84 2112 | xxd -p; do :; done
```

### Reference
[SOPAS Communication Interface Description.zip](https://github.com/ericwu1997/ericwu1997.github.io/raw/refs/heads/main/content/docs/app-layer-protocols/cola-b/SOPAS_Communication_Interface_Description.zip)