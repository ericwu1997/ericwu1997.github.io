---
title: AMQP
description: AMQP
permalink: /docs/app-layer-protocols/amqp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-22
updateTime: 2026-09-22
tags: [Markdown, Writing]
---

## Overview
**AMQP** (Advanced Message Queuing Protocol) is an open, binary wire-level messaging protocol, originally developed at JPMorgan Chase and later standardized by OASIS and ISO/IEC. It runs over **TCP**, on IANA-assigned port **5672** for cleartext traffic and **5671** for TLS-secured **AMQPS**, with SASL negotiation on 5672 also able to upgrade a connection to TLS in place. AMQP is broker-centric messaging middleware: producers publish messages to a broker (RabbitMQ, ActiveMQ, Azure Service Bus, etc.) that routes them via exchanges and queues (0-9-1) or link/node addressing (1.0) to consumers, making it common in enterprise messaging, IoT telemetry, and financial transaction systems.

Two incompatible wire formats circulate under the same protocol name and are readily distinguished on the wire: both open a connection with the fixed 8-byte ASCII preamble **`AMQP`** followed by a protocol-ID byte and three version bytes — `41 4D 51 50 00 00 09 01` for **AMQP 0-9-1** (the format used by RabbitMQ) versus `41 4D 51 50 00 01 00 00` for **AMQP 1.0** (the OASIS/ISO standard) — giving a reliable version fingerprint independent of payload. Traffic is cleartext by default unless the AMQPS/TLS variant or a SASL security layer is negotiated, and frames carry broker-, exchange-, and queue-name strings in plaintext that can further identify the messaging backend in use.

### General Frame Format
<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:6%"><col style="width:12%"><col style="width:14%"><col style="width:58%"><col style="width:10%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:2px 8px;">0</td>
      <td style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>1</span><span>2</span></div>
      </td>
      <td style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>3</span><span>6</span></div>
      </td>
      <td style="border:1px solid #333; padding:2px 8px;">
        <div style="display:flex; justify-content:space-between;"><span>7</span><span>size+6</span></div>
      </td>
      <td style="border:1px solid #333; padding:2px 8px;">size+7</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px;"><i>type</i><br><span style="font-size:0.8em; opacity:0.7;">octet</span></td>
      <td style="border:1px solid #333; padding:6px;"><i>channel</i><br><span style="font-size:0.8em; opacity:0.7;">short</span></td>
      <td style="border:1px solid #333; padding:6px;"><i>size</i><br><span style="font-size:0.8em; opacity:0.7;">long</span></td>
      <td style="border:1px solid #333; padding:6px;"><i>payload</i><br><span style="font-size:0.8em; opacity:0.7;">'size' octets</span></td>
      <td style="border:1px solid #333; padding:6px;"><i>frame-end</i><br><span style="font-size:0.8em; opacity:0.7;">octet</span></td>
    </tr>
  </tbody>
</table>

AMQP defines these frame types:

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:15%"><col style="width:25%"><col style="width:60%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Type</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Name</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">1</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>METHOD</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Method frame.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">2</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>HEADER</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Content header frame.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">3</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>BODY</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Content body frame.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">4</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>HEARTBEAT</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>Heartbeat frame.</td>
    </tr>
  </tbody>
</table>


### Method Payloads
<table style="display:table; width:100%; text-align:center; table-layout:fixed; border-collapse:collapse; border:1px solid #333;">
  <colgroup>
    <col style="width:20%"><col style="width:20%"><col style="width:60%">
  </colgroup>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:2px 8px;">0</td>
      <td style="border:1px solid #333; padding:2px 8px;">2</td>
      <td style="border:1px solid #333; padding:2px 8px;">4</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:6px;"><i>class-id</i><br><span style="font-size:0.8em; opacity:0.7;">short</span></td>
      <td style="border:1px solid #333; padding:6px;"><i>method-id</i><br><span style="font-size:0.8em; opacity:0.7;">short</span></td>
      <td style="border:1px solid #333; padding:6px;"><i>arguments...</i><br><span style="font-size:0.8em; opacity:0.7;">...</span></td>
    </tr>
  </tbody>
