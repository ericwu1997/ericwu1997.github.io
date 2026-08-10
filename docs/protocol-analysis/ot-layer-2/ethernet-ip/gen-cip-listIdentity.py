from scapy.all import *
import struct
import argparse
import base64
import gzip
from io import BytesIO

PCAP_B64 = (
    "H4sIAMq2dGoC/5WU70sTcRzHP/txakvBVg80NL4IwUae3d222yYGm06zaGtO0zShze3QpW1jzo0M"
    "SaFn9sMiMPBJoIQbhA/qaTBYEEgQhUL/gIzIB4seuQj7fu8OOY5L6AvH971x39f78/58jq+pocFU"
    "BAB/14WzOrwfyksPPFxJZIQZS8iKepJpwTLkt6K4k2YZJ8OgnuAN5EFch5u53D+PLLl4ZgoNDvba"
    "OzgrgAHOA2+nJ+IZNBJPxJK5WcQyyMKx/Zy1HU3MxWdiiHUzdjv2MwIHvrm7qWgkhSwj8bQwOxVJ"
    "T1uRrYPvcCFLVtxphp6McQ43w0QdrINxYQ+ySN2k5k15JzQ95o37hGw8KowHgn237/tsrM3hZVy0"
    "2+3to+1cL0e72e5ummH73F4n72ScDtsCqbkVhv25SFpAASGTS6ankTcWSWWENBr2J4SMC9NPYJca"
    "vNf/Rz6Q6yPnZuTfHw8ocDX/zl/FmjwQHP4ZWoV664Jpvg56AbpKjR7w1KztFDe3X8y/3v1V3tgy"
    "718PJcjLr/TVysNdAL2RemfU15maF/+IYJ3BUCt5EK9xhVfjwGG+E2vySC6So+jVTj0BWKwZnSQ+"
    "xG/LXN64NTM8iv2SYXO10mmWvCSmmn2A2V1Yd2nlsJROiTnKqhxJzB8LNlYrA59l1BE7o2Cvlw7z"
    "IaxDWmxfySyytzXZTdVKuQAg4C9Ca0lfS0b2vKnw5D8c5nmsea1eWainYq/uqHo1hn2XxTxvQeap"
    "s/R8MRSOsqi5PmpF5Po1uTjL3jU5S5seHZ9FOZvWr4bCMbM5LfZvT9W/ZeybxVl2pCzK2aQU7LZv"
    "hkIA64AW21M6I7I/abKbqjv7QYAoOamRR/JRz2US+x0zl2di/6ZU/ctiz3VxLg+Uc9lQcB99ry0s"
    "Yb2kxZ2lnovcFk0unkv4Pclh+8dc6oEm09FvmYubOp3y/1UwGsPArVwKn2SdvIvuDXQPXfQa5Noo"
    "1V3xg3r5Rgct0JOcwzdyehal0slsPCbE0MQ9FJMuTz3Uie+uPS7mDbIm54xYn5NZFNbKRTz+ArMu"
    "EKMABgAA"
)

parser = argparse.ArgumentParser()
parser.add_argument("--vendor_id", type=int, default=1)
parser.add_argument("--device_type", type=int, default=12)
parser.add_argument("--product_code", type=int, default=151)
parser.add_argument("--version", default="4.04")
parser.add_argument("--product_name", default="1768-ENBT/A")
parser.add_argument("--state", type=int, default=3)

args = parser.parse_args()


def build_payload(args):

    # -----------------
    # Identity data
    # -----------------
    product_name = args.product_name.encode("ascii")

    identity = b""

    # Encapsulation Protocol Version
    identity += struct.pack("<H", 1)

    # Socket Address
    identity += struct.pack("<H", 2)          # sin_family
    identity += struct.pack(">H", 44818)      # sin_port
    identity += bytes([192, 168, 1, 1])       # sin_addr
    identity += b"\x00" * 8                  # sin_zero

    # Identity fields
    identity += struct.pack("<H", args.vendor_id)
    identity += struct.pack("<H", args.device_type)
    identity += struct.pack("<H", args.product_code)

    # Revision (major.minor)
    major, minor = args.version.split(".")
    identity += bytes([int(major), int(minor)])

    identity += struct.pack("<H", 0x0060)        # Status
    identity += struct.pack("<I", 0x603d9032)    # Serial Number

    # Product Name
    identity += struct.pack("B", len(product_name))
    identity += product_name

    # State
    identity += struct.pack("B", args.state)


    # -----------------
    # Identity item
    # -----------------
    item = b""
    item += struct.pack("<H", 0x000c)       # Item Type: CIP Identity
    item += struct.pack("<H", len(identity))
    item += identity


    # -----------------
    # EtherNet/IP Encapsulation
    # -----------------
    encap = b""

    encap += struct.pack("<H", 0x0063)       # ListIdentity
    encap += struct.pack("<H", len(item) + 2)
    encap += struct.pack("<I", 0)            # Session Handle
    encap += struct.pack("<I", 0)            # Status
    encap += b"\x00" * 8                     # Sender Context
    encap += struct.pack("<I", 0)            # Options

    # Item Count
    encap += struct.pack("<H", 1)

    # Identity Item
    encap += item

    return encap


pcap_data = gzip.decompress(base64.b64decode(PCAP_B64))
p = list(rdpcap(BytesIO(pcap_data)))

# Modify 10th packet
pkt = p[9]
pkt_time = pkt.time

# Replace TCP payload
pkt[TCP].payload = Raw(build_payload(args))

# Force Scapy recalculation
if IP in pkt:
    del pkt[IP].len
    del pkt[IP].chksum

if TCP in pkt:
    del pkt[TCP].chksum

pkt = IP(bytes(pkt))

p = list(p)
pkt.time = pkt_time
p[9] = pkt

wrpcap("out.pcap", p)
