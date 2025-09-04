#specify interface on to which you want to sniff packet
#store argument is false we dont want to store packets on to system to avoid burden on system Memory
#prn is callback fuction which is called when packet is captured on eth0

import scapy.all as scapy

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    print(packet)

sniff("eth0") #it can be wifi interface also