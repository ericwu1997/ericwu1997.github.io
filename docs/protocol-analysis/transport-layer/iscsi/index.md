---
title: (TCP 3260) iSCSI
parent: Transport Layer
nav_order: 2
---

# Internet Small Computer Systems Interface (iSCSI)
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
<b>ISCSI</b> (Internet Small Computer System Interface) is a transport layer protocol that describes how Small Computer System Interface (SCSI) packets should be transported over a TCP/IP network. The iSCSI protocol encapsulates SCSI commands and assembles the data in packets for the TCP/IP layer. The protocol typically runs on port <b>3260</b>. 

### iscsiadm
The iscsiadm utility is a command-line tool allowing discovery and login to iSCSI targets. Some iSCSI commands related to device info and login are listed below.

1. Discover available targets from a discovery portal
```
### Example CLI output
┌──(root㉿kali)-[/home/kali]
└─# iscsiadm -m discovery -t sendtargets -p 10.0.0.1                                   
10.0.0.1:3260,1 iqn.2004-04.com.qnap:ts-431u:iscsi.vmware.fa8a99
10.0.0.1:3260,1 iqn.2004-04.com.qnap:ts-431u:iscsi.vmware.fa8a99
```

2. Login to all targets/specific target
```
iscsiadm -m node -l
iscsiadm -m node -T targetname -p ipaddress -l
```

3. Log out of all targets/specific target
```
iscsiadm -m node -u
iscsiadm -m node -T targetname -p ipaddress -u
```

4. Display information about a target
```
iscsiadm -m node -T targetname -p ipaddress
```

5. Display statistics of a target:
```
iscsiadm -m node -s -T targetname -p ipaddress
```

### Qualified Name (IQN)
The iSCSI Qualified Name (IQN) format takes the form iqn.yyyy-mm.naming-authority:unique name
- yyyy-mm is the year and month when the naming authority was established
- naming-authority is the reverse syntax of the Internet domain name of the naming authority. For example, the iscsi.vmware.com naming authority can have the iSCSI qualified name form of iqn.1998-01.com.vmware.iscsi. The name indicates that the vmware.com domain name was registered in January of 1998, and iscsi is a subdomain, maintained by vmware.com
- unique name is any name you want to use, for example, the name of your host. The naming authority must make sure that any names assigned following the colon are unique, such as:

### Sample Reply Hex Dump (Discovery)
bit [4:5] in the Opcode section indicates the flow of traffic. (..10) indicates a server reply, (..00) indicates request.
```
iSCSI (Text Response) 
    ..10 0100 = Opcode: Text Response (0x24)
    Flags: 0x80
        1... .... = F: Final PDU in sequence
        .0.. .... = C: Text is complete
    TotalAHSLength: 0 (0x00)
    DataSegmentLength: 133 (0x00000085)
    LUN
    InitiatorTaskTag: 0x00000001
    TargetTransferTag: 0xffffffff
    StatSN: 3003212686 (0xb301638e)
    ExpCmdSN: 2 (0x00000002)
    MaxCmdSN: 2 (0x00000002)
    Key/Value Pairs
        KeyValue: TargetName=iqn.2004-04.com.qnap:ts-431u:iscsi.vmware.fa8a99
        KeyValue: TargetAddress=XXX.XX.XXX.XXX:3260,1
        KeyValue: TargetAddress=192.168.100.250:3260,1
    Padding: 000000

0000   24 80 00 00 00 00 00 85 00 00 00 00 00 00 00 00   $...............
0010   00 00 00 01 ff ff ff ff b3 01 63 8e 00 00 00 02   ..........c.....
0020   00 00 00 02 00 00 00 00 00 00 00 00 00 00 00 00   ................
0030   54 61 72 67 65 74 4e 61 6d 65 3d 69 71 6e 2e 32   TargetName=iqn.2
0040   30 30 34 2d 30 34 2e 63 6f 6d 2e 71 6e 61 70 3a   004-04.com.qnap:
0050   74 73 2d 34 33 31 75 3a 69 73 63 73 69 2e 76 6d   ts-431u:iscsi.vm
0060   77 61 72 65 2e 66 61 38 61 39 39 00 54 61 72 67   ware.fa8a99.Targ
0070   65 74 41 64 64 72 65 73 73 3d XX XX XX 2e XX XX   etAddress=XXX.XX
0080   2e XX XX XX 2e XX XX XX 3a 33 32 36 30 2c 31 00   .XXX.XXX:3260,1.
0090   54 61 72 67 65 74 41 64 64 72 65 73 73 3d 31 39   TargetAddress=19
00a0   32 2e 31 36 38 2e 31 30 30 2e 32 35 30 3a 33 32   2.168.100.250:32
00b0   36 30 2c 31 00 00 00 00                           60,1....
```

## Reference
[Internet Small Computer Systems Interface (iSCSI) Naming and Discovery](https://datatracker.ietf.org/doc/html/rfc3721#page-5)<br>
[iscsiadm(8) - Linux man page](https://linux.die.net/man/8/iscsiadm)