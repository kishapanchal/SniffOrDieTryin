#to extract data which is useful and interpretable perform filtering
#add filter argument in sniff
#open any web site while running like bing.com to see http request,,local traffic from own browser

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
    #scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter = "port 21")

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest): 
        print(packet)

sniff("eth0")