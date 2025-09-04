import scapy.all as scapy

def scan(ip, iface="eth0"):
    my_mac = scapy.get_if_hwaddr(iface)
    print(f"My Source MAC: {my_mac}")

    arp_request = scapy.ARP(pdst=ip)
    arp_request.show()

    broadcast = scapy.Ether(src=my_mac, dst="ff:ff:ff:ff:ff:ff")
    broadcast.show()

    arp_request_broadcast = broadcast / arp_request
    arp_request_broadcast.show()

scan("192.168.100.2/24", iface="eth0")