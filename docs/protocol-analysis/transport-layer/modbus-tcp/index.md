---
title: Schneider Electric UMAS
parent: Transport Layer
nav_order: 3
---

# Schneider Electric UMAS
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Structure

<table>
    <tbody>
        <tr>
            <th>Modbus/TCP</th>
            <th colspan=5>UMAS</th>
        </tr>
        <tr>
            <th>Modbus Header</th>
            <th>Func Code (\x5A)</th>
            <th>Session Key</th>
            <th>UMAS Func</th>
            <th>Data</th>
        </tr>
        <tr>
            <th></th>
            <th>1 Byte</th>
            <th>1 Byte</th>
            <th>1 Byte</th>
            <th>1 Byte</th>
        </tr>
    </tbody>
</table>

## UMAS Function Code

request information about a device

| Code | Function | Description |
|:-----|:---------|:------------|
| 0x02 | pu_GetPlcInfo | requests information about the device |
| 0x04 | pu_GetPlcStatus | queries the PLC status |
| 0x06 | pu_GetMemoryCardInfo | requests information about the device’s SD card |

## Reference
[modbus-umas-schneider.lua](https://github.com/biero-el-corridor/Wireshark-UMAS-Modicon-M340-protocol/blob/main/modbus-umas-schneider.lua) \
[modicon-info.nse](https://github.com/digitalbond/Redpoint/blob/master/modicon-info.nse) \
[Kaspersky ICS-Cert- The secrets of Schneider Electric’s UMAS protocol](https://ics-cert.kaspersky.com/publications/reports/2022/09/29/the-secrets-of-schneider-electrics-umas-protocol/#umas-protocol)