---
title: Vivotek UDP Broadcast
parent: Protocol Analysis
nav_order: 1
has_toc: false
---

# Vivotek UDP Broadcast
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
Vivotek UDP Broadcast is a protocol used in the ["Shepherd Device Management Tool"](https://www.vivotek.com/products/software/shepherd) for discovering Vivotek Devices

### Structure
Request<br>
```
0000   01 f5 dd 76 03                                    ...v.
```
- 01 - Request
- F5 DD 76 - Seems to be sequence number, value can vary
- 03 - Always the same for scan request

Response<br>
```
0000   02 f5 dd 76 03 01 11 49 42 39 33 36 30 2d 56 56   ...v...IB9360-VV
0010   54 4b 2d 30 32 32 33 62 02 06 00 02 d1 97 64 70   TK-0223b......dp
0020   03 04 a9 fe 08 2a 04 24 06 02 3d 22 16 02 bb 01   .....*.$..="....
0030   08 02 65 6e 09 08 49 42 39 33 36 30 2d 48 10 04   ..en..IB9360-H..
0040   03 00 82 00 0a 01 00 17 03 01 01 81 05 04 00 00   ................
0050   00 00                                             ..
```
- 02 -  Reply
- F5 DD 76 - Seems to be sequence number, must be the same as the one in request
- 01 11 - tag for long name (\x01), followed by length (\x11). Name format: Model-VVTK-Version. In the case above, the model name is IB9360, Firmware version is 0223b.
- 02 06 - tag for mac address (\x02), followed by length (\x06). 00:02:D1:97:64:70
- 03 04 - tag for IP address (\x03), followed by length (\x04). 169.254.8.42
- 04 24 - Unknown type (\x04), followed by length (\x24)
- 05 05 - Unknown type (\x05), followed by length (\x24)

### Discovery Request
*The hex value "ABCDEF" seems to be session identifier, thus value can vary
```
echo -n "01ABCDEF03" | xxd -r -p | netcat -u -p 5678 XXX.XXX.XXX.XXX 10000
```

### Wireshark Filter
```
udp.payload[0:1] == 02 && udp.payload[4:2] == 03:01 && udp.srcport==10000
```