# HTTP sniffer (structure same as your snippet; prints full packet on HTTP request)
# NOTE: Only plain HTTP (not HTTPS). Run with root privileges.

# import scapy.all as scapy
# from scapy.layers.http import HTTPRequest  # modern Scapy HTTP layer (no scapy_http)
#
# def sniff(interface):
#     # You can add a BPF filter if you want (e.g., "tcp port 80")
#     # Example with filter:
#     # scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="tcp port 80")
#     scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
#
# def process_sniffed_packet(packet):
#     # Check whether the packet contains an HTTP request
#     if packet.haslayer(HTTPRequest):
#         # As in your original: print the whole packet
#         print(packet)
#
# # Example
# sniff("eth0")