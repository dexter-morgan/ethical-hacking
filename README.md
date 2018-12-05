# ethical-hacking
My implementations for Zaid Sabih's course on Ethical Hacking

1) MAC Changer     : Changes the Mac address of your machine to any desired Mac value. Alternative: simply execute a)ifconfig eth0 down 2) ifconfig eth0 hw ether mac 3) ifconfig eth0 up

2) Network Scanner : Scans the local network by sending out ARP requests and prints a table of IPs and corresponding MACs. Alternative: netdiscover or arping function call in scapy

3) ARP Spoofer     : Spoofs the target ip to the gateway router and the gateway ip to the target router and establishes the attacker machine as the MAN in The Middle. Alternative: arpspoof -i eth0 -t target_machine_ip spoofed_ip

4) Packet Sniffer  : Sniffs packets flowing through the interface and processes them. You must be MITM. Prints Url of webpages accessed and, sniffs passwords and usernames. Works for HTTP(not HTTPS--added later on) only.
