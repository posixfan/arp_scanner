# ARP Scanner
**arp_scanner** is a simple tool that can be used list the IP addresses (and devices) used in a network. It works by sender ARP 'who-has' requests for every IP address of the subnet. If the IP address is used by a device, it will reply with an ARP 'reply' packet.

Author: Andrew Razuvaev <posixfan87@yandex.ru>

# Install packages with pip and requirements.txt

The following command installs packages in bulk according to the configuration file, requirements.txt. In some environments, use pip3 instead of pip.
<pre>$ pip install -r requirements.txt</pre>
Or
<pre>
$ pip install scapy
$ pip install mac_vendor_lookup
</pre>

# New versions of Ubuntu and Debian use VENV
What is VENV => https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

Quick Start Guide
<pre>
~/arp_scanner$ sudo apt install python3-venv
~/arp_scanner$ python3 -m venv venv
~/arp_scanner$ source venv/bin/activate
~/arp_scanner$ pip install scapy
~/arp_scanner$ pip install mac_vendor_lookup
~/arp_scanner$ sudo venv/bin/python3 arp_scanner.py __your_network_address__
~/arp_scanner$ deactivate
</pre>

# How to use
<pre>
$ ./arp_scanner.py -h
usage: arp_scan target [options]

Search for live hosts by arp responses.

positional arguments:
  target      Target IPv4 addresses. You can also use CIDR notation 10.0.0.0/24

options:
  -h, --help  show this help message and exit
</pre>
  
**Scan the host (without VENV)**
<pre>
$ sudo ./arp_scanner.py 192.168.10.1 

IP			MAC Address		Manufacturer
------------------------------------------------------------------------------
192.168.10.1		50:d4:f7:3e:91:9c	TP-LINK TECHNOLOGIES CO.,LTD.
</pre>

**Scan the host (with VENV)**
<pre>
$ sudo venv/bin/python3 arp_scanner.py 192.168.10.1

IP			MAC Address		Manufacturer
------------------------------------------------------------------------------
192.168.10.1		50:d4:f7:3e:91:9c	TP-LINK TECHNOLOGIES CO.,LTD.

</pre>

**Scan the network (without VENV)**
<pre>
$ sudo ./arp_scanner.py 192.168.10.0/24

IP			MAC Address		Manufacturer
------------------------------------------------------------------------------
192.168.10.1		50:d4:f7:3e:91:9c	TP-LINK TECHNOLOGIES CO.,LTD.
192.168.10.103		52:1a:9a:23:0c:14	Manufacturer not found
192.168.10.234		d0:37:45:4d:d1:fe	TP-LINK TECHNOLOGIES CO.,LTD.
192.168.10.143		44:cb:8b:53:b0:b2	LG Innotek
192.168.10.222		34:c9:3d:a2:06:ca	Intel Corporate
192.168.10.235		98:2c:bc:ba:cd:86	Intel Corporate
</pre>

**Scan the network (with VENV)**
<pre>
$ sudo venv/bin/python3 arp_scanner.py 192.168.10.0/24

IP			MAC Address		Manufacturer
------------------------------------------------------------------------------
192.168.10.1		50:d4:f7:3e:91:9c	TP-LINK TECHNOLOGIES CO.,LTD.
192.168.10.103		52:1a:9a:23:0c:14	Manufacturer not found
192.168.10.234		d0:37:45:4d:d1:fe	TP-LINK TECHNOLOGIES CO.,LTD.
192.168.10.143		44:cb:8b:53:b0:b2	LG Innotek
192.168.10.222		34:c9:3d:a2:06:ca	Intel Corporate
192.168.10.235		98:2c:bc:ba:cd:86	Intel Corporate

</pre>

# To understand better
https://en.wikipedia.org/wiki/Address_Resolution_Protocol
