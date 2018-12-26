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

Most of the above programs rely on ARP spoofing to establish the attacker as the MITM. To defend against this here's an arp spoof detector program:

10) Arp Spoof Detector: Detects Arp spoofing attacks and can be modified to give alerts to the user.

11) Malware           : This script when executed on a target machine emails usernames and passwords stored locally to a chosen email id. It uses the tool laZagne.

12) Backdoor          : Listener listens on the attacker machine and reverse_backdoor establishes a reverse connection from victim machine to the attacker machine. You can upload and download files, run system command and look around the file system. This is python implemented and hence has cross-platform usability.

13) Persistence       : A function that adds persistence to any of the above programs for a Windows machine.

14) Anti virus bypass : Use https://spyralscanner.net/ or https://nodistribute.com/ to test progams against AV softwares online. Use https://github.com/upx/upx/releases/ to compress exe files.

Next couple scripts are for website pen testing. Note: Use only on websites that you have permission to  test!

15) Info Gathering    : Code for for path discovery on a particular domain. Wordlists should be made available. You can tweak the code a bit and use it for discovering subdomains for a site.

16) Crawler           : Code to recursively discover all links on a website.

17) Brute Force       : Code to guess login info (password) of a website's admin user.