</table>

### Property and Method Summary

#### connection (Class ID 10)
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>start</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">10</td><td style="border:1px solid #333; padding:8px 12px;">start connection negotiation</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>tune-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">31</td><td style="border:1px solid #333; padding:8px 12px;">negotiate connection tuning parameters</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>start-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">11</td><td style="border:1px solid #333; padding:8px 12px;">select security mechanism and locale</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>open</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">40</td><td style="border:1px solid #333; padding:8px 12px;">open connection to virtual host</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>secure</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">20</td><td style="border:1px solid #333; padding:8px 12px;">security mechanism challenge</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>open-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">41</td><td style="border:1px solid #333; padding:8px 12px;">signal that connection is ready</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>secure-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">21</td><td style="border:1px solid #333; padding:8px 12px;">security mechanism response</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>close</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">50</td><td style="border:1px solid #333; padding:8px 12px;">request a connection close</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>tune</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">30</td><td style="border:1px solid #333; padding:8px 12px;">propose connection tuning parameters</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>close-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">51</td><td style="border:1px solid #333; padding:8px 12px;">confirm a connection close</td>
    </tr>
  </tbody>
</table>

#### channel (Class ID 20)
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>open</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">10</td><td style="border:1px solid #333; padding:8px 12px;">open a channel for use</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>flow-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">21</td><td style="border:1px solid #333; padding:8px 12px;">confirm a flow method</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>open-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">11</td><td style="border:1px solid #333; padding:8px 12px;">signal that the channel is ready</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>close</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">40</td><td style="border:1px solid #333; padding:8px 12px;">request a channel close</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>flow</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">20</td><td style="border:1px solid #333; padding:8px 12px;">enable/disable flow from peer</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>close-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">41</td><td style="border:1px solid #333; padding:8px 12px;">confirm a channel close</td>
    </tr>
  </tbody>
</table>

#### exchange (Class ID 40)
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>declare</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">10</td><td style="border:1px solid #333; padding:8px 12px;">verify exchange exists, create if needed</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>delete</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">20</td><td style="border:1px solid #333; padding:8px 12px;">delete an exchange</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>declare-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">11</td><td style="border:1px solid #333; padding:8px 12px;">confirm exchange declaration</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>delete-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">21</td><td style="border:1px solid #333; padding:8px 12px;">confirm deletion of an exchange</td>
    </tr>
  </tbody>
</table>

#### queue (Class ID 50)
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>declare</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">10</td><td style="border:1px solid #333; padding:8px 12px;">declare queue, create if needed</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>purge-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">31</td><td style="border:1px solid #333; padding:8px 12px;">confirms a queue purge</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>declare-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">11</td><td style="border:1px solid #333; padding:8px 12px;">confirms a queue definition</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>delete</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">40</td><td style="border:1px solid #333; padding:8px 12px;">delete a queue</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>bind</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">20</td><td style="border:1px solid #333; padding:8px 12px;">bind queue to an exchange</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>delete-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">41</td><td style="border:1px solid #333; padding:8px 12px;">confirm deletion of a queue</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>bind-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">21</td><td style="border:1px solid #333; padding:8px 12px;">confirm bind successful</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>unbind</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">50</td><td style="border:1px solid #333; padding:8px 12px;">unbind a queue from an exchange</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>purge</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">30</td><td style="border:1px solid #333; padding:8px 12px;">purge a queue</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>unbind-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">51</td><td style="border:1px solid #333; padding:8px 12px;">confirm unbind successful</td>
    </tr>
  </tbody>
</table>

