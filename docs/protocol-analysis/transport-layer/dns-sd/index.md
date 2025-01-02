---
title: (UDP 5353) DNS SD
parent: Transport Layer
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
DNS Service Discovery aka DNS-SD requests can also be sent using mDNS to yield zero-configuration DNS-SD. This uses DNS PTR, SRV, TXT records to advertise instances of service types, domain names for those instances, and optional configuration parameters for connecting to those instances. But SRV records can now resolve to .local domain names, which mDNS can resolve to local IP addresses.<br>

Service instance can be described using a <b>DNS SRV</b> [RFC 2782] and <b>DNS TXT</b> [RFC 1035] record. The SRV record has a name of the form "<Instance>.<Service>.<Domain>" and gives the target host and port where the service instance can be reached. The DNS TXT record of the same name gives additional information about this instance, in a structured form using key/value pairs.<br>

## Common DNS Record
While there are other DNS recrod type, this section only covers SRV, TXT and PTR type.<br>

SRV record
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

Example of PTR record and TXT record
```
1.0.0.10.in-addr.arpa. 3600 PTR mailserver.example.org.
example.com.   IN   TXT   "This domain name is reserved for use in documentation"
```

A client can discover list of available instances of a given service type using a query for a DNS PTR [RFC 1035] record with a name of the form "<Service>.<Domain>", which returns a set of zero or more names. The example below uses linux "dig" command to do so.<br>

References: [https://www.rfc-editor.org/rfc/rfc6763.html#section-7.2](https://www.rfc-editor.org/rfc/rfc6763.html#section-7.2)

```
dig _axis-video._tcp.local PTR @10.0.0.1 -p 5353 # SRV Record
dig _axis-video._tcp.local TXT @10.0.0.1 -p 5353 # TXT Record
```

## Device inquiry with DNS-SD

1 - reuqest PTR record "_services._dns-sd._udp.local"<br>
on port 5353 (service = _services._dns-sd, porto = _udp, domain = .local)
```
dig _services._dns-sd._udp.local PTR @10.0.0.1 -p 5353 
```

Below snippet shows an example reply

```
──(root㉿kali)-[/home/kali/Desktop]
└─# dig _services._dns-sd._udp.local PTR @10.0.0.1 -p 5353 

; <<>> DiG 9.18.0-2-Debian <<>> _services._dns-sd._udp.local PTR @10.0.0.1 -p 5353
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 37526
;; flags: qr aa; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;_services._dns-sd._udp.local.  IN      PTR

;; ANSWER SECTION:
_services._dns-sd._udp.local. 10 IN     PTR     _workstation._tcp.local.
_services._dns-sd._udp.local. 10 IN     PTR     _http._tcp.local.
_services._dns-sd._udp.local. 10 IN     PTR     _device-info._tcp.local.
_services._dns-sd._udp.local. 10 IN     PTR     _ASUSTOR_ADM._tcp.local.

;; Query time: 243 msec
;; SERVER: 10.0.0.1#5353(10.0.0.1) (UDP)
;; WHEN: Wed Dec 11 18:38:32 EST 2024
;; MSG SIZE  rcvd: 152
```

1 - Additional request based on service available<br>
Based on the answer section in the reply, we can do additional inquery. "_device-info" seem to return device information, while "_ASUSTOR_ADM" indicates that the device the device could be from the vendor "Asustor". Below snippets shows PTR request/reply on "_ASUSTOR_ADM"

```
──(root㉿kali)-[/home/kali/Desktop]
└─# dig _ASUSTOR_ADM._tcp.local PTR @10.0.0.1 -p 5353

; <<>> DiG 9.18.0-2-Debian <<>> _ASUSTOR_ADM._tcp.local PTR @10.0.0.1 -p 5353
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47741
;; flags: qr aa; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;_ASUSTOR_ADM._tcp.local.       IN      PTR

;; ANSWER SECTION:
_ASUSTOR_ADM._tcp.local. 10     IN      PTR     Fileservers._ASUSTOR_ADM._tcp.local.
Fileservers._ASUSTOR_ADM._tcp.local. 10 IN TXT  "httpport=3000" "httpenabled=No" "httpsport=3001" "httpsenabled=Yes" "model=AS6404T" "version=3.2.1.RKU4" "hostid=aa-bb-cc-dd-ee-ff" "serialnumber=AL18036404TM0052" "wol=Yes" "canSuspend=Yes" "netif=[\010  {\010    \"name\":\"LAN1\",\010    \"mac\":\"aa:bb:cc:dd:ee:ff\"\010  },\010  {\010    \"name\":\"LAN2\",\010    \"mac\":\"aa:bb:cc:dd:ee:ff\"\010  }\010]"
Fileservers._ASUSTOR_ADM._tcp.local. 10 IN SRV  0 0 3001 Fileservers.local.
Fileservers.local.      10      IN      A       192.168.1.243

;; Query time: 211 msec
;; SERVER: 10.0.0.1#5353(10.0.0.1) (UDP)
;; WHEN: Wed Dec 11 18:44:35 EST 2024
;; MSG SIZE  rcvd: 424

```

## Useful service name for IoT scanning
```
_device-info._tcp.local  # General device info
_axis-video._tcp.local   # Axis Camera
_qdiscover._tcp.local    # QNAP Camera
_qsan-storage._tcp.local # QSAN NAS
_ASUSTOR_ADM._tcp.local  # Asustor NAS
```

## References
[https://www.rfc-editor.org/rfc/rfc6763.html](https://www.rfc-editor.org/rfc/rfc6763.html)