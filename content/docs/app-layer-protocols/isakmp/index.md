---
title: ISAKMP
description: ISAKMP
permalink: /docs/app-layer-protocols/isakmp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-23
updateTime: 2026-09-23
tags: [Markdown, Writing]
---

#### Overview
**ISAKMP** (Internet Security Association and Key Management Protocol), defined in **RFC 2408**, is a framework for establishing, negotiating, modifying, and deleting Security Associations (SAs) and cryptographic keying material, most commonly as the base protocol underlying **IKE** (Internet Key Exchange) for IPsec. It runs over **UDP**, on the IANA-assigned port **500**; when NAT is detected between peers, NAT-Traversal (NAT-T) switches the exchange to UDP port **4500**, encapsulating the IKE/IPsec traffic to survive NAT rewriting. ISAKMP is peer-to-peer (either side can initiate) and defines its own message/payload framework independent of the specific key-exchange algorithm in use.

Every ISAKMP message opens with a fixed 28-byte header carrying a pair of 8-byte **Initiator/Responder Cookies** (an anti-clogging/session identifier), a **Next Payload** chain type, protocol **version**, **Exchange Type**, and **Flags** — none of it encrypted at this layer, since ISAKMP negotiates the security association before any payload encryption applies. The most identification-relevant payload is the **Vendor ID** (payload type 13): implementations advertise an MD5 (or similar) hash of a vendor-specific string, often with extra bytes appended encoding the exact product, version, or OS build, making it a direct and widely-used fingerprint for VPN gateway/OS identification (e.g. differentiating Windows releases, Check Point versions, or Cisco/Fortinet/SonicWall/NetScreen implementations) from a single cleartext payload.

#### ISAKMP Header Format
<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse;">
  <colgroup>
    <col style="width:6%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
  </colgroup>
  <tbody>
    <!-- Ruler -->
    <tr>
      <td style="border:1px solid #333; padding:2px 4px; font-size:0.7em; opacity:0.7; line-height:1.2;">Bit&rarr;<br>Byte&darr;</td>
      <td colspan="32" style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>0</span><span>7</span><span>15</span><span>23</span><span>31</span></div>
      </td>
    </tr>
    <!-- Offset 0-7: Initiator Cookie (merged, 8 bytes) -->
    <tr>
      <td rowspan="2" style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">0</td>
      <td rowspan="2" colspan="32" style="border:1px solid #333; padding:6px;"><i>Initiator Cookie<br><span style="font-size:0.8em; opacity:0.7;">(8 bytes)</span></i></td>
    </tr>
    <tr></tr>
    <!-- Offset 8-15: Responder Cookie (merged, 8 bytes) -->
    <tr>
      <td rowspan="2" style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">8</td>
      <td rowspan="2" colspan="32" style="border:1px solid #333; padding:6px;"><i>Responder Cookie<br><span style="font-size:0.8em; opacity:0.7;">(8 bytes)</span></i></td>
    </tr>
    <tr></tr>
    <!-- Offset 16: Next Payload | MjVer | MnVer | Exchange Type | Flags -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">16</td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>Next Payload<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>MjVer<br><span style="font-size:0.8em; opacity:0.7;">(4 bits)</span></i></td>
      <td colspan="4" style="border:1px solid #333; padding:6px;"><i>MnVer<br><span style="font-size:0.8em; opacity:0.7;">(4 bits)</span></i></td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>Exchange Type<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>Flags<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
    </tr>
    <!-- Offset 20: Message ID -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">20</td>
      <td colspan="32" style="border:1px solid #333; padding:6px;"><i>Message ID<br><span style="font-size:0.8em; opacity:0.7;">(4 bytes)</span></i></td>
    </tr>
    <!-- Offset 24: Length -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">24</td>
      <td colspan="32" style="border:1px solid #333; padding:6px;"><i>Length<br><span style="font-size:0.8em; opacity:0.7;">(4 bytes)</span></i></td>
    </tr>
  </tbody>
</table>

<div style="display:flex; gap:16px; align-items:flex-start; flex-wrap:wrap;">

