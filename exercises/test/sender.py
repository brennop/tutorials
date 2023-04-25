import p4runtime_sh.shell as sh
from p4runtime_sh.p4runtime import P4RuntimeClient

# dir = "/home/p4/tutorials/exercises/basic/"

# client = P4RuntimeClient(1, "localhost:50051", (1,0), None, None)
# p4_info = client.get_p4info()

sh.setup(
    device_id = 1,
    grpc_addr = "localhost:50051",
    election_id = (0, 1),
    config = None
    # sh.FwdPipeConfig( "build/basic.p4.p4info.txt", "build/basic.json")
)

packet = sh.PacketOut()
packet.payload = b'AAAA'
packet.metadata["egress_port"] = 1

packet.send()