#### basic (Class ID 60)
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:15%"><col style="width:8%"><col style="width:27%">
    <col style="width:15%"><col style="width:8%"><col style="width:27%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>qos</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">10</td><td style="border:1px solid #333; padding:8px 12px;">specify quality of service</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>get</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">70</td><td style="border:1px solid #333; padding:8px 12px;">direct access to a queue</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>qos-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">11</td><td style="border:1px solid #333; padding:8px 12px;">confirm the requested qos</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>get-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">71</td><td style="border:1px solid #333; padding:8px 12px;">provide client with a message</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>consume</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">20</td><td style="border:1px solid #333; padding:8px 12px;">start a queue consumer</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>get-empty</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">72</td><td style="border:1px solid #333; padding:8px 12px;">indicate no messages available</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>consume-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">21</td><td style="border:1px solid #333; padding:8px 12px;">confirm a new consumer</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>ack</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">80</td><td style="border:1px solid #333; padding:8px 12px;">acknowledge one or more messages</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>cancel</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">30</td><td style="border:1px solid #333; padding:8px 12px;">end a queue consumer</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>reject</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">90</td><td style="border:1px solid #333; padding:8px 12px;">reject an incoming message</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>cancel-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">31</td><td style="border:1px solid #333; padding:8px 12px;">confirm a cancelled consumer</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>recover-async</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">100</td><td style="border:1px solid #333; padding:8px 12px;">redeliver unacknowledged messages</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>publish</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">40</td><td style="border:1px solid #333; padding:8px 12px;">publish a message</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>recover</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">110</td><td style="border:1px solid #333; padding:8px 12px;">redeliver unacknowledged messages</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>return</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">50</td><td style="border:1px solid #333; padding:8px 12px;">return a failed message</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>recover-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">111</td><td style="border:1px solid #333; padding:8px 12px;">confirm recovery</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>deliver</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">60</td><td style="border:1px solid #333; padding:8px 12px;">notify the client of a consumer message</td>
      <td style="border:1px solid #333; padding:8px 12px;"></td><td style="border:1px solid #333; padding:8px 12px;"></td><td style="border:1px solid #333; padding:8px 12px;"></td>
    </tr>
  </tbody>
</table>

#### tx (Class ID 90)
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
    <col style="width:14%"><col style="width:9%"><col style="width:27%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Method</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:center; background:rgba(128,128,128,0.1);">ID</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>select</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">10</td><td style="border:1px solid #333; padding:8px 12px;">select standard transaction mode</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>commit-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">21</td><td style="border:1px solid #333; padding:8px 12px;">confirm a successful commit</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>select-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">11</td><td style="border:1px solid #333; padding:8px 12px;">confirm transaction mode</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>rollback</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">30</td><td style="border:1px solid #333; padding:8px 12px;">abandon the current transaction</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>commit</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">20</td><td style="border:1px solid #333; padding:8px 12px;">commit the current transaction</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>rollback-ok</code></td><td style="border:1px solid #333; padding:8px 12px; text-align:center;">31</td><td style="border:1px solid #333; padding:8px 12px;">confirm successful rollback</td>
    </tr>
  </tbody>
</table>

### Sample Hexdump
Protocol Header. The client MUST start a new connection by sending a protocol header. This is an 8-octet sequence:
```
Advanced Message Queuing Protocol
    Type: Method (1)
    Channel: 0
    Length: 524
    Class: Connection (10)
    Method: Start (10)
    Arguments

0000   41 4d 51 50 00 00 09 01                           AMQP....
```

Connection.Open
```
Advanced Message Queuing Protocol
    Type: Method (1)
    Channel: 0
    Length: 8
    Class: Connection (10)
    Method: Open (40)
    Arguments
        Virtual-Host: /
        Capabilities: 
        .... ...1 = Insist: True

0000   01 00 00 00 00 00 08 00 0a 00 28 01 2f 00 01 ce   ..........(./...
```

### Reference
[AMQP Wireshark Wiki](https://wiki.wireshark.org/AMQP)<br>
[IANA search=amqp](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=amqp)<br>
[RabbitMQ: Inspecting AMQP 0-9-1 Traffic using Wireshark](https://www.rabbitmq.com/amqp-wireshark)<br>
[amqp-specification.zip](https://github.com/ericwu1997/ericwu1997.github.io/raw/refs/heads/content/docs/app-layer-protocols/amqpamqp-specification.zip)
