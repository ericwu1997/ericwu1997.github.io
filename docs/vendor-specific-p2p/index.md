---
title: Vendor Specific P2P
nav_order: 3
---

# Vendor Specific P2P
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Blackmagic HyperDeck Ethernet Protocol
References:<br>
[hyperdeck-disk-recorders/developer-information#protocol-details](https://usermanual.com/support/blackmagicdesign/web-manual/hyperdeck-disk-recorders/developer-information#protocol-details)<br>
```
echo -n "device\x20info\x0d\x0a" | netcat XXX.XXX.XXX.XXX 9993
```
```
0000   35 30 30 20 63 6f 6e 6e 65 63 74 69 6f 6e 20 69   500 connection i
0010   6e 66 6f 3a 0d 0a 70 72 6f 74 6f 63 6f 6c 20 76   nfo:..protocol v
0020   65 72 73 69 6f 6e 3a 20 31 2e 30 0d 0a 6d 6f 64   ersion: 1.0..mod
0030   65 6c 3a 20 41 54 45 4d 20 53 44 49 20 45 78 74   el: ATEM SDI Ext
0040   72 65 6d 65 20 49 53 4f 0d 0a 66 72 69 65 6e 64   reme ISO..friend
0050   6c 79 20 6e 61 6d 65 3a 20 41 54 45 4d 20 53 44   ly name: ATEM SD
0060   49 20 45 78 74 72 65 6d 65 20 49 53 4f 0d 0a 75   I Extreme ISO..u
0070   6e 69 71 75 65 20 69 64 3a 20 XX XX XX XX XX XX   nique id: XXXXXX
0080   XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX   XXXXXXXXXXXXXXXX
0090   XX XX XX XX XX XX XX XX XX XX 0d 0a 0d 0a 32 30   XXXXXXXXXX....20
00a0   34 20 64 65 76 69 63 65 20 69 6e 66 6f 3a 0d 0a   4 device info:..
00b0   70 72 6f 74 6f 63 6f 6c 20 76 65 72 73 69 6f 6e   protocol version
00c0   3a 20 31 2e 30 0d 0a 6d 6f 64 65 6c 3a 20 41 54   : 1.0..model: AT
00d0   45 4d 20 53 44 49 20 45 78 74 72 65 6d 65 20 49   EM SDI Extreme I
00e0   53 4f 0d 0a 66 72 69 65 6e 64 6c 79 20 6e 61 6d   SO..friendly nam
00f0   65 3a 20 41 54 45 4d 20 53 44 49 20 45 78 74 72   e: ATEM SDI Extr
0100   65 6d 65 20 49 53 4f 0d 0a 75 6e 69 71 75 65 20   eme ISO..unique 
0110   69 64 3a XX XX XX XX XX XX XX XX XX XX XX XX XX   id: XXXXXXXXXXXX
0120   XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX   XXXXXXXXXXXXXXXX
0130   XX XX XX XX 0d 0a 0d 0a                           XXXX....
```