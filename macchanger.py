#!usr/bin/env python

#Usage example : python macchanger.py -i eth0 -m 00:00:00:00:00:00

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest = "interface", help = "Interface of which we change mac address")
    parser.add_option("-m","--mac",dest = "new_mac", help = "New Mac")
    (options, arguments) = parser.parse_args()
    return options

def change_mac(interface,new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_result:
        return mac_result.group(0)
    else:
        print("No mac found")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("current mac is "+ str(current_mac))

change_mac(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("Mac changed to " + current_mac)
else:
    print("Mac unchanged")
