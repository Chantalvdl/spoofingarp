import scapy.all as scapy
#from scapy.all import *
from tkinter import *


def scanning(ip):
    arp_request = scapy.all.ARP(pdst=ip)
    broadcast = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    a = arp_request /broadcast