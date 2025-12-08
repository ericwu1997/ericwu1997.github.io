---
title: Device Searching Cases
nav_order: 2
---

# Device Broadcast Discovery
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### HID Global - VertX Controller UDP Discovery
References:<br>
[https://www.zerodayinitiative.com/advisories/ZDI-16-223/](https://www.zerodayinitiative.com/advisories/ZDI-16-223/)<br>
[https://github.com/coldfusion39/VertXploit/tree/master](https://github.com/coldfusion39/VertXploit/tree/master)
```
echo -n "discover;013;" | netcat -u XXX.XXX.XXX.XXX 4070
```
```
0000   64 69 73 63 6f 76 65 72 65 64 3b 30 39 36 3b XX   discovered;096;X
0010   XX 3a XX XX 3a XX XX 3a XX XX 3a XX XX 3a XX XX   X:XX:XX:XX:XX:XX
0020   3b 56 65 72 74 58 5f 45 56 4f 5f 56 32 30 30 30   ;VertX_EVO_V2000
0030   3b XX XX XX 2e XX XX XX 2e XX XX XX 2e XX XX 3b   ;XXX.XXX.XXX.XX;
0040   31 3b 56 32 2d 56 32 30 30 30 3b 33 2e 36 2e 33   1;V2-V2000;3.6.3
0050   2e 31 30 31 3b 30 37 2f 32 37 2f 32 30 31 37 3b   .101;07/27/2017;
```

### Roku - External Control Protocol (ECP)
References:<br>
[https://developer.roku.com/en-ca/docs/developer-program/dev-tools/external-control-api.md](https://developer.roku.com/en-ca/docs/developer-program/dev-tools/external-control-api.md)<br>
```
echo "M-SEARCH * HTTP/1.1\nHost:239.255.255.250:1900\nMan: \"ssdp:discover\"\nST: roku:ecp" | netcat -u XXX.XXX.XXX.XXX 1900
```
```
0000   48 54 54 50 2f 31 2e 31 20 32 30 30 20 4f 4b 0d   HTTP/1.1 200 OK.
0010   0a 43 61 63 68 65 2d 43 6f 6e 74 72 6f 6c 3a 20   .Cache-Control: 
0020   6d 61 78 2d 61 67 65 3d 33 36 30 30 0d 0a 53 54   max-age=3600..ST
0030   3a 20 72 6f 6b 75 3a 65 63 70 0d 0a 55 53 4e 3a   : roku:ecp..USN:
0040   20 75 75 69 64 3a 72 6f 6b 75 3a 65 63 70 3a 58    uuid:roku:ecp:X
0050   30 31 36 30 30 43 48 56 47 44 33 0d 0a 45 78 74   01600CHVGD3..Ext
0060   3a 20 0d 0a 53 65 72 76 65 72 3a 20 52 6f 6b 75   : ..Server: Roku
0070   2f 31 34 2e 30 2e 34 20 55 50 6e 50 2f 31 2e 30   /14.0.4 UPnP/1.0
0080   20 52 6f 6b 75 2f 31 34 2e 30 2e 34 0d 0a 4c 4f    Roku/14.0.4..LO
0090   43 41 54 49 4f 4e 3a 20 68 74 74 70 3a 2f 2f 31   CATION: http://1
00a0   39 32 2e 31 36 38 2e 30 2e 34 3a 38 30 36 30 2f   92.168.0.4:8060/
00b0   0d 0a 64 65 76 69 63 65 2d 67 72 6f 75 70 2e 72   ..device-group.r
00c0   6f 6b 75 2e 63 6f 6d 3a 20 37 45 37 38 39 30 35   oku.com: 7E78905
00d0   38 30 35 31 39 31 32 44 32 42 34 44 31 0d 0a 0d   8051912D2B4D1...
00e0   0a                                                .
```

### Axis - VAPIX mDNS
References:<br>
[https://developer.axis.com/vapix/network-video/mdns-sd-api#discover](https://developer.axis.com/vapix/network-video/mdns-sd-api#discover)<br>
```
dig _axis-video._tcp.local ptr @XXX.XXX.XXX.XXX -p 5353
dig _axis-nvr._tcp.local ptr @XXX.XXX.XXX.XXX -p 5353
```
```
0000   84 d1 84 00 00 01 00 01 00 00 00 04 0b 5f 61 78   ............._ax
0010   69 73 2d 76 69 64 65 6f 04 5f 74 63 70 05 6c 6f   is-video._tcp.lo
0020   63 61 6c 00 00 0c 00 01 c0 0c 00 0c 00 01 00 00   cal.............
0030   00 0a 00 1c 19 41 58 49 53 20 32 34 31 51 41 20   .....AXIS 241QA 
0040   2d 20 30 30 34 30 38 43 37 33 46 45 36 45 c0 0c   - 00408C73FE6E..
0050   c0 34 00 21 00 01 00 00 00 0a 00 1a 00 00 00 00   .4.!............
0060   00 50 11 61 78 69 73 2d 30 30 34 30 38 63 37 33   .P.axis-00408c73
0070   66 65 36 65 c0 1d c0 34 00 10 00 01 00 00 00 0a   fe6e...4........
0080   00 18 17 6d 61 63 61 64 64 72 65 73 73 3d XX XX   ...macaddress=XX
0090   XX XX XX XX XX XX XX XX XX XX c0 62 00 01 00 01   XXXXXXXXXX.b....
00a0   00 00 00 0a 00 04 80 df 0a 0e c0 62 00 01 00 01   ...........b....
00b0   00 00 00 0a 00 04 a9 fe 6b a5                     ........k.
```

### Vivotek - UDP port 10000
References:<br>
[https://www.vivotek.com/products/software/shepherd](https://www.vivotek.com/products/software/shepherd)<br>
[https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Vivotek.cs](https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Vivotek.cs)<br>
*The hex value "ABCDEF" seems to be session identifier, thus value can vary
```
echo -n "01ABCDEF03" | xxd -r -p | netcat -u -p 5678 XXX.XXX.XXX.XXX 10000
```
```
0000   02 f5 dd 76 03 01 11 49 42 39 33 36 30 2d 56 56   ...v...IB9360-VV
0010   54 4b 2d 30 32 32 33 62 02 06 00 02 d1 97 64 70   TK-0223b......dp
0020   03 04 a9 fe 08 2a 04 24 06 02 3d 22 16 02 bb 01   .....*.$..="....
0030   08 02 65 6e 09 08 49 42 39 33 36 30 2d 48 10 04   ..en..IB9360-H..
0040   03 00 82 00 0a 01 00 17 03 01 01 81 05 04 00 00   ................
0050   00 00                                             ..
```

### Vstarcam - UDP port 8600
References:<br>
[https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Vstarcam.cs](https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Vstarcam.cs)<br>
[Eye4 for Windows](https://www.vstarcam.com/software-download)<br>
```
echo -n "44480101" | xxd -r -p | netcat -u -p 8601 XXX.XXX.XXX.XXX 8600
```
```
0000   44 48 01 08 31 39 32 2e 31 36 38 2e 31 2e 35 31   DH..192.168.1.51
0010   00 00 00 00 32 35 35 2e 32 35 35 2e 32 35 35 2e   ....255.255.255.
0020   30 00 00 00 31 39 32 2e 31 36 38 2e 31 2e 31 00   0...192.168.1.1.
0030   00 00 00 00 38 2e 38 2e 38 2e 38 00 00 00 00 00   ....8.8.8.8.....
0040   00 00 00 00 31 39 32 2e 31 36 38 2e 31 2e 31 00   ....192.168.1.1.
0050   00 00 00 00 48 02 2d 01 5c e9 55 00 56 53 54 41   ....H.-.\.U.VSTA
0060   35 32 33 39 35 34 58 43 43 58 58 00 00 00 00 00   523954XCCXX.....
0070   00 00 00 00 00 00 00 00 00 00 00 00 49 50 43 41   ............IPCA
0080   4d 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   M...............
0090   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00a0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00b0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00c0   00 00 00 00 00 00 00 00 00 00 00 00 XX XX 2e XX   ............XX.X
00d0   XX 2e XX XX 2e XX XX 00 00 00 00 00 00 00 00 00   X.XX.XX.........
00e0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
00f0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0100   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0110   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0120   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0130   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0140   00 00 00 00 75 73 65 72 32 2e 67 6f 63 61 6d 2e   ....user2.gocam.
0150   73 6f 00 00 00 00 00 00 00 00 00 00 00 00 00 00   so..............
0160   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0170   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0180   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0190   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01a0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01b0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01c0   00 00 00 00 66 6a 65 64 72 00 00 00 00 00 00 00   ....fjedr.......
01d0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
01e0   00 00 00 00 38 31 39 38 33 39 00 00 00 00 00 00   ....819839......
01f0   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0200   00 00 00 00 44 48 01 08 31 39 32 2e               ....DH..192.
```

### Dahua - UDP DHCPDiscover port 37810
References:<br>
[https://www.shadowserver.org/what-we-do/network-reporting/open-dvr-dhcpdiscover-report/](https://www.shadowserver.org/what-we-do/network-reporting/open-dvr-dhcpdiscover-report/)<br>
```
echo -ne '\xff'|nc -u 218.5.136.140 37810
```
```
0000   20 00 00 00 44 48 49 50 00 00 00 00 00 00 00 00    ...DHIP........
0010   b4 02 00 00 00 00 00 00 b4 02 00 00 00 00 00 00   ................
0020   7b 22 6d 61 63 22 3a 22 XX XX 3a XX XX 3a XX XX   {"mac":"XX:XX:XX
0030   3a XX XX 3a XX XX 3a XX XX 22 2c 22 6d 65 74 68   :XX:XX:XX","meth
0040   6f 64 22 3a 22 63 6c 69 65 6e 74 2e 6e 6f 74 69   od":"client.noti
0050   66 79 44 65 76 49 6e 66 6f 22 2c 22 70 61 72 61   fyDevInfo","para
0060   6d 73 22 3a 7b 22 64 65 76 69 63 65 49 6e 66 6f   ms":{"deviceInfo
0070   22 3a 7b 22 41 6c 61 72 6d 49 6e 70 75 74 43 68   ":{"AlarmInputCh
0080   61 6e 6e 65 6c 73 22 3a 38 2c 22 41 6c 61 72 6d   annels":8,"Alarm
0090   4f 75 74 70 75 74 43 68 61 6e 6e 65 6c 73 22 3a   OutputChannels":
00a0   30 2c 22 44 65 76 69 63 65 43 6c 61 73 73 22 3a   0,"DeviceClass":
00b0   22 56 54 4f 22 2c 22 44 65 76 69 63 65 54 79 70   "VTO","DeviceTyp
00c0   65 22 3a 22 56 54 4f 32 30 30 30 41 2d 32 22 2c   e":"VTO2000A-2",
00d0   22 46 69 6e 64 22 3a 22 42 43 22 2c 22 48 74 74   "Find":"BC","Htt
00e0   70 50 6f 72 74 22 3a 38 30 2c 22 49 50 76 34 41   pPort":80,"IPv4A
00f0   64 64 72 65 73 73 22 3a 7b 22 44 65 66 61 75 6c   ddress":{"Defaul
0100   74 47 61 74 65 77 61 79 22 3a 22 31 39 32 2e 31   tGateway":"192.1
0110   36 38 2e 31 2e 31 22 2c 22 44 68 63 70 45 6e 61   68.1.1","DhcpEna
0120   62 6c 65 22 3a 66 61 6c 73 65 2c 22 49 50 41 64   ble":false,"IPAd
0130   64 72 65 73 73 22 3a 22 31 39 32 2e 31 36 38 2e   dress":"192.168.
0140   31 2e 32 30 32 22 2c 22 53 75 62 6e 65 74 4d 61   1.202","SubnetMa
0150   73 6b 22 3a 22 32 35 35 2e 32 35 35 2e 32 35 35   sk":"255.255.255
0160   2e 30 22 7d 2c 22 49 50 76 36 41 64 64 72 65 73   .0"},"IPv6Addres
0170   73 22 3a 7b 22 44 65 66 61 75 6c 74 47 61 74 65   s":{"DefaultGate
0180   77 61 79 22 3a 6e 75 6c 6c 2c 22 44 68 63 70 45   way":null,"DhcpE
0190   6e 61 62 6c 65 22 3a 66 61 6c 73 65 2c 22 49 50   nable":false,"IP
01a0   41 64 64 72 65 73 73 22 3a 22 5c 2f 30 22 2c 22   Address":"\/0","
01b0   4c 69 6e 6b 4c 6f 63 61 6c 41 64 64 72 65 73 73   LinkLocalAddress
01c0   22 3a 22 XX XX XX XX 3a 3a XX XX XX XX 3a XX XX   ":"XXXX::XXXX:XX
01d0   XX XX 3a XX XX XX XX 3a 34 66 65 35 5c 2f 36 34   XX:XXXX:4fe5\/64
01e0   22 7d 2c 22 49 6e 69 74 22 3a 33 32 32 32 2c 22   "},"Init":3222,"
01f0   4d 61 63 68 69 6e 65 4e 61 6d 65 22 3a 22 35 46   MachineName":"5F
0200   30 34 36 39 30 50 41 5a 46 30 39 33 34 22 2c 22   04690PAZF0934","
0210   4d 61 6e 75 66 61 63 74 75 72 65 72 22 3a 22 47   Manufacturer":"G
0220   65 6e 65 72 61 6c 22 2c 22 50 6f 72 74 22 3a 33   eneral","Port":3
0230   37 37 37 37 2c 22 52 65 6d 6f 74 65 56 69 64 65   7777,"RemoteVide
0240   6f 49 6e 70 75 74 43 68 61 6e 6e 65 6c 73 22 3a   oInputChannels":
0250   30 2c 22 53 65 72 69 61 6c 4e 6f 22 3a 22 XX XX   0,"SerialNo":"5F
0260   XX XX XX XX XX XX XX XX XX XX XX XX XX 22 2c 22   XXXXXXXXXXXXX","
0270   56 65 6e 64 6f 72 22 3a 22 47 65 6e 65 72 61 6c   Vendor":"General
0280   22 2c 22 56 65 72 73 69 6f 6e 22 3a 22 34 2e 33   ","Version":"4.3
0290   30 30 2e 30 30 30 30 30 30 30 2e 31 2e 52 22 2c   00.0000000.1.R",
02a0   22 56 69 64 65 6f 49 6e 70 75 74 43 68 61 6e 6e   "VideoInputChann
02b0   65 6c 73 22 3a 31 2c 22 56 69 64 65 6f 4f 75 74   els":1,"VideoOut
02c0   70 75 74 43 68 61 6e 6e 65 6c 73 22 3a 31 36 7d   putChannels":16}
02d0   7d 7d 0a 00                                       }}..
```

### Advantech - UDP discovery port 5048
References:<br>
[https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Advantech.cs](https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Advantech.cs)
```
echo -n "4D41444100000083010050(print "%0*d 84)20000000000000" | xxd -r -p | netcat -u XXX.XXX.XXX.XXX 5048
```
```
0000   4d 41 44 41 00 00 00 83 01 00 60 60 00 00 d0 c9   MADA......``....
0010   00 f8 81 13 0f 0f 0f 0f 0f 0f 0f 0f 00 00 00 00   ................
0020   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0030   00 00 00 00 80 20 00 48 00 00 00 00 00 07 00 1e   ..... .H........
0040   00 1f 00 07 00 01 00 e8 00 08 00 00 00 00 00 00   ................
0050   00 01 0d 53 00 03 84 00 00 00 00 32 00 01 c2 00   ...S.......2....
0060   31 30 32 30 00 00 00 18 41 44 41 4d 36 30 36 30   1020....ADAM6060
0070   20 44 69 67 69 74 61 6c 20 49 2f 4f 20 4d 6f 64    Digital I/O Mod
0080   75 6c 65 00 00                                    ule..
```

### Ubiquiti - UBNT Discovery UDP port 10001
References:<br>
[https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Ubiquiti.cs](https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Ubiquiti.cs)<br>
[https://github.com/MatrixEditor/ubnt-discovery-tool/blob/master/ubnt.lua](https://github.com/MatrixEditor/ubnt-discovery-tool/blob/master/ubnt.lua)<br>
[https://gist.github.com/sgrodzicki/265273ff0ede952d6fcd1a1eedb6aa60](https://gist.github.com/sgrodzicki/265273ff0ede952d6fcd1a1eedb6aa60)
```
echo -n "01000000" | xxd -r -p | netcat -u XXX.XXX.XXX.XXX 10001
```
```
0000   01 00 00 7d 02 00 0a [      MAC      ] [ IPADDR   ...}....*.!}.g-.
0010    ] 02 00 0a [      MAC      ] [  IPADDR ] 01 00   .....*. }.......
0020   06 80 2a a8 20 7d a5 0a 00 04 00 1d 2a c9 0b 00   ..*. }......*...
0030   0a 61 69 72 47 61 74 65 77 61 79 0c 00 03 41 47   .airGateway...AG
0040   57 0d 00 0c 52 69 64 67 65 43 6f 74 74 61 67 65   W...RidgeCottage
0050   0e 00 01 03 03 00 25 41 69 72 47 57 2e 61 72 39   ......%AirGW.ar9
0060   33 33 78 2e 76 31 2e 31 2e 36 2e 32 38 30 36 32   33x.v1.1.6.28062
0070   2e 31 35 30 37 33 31 2e 31 35 31 30 10 00 02 e4   .150731.1510....
0080   c2                                                .
```

### Hikvision - SADP UDP port 37020
References:<br>
[https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Hikvision.cs](https://github.com/julienblitte/UniversalScanner/blob/master/UniversalScanner/Hikvision.cs)
```
echo -n '<?xml version="1.0" encoding="utf-8"?><Probe><Uuid>{0}</Uuid><Types>inquiry</Types></Probe>' | netcat -u 10.0.0.1 37020
```
```
0000   3c 3f 78 6d 6c 20 76 65 72 73 69 6f 6e 3d 22 31   <?xml version="1
0010   2e 30 22 20 65 6e 63 6f 64 69 6e 67 3d 22 55 54   .0" encoding="UT
0020   46 2d 38 22 3f 3e 0d 0a 3c 50 72 6f 62 65 4d 61   F-8"?>..<ProbeMa
0030   74 63 68 3e 3c 55 75 69 64 3e XX XX XX XX XX XX   tch><Uuid>XXXXXX
0040   XX XX 2d XX XX XX XX 2d XX XX XX XX 2d XX XX XX   XX-XXXX-XXXX-XXX
0050   XX 2d XX XX XX XX XX XX XX XX XX XX XX XX 3c 2f   X-XXXXXXXXXXXX</
0060   55 75 69 64 3e 0d 0a 3c 54 79 70 65 73 3e 69 6e   Uuid>..<Types>in
0070   71 75 69 72 79 3c 2f 54 79 70 65 73 3e 0d 0a 3c   quiry</Types>..<
0080   44 65 76 69 63 65 54 79 70 65 3e 31 33 39 37 38   DeviceType>13978
0090   33 3c 2f 44 65 76 69 63 65 54 79 70 65 3e 0d 0a   3</DeviceType>..
00a0   3c 44 65 76 69 63 65 44 65 73 63 72 69 70 74 69   <DeviceDescripti
00b0   6f 6e 3e 44 53 2d 32 43 44 32 30 32 32 57 44 2d   on>DS-2CD2022WD-
00c0   49 3c 2f 44 65 76 69 63 65 44 65 73 63 72 69 70   I</DeviceDescrip
00d0   74 69 6f 6e 3e 0d 0a 3c 44 65 76 69 63 65 53 4e   tion>..<DeviceSN
00e0   3e XX XX 2d XX XX XX XX XX XX XX XX XX 2d XX XX   >XX-XXXXXXXXX-XX
00f0   XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX XX   XXXXXXXXXXXXXXXX
0100   XX XX XX XX 3c 2f 44 65 76 69 63 65 53 4e 3e 0d   XXXX</DeviceSN>.
0110   0a 3c 43 6f 6d 6d 61 6e 64 50 6f 72 74 3e 38 30   .<CommandPort>80
0120   30 30 3c 2f 43 6f 6d 6d 61 6e 64 50 6f 72 74 3e   00</CommandPort>
0130   0d 0a 3c 48 74 74 70 50 6f 72 74 3e 38 30 3c 2f   ..<HttpPort>80</
0140   48 74 74 70 50 6f 72 74 3e 0d 0a 3c 4d 41 43 3e   HttpPort>..<MAC>
0150   XX XX 2d XX XX 2d XX XX 2d XX XX 2d XX XX 2d XX   XX-XX-XX-XX-XX-X
0160   XX 3c 2f 4d 41 43 3e 0d 0a 3c 49 50 76 34 41 64   X</MAC>..<IPv4Ad
0170   64 72 65 73 73 3e XX XX 2e XX XX 2e XX XX XX 2e   dress>XX.XX.XXX.
0180   XX XX 3c 2f 49 50 76 34 41 64 64 72 65 73 73 3e   XX</IPv4Address>
0190   0d 0a 3c 49 50 76 34 53 75 62 6e 65 74 4d 61 73   ..<IPv4SubnetMas
01a0   6b 3e 32 35 35 2e 32 35 35 2e 32 35 35 2e 30 3c   k>255.255.255.0<
01b0   2f 49 50 76 34 53 75 62 6e 65 74 4d 61 73 6b 3e   /IPv4SubnetMask>
01c0   0d 0a 3c 49 50 76 34 47 61 74 65 77 61 79 3e 31   ..<IPv4Gateway>1
01d0   30 2e 39 39 2e 31 36 35 2e 31 3c 2f 49 50 76 34   0.99.165.1</IPv4
01e0   47 61 74 65 77 61 79 3e 0d 0a 3c 49 50 76 36 41   Gateway>..<IPv6A
01f0   64 64 72 65 73 73 3e 3a 3a 3c 2f 49 50 76 36 41   ddress>::</IPv6A
0200   64 64 72 65 73 73 3e 0d 0a 3c 49 50 76 36 47 61   ddress>..<IPv6Ga
0210   74 65 77 61 79 3e 3a 3a 3c 2f 49 50 76 36 47 61   teway>::</IPv6Ga
0220   74 65 77 61 79 3e 0d 0a 3c 49 50 76 36 4d 61 73   teway>..<IPv6Mas
0230   6b 4c 65 6e 3e 30 3c 2f 49 50 76 36 4d 61 73 6b   kLen>0</IPv6Mask
0240   4c 65 6e 3e 0d 0a 3c 44 48 43 50 3e 66 61 6c 73   Len>..<DHCP>fals
0250   65 3c 2f 44 48 43 50 3e 0d 0a 3c 41 6e 61 6c 6f   e</DHCP>..<Analo
0260   67 43 68 61 6e 6e 65 6c 4e 75 6d 3e 30 3c 2f 41   gChannelNum>0</A
0270   6e 61 6c 6f 67 43 68 61 6e 6e 65 6c 4e 75 6d 3e   nalogChannelNum>
0280   0d 0a 3c 44 69 67 69 74 61 6c 43 68 61 6e 6e 65   ..<DigitalChanne
0290   6c 4e 75 6d 3e 31 3c 2f 44 69 67 69 74 61 6c 43   lNum>1</DigitalC
02a0   68 61 6e 6e 65 6c 4e 75 6d 3e 0d 0a 3c 53 6f 66   hannelNum>..<Sof
02b0   74 77 61 72 65 56 65 72 73 69 6f 6e 3e 56 35 2e   twareVersion>V5.
02c0   33 2e 33 62 75 69 6c 64 20 31 35 30 36 33 30 3c   3.3build 150630<
02d0   2f 53 6f 66 74 77 61 72 65 56 65 72 73 69 6f 6e   /SoftwareVersion
02e0   3e 0d 0a 3c 44 53 50 56 65 72 73 69 6f 6e 3e 56   >..<DSPVersion>V
02f0   37 2e 30 20 62 75 69 6c 64 20 31 35 30 36 30 39   7.0 build 150609
0300   3c 2f 44 53 50 56 65 72 73 69 6f 6e 3e 0d 0a 3c   </DSPVersion>..<
0310   42 6f 6f 74 54 69 6d 65 3e 32 30 32 32 2d 30 39   BootTime>2022-09
0320   2d 31 34 20 31 38 3a 30 34 3a 34 32 3c 2f 42 6f   -14 18:04:42</Bo
0330   6f 74 54 69 6d 65 3e 0d 0a 3c 52 65 73 65 74 41   otTime>..<ResetA
0340   62 69 6c 69 74 79 3e 66 61 6c 73 65 3c 2f 52 65   bility>false</Re
0350   73 65 74 41 62 69 6c 69 74 79 3e 0d 0a 3c 44 69   setAbility>..<Di
0360   73 6b 4e 75 6d 62 65 72 3e 30 3c 2f 44 69 73 6b   skNumber>0</Disk
0370   4e 75 6d 62 65 72 3e 0d 0a 3c 41 63 74 69 76 61   Number>..<Activa
0380   74 65 64 3e 74 72 75 65 3c 2f 41 63 74 69 76 61   ted>true</Activa
0390   74 65 64 3e 0d 0a 3c 50 61 73 73 77 6f 72 64 52   ted>..<PasswordR
03a0   65 73 65 74 41 62 69 6c 69 74 79 3e 74 72 75 65   esetAbility>true
03b0   3c 2f 50 61 73 73 77 6f 72 64 52 65 73 65 74 41   </PasswordResetA
03c0   62 69 6c 69 74 79 3e 0d 0a 3c 2f 50 72 6f 62 65   bility>..</Probe
03d0   4d 61 74 63 68 3e 0d 0a                           Match>..
```

### Devolo - UDP port 19375
References:<br>
[https://github.com/activecm/passer/blob/d59b1824b889a80e38235c17d7eb139cfeb76f36/passer.py#L1479](https://github.com/activecm/passer/blob/d59b1824b889a80e38235c17d7eb139cfeb76f36/passer.py#L1479)
[https://github.com/2Fake/devolo_plc_api/issues/39](https://github.com/2Fake/devolo_plc_api/issues/39)
```
# Censys Search Filter
services.parsed.mdns.names=`_dvl-deviceapi._tcp.local.`
```
second last byte set to 1 for unicast, 2 for broadcast
```
echo -n 'whoisthere\x0010.0.0.1\x00255.255.255.0\x00\x001\x00' | netcat -u 10.0.0.1 19375
```
```
0000   68 65 6c 6c 6f 00 64 4c 41 4e 20 35 35 30 20 57   hello.dLAN 550 W
0010   69 46 69 00 XX XX XX XX XX XX XX XX XX XX XX XX   iFi.XXXXXXXXXXXX
0020   XX XX XX XX 00 31 39 32 2e 31 36 38 2e 30 2e 31   XXXX.192.168.0.1
0030   31 00 32 35 35 2e 32 35 35 2e 32 35 35 2e 30 00   1.255.255.255.0.
0040   3c 3f 78 6d 6c 20 76 65 72 73 69 6f 6e 3d 22 31   <?xml version="1
0050   2e 30 22 3f 3e 3c 73 74 61 74 75 73 3e 3c 64 65   .0"?><status><de
0060   76 69 63 65 2d 74 79 70 65 3e 64 4c 41 4e 20 35   vice-type>dLAN 5
0070   35 30 20 57 69 46 69 3c 2f 64 65 76 69 63 65 2d   50 WiFi</device-
0080   74 79 70 65 3e 3c 68 6f 73 74 6e 61 6d 65 3e 64   type><hostname>d
0090   65 76 6f 6c 6f 2d 31 32 33 3c 2f 68 6f 73 74 6e   evolo-123</hostn
00a0   61 6d 65 3e 3c 6d 74 2d 6e 75 6d 62 65 72 3e 32   ame><mt-number>2
00b0   37 33 33 3c 2f 6d 74 2d 6e 75 6d 62 65 72 3e 3c   733</mt-number><
00c0   73 65 72 69 61 6c 2d 6e 75 6d 62 65 72 3e XX XX   serial-number>XX
00d0   XX XX XX XX XX XX XX XX XX XX XX XX XX XX 3c 2f   XXXXXXXXXXXXXX</
00e0   73 65 72 69 61 6c 2d 6e 75 6d 62 65 72 3e 3c 64   serial-number><d
00f0   65 76 69 63 65 61 70 69 3e 3c 66 65 61 74 75 72   eviceapi><featur
0100   65 73 3e 69 6e 74 6d 74 67 2c 6c 65 64 2c 6e 6f   es>intmtg,led,no
0110   74 63 68 2c 72 65 73 65 74 2c 72 65 73 74 61 72   tch,reset,restar
0120   74 2c 73 75 70 70 6f 72 74 2c 75 70 64 61 74 65   t,support,update
0130   2c 77 69 66 69 31 3c 2f 66 65 61 74 75 72 65 73   ,wifi1</features
0140   3e 3c 6d 69 6e 6f 72 56 65 72 73 69 6f 6e 3e 32   ><minorVersion>2
0150   3c 2f 6d 69 6e 6f 72 56 65 72 73 69 6f 6e 3e 3c   </minorVersion><
0160   70 61 74 68 3e XX XX XX XX XX XX XX XX XX XX XX   path>XXXXXXXXXXX
0170   XX XX XX XX XX 2f 64 65 76 69 63 65 61 70 69 3c   XXXXX/deviceapi<
0180   2f 70 61 74 68 3e 3c 70 6f 72 74 3e 31 34 37 39   /path><port>1479
0190   31 3c 2f 70 6f 72 74 3e 3c 76 65 72 73 69 6f 6e   1</port><version
01a0   3e 76 30 3c 2f 76 65 72 73 69 6f 6e 3e 3c 2f 64   >v0</version></d
01b0   65 76 69 63 65 61 70 69 3e 3c 66 69 72 6d 77 61   eviceapi><firmwa
01c0   72 65 3e 3c 64 61 74 65 3e 32 30 32 33 2d 30 39   re><date>2023-09
01d0   2d 30 36 3c 2f 64 61 74 65 3e 3c 76 65 72 73 69   -06</date><versi
01e0   6f 6e 3e 36 2e 30 2e 31 3c 2f 76 65 72 73 69 6f   on>6.0.1</versio
01f0   6e 3e 3c 2f 66 69 72 6d 77 61 72 65 3e 3c 70 6c   n></firmware><pl
0200   63 6e 65 74 61 70 69 3e 3c 70 61 74 68 3e XX XX   cnetapi><path>XX
0210   XX XX XX XX XX XX XX XX XX XX XX XX XX XX 2f 70   XXXXXXXXXXXXXX/p
0220   6c 63 6e 65 74 61 70 69 3c 2f 70 61 74 68 3e 3c   lcnetapi</path><
0230   70 6f 72 74 3e 31 34 37 39 31 3c 2f 70 6f 72 74   port>14791</port
0240   3e 3c 76 65 72 73 69 6f 6e 3e 76 30 3c 2f 76 65   ><version>v0</ve
0250   72 73 69 6f 6e 3e 3c 2f 70 6c 63 6e 65 74 61 70   rsion></plcnetap
0260   69 3e 3c 70 6f 77 65 72 6c 69 6e 65 3e 3c 6d 61   i><powerline><ma
0270   63 2d 61 64 64 72 65 73 73 3e 42 38 3a 42 45 3a   c-address>B8:BE:
0280   46 34 3a XX XX 3a XX XX 3a XX XX 3c 2f 6d 61 63   F4:XX:XX:XX</mac
0290   2d 61 64 64 72 65 73 73 3e 3c 74 65 63 68 6e 6f   -address><techno
02a0   6c 6f 67 79 3e 68 70 61 76 3c 2f 74 65 63 68 6e   logy>hpav</techn
02b0   6f 6c 6f 67 79 3e 3c 2f 70 6f 77 65 72 6c 69 6e   ology></powerlin
02c0   65 3e 3c 2f 73 74 61 74 75 73 3e 00 00            e></status>..
```