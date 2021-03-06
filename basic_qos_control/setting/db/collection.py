"""class for member & group."""
import networkx as nx


class Member:

    """Class for Member."""

    def __init__(self, name, group):
        """Initial Setting methid."""
        self.name = name
        self.group_id = group
        self.datapath = None
        self.port = None
        self.ip = None


class Group:

    """Class for Group."""

    def __init__(self, group_id):
        """Initial Setting methid."""
        self.group_id = group_id
        self.topology = nx.DiGraph()
        self.switches = []
        self.links = []
        self.members = []


class Flow:

        """Class for Flow."""

        def __init__(self, dpid, src_mac, dst_mac, src_ip, dst_ip,
                     ip_proto, src_port, dst_port, byte, exist):
            """Initial Setting method."""
            self.dpid = dpid
            self.src_mac = src_mac
            self.dst_mac = dst_mac
            self.src_ip = src_ip
            self.dst_ip = dst_ip
            self.ip_proto = ip_proto
            self.src_port = src_port
            self.dst_port = dst_port
            self.byte_count_1 = 0
            self.byte_count_2 = byte
            self.app = "Others"
            self.rate = 0
            self.exist = exist
            self.limited = 0
            self.r_limited = 0
            self.counter = 0

        def rate_calculation(self):
            """calculate flow rate."""
            if self.byte_count_2 > self.byte_count_1:
                self.rate = (float(self.byte_count_2) - float(self.byte_count_1))/1


# class Port:
#
#     """Class for Port."""
#
#     def __init__(self, dpid, port_num):
#         """Initial Setting method."""
#         self.dpid = dpid
#         self.port_num = port_num
#         self.cost = 0.0
#         self.recv_rate = 0.0
#         self.trans_rate = 0.0
