---
title: (TCP 40001) SUS SiO
parent: Transport Layer
---

# SUS SiO Ethernet IO protocol
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
SiO-X Ethernet Communication Protocol is a simple ASCII-based TCP protocol used to interact with the SiO-X Controller over Ethernet. It allows a client (e.g., PC or automation host) to connect to the controller’s TCP server (default port 40001), issue commands to read or write controller states and parameters, and receive structured ASCII responses. All command messages begin with the character @, end with CR/LF, and use ASCII encoding for command and response fields.

## Commands
For additional payload formats, refer to the insturction manual

Readout

| **#** | **#** | **#** |
|--------------------------------|--------------------------------|--------------------------------|
| R01 IO State Readout | R20 Bulk State Readout | R39 Barcode Log Readout |
| R02 Flag State Readout | R21 Bulk State Readout | R40 Barcode Char Count Readout |
| R03 IO State Readout | R22 Flag State Readout | R43 Serial Response Value Readout |
| R04 Flag State Readout | R23 Flag State Readout | R44 Serial Error Readout |
| R06 Run Uptime Readout | R24 Flag Counter Readout | R45 Serial Cutout Value Readout |
| R07 Out Counter Readout | R25 Ether Flag State Readout | R47 Serial Settings Readout |
| R09 Flag Counter Value Readout | R26 Flag State Readout | R48 Function Timer Value Readout |
| R10 Run State Readout | R27 Flag Counter Readout | R49 Function Counter Value Readout |
| R11 Run State Readout | R28 TP Connection Status Readout | R50 Multi Select State Readout |
| R12 Out Counter Readout | R29 Flag Counter Value Readout | R51 Free Input State Readout |
| R13 Flag Counter Readout | R30 SD Card Log Readout | R52 Controller Time Readout |
| R15 Connection State Readout | R31 SD Card Log Number Readout | R53 Controller ID Readout |
| R16 Mac Address Readout | R32 SD Card Insertion Status Readout | R56 Run Status & Connector Status Read |
| R17 Controller Name Readout | R33 SD Card Remaining Capacity Readout | R57 Ether Barcode Registration Readout |
| R19 Version Readout | R34 SD Card Log Data Init | R58 Last Value Scan Time Readout |
|  | R37 Barcode Scan Data Readout | R59 Ether Integer Readout |
|  | R38 Barcode Matched Result Readout | R60 Ether Decimal Readout |
|  |  | R61 Time Function State Readout |
|  |  | R62 TP-IN State Readout |
|  |  | R63 Serial Comm Data Readout |

Writeout

| **#** | **#** | **#** |
|--------------------------------|--------------------------------|--------------------------------|
| W03 Out State Write | W10 Run State Write | W20 Ether Decimal Write |
| W04 Ether Flag State Write | W17 Controller Name Write | W19 Ether Integer Write |
| W09 Ether Barcode Registration Write |  |  |

## Sample Request
Request (R20 Bulk State Readout)
```
0000   40 52 32 30 0d 0a                                 @R20..
```

## References
[SiO Controller Instruction Manual](https://fa.sus.co.jp/products/sio/software/sio_manual/)<br>
[siox_ethernet_manual_1_4.pdf](https://fa.sus.co.jp/products/files/siox_ethernet_manual_1_4.pdf)