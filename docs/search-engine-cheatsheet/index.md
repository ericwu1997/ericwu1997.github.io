---
title: Search Engine Cheatsheet
nav_order: 3
---

# Search Engine Cheatsheet
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Google Dorking

### Text Dork

| Filter          | Description                                        | Example                              |
| :-------------- |:---------------------------------------------------| :------------------------------------|
| allintext      | Searches for occurrences of all the keywords given. | `allintext:"keyword"` |
| intext      | Searches for the occurrences of keywords all at once or one at a time. | `intext:"keyword"` |
| inurl      | Searches for a URL matching one of the keywords. | `inurl:"keyword"` |
| allinurl      | Searches for a URL matching all the keywords in the query. | `allinurl:"keyword"` |
| intitle      | Searches for occurrences of keywords in title all or one. | `intitle:"keyword"` |
| allintitle      | Searches for occurrences of keywords all at a time. | `allintitle:"keyword"` |
| site      | Specifically searches that particular site and lists all the results for that site. | `site:"www.google.com"` |
| filetype      | Searches for a particular filetype mentioned in the query. | `filetype:"pdf"` |
| link      | Searches for external links to pages. | `link:"keyword"` |
| numrange      | Used to locate specific numbers in your searches. | `numrange:321-325` |
| before/after      | Used to search within a particular date range. | `filetype:pdf & (before:2000-01-01 after:2001-01-01)` |
| allinanchor (and also inanchor)      | This shows sites which have the keyterms in links pointing to them, in order of the most links. | `inanchor:rat` |
| allinpostauthor (and also inpostauthor)      | Exclusive to blog search, this one picks out blog posts that are written by specific individuals. | `allinpostauthor:"keyword"` |
| related      | List web pages that are “similar” to a specified web page. | `related:www.google.com` |
| cache      | Shows the version of the web page that Google has in its cache. | `cache:www.google.com` |

### Search Operator

| Operator | Description                                                         | Example      |
| :--------|:--------------------------------------------------------------------| :------------|
| " "      | exact matches of a query string enclosed in the double quotes.      | `"keyword"`  |
| OR, \|   | containing either query item joined by OR or the pipe character \|  | `"A" | "B"`  |
| ( )      | Group multiple Google dork operators as a logical statement.        | `("A" | "B")`|
| *        | Wildcard or glob pattern as a placeholder for query item            | `A * B`      |
| #..#     | Search a numerical range specified by the two endpoints # inclusive | `1..1000`    |

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
</div>

## Censys

### Text Search

| Filter / Operator | Description | Example |
| :----------------------| :----------------------| :----------------------|
| services.service_name  | Service Filters  | `services.service_name="SNMP"` |
| : | containing keywords (will not match if no word break e.g: Camera-ABC) | `services.http.response.html_title:"Camera"` |
| * | wildcard | `services.http.response.html_title:AXIS*Camera` |
| AND, AND NOT | positive/negative search | `services.http.response.html_title:*Camera* and not "AXIS"` |

### Commonly used for device searching
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
</div>

### Online Pcap resource
```
"DHCP" site:"cloudshark.org"
```
