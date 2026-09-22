---
title: ASTERIX
description: ASTERIX
permalink: /docs/app-layer-protocols/asterix/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-08-05
updateTime: 2026-08-05
tags: [Markdown, Writing]
---

### Overview

ASTERIX (All Purpose Structured EUROCONTROL Surveillance Information EXchange) is a standardized data format developed by EUROCONTROL for exchanging surveillance and related information between air traffic management systems. It operates primarily over network protocols such as UDP and TCP, with UDP commonly used for real-time surveillance data. ASTERIX defines multiple standardized categories (CAT), such as CAT001, CAT002, CAT021, and CAT048, covering different types of surveillance and aeronautical information. It enables interoperability between radar, ADS-B, multilateration, and other surveillance systems without relying on proprietary data formats.

Port 8600 is registered with IANA for ASTERIX, although the ASTERIX specification does not mandate a specific UDP port. ASTERIX data is commonly transported over UDP, including local multicast. The specific multicast address and UDP port remain implementation-dependent.

### Protocol Strucutre / Field Type

```text title="ASTERIX tree structure"
ASTERIX DATA BLOCK
├── CAT        (1 octet)
├── LEN        (2 octets)
└── DATA RECORD(1) ... DATA RECORD(k)
        └── DATA RECORD
            ├── FSPEC              ← the bitfield table
            ├── DATA FIELD(1)
            ├── ...
            └── DATA FIELD(k)
```

#### General Structure

<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:8%"><col style="width:14%"><col style="width:28%"><col style="width:50%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:2px 8px;">0</td>
      <td style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>1</span><span>2</span></div>
      </td>
      <td style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>3</span><span>f</span></div>
      </td>
      <td style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>f+1</span><span>N</span></div>
      </td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px;"><i>CAT</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>LEN</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FSPEC(1) ... FSPEC(m)</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>DATA FIELD(1) ... DATA FIELD(k)</i></td>
    </tr>
  </tbody>
</table>

#### FSPEC

<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse;">
  <colgroup>
    <col style="width:12%"><col style="width:11%"><col style="width:11%"><col style="width:11%"><col style="width:11%"><col style="width:11%"><col style="width:11%"><col style="width:11%"><col style="width:11%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:2px 8px;"></td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 8</td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 7</td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 6</td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 5</td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 4</td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 3</td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 2</td>
      <td style="border:1px solid #333; padding:2px 8px;">Bit 1</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px;">Byte 1</td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 1</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 2</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 3</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 4</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 5</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 6</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 7</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FX</i></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px;">Byte 2</td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 8</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 9</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 10</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 11</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 12</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 13</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 14</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FX</i></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px;">Byte 3</td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 15</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 16</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 17</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 18</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 19</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 20</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FRN 21</i></td>
      <td style="border:1px solid #333; padding:6px;"><i>FX</i></td>
    </tr>
  </tbody>
</table>

FSPEC is a bitmap at the start of each Data Record where every bit (FRN 1, FRN 2, ...) flags whether a specific Data Field is present — 1 means read it, 0 means skip it, and each FRN number maps to a specific item defined by that record's ASTERIX Category (e.g. FRN 1 = I021/010 for Category 021). The last bit in each FSPEC byte is FX: 1 means another FSPEC byte follows, 0 means FSPEC ends there and the actual Data Fields begin, in the order their FRN bits were set.

### Item Type
Item Type identifies the specific type of information contained within a Data Field, such as aircraft identification, position, altitude, or other surveillance data. Each item type defines how its corresponding data is structured and interpreted. Below is an example for CAT002 Item Type [Category 002 Specification](https://www.eurocontrol.int/sites/default/files/2024-03/cat002-asterix-monoradar-service-messages-part2b-042021-1-2.pdf)

CAT002 Item type

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:20%"><col style="width:45%"><col style="width:35%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Data Item Ref. No.</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">System Units</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/000</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Message Type</td>
      <td style="border:1px solid #333; padding:8px 12px;">N.A.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/010</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Data Source Identifier</td>
      <td style="border:1px solid #333; padding:8px 12px;">N.A.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/020</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Sector Number</td>
      <td style="border:1px solid #333; padding:8px 12px;">360°/(2<sup>8</sup>)</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/030</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Time of Day</td>
      <td style="border:1px solid #333; padding:8px 12px;">1/128 s</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/041</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Antenna Rotation Period</td>
      <td style="border:1px solid #333; padding:8px 12px;">1/128 s</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/050</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Station Configuration Status</td>
      <td style="border:1px solid #333; padding:8px 12px;">N.A.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/060</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Station Processing Mode</td>
      <td style="border:1px solid #333; padding:8px 12px;">N.A.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/070</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Plot Count Values</td>
      <td style="border:1px solid #333; padding:8px 12px;">N.A.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/080</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Warning/Error Conditions</td>
      <td style="border:1px solid #333; padding:8px 12px;">N.A.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/090</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Collimation Error</td>
      <td style="border:1px solid #333; padding:8px 12px;">Range: 1/128 NM<br>Azimuth: 360°/(2<sup>16</sup>)</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>I002/100</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Dynamic Window - Type 1</td>
      <td style="border:1px solid #333; padding:8px 12px;">RHO: 1/128 NM<br>THETA: 360°/(2<sup>16</sup>)</td>
    </tr>
  </tbody>
</table>

### Multicast Address Scope

IANA reserves two IPv4 multicast ranges relevant here: 224.0.0.0/24, the Local Network Control Block, for local network control traffic that generally stays within the local subnet, and 239.0.0.0/8, the Administratively Scoped range, for multicast traffic confined to private or local networks by the administrator ([IANA multicast address registry](https://www.iana.org/assignments/multicast-addresses)).

### Example Hexdump
```
ASTERIX packet, Category 034
    Category: 34
    Length: 16
    Asterix message, #01, length: 13
        FSPEC
        010, Data Source Identifier
        000, Message Type
        030, Time of Day
        020, Sector Number
        050, System Configuration and Status

0000   22 00 10 f4 93 19 02 37 8d 57 20 94 00 20 20 00   "......7.W ..  .
```

# Reference 
[ASTERIX Wireshark Dissector Github](https://gitlab.com/wireshark/wireshark/-/blob/master/epan/dissectors/packet-asterix.c)<br>
[EUROCONTROL Specification for Surveillance Data Exchange Part I](https://www.eurocontrol.int/publication/eurocontrol-specification-surveillance-data-exchange-part-i)<br>