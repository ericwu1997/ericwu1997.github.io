import struct

from scapy.all import IP, TCP, Raw, wrpcap

from .cip import CIP
from templates.cip.list_identity import CIP_LISTIDENTITY_PCAP


class CIPListIdentity(CIP):

    def __init__(
        self,
        vendor_id,
        model,
        version,
        device_type=12,
        product_code=151,
        state=3,
        src_ip=None,
        dst_ip=None
    ):
        super().__init__(
            vendor_id,
            model,
            version,
            src_ip,
            dst_ip
        )

        self.device_type = device_type
        self.product_code = product_code
        self.state = state

    @staticmethod
    def add_arguments(parser):

        parser.add_argument("--vendor_id", type=int, required=True)
        parser.add_argument("--model", required=True)
        parser.add_argument("--version", required=True)

        parser.add_argument("--device_type", type=int, default=12)
        parser.add_argument("--product_code", type=int, default=151)
        parser.add_argument("--state", type=int, default=3)

    @classmethod
    def from_args(cls, args):

        return cls(
            args.vendor_id,
            args.model,
            args.version,
            args.device_type,
            args.product_code,
            args.state
        )

    def build_payload(self):

        product_name = self.model.encode("ascii")

        identity = (
            struct.pack("<H", 1) +                 # Encapsulation Version
            struct.pack("<H", 2) +                 # sin_family
            struct.pack(">H", 44818) +             # sin_port
            bytes([192, 168, 1, 1]) +              # sin_addr
            b"\x00" * 8 +                          # sin_zero
            struct.pack("<H", self.vendor_id) +
            struct.pack("<H", self.device_type) +
            struct.pack("<H", self.product_code)
        )

        major, minor = self.version.split(".")

        identity += (
            bytes([int(major), int(minor)]) +
            struct.pack("<H", 0x0060) +
            struct.pack("<I", 0x603d9032) +
            bytes([len(product_name)]) +
            product_name +
            bytes([self.state])
        )

        item = (
            struct.pack("<H", 0x000c) +
            struct.pack("<H", len(identity)) +
            identity
        )

        return (
            struct.pack("<H", 0x0063) +
            struct.pack("<H", len(item) + 2) +
            b"\x00" * 16 +
            struct.pack("<I", 0) +
            struct.pack("<H", 1) +
            item
        )

    def build_pcap(self, filename):

        packets = self.get_template(CIP_LISTIDENTITY_PCAP)

        # Get original client/server IPs
        original_src = packets[0][IP].src
        original_dst = packets[0][IP].dst

        # Change IPs while preserving direction
        for pkt in packets:

            if IP not in pkt:
                continue

            if pkt[IP].src == original_src:
                pkt[IP].src = self.src_ip
                pkt[IP].dst = self.dst_ip

            elif pkt[IP].src == original_dst:
                pkt[IP].src = self.dst_ip
                pkt[IP].dst = self.src_ip

            del pkt[IP].len
            del pkt[IP].chksum

            if TCP in pkt:
                del pkt[TCP].chksum

        # Modify 10th packet payload
        pkt = packets[9]
        pkt_time = pkt.time

        pkt[TCP].payload = Raw(self.build_payload())

        # Recalculate packet fields
        pkt = IP(bytes(pkt))
        pkt.time = pkt_time

        packets[9] = pkt

        wrpcap(filename, packets)