import scapy.all as scapy

def scan(ip, iface="eth0"):   # replace eth0 with your interface (e.g., wlan0, Ethernet, Wi-Fi)
    my_mac = scapy.get_if_hwaddr(iface)
    print(f"My Source MAC: {my_mac}")

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(src=my_mac, dst="ff:ff:ff:ff:ff:ff")
    print(broadcast.summary())

scan("192.168.100.2/24", iface="eth0")