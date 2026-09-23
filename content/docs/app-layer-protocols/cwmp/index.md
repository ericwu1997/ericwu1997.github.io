---
title: CWMP
description: CWMP
permalink: /docs/app-layer-protocols/cwmp/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-23
updateTime: 2026-09-23
tags: [Markdown, Writing]
---

### Overview
**CWMP** (CPE WAN Management Protocol), commonly known by its Broadband Forum specification number **TR-069**, is a bidirectional **SOAP-over-HTTP** application-layer protocol for remote management of customer-premises equipment (CPE). It runs over **TCP**, on the IANA-assigned port **7547**, and follows a client-server model between the managed CPE (routers, cable/DSL modems, VoIP ATAs, and increasingly cameras and other IoT devices) and an ISP-operated Auto Configuration Server (ACS), which uses it to provision configuration, push firmware updates, and run remote diagnostics without a truck roll.

The CPE-initiated `Inform` RPC — sent in a SOAP envelope under the XML namespace `urn:dslforum-org:cwmp-1-x` (version-dependent) — carries a `DeviceId` structure with **Manufacturer**, **OUI**, **ProductClass**, and **SerialNumber** fields in cleartext XML, making it a direct device fingerprint whenever the exchange isn't wrapped in TLS. The ACS can also issue an unsolicited **Connection Request** back to the CPE on port 7547 (typically HTTP Basic/Digest authenticated) to trigger an immediate session. CWMP traffic is plaintext HTTP by default unless the HTTPS variant is negotiated, and internet-exposed port 7547 endpoints have been a recurring target for CPE-hijacking botnets (e.g., the 2016 Mirai/Annie attacks).

### Protocol Stacks
```
 ------------------------------------     Customer Premises Equipment
|   CPE/ACS Management Application   | <= Auto Configuration Server
|------------------------------------|
|            PRC method              | <= Remote Procedure Call
|------------------------------------|
|               SOAP                 | 
|------------------------------------|
|               HTTP                 |
|------------------------------------|
|              SSL/TLS               | 
|------------------------------------|
|              TCP/IP                |
 ------------------------------------
```

### Baseline RPC Messages 
tr-069-1-6-1.pdf#page=83&zoom=100,117,494

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:30%"><col style="width:70%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Generic Methods</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>GetRPCMethods</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Discover the set of methods.</td>
    </tr>
  </tbody>
</table>


<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:30%"><col style="width:70%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">CPE Methods (ACS &rarr; CPE)</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>SetParameterValues</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Modify the value of one or more CPE Parameters.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>GetParameterValues</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Obtain the value of one or more CPE Parameters.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>GetParameterNames</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Discover the Parameters accessible on a particular CPE.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>SetParameterAttributes</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Modify attributes associated with one or more CPE Parameter.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>GetParameterAttributes</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Read the attributes associated with one or more CPE Parameter.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>AddObject</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Create a new instance of a Multi-Instance Object.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>DeleteObject</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Remove a particular instance of an Object.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>Download</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Cause the CPE to download a specified file from the designated location.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>Reboot</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Causes the CPE to reboot.</td>
    </tr>
  </tbody>
</table>

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:30%"><col style="width:70%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">ACS Methods (CPE &rarr; ACS)</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>Inform</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">CPE MUST call the Inform method to initiate a transaction sequence whenever a Session with an ACS is established.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>TransferComplete</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Informs the ACS of the completion (either successful or unsuccessful) of a file transfer initiated by an earlier Download, ScheduleDownload or Upload method call.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>AutonomousTransferComplete</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Informs the ACS of the completion (either successful or unsuccessful) of a file transfer that was not specifically requested by the ACS.</td>
    </tr>
  </tbody>
</table>

### Inform
tr-069-1-6-1.pdf#page=107&zoom=100,117,406
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:16%"><col style="width:24%"><col style="width:60%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Argument</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Type</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>DeviceId</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>DeviceIdStruct</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Uniquely identifies the CPE.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>Event</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>EventStruct[64]</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Event.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>MaxEnvelopes</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>unsignedInt</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Set to a value of 1.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>CurrentTime</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>dateTime</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">CPE current date and time.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>RetryCount</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>unsignedInt</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Number of prior times an attempt was made to retry this Session.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>ParameterList</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>ParameterValueStruct[]</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Name-value pairs.</td>
    </tr>
  </tbody>
</table>

### DeviceIdStruct
tr-069-1-6-1.pdf#page=109&zoom=100,117,96

<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:16%"><col style="width:14%"><col style="width:70%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Name</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Type</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>Manufacturer</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>string(64)</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Manufacturer of the device (for display only). The value MUST be the same as the value of the <code>DeviceInfo.Manufacturer</code> Parameter.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>OUI</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>string(6)</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Same as the value of the <code>DeviceInfo.ManufacturerOUI</code> Parameter.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>ProductClass</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>string(64)</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Same as the value of the <code>DeviceInfo.ProductClass</code> Parameter. Often a strong indication for model name.</td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;"><code>SerialNumber</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>string(64)</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">Same as the value of the <code>DeviceInfo.SerialNumber</code> Parameter.</td>
    </tr>
  </tbody>
</table>

