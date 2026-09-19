---
title: GVCP
description: GVCP (GigE Vision Control Protocol)
permalink: /docs/app-layer-protocols/gvcp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-19
updateTime: 2026-09-19
tags: [Markdown, Writing]
---

## DISCOVERY_CMD

<table style="width:100%; text-align:center; table-layout:fixed; border-collapse:collapse;">
  <colgroup>
    <col style="width:25%"><col style="width:25%"><col style="width:25%"><col style="width:25%">
  </colgroup>
  <tbody>
    <tr>
      <td>0x42<br><sub>8 bits</sub></td>
      <td>flag<br><sub>8 bits</sub></td>
      <td colspan="2">command<br><sub>16 bits</sub></td>
    </tr>
    <tr>
      <td colspan="2">length<br><sub>16 bits</sub></td>
      <td colspan="2">req_id<br><sub>16 bits</sub></td>
    </tr>
  </tbody>
</table>