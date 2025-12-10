---
title: (TCP 8728:8729) MikroTik RouterOS API
parent: Vendor Specific P2P
---

# MikroTik RouterOS API
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
The MikroTik RouterOS API is a programmable interface that allows developers and network administrators to manage and automate RouterOS devices programmatically instead of using the GUI or CLI. It uses a proprietary binary-like protocol over TCP (default port 8728, or 8729 for TLS) and supports operations like configuring interfaces, firewall rules, queues, routing, and retrieving system information.
<br>
The API provides structured communication, returning data in key-value pairs, and can be accessed using various programming languages (e.g., Python, PHP, Go) through available client libraries. It is widely used for automation, monitoring, and integration with external systems like billing platforms, network management tools, and custom applications.

### API request format
A RouterOS API request is a sequence of words, each encoded as a length-prefixed string followed by its ASCII content, and terminated by a zero-length word (0x00). The length prefix uses a variable-length encoding (1–4 bytes) depending on the size of the word. Each command or attribute is sent as one word (e.g., /system/resource/print or =name=admin), and an empty word marks the end of the sentence. For example, /system/resource/print becomes 16 2F 73 79 73 74 65 6D 2F 72 65 73 6F 75 72 63 65 2F 70 72 69 6E 74 00 in hex, where 16 is the length (22 bytes) and 00 terminates the request. RouterOS API is very similar to the CLI in terms of commands and parameters, but the format for sending them is different.

### Censys Search
```
MikroTik and services.port=`8728`
```

## Sample Response
```
echo -n '\x06/login\x0b=name=admin\x0a=password=\x00' | netcat 10.0.0.1 8728
```
Login attempt and response
```
0000   06 2f 6c 6f 67 69 6e 0b 3d 6e 61 6d 65 3d 61 64   ./login.=name=ad
0010   6d 69 6e 10 3d 70 61 73 73 77 6f 72 64 3d 73 65   min.=password=se
0020   63 72 65 74 00                                    cret.


0000   05 21 74 72 61 70 2a 3d 6d 65 73 73 61 67 65 3d   .!trap*=message=
0010   69 6e 76 61 6c 69 64 20 75 73 65 72 20 6e 61 6d   invalid user nam
0020   65 20 6f 72 20 70 61 73 73 77 6f 72 64 20 28 36   e or password (6
0030   29 00 05 21 64 6f 6e 65 00                        )..!done.
```
Response for /system/routerboard/print (RouterOS API)
```
0000   03 21 72 65 11 3d 72 6f 75 74 65 72 62 6f 61 72   .!re.=routerboar
0010   64 3d 74 72 75 65 1f 3d 6d 6f 64 65 6c 3d 53 35   d=true.=model=S5
0020   33 55 47 2b 35 48 61 78 44 32 48 61 78 44 26 45   3UG+5HaxD2HaxD&E
0030   47 31 38 2d 45 41 1a 3d 73 65 72 69 61 6c 2d 6e   G18-EA.=serial-n
0040   75 6d 62 65 72 3d XX XX XX XX XX XX XX XX XX XX   umber=XXXXXXXXXX
0050   XX 16 3d 66 69 72 6d 77 61 72 65 2d 74 79 70 65   X.=firmware-type
0060   3d 69 70 71 36 30 30 30 15 3d 66 61 63 74 6f 72   =ipq6000.=factor
0070   79 2d 66 69 72 6d 77 61 72 65 3d 37 2e 38 18 3d   y-firmware=7.8.=
0080   63 75 72 72 65 6e 74 2d 66 69 72 6d 77 61 72 65   current-firmware
0090   3d 37 2e 31 39 2e 34 18 3d 75 70 67 72 61 64 65   =7.19.4.=upgrade
00a0   2d 66 69 72 6d 77 61 72 65 3d 37 2e 31 39 2e 34   -firmware=7.19.4
00b0   00 05 21 64 6f 6e 65 00                           ..!done.
```
Response for "system routerboard print" (RouterOS CLI) 
```
[demo@demo.mt.lv] > system routerboard print
                ;;; Firmware upgraded successfully, please reboot for changes to take effect!
       routerboard: yes                                                                      
        board-name: LtAP                                                                     
             model: RBLtAP-2HnD                                                              
     serial-number: D7240F566244                                                             
     firmware-type: mt7621L                                                                  
  factory-firmware: 6.47.10                                                                  
  current-firmware: 7.20beta7                                                                
  upgrade-firmware: 7.20beta9 
```

## References
[MikroTik RouterOS API documentation](https://help.mikrotik.com/docs/spaces/ROS/pages/47579160/API#API-Commandexamples)<br>
[RouterOS Console Cheat Sheet](https://www.mkesolutions.net/pdf/routeros-cheat-sheet-v1.1.pdf)<br>
[MikroTik DEMO server](https://mikrotik.com/software#:~:text=demo)<br>