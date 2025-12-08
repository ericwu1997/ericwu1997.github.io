---
title: PROFINET PTCP
parent: OT Layer 2
nav_order: 2
---

# PROFINET PTCP (Precision Time Control Protocol)
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
PROFINET RT PTCP (Precision Time Control Protocol) is part of the PROFINET Real-Time communication framework that provides precision time synchronization across networked devices. It aligns the clocks of all nodes to enable consistent cycle timing for both cyclic and isochronous data exchange, supporting coordinated operations in standard RT as well as the stricter timing requirements of IRT. PTCP is also used for acyclic tasks such as clock master election through announce messages.

### Frame ID
```
https://github.com/boundary/wireshark/blob/master/plugins/profinet/packet-pn-ptcp.c#L810-L865
```
```
0x0020-0x0021: Real-Time: Sync (with follow up)
0x0080-0x0081: Real-Time: Sync (without follow up)

0xFF00-0xFF01: PTCP Announce
0xFF02-0xFF1F: Reserved
0xFF20-0xFF21: PTCP Follow Up
0xFF22-0xFF3F: Reserved
0xFF40-0xFF43: Acyclic Real-Time: Delay
```

### Reference
[https://github.com/boundary/wireshark/blob/master/plugins/profinet/packet-pn.h](https://github.com/boundary/wireshark/blob/master/plugins/profinet/packet-pn-ptcp.c#L810-L865)<br>
[https://github.com/ericwu1997/references/blob/master/Technical-Specification-for-PROFINET.zip](Technical-Specification-for-PROFINET.zip)<br>