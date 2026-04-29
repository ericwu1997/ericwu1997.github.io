---
title: (TCP 20000) DNP3
parent: Transport Layer
---

# Distributed Network Protocol 3
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
DNP3 (Distributed Network Protocol) is a vendor-neutral protocol used in SCADA and electric utility systems for communication between control centers (masters) and field devices (outstations). It typically runs over serial links or TCP/IP (commonly port 20000) and supports reading data, reporting events, and issuing control commands. DNP3 is designed for reliability in noisy environments and includes features like event-based reporting, time-stamping, and optional secure authentication for improved security and integrity.

## Wireshark dissector tree view & Hex dump

Function Code: Authentication Request (0x20)<br>
Authentication Session Key Status Request (Obj:120, Var:04) (0x7804)<br>

```
Distributed Network Protocol 3.0
    Data Link Layer, Len: 14, From: 3, To: 4, DIR, PRM, Unconfirmed User Data
        Start Bytes: 0x0564
        Length: 14
        Control: 0xc4 (DIR, PRM, Unconfirmed User Data)
        Destination: 4
        Source: 3
        Data Link Header checksum: 0xd36d [correct]
        [Data Link Header Checksum Status: Good]
    Transport Control: 0xc0, Final, First(FIR, FIN, Sequence 0)
    Data Chunks
    [1 DNP 3.0 AL Fragment (8 bytes): #4(8)]
    Application Layer: (FIR, FIN, Sequence 1, Authentication Request)
        Application Control: 0xc1, First, Final(FIR, FIN, Sequence 1)
        Function Code: Authentication Request (0x20)
        Authentication Request Data Objects
            Object(s): Authentication Session Key Status Request (Obj:120, Var:04) (0x7804), 1 point
                Qualifier Field, Prefix: None, Range: 8-bit Single Field Quantity
                Number of Items: 1
                Point Number 0
                User Number: 1


0000   05 64 0e c4 04 00 03 00 6d d3 c0 c1 20 78 04 07   .d......m... x..
0010   01 01 00 9e 40   
```

## Reference 
[DNP3 Specification Volumn 1](https://cdn.chipkin.com/assets/uploads/imports/resources/DNP3Introduction-Draft_G.pdf)<br>
[Wireshark DNP3 Dissector](https://fossies.org/linux/wireshark/epan/dissectors/packet-dnp.c)<br>