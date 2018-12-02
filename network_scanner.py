#!/usr/bin/env python

#Example usage: python network_scanner.py


import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast   = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    combined    = broadcast/arp_request
    answered_list = scapy.srp(combined, timeout = 1, verbose = False)[0]
    print("IP\t\t\tMAC\n-------------------------------------------------------------")
    for i in answered_list:
        print(i[1].psrc + "\t\t" + i[1].hwsrc)

scan("10.0.2.8/24")
