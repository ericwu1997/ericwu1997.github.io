import argparse

from builder.cip.list_identity import CIPListIdentity


TRAFFIC_TYPES = {
    "cip-listidentity": CIPListIdentity,
}


parser = argparse.ArgumentParser()

parser.add_argument(
    "--type",
    required=True,
    choices=TRAFFIC_TYPES.keys()
)

parser.add_argument(
    "--output",
    default="output.pcap"
)

# Common network arguments
parser.add_argument("--src_ip")
parser.add_argument("--dst_ip")

args, _ = parser.parse_known_args()

traffic_class = TRAFFIC_TYPES[args.type]

traffic_class.add_arguments(parser)

args = parser.parse_args()

traffic = traffic_class.from_args(args)

# Set common network configuration
if args.src_ip:
    traffic.src_ip = args.src_ip

if args.dst_ip:
    traffic.dst_ip = args.dst_ip

traffic.build_pcap(args.output)