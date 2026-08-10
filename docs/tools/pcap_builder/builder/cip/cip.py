from ..traffic_builder import TrafficBuilder


class CIP(TrafficBuilder):

    def __init__(
        self,
        vendor_id,
        model,
        version,
        src_ip=None,
        dst_ip=None
    ):
        super().__init__(
            src_ip=src_ip,
            dst_ip=dst_ip
        )

        self.vendor_id = vendor_id
        self.model = model
        self.version = version