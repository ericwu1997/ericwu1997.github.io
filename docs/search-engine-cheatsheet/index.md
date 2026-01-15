---
title: Search Engine Cheatsheet
nav_order: 5
---

# Search Engine Cheatsheet
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### CVE / PoC Search

<div class="code-example" markdown="1">
```markdown
site:"nvd.nist.gov" intext:("CVE-2020" | "CVE-2021") "cpe:2.3:(o|h|a):Tenda"
```
```markdown
site:"nvd.nist.gov" intext:"CVE-" "Tenda" ("github.com" | "github.io")
```
```markdown
inurl:"exploit-db.com/exploits" intext:"Tenda" "PoC"
```
```markdown
inurl:"https://www.zeroscience.mk" intext:"Tenda" "PoC"
```
</div>

### Censys (Legacy)

Censys has moved from legacy search to new platform. Most of the query list below would not work.

| Filter / Operator | Description | Example |
| :----------------------| :----------------------| :----------------------|
| services.service_name  | Service Filters  | `services.service_name="SNMP"` |
| : | containing keywords (will not match if no word break e.g: Camera-ABC) | `services.http.response.html_title:"Camera"` |
| * | wildcard | `services.http.response.html_title:AXIS*Camera` |
| AND, AND NOT | positive/negative search | `services.http.response.html_title:*Camera* and not "AXIS"` |

#### Commonly used for device searching

<div class="code-example" markdown="1">
```markdown
services.tls.certificate.parsed.subject_dn:*serialNumber\=PID*
```
```markdown
services.snmp.oid_system.desc:*Camera* AND NOT services.truncated = true
```
```markdown
services.http.response.html_title:*Camera* AND NOT services.truncated = true
```
```markdown
services.service_name: {ATG, BACNET, CITRIX, CODESYS, DIGI, DNP3, EIP, FINS, FOX, GE_SRTP, IEC60870_5_104, MODBUS, PCWORX, PRO_CON_OS, S7, WDRPC} AND NOT services.truncated = true
```
```markdown
services.telnet.banner:*E0\:E8\:E6*
```
```markdown
https://search.censys.io/search/report?resource=hosts&q=[QUERY_SYNTAX]&virtual_hosts=EXCLUDE&field=[BREAKDOWN_FILTER]&num_buckets=1000
```
```markdown
https://search.censys.io/search/report?resource=hosts&q=+services.tls.certificates.leaf_data.subject_dn%3A*CN%5C%3D*&virtual_hosts=EXCLUDE&field=services.tls.certificates.leaf_data.subject_dn&num_buckets=1000
```
```markdown
https://search.censys.io/search/report?resource=hosts&q=services.tls.certificates.leaf_data.issuer_dn%3A*CN%5C%3D*&virtual_hosts=EXCLUDE&field=services.tls.certificates.leaf_data.issuer_dn&num_buckets=1000
```
```markdown
https://search.censys.io/search/report?resource=hosts&q=services.tls.certificates.leaf_data.issuer_dn%3A*PID*+and+not+services.tls.certificates.leaf_data.issuer_dn%3A*RAPID*&virtual_hosts=EXCLUDE&field=services.tls.certificates.leaf_data.issuer_dn&num_buckets=1000
```

[Censys Certificates Definition](https://search.censys.io/data/certificates/definitions)
</div>

### Shodan
filter html reponse with "resource.php?a=r&m=eg_pub" and specific faveicon hash 

```
http.html:"resource.php?a=r&m=eg_pub" http.favicon.hash:-69294755
```

### Online Pcap resource
```
"DHCP" site:"cloudshark.org"
```
