import scapy.all as scapy

def scan(ip, iface=None, timeout=1):
    arp_request = scapy.ARP(pdst=ip)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    if iface:
        try:
            ether.src = scapy.get_if_hwaddr(iface)
        except Exception:
            pass

    packet = ether / arp_request

    if iface:
        answered_list = scapy.srp(packet, timeout=timeout, verbose=0, iface=iface)[0]
    else:
        answered_list = scapy.srp(packet, timeout=timeout, verbose=0)[0]

    print("IP \t\t\t\t MAC Address\n--------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t\t" + element[1].hwsrc)

scan("192.168.100.2/24", iface="eth0")