<table style="display:table; flex:2 1 420px; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:30%"><col style="width:20%"><col style="width:30%"><col style="width:20%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Next Payload Type</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">Value</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Next Payload Type</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">None</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">0</td>
      <td style="border:1px solid #333; padding:8px 12px;">Hash</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">8</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Security Association</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">1</td>
      <td style="border:1px solid #333; padding:8px 12px;">Signature</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">9</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Proposal</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">2</td>
      <td style="border:1px solid #333; padding:8px 12px;">Nonce</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">10</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Transform</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">3</td>
      <td style="border:1px solid #333; padding:8px 12px;">Notification</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">11</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Key Exchange</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">4</td>
      <td style="border:1px solid #333; padding:8px 12px;">Delete</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">12</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Identification</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">5</td>
      <td style="border:1px solid #333; padding:8px 12px;">Vendor ID</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">13</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Certificate</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">6</td>
      <td style="border:1px solid #333; padding:8px 12px;">Reserved</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">14-127</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">Certificate Request</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">7</td>
      <td style="border:1px solid #333; padding:8px 12px;">Private Use</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">128-255</td>
    </tr>
  </tbody>
</table>

<table style="display:table; flex:1 1 260px; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:65%"><col style="width:35%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Exchange Type</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="border:1px solid #333; padding:8px 12px;">None</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">0</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">Base</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">1</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">Identity Protection</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">2</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">Authentication Only</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">3</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">Aggressive</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">4</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">Informational</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">5</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">ISAKMP Future Use</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">6-31</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">DOI Specific Use</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">32-239</td></tr>
    <tr><td style="border:1px solid #333; padding:8px 12px;">Private Use</td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">240-255</td></tr>
  </tbody>
</table>

</div>

<!-- | Next Payload Type   | Value | Next Payload Type   | Value  |
|----------------------|-------|----------------------|--------|
| None                  | 0     | Hash                 | 8      |
| Security Association  | 1     | Signature            | 9      |
| Proposal               | 2     | Nonce                | 10     |
| Transform              | 3     | Notification         | 11     |
| Key Exchange           | 4     | Delete               | 12     |
| Identification         | 5     | Vendor ID            | 13     |
| Certificate            | 6     | Reserved             | 14-127 |
| Certificate Request    | 7     | Private Use          | 128-255|

| Exchange Type          | Value  |
|--------------------------|--------|
| None                     | 0      |
| Base                     | 1      |
| Identity Protection      | 2      |
| Authentication Only      | 3      |
| Aggressive               | 4      |
| Informational            | 5      |
| ISAKMP Future Use        | 6-31   |
| DOI Specific Use         | 32-239 |
| Private Use              | 240-255| -->

### Identification Payload
<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse;">
  <colgroup>
    <col style="width:6%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
  </colgroup>
  <tbody>
    <!-- Ruler -->
    <tr>
      <td style="border:1px solid #333; padding:2px 4px; font-size:0.7em; opacity:0.7; line-height:1.2;">Bit&rarr;<br>Byte&darr;</td>
      <td colspan="32" style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>0</span><span>7</span><span>15</span><span>23</span><span>31</span></div>
      </td>
    </tr>
    <!-- Offset 0: Next Payload | RESERVED | Payload Length -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">0</td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>Next Payload<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>RESERVED<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
      <td colspan="16" style="border:1px solid #333; padding:6px;"><i>Payload Length<br><span style="font-size:0.8em; opacity:0.7;">(2 bytes)</span></i></td>
    </tr>
    <!-- Offset 4: ID Type | DOI Specific ID Data -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">4</td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>ID Type<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
      <td colspan="24" style="border:1px solid #333; padding:6px;"><i>DOI Specific ID Data<br><span style="font-size:0.8em; opacity:0.7;">(3 bytes)</span></i></td>
    </tr>
    <!-- Offset 8: Identification Data (variable) -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">8</td>
      <td colspan="32" style="border:1px solid #333; padding:6px;"><i>Identification Data<br><span style="font-size:0.8em; opacity:0.7;">(variable length)</span></i></td>
    </tr>
  </tbody>
</table>

| ID Type              | Value | Description |
|------------------------|-------|-------------|
| RESERVED                | 0     | |
| ID_IPV4_ADDR             | 1     | single four (4) octet IPv4 address |
| ID_FQDN                  | 2     | fully-qualified domain name string, example: "foo.bar.com" |
| ID_USER_FQDN             | 3     | fully-qualified username string, example: "piper@foo.bar.com" |
| ID_IPV4_ADDR_SUBNET      | 4     | range of IPv4 addresses, two four (4) octet values |
| ID_IPV6_ADDR             | 5     | single sixteen (16) octet IPv6 address |
| ID_IPV6_ADDR_SUBNET      | 6     | range of IPv6 addresses, two sixteen (16) octet values |
| ID_IPV4_ADDR_RANGE       | 7     | range of IPv4 addresses, two four (4) octet values |
| ID_IPV6_ADDR_RANGE       | 8     | range of IPv6 addresses, two sixteen (16) octet values |
| ID_DER_ASN1_DN           | 9     | binary DER encoding of an ASN.1 X.500 Distinguished Name |
| ID_DER_ASN1_GN           | 10    | binary DER encoding of an ASN.1 X.500 GeneralName |
| ID_KEY_ID                | 11    | opaque byte stream which may be used to pass vendor-specific information necessary to identify which pre-shared key should be used to authenticate Aggressive mode negotiations |

