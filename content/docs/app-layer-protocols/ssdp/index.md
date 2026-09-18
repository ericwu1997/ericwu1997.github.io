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
<!-- Frontmatter (title, parent, and other page metadata) is out of scope for
     this skill - handled by a separate metadata skill. Insert its output
     above this line before publishing. -->

# Simple Service Discovery Protocol
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. [Overview](#overview)
2. [M-SEARCH Request Headers](#m-search-request-headers)
3. [Response Headers](#response-headers)
4. [Nmap Script / Search Filter](#nmap-script--search-filter)
5. [Sample Request and Response](#sample-request-and-response)
6. [Reference](#reference)

---

## Overview
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

## M-SEARCH Request Headers
| **Field** | **Example** | **Note** |
|---|---|---|
| Host | `239.255.255.250:1900` | SSDP multicast address:port |
| Man | `"ssdp:discover"` | Identifies the request as a discovery search |
| ST | `roku:ecp` | Search target — service/device type being searched for |

## Response Headers
| **Field** | **Example** | **Note** |
|---|---|---|
| Cache-Control | `max-age=3600` | Advertisement lifetime |
| ST | `roku:ecp` | Search target that matched |
| USN | `uuid:roku:ecp:XXXXXXXXXXXX` | Unique service name — masked device UUID |
| Ext | *(empty)* | Present for backward compatibility only, carries no value |
| Server | `Roku/14.0.4 UPnP/1.0 Roku/14.0.4` | OS/UPnP-stack/product version — the primary device-identification field in an SSDP response |
| Location | `http://192.168.0.4:8060/` | URL of the device description document |

## Nmap Script / Search Filter
```
nmap -sU -p 1900 --script=upnp-info 10.0.0.1
```
```
services.service_name: SSDP
```

## Sample Request and Response
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
