---
title: SSDP
description: SSDP (Simple Service Discovery Protocol)
permalink: /docs/app-layer-protocols/ssdp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-18
updateTime: 2026-09-18
tags: [Markdown, Writing]
---

### Overview
SSDP is a text-based, HTTP-style protocol over **UDP port 1900** for
advertisement and discovery of network services and presence information.
It is the basis of the discovery mechanism in Universal Plug and Play
(UPnP), intended for residential or small-office environments.

SSDP uses the HTTP method **NOTIFY** to announce the establishment or
withdrawal of services (presence information) to a multicast group. A
client that wishes to discover available services on a network uses the
method **M-SEARCH**. Responses to such search requests are sent via unicast
addressing to the originating address and port number of the multicast
request.


### M-SEARCH Request

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:25%"><col style="width:75%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Field</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">M-SEARCH * HTTP/1.1</td>
      <td style="border:1px solid #333; padding:8px 12px;">Literal request line. No colon, unlike the headers below.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">HOST</td>
      <td style="border:1px solid #333; padding:8px 12px;">SSDP multicast address/port, always <code>239.255.255.250:1900</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">MAN</td>
      <td style="border:1px solid #333; padding:8px 12px;">Discovery indicator, always the quoted literal <code>"ssdp:discover"</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">MX</td>
      <td style="border:1px solid #333; padding:8px 12px;">Max wait (seconds) before a device sends its response, e.g. <code>MX: 2</code>. Devices randomize their reply delay within this window.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">ST</td>
      <td style="border:1px solid #333; padding:8px 12px;">Search target (what to look for), e.g. <code>ssdp:all</code>, <code>upnp:rootdevice</code>, or a specific <code>urn:schemas-upnp-org:device:...</code> type/version.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Terminator</td>
      <td style="border:1px solid #333; padding:8px 12px;">Blank line ending the header block, per HTTP-style message framing. Value is <code>CRLF CRLF</code>.</td>
    </tr>
  </tbody>
</table>

### Search Response

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:25%"><col style="width:75%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Field</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">HTTP/1.1 200 OK</td>
      <td style="border:1px solid #333; padding:8px 12px;">Literal status line. No colon, unlike the headers below.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">CACHE-CONTROL</td>
      <td style="border:1px solid #333; padding:8px 12px;">How long this advertisement is valid, e.g. <code>CACHE-CONTROL: max-age=1800</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">EXT</td>
      <td style="border:1px solid #333; padding:8px 12px;">Empty header confirming compliance with the UPnP base standard. Present with no value.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">LOCATION</td>
      <td style="border:1px solid #333; padding:8px 12px;">URL of the device/service description document, served on an arbitrary TCP port (not the UDP 1900 discovery port), e.g. <code>LOCATION: http://192.168.1.5:8080/desc.xml</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">SERVER</td>
      <td style="border:1px solid #333; padding:8px 12px;">OS/version, UPnP/version, and product/version of the responding device, e.g. <code>SERVER: Linux/5.4 UPnP/1.1 MyDevice/1.0</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">ST</td>
      <td style="border:1px solid #333; padding:8px 12px;">Search target that was matched, echoing the value from the request, e.g. <code>upnp:rootdevice</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">USN</td>
      <td style="border:1px solid #333; padding:8px 12px;">Unique service name identifying this exact device/service instance, e.g. <code>uuid:abc123::upnp:rootdevice</code>.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Terminator</td>
      <td style="border:1px solid #333; padding:8px 12px;">Blank line ending the header block, per HTTP-style message framing. Value is <code>CRLF CRLF</code>.</td>
    </tr>
  </tbody>
</table>

### Nmap Script / Search Filter
```
nmap -sU -p 1900 --script=upnp-info 10.0.0.1
```
```
services.service_name: SSDP
```

### Sample Request and Response
*Note: this capture's M-SEARCH request uses bare LF (`\n`) line breaks rather than the CRLF CRLF the tables above describe — some real-world SSDP clients send LF-only framing and devices are commonly tolerant of it. The Response below uses standard CRLF.*

Request
```
0000   4d 2d 53 45 41 52 43 48 20 2a 20 48 54 54 50 2f   M-SEARCH * HTTP/
0010   31 2e 31 0a 48 6f 73 74 3a 20 32 33 39 2e 32 35   1.1.Host: 239.25
0020   35 2e 32 35 35 2e 32 35 30 3a 31 39 30 30 0a 4d   5.255.250:1900.M
0030   61 6e 3a 20 22 73 73 64 70 3a 64 69 73 63 6f 76   an: "ssdp:discov
0040   65 72 22 0a 53 54 3a 20 72 6f 6b 75 3a 65 63 70   er".ST: roku:ecp
0050   0a                                                .
```
Response
```
0000   48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d   HTTP/1.1 200 OK.
0010   0a 43 61 63 68 65 2d 43 6f 6e 74 72 6f 6c 3a 20   .Cache-Control: 
0020   6d 61 78 2d 61 67 65 3d 33 36 30 30 0d 0a 53 54   max-age=3600..ST
0030   3a 20 72 6f 6b 75 3a 65 63 70 0d 0a 55 53 4e 3a   : roku:ecp..USN:
0040   20 75 75 69 64 3a 72 6f 6b 75 3a 65 63 70 3a XX    uuid:roku:ecp:X
0050   XX XX XX XX XX XX XX XX XX XX XX 0d 0a 45 78 74   XXXXXXXXXXX..Ext
0060   3a 20 0d 0a 53 65 72 76 65 72 3a 20 52 6f 6b 75   : ..Server: Roku
0070   2f 31 34 2e 30 2e 34 20 55 50 6e 50 2f 31 2e 30   /14.0.4 UPnP/1.0
0080   20 52 6f 6b 75 2f 31 34 2e 30 2e 34 0d 0a 4c 4f    Roku/14.0.4..LO
0090   43 41 54 49 4f 4e 3a 20 68 74 74 70 3a 2f 2f 31   CATION: http://1
00a0   39 32 2e 31 36 38 2e 30 2e 34 3a 38 30 36 30 2f   92.168.0.4:8060/
00b0   0d 0a 64 65 76 69 63 65 2d 67 72 6f 75 70 2e 72   ..device-group.r
00c0   6f 6b 75 2e 63 6f 6d 3a 20 XX XX XX XX XX XX XX   oku.com: XXXXXXX
00d0   XX XX XX XX XX XX XX XX XX XX XX XX XX 0d 0a 0d   XXXXXXXXXXXXX...
00e0   0a                                                .
```

## Reference
[https://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol](https://en.wikipedia.org/wiki/Simple_Service_Discovery_Protocol)

[https://nmap.org/nsedoc/scripts/upnp-info.html](https://nmap.org/nsedoc/scripts/upnp-info.html)