### Vendor ID Payload
<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse;">
  <colgroup>
    <col style="width:6%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
    <col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%"><col style="width:2.9375%">
  </colgroup>
  <tbody>
    <!-- Ruler -->
    <tr>
      <td style="border:1px solid #333; padding:2px 4px; font-size:0.7em; opacity:0.7; line-height:1.2;">Bit&rarr;<br>Byte&darr;</td>
      <td colspan="32" style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>0</span><span>7</span><span>15</span><span>23</span><span>31</span></div>
      </td>
    </tr>
    <!-- Offset 0: Next Payload | RESERVED | Payload Length -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">0</td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>Next Payload<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
      <td colspan="8" style="border:1px solid #333; padding:6px;"><i>RESERVED<br><span style="font-size:0.8em; opacity:0.7;">(1 byte)</span></i></td>
      <td colspan="16" style="border:1px solid #333; padding:6px;"><i>Payload Length<br><span style="font-size:0.8em; opacity:0.7;">(2 bytes)</span></i></td>
    </tr>
    <!-- Offset 4: Vendor ID (VID), variable -->
    <tr>
      <td style="border:1px solid #333; padding:6px; font-size:0.85em; opacity:0.7;">4</td>
      <td colspan="32" style="border:1px solid #333; padding:6px;"><i>Vendor ID (VID)<br><span style="font-size:0.8em; opacity:0.7;">(variable length)</span></i></td>
    </tr>
  </tbody>
</table>

Vendor ID is a hash of a vendor-specific string, sometimes with vendor/product/version bytes appended.

### nmap Script
```
┌──(root㉿kali)-[/home/kali]
└─# nmap -sU -p 500 --script ike-version 10.0.0.1
Starting Nmap 7.92 ( https://nmap.org ) at 2025-07-23 13:46 EDT
Nmap scan report for 10.0.0.1
Host is up (0.25s latency).

PORT    STATE SERVICE
500/udp open  isakmp
| ike-version: 
|   vendor_id: Microsoft Windows 2000
|   attributes: 
|     MS NT5 ISAKMPOAKLEY
|     IKE FRAGMENTATION
|_    draft-ietf-ipsec-nat-t-ike-02\n
Service Info: OS: Windows 2000; CPE: cpe:/o:microsoft:windows:2000, cpe:/o:microsoft:windows
```

### Known Vendor ID

#### Windows
The Microsoft implementation Vendor ID is constructed by appending a 4-byte version number (network byte order) to the 16-byte MD5 hash of the string `"MS NT5 ISAKMPOAKLEY"`. The 4-byte suffix denotes the Windows release. ([reference](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ikee/74df968a-7125-431d-9c98-4ea929e548dc))

| Input String          | md5 |
|------------------------|-----|
| MS NT5 ISAKMPOAKLEY    | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61` |

| Windows Release          | md5 + version suffix (hex)                                             | base64 |
|----------------------------|---------------------------------------------------------------------|--------|
| Windows 2000                | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 02`        | `HitRaQWZHH18lvy/tYfkYQAAAAI=` |
| Windows XP                  | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 03`        | `HitRaQWZHH18lvy/tYfkYQAAAAM=` |
| Windows 2003 Server          | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 04`        | `HitRaQWZHH18lvy/tYfkYQAAAAQ=` |
| Windows Vista                | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 05`        | `HitRaQWZHH18lvy/tYfkYQAAAAU=` |
| Windows Server 2008          | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 06`        | `HitRaQWZHH18lvy/tYfkYQAAAAY=` |
| Windows 7                    | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 07`        | `HitRaQWZHH18lvy/tYfkYQAAAAc=` |
| Windows Server 2008 R2        | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 08`        | `HitRaQWZHH18lvy/tYfkYQAAAAg=` |
| Windows 8 and later           | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 09`        | `HitRaQWZHH18lvy/tYfkYQAAAAk=` |
| Windows 2012 and later        | `1E 2B 51 69 05 99 1C 7D 7C 96 FC BF B5 87 E4 61 00 00 00 09`        | `HitRaQWZHH18lvy/tYfkYQAAAAk=` |

```
# Wireshark Tree view
Payload: Vendor ID (13) : MS NT5 ISAKMPOAKLEY
    Next payload: Vendor ID (13)
    Reserved: 00
    Payload length: 24
    Vendor ID: 1e2b516905991c7d7c96fcbfb587e46100000002
    Vendor ID: MS NT5 ISAKMPOAKLEY
    MS NT5 ISAKMPOAKLEY: Windows 2000 (2)

