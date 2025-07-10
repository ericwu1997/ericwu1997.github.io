---
title: (UDP 1812, 1813) RADISU
parent: Transport Layer
---

# GVCP (GigE Vision Control Protocol)
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
RADIUS is a UDP-based protocol for centralized Authentication, Authorization, and Accounting (AAA) of network users. It allows clients to send user credentials to a RADIUS server, which verifies access and logs usage. Commonly used for VPN, Wi-Fi, and ISP access, it supports standard and vendor-specific attributes.

### Hex dump
```
RADIUS Protocol
    Code: Access-Request (1)
    Packet identifier: 0x3a (58)
    Length: 257
    Authenticator: 01234567890123456789012345678901
    [The response to this request is in frame 16816]
    Attribute Value Pairs
        AVP: t=User-Name(1) l=18 val=XXXXXXXXX@XXXXXX
        AVP: t=CHAP-Password(3) l=19 val=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        AVP: t=CHAP-Challenge(60) l=18 val=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        AVP: t=NAS-IP-Address(4) l=6 val=192.168.1.89
        AVP: t=NAS-Identifier(32) l=9 val=telin̩
        AVP: t=NAS-Port(5) l=6 val=16785409
        AVP: t=NAS-Port-Id(87) l=18 val=0100002000000001
        AVP: t=NAS-Port-Type(61) l=6 val=Wireless-802.11(19)
        AVP: t=Service-Type(6) l=6 val=Framed(2)
        AVP: t=Framed-Protocol(7) l=6 val=Ascend-ARA(255)
        AVP: t=Calling-Station-Id(31) l=19 val=XX-XX-XX-XX-XX-XX
        AVP: t=Called-Station-Id(30) l=22 val=XXXX-XXXX-XXXX:test2
        AVP: t=Acct-Session-Id(44) l=16 val=11308131713150
        AVP: t=Framed-IP-Address(8) l=6 val=192.168.1.68
        AVP: t=Vendor-Specific(26) l=62 vnd=HUAWEI Technology Co.,Ltd(2011)
            Type: 26
            Length: 62
            Vendor ID: HUAWEI Technology Co.,Ltd (2011)
            VSA: t=Huawei-Connect-ID(26) l=6 val=59
            VSA: t=Huawei-Product-ID(255) l=12 val=H3C WX5004
            VSA: t=Huawei-IPHost-Addr(60) l=32 val=192.168.1.68 XX:XX:XX:XX:XX:XX
            VSA: t=Huawei-Startup-Stamp(59) l=6 val=1378832102

```
```
0000   01 3a 01 01 XX XX XX XX XX XX XX XX XX XX XX XX   .:....Qy..M<..\.
0010   XX XX XX XX 01 12 XX XX XX XX XX XX XX XX XX XX   ......XXXXXXXXX@
0020   XX XX XX XX XX XX 03 13 XX XX XX XX XX XX XX XX   XXXXXX....F.....
0030   XX XX XX XX XX XX XX XX XX 3c 12 XX XX XX XX XX   .=....m2.<...Qy.
0040   XX XX XX XX XX XX XX XX XX XX XX 04 06 c0 a8 01   .M<..\..........
0050   59 20 09 74 65 6c 69 6e cc a9 05 06 01 00 20 01   Y .telin...... .
0060   57 12 30 31 30 30 30 30 32 30 30 30 30 30 30 30   W.01000020000000
0070   30 31 3d 06 00 00 00 13 06 06 00 00 00 02 07 06   01=.............
0080   00 00 00 ff 1f 13 XX XX 2d XX XX 2d XX XX 2d XX   ......XX-XX-XX-X
0090   XX 2d XX XX 2d XX XX 1e 16 XX XX XX XX 2d XX XX   X-XX-XX..XXXX-XX
00a0   XX XX 2d XX XX XX XX 3A XX XX XX XX XX 2c 10 31   XX-XXXX:test2,.1
00b0   31 33 30 38 31 33 31 37 31 33 31 35 30 08 06 c0   1308131713150...
00c0   a8 01 44 1a 3e 00 00 07 db 1a 06 00 00 00 3b ff   ..D.>.........;.
00d0   0c 48 33 43 20 57 58 35 30 30 34 3c 20 31 39 32   .H3C WX5004< 192
00e0   2e 31 36 38 2e 31 2e 36 38 20 XX XX 3a XX XX 3a   .168.1.68 XX:XX:
00f0   XX XX 3a XX XX 3a XX XX 3a XX XX 3b 06 52 2f 4e   XX:XX:XX:XX;.R/N
0100   e6                                                .
```

## Reference 
[Wireshark RADIUS Dissector Github](https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-radius.c)<br>