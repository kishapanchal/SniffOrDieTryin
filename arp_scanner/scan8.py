import scapy.all as scapy

def scan(ip, iface="eth0", timeout=2):
    try:
        my_mac = scapy.get_if_hwaddr(iface)
    except Exception:
        my_mac = None

    arp_request = scapy.ARP(pdst=ip)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    if my_mac:
        ether.src = my_mac
    packet = ether / arp_request

    answered, _ = scapy.srp(packet, timeout=timeout, iface=iface, verbose=0)

    for _, resp in answered:
        print(resp.psrc)
        print(resp.hwsrc)
        print("-------------------------------------------------------------------------------------")

scan("192.168.100.2/24", iface="eth0")