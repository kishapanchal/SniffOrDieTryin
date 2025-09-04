import scapy.all as scapy

def scan(ip, iface="eth0"):
    my_mac = scapy.get_if_hwaddr(iface)
    print(f"My Source MAC: {my_mac}")

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(src=my_mac, dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    packet.show()
    answered, unanswered = scapy.srp(packet, timeout=2, iface=iface)
    print(answered.summary())

scan("192.168.100.2/24", iface="eth0")