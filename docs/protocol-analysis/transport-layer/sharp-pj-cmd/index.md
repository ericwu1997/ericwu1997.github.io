---
title: (TCP 7142) Sharp PJ CMD
parent: Transport Layer
---

# Sharp Projector Control Command
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
Sharp NEC Display Solutions projector control commands use TCP port 7142 to send structured byte sequences for controlling and monitoring projectors. The protocol supports functions such as power, input selection, picture adjustments, mute, and status queries, with corresponding responses returned by the projector.

## Command Details

commands and responses are expressed as follows

```
20h 88h <ID1> <ID2> 0Ch <DATA01> - <DATA12> <CKS>
```

| | |
|------------------|--------------------------------|
| Command/response | A series of strings enclosed in a frame represents a command or response (inhexadecimal notation). |
| Parameter        | A character string in italic enclosed in brackets represents a parameter. For information about the parameters that are common to the control commands (ID1, ID2, CKS, LEN, ERR1, and ERR2), see "2.2 Parameters" (page 10). For information about those parameters whose content varies from command to command (DATA), see the description of the relevant command. |

| Parameter name | Description |
|------------------|--------------------------------|
| Control ID - ID1 | The value of the "control ID" set for the projector is used |
| Model code - ID2 | This varies depending on the model in use. (refer to pj-controlcommands-appendixes.pdf) |
| Checksum         | The checksum is calculated as - 1) Add all preceding bytes of data. 2) Use the value of the low-order one byte (eight bits) of the addition result obtained in ① as the checksum. |
| LEN              | This indicates the data length of the data part (DATA??) following LEN (inbytes). |
| DATA??           | This varies depending on the character string stored. |
| ERR1/2           | The cause of an error is represented by a combination of error codes. |

## Base Model Type Request

Response

| 20h BFh \<ID1> \<ID2> 10h 00h \<DATA01> - \<DATA15> \<CKS> |
|-|

| Item        | Description                                    |
|-------------|------------------------------------------------|
| DATA01 - 02 | Base model type                                |
| DATA03 - 11 | Model name (NUL: termination character string) |
| DATA12 - 13 | Base model type                                |
| DATA14 - 15 | Reserved for the system                        |

## Sample Response

BASE MODEL TYPE REQUEST/RESPONSE

```
0000   00 bf 00 00 01 00 c0    .......
```

```
0000   20 bf 01 20 10 00 ff 22 4d 33 32 33 57 00 00 00    .. ..."M323W...
0010   00 06 12 00 00 85                                 ......
```


## References
[pj-control-command-codes.pdf](https://assets.sharpnecdisplays.us/documents/miscellaneous/pj-control-command-codes.pdf)<br>
[pj-controlcommands-appendixes.pdf](https://assets.sharpnecdisplays.us/documents/usermanuals/pj-controlcommands-appendixes.pdf)