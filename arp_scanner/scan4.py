import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()
    arp_request.pdst = ip  # passing ip to check ipfield change
    print(arp_request.summary())
    scapy.ls(scapy.ARP())

#scan("192.168.254.2")
scan("192.168.100.2/24")