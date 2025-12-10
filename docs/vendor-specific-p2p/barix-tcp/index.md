---
title: (TCP 12302) Barix TCP
parent: Vendor Specific P2P
---

# Barix TCP Command Interface
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
The Barix Instreamer’s TCP command interface on port 12302 accepts ASCII commands in the form c=<number>, each ending with CR, LF, or NUL. Commands control basic functions such as volume, streaming start/stop, reboot, and device discovery, and multiple commands can be chained with &. Only one TCP connection is allowed at a time, and the device returns simple acknowledgment or error responses based on the command.
<br>
Commands to the Barix Instreamer are sent as ASCII strings in the format c=<number>, optionally chaining multiple commands with &. Each command must end with a CR, LF, or NUL terminator, and the device responds with an acknowledgment or error depending on the command’s validity.

### Search Engine filter
Censys
```
services.http.response.html_tags="<title>Barix Instreamer Instreamer</title>" and services.port=`12302`
```
Shodan
```
instreamer
```

### Sample Request/Response
#### DISCOVER
```
echo "633D363535333500" | xxd -r -p | nc XXX.XXX.XX.XXX 12302
```
```
0000   63 3d 36 35 35 33 35 00                           c=65535.
```
```
0000   3c 49 4e 53 54 52 45 41 4d 45 52 3e 3c 48 57 54   <INSTREAMER><HWT
0010   59 50 45 3e 38 3c 2f 48 57 54 59 50 45 3e 3c 49   YPE>8</HWTYPE><I
0020   50 41 4d 54 59 50 45 3e 30 3c 2f 49 50 41 4d 54   PAMTYPE>0</IPAMT
0030   59 50 45 3e 3c 43 4f 44 45 43 54 59 50 45 3e 32   YPE><CODECTYPE>2
0040   3c 2f 43 4f 44 45 43 54 59 50 45 3e 3c 53 4f 46   </CODECTYPE><SOF
0050   54 57 41 52 45 3e 34 2e 35 3c 2f 53 4f 46 54 57   TWARE>4.5</SOFTW
0060   41 52 45 3e 3c 49 50 3e XX XX XX 2e XX XX XX 2e   ARE><IP>XXX.XXX.
0070   XX XX 2e XX XX XX 3c 2f 49 50 3e 3c 4d 41 43 3e   XX.XXX</IP><MAC>
0080   XX XX XX XX XX XX XX XX XX XX XX XX 3c 2f 4d 41   XXXXXXXXXXXX</MA
0090   43 3e 3c 4e 41 4d 45 3e 49 6e 73 74 72 65 61 6d   C><NAME>Instream
00a0   65 72 3c 2f 4e 41 4d 45 3e 3c 54 49 4d 45 3e 33   er</NAME><TIME>3
00b0   36 32 37 32 35 34 3c 2f 54 49 4d 45 3e 3c 2f 49   627254</TIME></I
00c0   4e 53 54 52 45 41 4d 45 52 3e 0a 00               NSTREAMER>..
```
#### GETCONFIG
```
echo "4C3D676574636F6E6669672E61636B00" | xxd -r -p | nc XXX.XXX.XX.XXX 12302
```
```
0000   4c 3d 67 65 74 63 6f 6e 66 69 67 2e 61 63 6b 00   L=getconfig.ack.
```
```
0000   3c 49 4e 53 54 52 45 41 4d 45 52 3e 0a 09 3c 53   <INSTREAMER>..<S
0010   54 41 54 45 3e 0a 09 09 3c 4d 41 43 3e XX XX XX   TATE>...<MAC>XXX
0020   XX XX XX XX XX XX XX XX XX 3c 2f 4d 41 43 3e 0a   XXXXXXXXX</MAC>.
0030   09 09 3c 49 50 3e XX XX XX 2e XX XX XX 2e XX XX   ..<IP>XXX.XXX.XX
0040   2e XX XX XX 3c 2f 49 50 3e 0a 09 09 3c 48 57 54   .XXX</IP>...<HWT
0050   59 50 45 3e 38 3c 2f 48 57 54 59 50 45 3e 0a 09   YPE>8</HWTYPE>..
0060   09 3c 49 50 41 4d 54 59 50 45 3e 30 3c 2f 49 50   .<IPAMTYPE>0</IP
0070   41 4d 54 59 50 45 3e 0a 09 09 3c 43 4f 44 45 43   AMTYPE>...<CODEC
0080   54 59 50 45 3e 32 3c 2f 43 4f 44 45 43 54 59 50   TYPE>2</CODECTYP
0090   45 3e 09 09 0a 09 09 3c 53 4f 46 54 57 41 52 45   E>.....<SOFTWARE
00a0   56 45 52 53 3e 30 34 30 35 5f 32 30 31 37 31 31   VERS>0405_201711
00b0   30 33 3c 2f 53 4f 46 54 57 41 52 45 56 45 52 53   03</SOFTWAREVERS
...
```

## References
[instreamer_tech_vb406_20220324.zip](https://release.barixupdate.com/Manuals/instreamer_tech_vb406_20220324.pdf)<br>