0000   0d 00 00 18 1e 2b 51 69 05 99 1c 7d 7c 96 fc bf
0010   b5 87 e4 61 00 00 00 02
```

#### Check Point Firewall
The Check Point Vendor ID is 40 bytes long. The first 20 bytes are constant across implementations; the second 20 bytes (bytes 21-40) encode the product, version, timestamp, and feature flags as five 4-byte big-endian integers. ([reference](https://www.royhills.co.uk/wiki/index.php/Check_Point_Firewall-1#Vendor_IDs))

| Byte Position | Example Data | Meaning |
|-----------------|-----------------|-----------|
| 1-20 | `F4 ED 19 E0 C1 14 EB 51 6F AA AC 0E E3 7D AF 28 07 B4 38 1F` | Check Point Vendor ID |
| 21-24 | `00 00 00 01` | Product (1=Firewall, 2=Client) |
| 25-28 | `00 00 13 8A` | Encoded Version |
| 29-32 | `00 00 00 00` | Timestamp |
| 33-36 | `00 00 00 00` | Reserved |
| 37-40 | `18 80 00 00` | Features |

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:16%"><col style="width:14%"><col style="width:20%">
    <col style="width:16%"><col style="width:14%"><col style="width:20%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Encoded Version</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Timestamp</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Version</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Encoded Version</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Timestamp</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Version</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>00 02</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">4.1</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 8B</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">NG FP3</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>00 03</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">4.1 SP1</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 8C</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">NG AI R54</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>0F A2</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">4.1 SP2 to SP6</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 8D</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">NG AI R55</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 88</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">NG</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 8E</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">NG AI R56</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 89</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">NG FP1</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 8D</code></td><td style="border:1px solid #333; padding:8px 12px;">non-zero</td><td style="border:1px solid #333; padding:8px 12px;">NGX R60</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>13 8A</code></td><td style="border:1px solid #333; padding:8px 12px;">zero</td><td style="border:1px solid #333; padding:8px 12px;">NG FP2</td>
      <td style="border:1px solid #333; padding:8px 12px;"></td><td style="border:1px solid #333; padding:8px 12px;"></td><td style="border:1px solid #333; padding:8px 12px;"></td>
    </tr>
  </tbody>
</table>

```
# Wireshark Tree view
Payload: Vendor ID (13) : CryptoPro/GOST 0.1 / Check Point R65
    Next payload: NONE / No Next Payload (0)
    Reserved: 00
    Payload length: 44
    Vendor ID: f4ed19e0c114eb516faaac0ee37daf2807b4381f000000010000138d68826f6a0000000018280000
    Vendor ID: CryptoPro/GOST 0.1 / Check Point R65
    Checkpoint Product: Firewall-1 (1)
    Checkpoint Version: NG with Application Intelligence R55 (5005)
    Checkpoint Timestamp: 1753378666
    Checkpoint Reserved: 0x00000000
    Checkpoint Features: 0x18280000

