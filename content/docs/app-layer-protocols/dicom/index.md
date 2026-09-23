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

### Overview
**DICOM** (Digital Imaging and Communications in Medicine) is the NEMA-maintained standard for exchanging and storing medical images (radiology, cardiology, pathology, etc.) and their associated metadata between imaging modalities, workstations, and PACS (Picture Archiving and Communication System) servers. Its Upper Layer Protocol runs over **TCP**, on the well-known port **104** (privileged, requires elevated access) or the IANA-registered non-privileged alternative **11112**; DICOM-over-TLS uses port **2762**. The architecture is client-server, framed as an "Association" between a Service Class User (SCU, the requester) and a Service Class Provider (SCP, the server), negotiated once per connection and then reused for one or more DIMSE (DICOM Message Service Element) operations such as C-STORE (image transfer) or C-FIND (query).

Every Association begins with an **A-ASSOCIATE-RQ** PDU (PDU-type byte `0x01`) carrying two fixed 16-byte ASCII fields — the **Called AE Title** and **Calling AE Title** — which directly expose the application-entity names of the modality/workstation/PACS involved, along with an Application Context Name and a list of Presentation Contexts, each naming a **SOP Class UID** and one or more **Transfer Syntax UIDs** (dotted-decimal identifiers whose OID root, e.g. `1.2.840.10008.*` for standard DICOM vs. vendor-specific roots, can fingerprint the implementation). Traffic is cleartext by default unless the TLS variant on 2762 is negotiated, and internet-exposed, unauthenticated DICOM SCPs (particularly on 104/11112) have been a recurring target for PACS data-exposure research and attacks.

## DCMTK - DICOM query (Manufacturer)
```
findscu.exe 127.0.0.1 104 -P -k "(0008,0070)=*"
```

## DICOM query server 
```py title="dicom_server.py" :collapsed-lines=10
from pynetdicom import AE, evt, debug_logger
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind
from pydicom.dataset import Dataset

# Enable debug logging
debug_logger()

# Create the Application Entity
ae = AE()

# Add a supported presentation context
ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind, '1.2.840.10008.1.2.1')

# Define C-FIND response handler
def handle_find(event):
    """Handle a C-FIND request and yield a matching dataset."""
    ds = Dataset()

    # Standard DICOM tags (parsed from hex dump)
    ds.QueryRetrieveLevel = 'PATIENT'
    ds.Manufacturer = "Carestream Health "         # (0008,0070)
    ds.ManufacturerModelName = "5950"              # (0008,1090)
    ds.OtherPatientIDs = "12345678"                # (0010,0018)
    ds.PatientID = "4.3.1.p1"                       # (0010,0020)

    # Private tags
    ds.add_new((0x2110, 0x0010), 'CS', 'NORMAL')    # (2110,0010)
    ds.add_new((0x2110, 0x0020), 'CS', 'NORMAL')    # (2110,0020)
    ds.add_new((0x2110, 0x0030), 'LO', '5950')      # (2110,0030)

    # Send as pending response
    yield (0xFF00, ds)

# Set event handlers
handlers = [(evt.EVT_C_FIND, handle_find)]

# Start the SCP on a non-privileged port (e.g., 104)
ae.start_server(('localhost', 104), evt_handlers=handlers, block=True)
```

### Wireshark dissector tree view
```
dicom.pdu.type == 0x04 && frame contains "\x08\x00\x70\x00" && tcp.srcport == 104
```
```
DICOM, C-FIND-RSP-DATA
    PDU Type: Data (0x04)
    PDU Length: 132
    PDV, C-FIND-RSP-DATA
        PDV Length: 128
        Context: 0x01 (Explicit VR Little Endian, Patient Root Query/Retrieve Information Model - FIND)
        Flags: 0x02 (Data, Last Fragment)
        (0008,0052)          8 Query/Retrieve Level                          [CS] PATIENT 
        (0008,0070)         18 Manufacturer                                  [LO] Carestream Health 
        (0008,1090)          4 Manufacturer's Model Name                     [LO] 5950
        (0010,0020)          8 Patient ID                                    [LO] 4.3.1.p1
        (0010,1000)          8 (Retired) Other Patient IDs                   [LO] 12345678
        (2110,0010)          6 Printer Status                                [CS] NORMAL
        (2110,0020)          6 Printer Status Info                           [CS] NORMAL
        (2110,0030)          4 Printer Name                                  [LO] 5950                     .
```

## Hex dump
"|4C 4F|" is Long String
```
0000   04 00 00 00 00 84 00 00 00 80 01 02 08 00 52 00   ..............R.
0010   43 53 08 00 50 41 54 49 45 4e 54 20 08 00 70 00   CS..PATIENT ..p.
0020   4c 4f 12 00 43 61 72 65 73 74 72 65 61 6d 20 48   LO..Carestream H
0030   65 61 6c 74 68 20 08 00 90 10 4c 4f 04 00 35 39   ealth ....LO..59
0040   35 30 10 00 20 00 4c 4f 08 00 34 2e 33 2e 31 2e   50.. .LO..4.3.1.
0050   70 31 10 00 00 10 4c 4f 08 00 XX XX XX XX XX XX   p1....LO..123456
0060   XX XX 10 21 10 00 43 53 06 00 4e 4f 52 4d 41 4c   78.!..CS..NORMAL
0070   10 21 20 00 43 53 06 00 4e 4f 52 4d 41 4c 10 21   .! .CS..NORMAL.!
0080   30 00 4c 4f 04 00 35 39 35 30                     0.LO..5950
```



### Reference
[DICOM PS3.8 Network Communication Support for Message Exchange](https://dicom.nema.org/medical/dicom/current/output/chtml/part08/PS3.8.html)<br>
[IANA search=dicom](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml?search=dicom)<br>
[Wireshark DICOM Wiki](https://wiki.wireshark.org/DICOM)<br>
[DICOM Transfer Syntaxes](https://www.dicomlibrary.com/dicom/transfer-syntax/)<br>
[DICOM Standard Browser - Manufacturer](https://dicom.innolitics.com/ciods/rt-plan/general-equipment/00080070)<br>
[Pydicom](https://github.com/pydicom/pynetdicom)<br>
[Siemens - syngo® MR XA60A DICOM Conformance Statement](https://marketing.webassets.siemens-healthineers.com/f7fd6c5ec1e23b92/2d39cd0d6d81/DCS_MR_XA60.pdf?ste_sid=e312323985e874287e1e563f48276433)<br>
