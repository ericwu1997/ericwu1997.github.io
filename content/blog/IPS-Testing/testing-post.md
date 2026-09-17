---
title: Wireshark Packet Replay
description: Preview marks, callouts, collapses, tabs, task lists, and Mermaid diagrams.
permalink: /blog/ips-testing/
lang: en-US
createTime: 2026-09-16
updateTime: 2026-09-16
tags: [Markdown, Components, Writing]
cover: /img/logo.svg
coverStyle:
  layout: odd-right
  ratio: 3/2
  width: 180
---

## Wireshark Packet Replay

### Link-Layer Capture

Ethernet captures can typically be replayed directly. The commands below prepare a sample PCAP for replay. If the capture uses SLL (Linux Cooked Capture), refer to the [next section](#linux-cooked-capture-sll) to generate an output file before replaying it with tcpreplay.

```
TBD
```

### Linux Cooked Capture (SLL)

SLL (Linux Cooked Capture) is a pseudo link-layer header created by libpcap, commonly used when capturing on Linux’s any interface or when the real link-layer header is unavailable. It provides a consistent format for packets from different interfaces.

When replaying SLL captures with tcpreplay, the SLL link-layer header is not directly suitable for Ethernet replay. Using tcprewrite --dlt=enet may result in packets with a length of 0 when converting SLL captures to Ethernet. The Scapy code below instead rebuilds the packets with an Ethernet header and rewrites the client and server IP and MAC addresses using the supplied values.

```py title="scapy_rewrite.py" :collapsed-lines=10
from scapy.all import IP, TCP, UDP, Ether, rdpcap, wrpcap

# ====== CONFIG ======
INPUT_PCAP = "opc_filtered.pcap"
OUTPUT_PCAP = "opc_ready.pcap"

ORIGINAL_CLIENT_IP = "172.17.11.71"

CLIENT_IP = "10.0.0.2"
FORTIGATE_IP = "10.0.0.1"

CLIENT_MAC = "AA:BB:CC:DD:EE:FF"
FORTIGATE_MAC = "AA:BB:CC:DD:EE:FF"
# ====================

packets = rdpcap(INPUT_PCAP)
new_packets = []

for pkt in packets:
    if IP not in pkt:
        continue

    client_to_fortigate = pkt[IP].src == ORIGINAL_CLIENT_IP

    if client_to_fortigate:
        src_ip, dst_ip = CLIENT_IP, FORTIGATE_IP
        src_mac, dst_mac = CLIENT_MAC, FORTIGATE_MAC
    else:
        src_ip, dst_ip = FORTIGATE_IP, CLIENT_IP
        src_mac, dst_mac = FORTIGATE_MAC, CLIENT_MAC

    ip_pkt = pkt[IP].copy()
    ip_pkt.src = src_ip
    ip_pkt.dst = dst_ip

    new_pkt = Ether(src=src_mac, dst=dst_mac) / ip_pkt

    del new_pkt[IP].chksum

    if TCP in new_pkt:
        del new_pkt[TCP].chksum
    elif UDP in new_pkt:
        del new_pkt[UDP].chksum

    new_packets.append(new_pkt)

wrpcap(OUTPUT_PCAP, new_packets)

print(f"[+] Done. Wrote {len(new_packets)} packets to {OUTPUT_PCAP}")
```

