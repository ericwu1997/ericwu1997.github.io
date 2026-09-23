---
title: DICOM
description: DICOM
permalink: /docs/app-layer-protocols/dicom/
type: doc
group: APP Layer Protocols
order: 20
createTime: 2026-09-23
updateTime: 2026-09-23
tags: [Markdown, Writing]
---

## Overview
**DICOM** (Digital Imaging and Communications in Medicine) is the NEMA-maintained standard for exchanging and storing medical images (radiology, cardiology, pathology, etc.) and their associated metadata between imaging modalities, workstations, and PACS (Picture Archiving and Communication System) servers. Its Upper Layer Protocol runs over **TCP**, on the well-known port **104** (privileged, requires elevated access) or the IANA-registered non-privileged alternative **11112**; DICOM-over-TLS uses port **2762**. The architecture is client-server, framed as an "Association" between a Service Class User (SCU, the requester) and a Service Class Provider (SCP, the server), negotiated once per connection and then reused for one or more DIMSE (DICOM Message Service Element) operations such as C-STORE (image transfer) or C-FIND (query).

Every Association begins with an **A-ASSOCIATE-RQ** PDU (PDU-type byte `0x01`) carrying two fixed 16-byte ASCII fields — the **Called AE Title** and **Calling AE Title** — which directly expose the application-entity names of the modality/workstation/PACS involved, along with an Application Context Name and a list of Presentation Contexts, each naming a **SOP Class UID** and one or more **Transfer Syntax UIDs** (dotted-decimal identifiers whose OID root, e.g. `1.2.840.10008.*` for standard DICOM vs. vendor-specific roots, can fingerprint the implementation). Traffic is cleartext by default unless the TLS variant on 2762 is negotiated, and internet-exposed, unauthenticated DICOM SCPs (particularly on 104/11112) have been a recurring target for PACS data-exposure research and attacks.

## Reference
[DICOM PS3.8 Network Communication Support for Message Exchange](https://dicom.nema.org/medical/dicom/current/output/chtml/part08/PS3.8.html)<br>
[IANA search=dicom](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=dicom)<br>
[Wireshark DICOM Wiki](https://wiki.wireshark.org/DICOM)<br>
