---
title: LDP
description: LDP (Lantronix Discovery Protocol)
permalink: /docs/app-layer-protocols/ldp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-08-05
updateTime: 2026-08-05
tags: [Markdown, Writing]
---

### Overview

LDP (Lantronix Discovery Protocol) is a UDP-based protocol used by Lantronix tools, such as DeviceInstaller, to discover and identify Lantronix devices on a network. It commonly uses UDP port 30718 for discovery communication.

### Device Identification

Lantronix devices use predefined device IDs, with each ID corresponding to a specific product family or device type. The mapping of device IDs to product families can be found in the PIB (Product Information Base) file. The following hex dump shows an example request and response exchanged during the device discovery process. In this example, the device ID X9 identifies the device as an XPort-05.

| Filter            | Hex               | Description   | 
| ----------------- | ----------------- |-------------- |
| udp.payload[8:2]  | 58 39             | Device ID: X9 |
| udp.payload[24:6] | 00 80 a3 XX XX XX | Mac           |

```
echo -n "000000f6" | xxd -r -p | netcat -u XXX.XXX.XXX.XXX 30718
```
```
(00 01 00 f6 seems to do the same)
0000   00 00 00 f6                                       ....

0000   00 00 00 f7 XX XX XX XX 58 39 XX XX XX XX XX XX   ..... ..X90.\...
0010   XX XX XX XX XX XX XX XX 00 80 a3 XX XX XX         b...........C.
```

| Filter             | Hex                  | Description   | 
| ------------------ | -------------------- |---------------------------------- |
| udp.payload[16:7]  | 36 2e 39 2e 30 2e 32 | Extended Firmware Version 6.9.0.2 |

```
echo -n "000000f4" | xxd -r -p | netcat -u XXX.XXX.XXX.XXX 30718
```
```
0000   00 00 00 f4                                       ....

0000   00 00 00 f5 XX XX XX XX XX XX XX XX XX XX XX XX   ............\...
0010   36 2e 39 2e 30 2e 32 XX XX XX XX XX XX XX XX XX   6.9.0.2.....C...
0020   XX                                                .
```

### Reference 
[Product Information Base (PIB) Viewer](https://ts.lantronix.com/ftp/cpr/Generic/4.3/4.3.1.1/Help/Web/PIB_Viewer.htm)<br>
[Lantronix deviceinstaller](https://ts.lantronix.com/ftp/deviceinstaller/lantronix/4.4/4.4.0.7/Installers/Download_Web/)