---
title: (TCP 2111:2112) CoLa-B
parent: Transport Layer
---

# SICK CoLa-B (Command Language Binary)
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

### Overview
SICK CoLa (Command Language) refers to the family of communication protocols developed by SICK AG for interacting with their industrial sensors, such as LiDAR scanners, safety laser scanners, vision systems, and other detection devices. It operates as part of the SOPAS (SICK Open Protocol for Automation Systems) ecosystem, enabling configuration, parameter access (reading/writing), status monitoring, command execution, and data streaming (e.g., scan or measurement data) over TCP/IP connections. Devices commonly use dedicated ports: CoLa-A on 2111 and CoLa-B on 2112, with newer variants like CoLa-2 on 2122 for enhanced features including better security. CoLa supports event-driven communication and is widely integrated with SICK's SOPAS ET configuration software, which includes terminal tools for testing and debugging telegrams.

The main variants are CoLa-A (ASCII/text-based, human-readable for easy manual interaction and debugging) and CoLa-B (binary format for compact, efficient transmission suited to high-performance or data-intensive tasks). Many SICK devices support one, the other, or both, allowing flexibility based on application needs—CoLa-A simplifies development and troubleshooting, while CoLa-B reduces overhead for faster or bandwidth-constrained scenarios. Newer devices increasingly adopt CoLa-2 (an evolved protocol) for improved capabilities, though CoLa-A and CoLa-B remain broadly deployed in industrial automation for their reliability, compatibility, and mature support across sensor families.

### Protocol Stacks
```
  ------------------------------------
|     Sensor/Host Application        |  <= Client (e.g., PLC, PC, SOPAS ET software)
|------------------------------------|
|          CoLa-B Telegrams          |  <= Binary command/data framing (SOPAS commands)
|------------------------------------|
|               TCP                  |  <= Reliable, connection-oriented transport
|------------------------------------|
|              TCP/IP                |
 ------------------------------------
```

### Cola-B Dataframe

technical_information_ml20_en_im0059796.pdf#page=8&zoom=100<br>
![](./figure-1.png)
#### Request Frame<br>
![](./figure-2.png)
#### Response Frame<br>
![](./figure-3.png)

checksum = XOR all bytes 9 to 13

## Reference
[SOPAS Communication Interface Description.zip](http://ericwu1997.github.io/docs/protocol-analysis/transport-layer/cola-b/SOPAS_Communication_Interface_Description.zip)<br>