0000   00 00 00 2c f4 ed 19 e0 c1 14 eb 51 6f aa ac 0e   ...,.......Qo...
0010   e3 7d af 28 07 b4 38 1f 00 00 00 01 00 00 13 8d   .}.(..8.........
0020   68 82 6f 6a 00 00 00 00 18 28 00 00               h.oj.....(..
```

#### Other Known Vendor IDs
Vendor ID hashes for common VPN/firewall implementations, useful for device/implementation fingerprinting. Where the source string is known, the hash is `md5(<string>)`.

| Implementation | Vendor ID (hex) | Base64 | Derivation |
|-----------------|--------------------|----------|--------------|
| Cisco Dead Peer Detection | `AF CA D7 13 68 A1 F1 C9 6B 86 96 FC 77 57 01 00` | `r8rXE2ih8clrhpb8d1cBAA==` | `md5("CISCO-DEAD-PEER-DETECTION")` |
| Cisco Unity | `12 F5 F2 8C 45 71 68 A9 70 2D 9F E2 74 CC 01 00` | `EvXyjEVxaKlwLZ/idMwBAA==` | `md5("CISCO-UNITY")` |
| Cisco Unity (short form) | `12 F5 F2 8C 45 71 68 A9 70 2D 9F E2 74 CC` | — | — |
| Cisco Concentrator | `1F 07 F7 0E AA 65 14 D3 B0 FA 96 54 2A 50 01 00` | — | — |
| Netgear | `DB FB 81 EB 57 60 B0 78 85 62 06 7D A1 02 D7 55` | `2/uB61dgsHiFYgZ9oQLXVQ==` | `md5("NETGEAR")` |
| SonicWall (type 6) | `5B 36 2B C8 20 F6 00 06` | `WzYryCD2AAY=` | `md5("")` |
| SonicWall (type 7) | `5B 36 2B C8 20 F6 00 07` | `WzYryCD2AAc=` | `md5("")` |
| SonicWall (type 8) | `5B 36 2B C8 20 F6 00 08` | `WzYryCD2AAg=` | `md5("")` |
| SonicWall (type b) | `DA 8E 93 78 80 01 00 00` | `2o6TeIABAAA=` | `md5("")` |
| SonicWall (type c) | `5B 36 2B C8 20 F7 00 01` | `WzYryCD3AAE=` | `md4("")` |
| ZyXEL | `62 50 27 74 9D 5A B9 7F 56 16 C1 60 27 65 CF 48 0A 3B 7D 0B` | `YlAndJ1auX9WFsFgJ2XPSAo7fQs=` | — |
| ZyXEL ZyWALL USG 100 | `F7 58 F2 26 68 75 0F 03 B0 8D F6 EB E1 D0` | `91jyJmh1DwOwjfbr4dA=` | — |
| NetScreenOS | `16 6F 93 2D 55 EB 64 D8 E4 DF 4F D3 7E 23 13 F0 D0 FD 84 51 00 00 00 00 00 00 00 00` | `Fm+TLVXrZNjk30/TfiMT8ND9hFEAAAAAAAAAAA==` | — |
| NetScreenOS (variant) | `4A 43 40 B5 43 E0 2B 84 C8 8A 8B 96 A8 AF 9E BE 77 D9 AC CC 00 00 00 0B 00 00 05 00` | `SkNAtUPgK4TIiouWqK+evnfZrMwAAAALAAAFAA=` | — |
| Fortinet FortiGate | `82 99 03 17 57 A3 60 82 C6 A6 21 DE 00 05 04 28` | `gpkDF1ejYILGpiHeAAUEKA==` | `md5("FORTIGATE")` |
| Fortinet FortiGate (variant) | `1D 6E 17 8F 6C 2C 0B E2 84 98 54 65 45 0F E9 D4` | `HW4Xj2wsC+KEmFRlRQ/p1A==` | — |
| Check Point | `F4 ED 19 E0 C1 14 EB 51 6F AA AC 0E E3 7D AF 28 07 B4 38 1F` | `9O0Z4MEU61FvqqwO432vKAe0OB8=` | — |

### Reference
[Wireshark ISAKMP Dissector Github](https://github.com/wireshark/wireshark/blob/master/epan/dissectors/packet-isakmp.c)<br>
[RFC2408 - 3.1 ISAKMP Header Format](https://www.ietf.org/rfc/rfc2408.txt)<br>
[RFC2407 - 4.6.2 Identification Payload Content](https://datatracker.ietf.org/doc/html/rfc2407#section-4.6.2)<br>
[RFC2407 - 4.6.2.1 Identification Type Values](https://datatracker.ietf.org/doc/html/rfc2407#section-4.6.2.1)<br>
[RFC2408 - 3.16 Vendor ID Payload](https://datatracker.ietf.org/doc/html/rfc2408#section-3.16)<br>
[MS-IKEE: Vendor ID Payload Data](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-ikee/74df968a-7125-431d-9c98-4ea929e548dc)<br>
[Check Point Firewall-1 Vendor IDs](https://www.royhills.co.uk/wiki/index.php/Check_Point_Firewall-1#Vendor_IDs)<br>
[ike-scan Vendor ID list](https://github.com/royhills/ike-scan/blob/master/ike-vendor-ids)<br>
