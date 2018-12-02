#!/usr/bin/env python

#Example usage: python network_scanner.py --ip 10.0.2.1/24


import scapy.all as scapy
import argparse


def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast   = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    combined    = broadcast/arp_request
    answered_list = scapy.srp(combined, timeout = 1, verbose = False)[0]
    clients_list = []
    for i in answered_list:
        client_dict = {"ip": i[1].psrc, "mac": i[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(result_list):
    print("IP\t\t\tMAC\n-------------------------------------------------------------")
    for i in result_list:
        print(i["ip"] + "\t\t" + i["mac"])

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip",dest = "ip", help = "Ip range for which Mac is to be found")
    options = parser.parse_args()
    return options

options = get_arguments()
clients_list = scan(options.ip)
print_result(clients_list)
