---
title: (TCP 104) DICOM
parent: Transport Layer
---

# Digital Imaging and Communications in Medicine
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
DICOM (Digital Imaging and Communications in Medicine) is a vendor-neutral standard for transmitting, storing, and managing medical images and associated data. It uses TCP/IP (typically port 104) for communication and supports operations like sending (C-STORE), querying (C-FIND), and retrieving images. DICOM ensures interoperability across devices from different manufacturers, facilitating seamless integration in healthcare systems.

## DCMTK - DICOM query (Manufacturer)
findscu.exe 127.0.0.1 104 -P -k "(0008,0070)=*"

## DICOM query server 
```
from pynetdicom import AE, evt, debug_logger
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind
from pydicom.dataset import Dataset

# Enable debug logging to trace DICOM communication
debug_logger()

# Create the Application Entity (AE)
ae = AE()

# Add a supported presentation context (Patient Root C-FIND)
ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)

# C-FIND handler
def handle_find(event):
    """Handle a C-FIND request and yield matching datasets."""

    # Response dataset
    ds = Dataset()
    ds.QueryRetrieveLevel = 'PATIENT'
    ds.PatientName = 'John^Doe'
    ds.PatientID = '123456'

    # Add Manufacturer info
    ds.Manufacturer = 'Siemens Healthineers'
    ds.ManufacturerModelName = 'SOMATOM Definition Edge'

    yield (0xFF00, ds)  # Pending response

# Bind the C-FIND handler to the AE
handlers = [(evt.EVT_C_FIND, handle_find)]

# Start the SCP (server) on port 104
ae.start_server(('localhost', 104), evt_handlers=handlers, block=True)
```

## Wireshark dissector tree view
```
DICOM, C-FIND-RSP-DATA
    PDU Type: Data (0x04)
    PDU Length: 112
    PDV, C-FIND-RSP-DATA
        PDV Length: 108
        Context: 0x01 (Implicit VR Little Endian: Default Transfer Syntax for DICOM, Patient Root Query/Retrieve Information Model - FIND)
        Flags: 0x02 (Data, Last Fragment)
        (0008,0052)          8 Query/Retrieve Level                          PATIENT 
        (0008,0070)         20 Manufacturer                                  Siemens Healthineers
        (0008,1090)         24 Manufacturer's Model Name                     SOMATOM Definition Edge 
        (0010,0010)          8 Patient's Name                                John^Doe
        (0010,0020)          6 Patient ID                                    123456                                      .
```

## Reference 
[DICOM Standard Browser - Manufacturer](https://dicom.innolitics.com/ciods/rt-plan/general-equipment/00080070)<br>
[Pydicom](https://github.com/pydicom/pynetdicom)<br>
[Siemens - syngo® MR XA60A DICOM Conformance Statement](https://marketing.webassets.siemens-healthineers.com/f7fd6c5ec1e23b92/2d39cd0d6d81/DCS_MR_XA60.pdf?ste_sid=e312323985e874287e1e563f48276433)<br>