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

**CoLa-B (Command Language Binary)** is the binary variant of SICK AG's **CoLa** command protocol, part of the **SOPAS** device-communication framework used by SICK industrial sensors such as LiDAR/laser scanners, radar sensors and other detection devices. It runs over **TCP**, typically on **port 2112**. On many devices this port defaults to the ASCII variant CoLa-A and can be switched to CoLa-B, while **port 2111** carries CoLa-A. Neither port is an IANA assignment for SICK; both are vendor defaults. CoLa-B follows a **client-server** model: a host (PLC, PC, or the SOPAS ET configuration tool) sends command telegrams to the sensor to read and write variables, invoke methods, and subscribe to events such as scan-data streams.

Every CoLa-B telegram begins with a fixed **4-byte start sequence `02 02 02 02`**, followed by a **4-byte big-endian length** field, the payload, and a **1-byte XOR checksum** over the payload bytes. The payload opens with a 3-byte ASCII command type: `sRN`/`sRI` (read by name/index), `sWN` (write by name), `sMN` (method), `sEN` (event), with matching replies `sRA`, `sWA`, `sAN`, `sEA`. The variable or method is addressed either by name (e.g. `DeviceIdent`) or by a 2-byte index. A **DeviceIdent** read returns length-prefixed ASCII strings for the device name and firmware version (e.g. `ML20` / `1.110`), and related variables expose the serial number and order number. CoLa-B traffic is sent in **cleartext**. Write and method access is gated by a `SetAccessMode` login that sends a user level and a password hash, with no transport encryption. The newer CoLa-2 variant (port 2122) uses a different session-based framing.

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

![](/img/cola-b/figure-1.png)

#### Request Frame
![](/img/cola-b/figure-2.png)

#### Response Frame
![](/img/cola-b/figure-3.png)

checksum = XOR all bytes 9 to 13

### CoLa-A Dataframe
telegram_listing_nav210_en_im0084703.pdf#page=5&zoom=100,97,700

![](/img/cola-b/figure-4.png)

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

![](/img/cola-b/figure-5.png)

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
[SOPAS Communication Interface Description.zip](https://github.com/ericwu1997/ericwu1997.github.io/raw/refs/heads/main/content/docs/app-layer-protocols/cola-b/SOPAS_Communication_Interface_Description.zip)<br>
