---
title: DNS SD
parent: Protocol Analysis
nav_order: 2
---

# DNS-Based Service Discovery
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
DNS Service Discovery is a mechanism for discovering named instances of a perticular network service using standard DNS queries. DNS-SD requests can be sent using mDNS to yield zero-configuration DNS-SD. This uses DNS PTR, SRV, TXT records to advertise instances of service types, domain names for those instances, and optional configuration parameters for connecting to those instances.<br>

Service instance can be described using a <b>DNS SRV</b> and <b>DNS TXT</b> record. The SRV record has a name of the form "<Instance>.<Service>.<Domain>" and gives the target host and port where the service instance can be reached. The DNS TXT record of the same name gives additional information about this instance, in a structured form using key/value pairs.<br>

## SRV Record
A SRV record has the form
```
_service._proto.name. ttl IN SRV priority weight port target.
```
- service: the symbolic name of the desired service.
- proto: the transport protocol of the desired service; this is usually either TCP or UDP.
- name: the domain name for which this record is valid, ending in a dot.
- ttl: standard DNS time to live field.
- IN: standard DNS class field (this is always IN).
- SRV: Type of Record (this is always SRV).
- priority: the priority of the target host, lower value means more preferred.
- weight: A relative weight for records with the same priority, higher value means higher chance of getting picked.
- port: the TCP or UDP port on which the service is to be found.
- target: the canonical hostname of the machine providing the service, ending in a dot.
- An example SRV record in textual form that might be found in a zone file might be the following:

```
_sip._tcp.example.com. 86400 IN SRV 0 5 5060 sipserver.example.com.
```

This points to a server named sipserver.example.com listening on TCP port 5060 for Session Initiation Protocol (SIP) protocol services. The priority given here is 0, and the weight is 5.<br>

A client can discover list of available instances of a given service type using a query for a DNS PTR record with a name of the form "<Service>.<Domain>", which returns a set of zero or more names. The example below uses linux "dig" command to do so.<br>
References: [https://www.rfc-editor.org/rfc/rfc6763.html#section-7.2](https://www.rfc-editor.org/rfc/rfc6763.html#section-7.2)

```
dig _axis-video._tcp.local ptr @10.0.0.1 -p 5353
```