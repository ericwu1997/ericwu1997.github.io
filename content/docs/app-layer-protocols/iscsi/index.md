---
title: iSCSI
description: iSCSI (Internet Small Computer System Interface)
permalink: /docs/app-layer-protocols/iscsi/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-19
updateTime: 2026-09-19
tags: [Markdown, Writing]
---

# Overview
**iSCSI** (Internet Small Computer System Interface) is a transport protocol that encapsulates SCSI storage commands over TCP/IP, letting an initiator (client) address a remote target (disk array or SAN) as ordinary block storage. It runs over **TCP port 3260**, mandated by its governing standard (**RFC 7143**, consolidating the original RFC 3720) and registered with IANA, in a unicast, connection-oriented initiator–target architecture.

During the cleartext Login Phase, the initiator and target exchange text key–value pairs including **InitiatorName** and **TargetName**, each formatted as an **iSCSI Qualified Name (IQN)** — e.g. `iqn.1994-05.com.redhat:87b1e10c9dd0` — or, less commonly, an EUI-64 (`eui.<16 hex digits>`) or NAA identifier. These names are unique, persistent identifiers for the specific initiator host and target device, sent unauthenticated and readable directly off the wire before any CHAP negotiation or encryption takes effect.

# Reference
[RFC 7143 - Internet Small Computer System Interface (iSCSI) Protocol (Consolidated)](https://www.rfc-editor.org/rfc/rfc7143)<br>
[iSCSI - Wireshark Wiki](https://wiki.wireshark.org/iSCSI)<br>
