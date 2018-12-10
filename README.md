# ethical-hacking
My implementations for Zaid Sabih's course on Ethical Hacking

1) MAC Changer     : Changes the Mac address of your machine to any desired Mac value. Alternative: simply execute a)ifconfig eth0 down 2) ifconfig eth0 hw ether mac 3) ifconfig eth0 up

2) Network Scanner : Scans the local network by sending out ARP requests and prints a table of IPs and corresponding MACs. Alternative: netdiscover or arping function call in scapy

3) ARP Spoofer     : Spoofs the target ip to the gateway router and the gateway ip to the target router and establishes the attacker machine as the MAN in The Middle. Alternative: arpspoof -i eth0 -t target_machine_ip spoofed_ip

4) Packet Sniffer  : Sniffs packets flowing through the interface and processes them. You must be MITM. Prints Url of webpages accessed and, sniffs passwords and usernames. Works for HTTP(not HTTPS--added later on) only.

5) Net Cut          : Drops all packets coming to attacker machine which need to be forwarded to victim and hence cuts off internet access to the victim machine.

6) DNS Spoof        : Modifies the DNS responses coming to a victim machine and takes it to an ip of attackers choice.

7) Replace Download : Replaces the download of an exe file with a file of choice based on the location entered in the code by the attacker.

8) Code Injector    : Injects javascript code into the code served by the server and sends it to the victim. Use with Beef maybe.

9) HTTPS patch : Use sslstrip by moxie to make above codes to work with https websites.