### EventCode
tr-069-1-6-1.pdf#page=65&zoom=100,117,433
<table style="display:table; width:100%; border-collapse:collapse; background:transparent;">
  <colgroup>
    <col style="width:10%"><col style="width:40%">
    <col style="width:10%"><col style="width:40%">
  </colgroup>
  <thead>
    <tr>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">No.</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Event Code</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">No.</th>
      <th style="border:1px solid #333; padding:8px 12px; text-align:left; background:rgba(128,128,128,0.1);">Event Code</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">0</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>BOOTSTRAP</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">8</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>DIAGNOSTICS COMPLETE</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">1</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>BOOT</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">9</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>REQUEST DOWNLOAD</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">2</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>PERIODIC</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">10</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>AUTONOMOUS TRANSFER COMPLETE</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">3</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>SCHEDULED</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">11</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>DU STATE CHANGE COMPLETE</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">4</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>VALUE CHANGE</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">12</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>AUTONOMOUS DU STATE CHANGE COMPLETE</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">5</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>KICKED</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">13</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>WAKEUP</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">6</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>CONNECTION REQUEST</code></td>
      <td style="border:1px solid #333; padding:8px 12px;">14</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>HEARTBEAT</code></td>
    </tr>
    <tr>
      <td style="border:1px solid #333; padding:8px 12px;">7</td>
      <td style="border:1px solid #333; padding:8px 12px;"><code>TRANSFER COMPLETE</code></td>
      <td style="border:1px solid #333; padding:8px 12px;"></td>
      <td style="border:1px solid #333; padding:8px 12px;"></td>
    </tr>
  </tbody>
</table>

### Sample Inform
```js title="CWMP Inform" :collapsed-lines=10
POST / HTTP/1.1
Authorization: Digest username="qacafe", realm="qacafe", uri="/", algorithm=MD5, nonce="XXXXXXXXXXXXXXXX", nc=00000001, cnonce="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", qop=auth, response="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", opaque=""
Content-Length: 1833
Content-Type: text/xml
Host: acs1.broadband-forum.org
User-Agent: MikroTik

<soapenv:Envelope
 xmlns:soap='http://schemas.xmlsoap.org/soap/encoding/'
 xmlns:xsd='http://www.w3.org/2001/XMLSchema'
 xmlns:cwmp='urn:dslforum-org:cwmp-1-0'
 xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/'
 xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'>
 <soapenv:Body>
  <cwmp:Inform>
   <DeviceId>
    <Manufacturer>MikroTik</Manufacturer>
    <OUI>E48D8C</OUI>
    <ProductClass>hAP lite</ProductClass>
    <SerialNumber>XXXXXXXXXXXX</SerialNumber>
   </DeviceId>
   <Event soap:arrayType='cwmp:EventStruct[1]'>
    <EventStruct>
     <EventCode>8 DIAGNOSTICS COMPLETE</EventCode>
     <CommandKey></CommandKey>
    </EventStruct>
   </Event>
   <MaxEnvelopes>1</MaxEnvelopes>
   <CurrentTime>2018-04-01T19:45:02-04:00</CurrentTime>
   <RetryCount>0</RetryCount>
   <ParameterList soap:arrayType='cwmp:ParameterValueStruct[7]'>
    <ParameterValueStruct>
     <Name>Device.RootDataModelVersion</Name>
     <Value xsi:type='xsd:string'>2.11</Value>
    </ParameterValueStruct>
    <ParameterValueStruct>
     <Name>Device.DeviceInfo.SoftwareVersion</Name>
     <Value xsi:type='xsd:string'>6.42rc49</Value>
    </ParameterValueStruct>
    <ParameterValueStruct>
     <Name>Device.DeviceInfo.ProvisioningCode</Name>
     <Value xsi:type='xsd:string'></Value>
    </ParameterValueStruct>
    <ParameterValueStruct>
     <Name>Device.DeviceInfo.HardwareVersion</Name>
     <Value xsi:type='xsd:string'>v1.0</Value>
    </ParameterValueStruct>
    <ParameterValueStruct>
     <Name>Device.ManagementServer.ParameterKey</Name>
     <Value xsi:type='xsd:string'>cdrouter</Value>
    </ParameterValueStruct>
    <ParameterValueStruct>
     <Name>Device.ManagementServer.ConnectionRequestURL</Name>
     <Value xsi:type='xsd:string'>http://10.0.0.1:7547/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</Value>
    </ParameterValueStruct>
    <ParameterValueStruct>
     <Name>Device.ManagementServer.AliasBasedAddressing</Name>
     <Value xsi:type='xsd:boolean'>0</Value>
    </ParameterValueStruct>
   </ParameterList>
  </cwmp:Inform>
 </soapenv:Body>
</soapenv:Envelope>
```

### Reference
[Huawei - eSight Third-Party Device Management Specifications (Communication Terminals)](https://support.huawei.com/enterprise/en/doc/EDOC1100266815/f18f44a/inform-message-format)<br>
[Broadband forum - CWMP Technical Report](https://www.broadband-forum.org/technical-library/?search=cwmp)<br>
[Broadband forum - TR-069 Technical Report](https://www.broadband-forum.org/technical-library/?number=TR-069)<br>
[IANA search=cwmp](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=cwmp)<br>
[Broadband Forum TR-069 CPE WAN Management Protocol](https://www.broadband-forum.org/technical/download/TR-069.pdf)<br>
[Cisco - CWMP_Technology_Commands.zip](https://github.com/ericwu1997/ericwu1997.github.io/raw/refs/heads/main/content/docs/app-layer-protocols/cwmp/CWMP_Technology_Commands.zip)<br>
[University of New Hampshire InterOperability Laboratory - TR-069_Crash_Course.zip](https://github.com/ericwu1997/ericwu1997.github.io/raw/refs/heads/main/content/docs/app-layer-protocols/cwmp/TR-069_Crash_Course.zip)