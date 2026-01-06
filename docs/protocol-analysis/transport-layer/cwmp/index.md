---
title: (TCP 7547:7548) CWMP
parent: Transport Layer
---

# CPE WAN Management Protocol
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
The CPE WAN Management Protocol (CWMP), also known as TR-069, is a standardized protocol developed by the Broadband Forum for remote management of customer premises equipment (CPE) such as routers, gateways, and modems. It enables service providers to provision, configure, monitor, and update devices using a centralized Auto Configuration Server (ACS). CWMP operates over HTTP or HTTPS and uses SOAP-based XML messaging, with communication typically initiated by the CPE to support deployment behind NATs and firewalls.

CWMP supports a wide range of device management functions, including parameter configuration, firmware upgrades, diagnostics, and event notifications, using standardized data models such as TR-098 and TR-181. While it has higher overhead compared to lightweight IoT protocols, CWMP remains widely deployed in broadband networks due to its interoperability, mature tooling, and robust management capabilities, despite being gradually replaced by newer protocols like TR-369 (USP) in modern deployments.

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

| **Generic Methods**     | **Description**             |
|-------------------------|-----------------------------|
| GetRPCMethods           | discover the set of methods | 

| **CPE Methods (ACS -> CPE)** | **Description**                                                         |
|------------------------------|-------------------------------------------------------------------------|
| SetParameterValues           | modify the value of one or more CPE Parameters                          |
| GetParameterValues           | obtain the value of one or more CPE Parameters                          |
| GetParameterNames            | discover the Parameters accessible on a particular CPE                  |
| SetParameterAttributes       | modify attributes associated with one or more CPE Parameter             |
| GetParameterAttributes       | read the attributes associated with one or more CPE Parameter           |
| AddObject                    | create a new instance of a Multi-Instance Object                        |
| DeleteObject                 | remove a particular instance of an Object                               |
| Download                     | cause the CPE to download a specified file from the designated location |
| Reboot                       | causes the CPE to reboot                                                |


| **ACS Methods (CPE - > ACS)** | **Description**                                                                                                                                                   |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inform                        | CPE MUST call the Inform method to initiate a transaction sequence whenever a Session with an ACS is established                                                  |
| TransferComplete              | informs the ACS of the completion (either successful or unsuccessful) of a file transfer initiated by an earlier Download, ScheduleDownload or Upload method call |
| AutonomousTransferComplete    | informs the ACS of the completion (either successful or unsuccessful) of a file transfer that was not specifically requested by the ACS                           |

### Inform
tr-069-1-6-1.pdf#page=107&zoom=100,117,406

| **Arguemnts** | **Types**              | **Value**                                                       |
|---------------|------------------------|-----------------------------------------------------------------|
| DeviceId      | DeviceIdStruct         | uniquely identifies the CPE                                     |
| Event         | EventStruct[64]        | Event                                                           |
| MaxEnvelopes  | unsignedInt            | set to a value of 1                                             |
| CurrentTime   | dateTime               | CPE current date and time                                       |
| RetryCount    | unsignedInt            | Number of prior times an attempt was made to retry this Session |
| ParameterList | ParameterValueStruct[] | name-value pairs                                                |

### DeviceIdStruct
tr-069-1-6-1.pdf#page=109&zoom=100,117,96

| **Name**     | **Types**  | **Description**                                                                                                                 |
|--------------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| Manufacturer | string(64) | Manufacturer of the device (for display only). The value MUST be the same as the value of the DeviceInfo,Manufacturer Parameter |
| OUI          | string(6)  | same as the value of the DeviceInfo.ManufacturerOUI Parameter                                                                   |
| ProductClass | string(64) | same as the value of the DeviceInfo.ProductClass Parameter. Often a strong indication for model name                            |
| SerialNumber | string(64) | same as the value of the DeviceInfo.SerialNumber Parameter                                                                      |

### EventCode
tr-069-1-6-1.pdf#page=65&zoom=100,117,433

|||
|-|-|
| (0) BOOTSTRAP          | (8) DIAGNOSTICS COMPLETE                 |
| (1) BOOT               | (9) REQUEST DOWNLOAD                     |  
| (2) PERIODIC           | (10) AUTONOMOUS TRANSFER COMPLETE        |
| (3) SCHEDULED          | (11) DU STATE CHANGE COMPLETE            |
| (4) VALUE CHANGE       | (12) AUTONOMOUS DU STATE CHANGE COMPLETE |
| (5) KICKED             | (13) WAKEUP                              |
| (6) CONNECTION REQUEST | (14) HEARTBEAT
| (7) TRANSFER COMPLETE  |


### Sample Inform 
```
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


## Reference
[Huawei - eSight Third-Party Device Management Specifications (Communication Terminals)](https://support.huawei.com/enterprise/en/doc/EDOC1100266815/f18f44a/inform-message-format)<br>
[Cisco - CWMP_Technology_Commands.zip](http://ericwu1997.github.io/docs/protocol-analysis/transport-layer/amqp/CWMP_Technology_Commands.zip)<br>
[University of New Hampshire InterOperability Laboratory - TR-069_Crash_Course.zip](http://ericwu1997.github.io/docs/protocol-analysis/transport-layer/amqp/TR-069_Crash_Course.zip)<br>
[Broadband forum - CWMP Technical Report](https://www.broadband-forum.org/technical-library/?search=cwmp)<br>
[Broadband forum - TR-069 Technical Report](https://www.broadband-forum.org/technical-library/?number=TR-069)<br>