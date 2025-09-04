import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP()
    print(arp_request.summary())
    scapy.ls(scapy.ARP())  # to know which field we can set

#scan("192.168.254.2")
scan("192.168.254.2/24")