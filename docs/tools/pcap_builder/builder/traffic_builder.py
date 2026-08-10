import base64
import gzip
from io import BytesIO

from scapy.all import rdpcap


class TrafficBuilder:

    def __init__(
        self,
        src_ip="192.168.1.10",
        dst_ip="192.168.1.20"
    ):
        self.src_ip = src_ip or "192.168.1.10"
        self.dst_ip = dst_ip or "192.168.1.20"

    def get_template(self, template):

        pcap_data = gzip.decompress(
            base64.b64decode(template)
        )

        return list(rdpcap(BytesIO(pcap_data)))

    def build_pcap(self, filename):
        raise NotImplementedError