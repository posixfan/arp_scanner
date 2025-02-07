# ARP Scanner
**arp_scanner** is a simple tool that can be used list the IP addresses (and devices) used in a network. It works by sender ARP 'who-has' requests for every IP address of the subnet. If the IP address is used by a device, it will reply with an ARP 'reply' packet.

Author: Andrew Razuvaev <posixfan87@yandex.ru>

# Install packages with pip and requirements.txt

The following command installs packages in bulk according to the configuration file, requirements.txt. In some environments, use pip3 instead of pip.
<pre>$ pip install -r requirements.txt</pre>

# How to use
<pre>usage: arp_scan target [options]

Search for live hosts by arp responses.

positional arguments:
  target      Target IPv4 addresses. You can also use CIDR notation 10.0.0.0/24

options:
  -h, --help  show this help message and exit
  --hw        Identify the hardware vendor by mac address (Internet needed)</pre>

Scan the host
<pre>
$ sudo ./arp_scanner.py 192.168.10.1 

IP			MAC Address
-----------------------------------------
192.168.10.1		50:d4:f7:3e:91:9c	</pre>

Scan the network
<pre>
$ sudo ./arp_scanner.py 192.168.10.0/24

IP			MAC Address
-----------------------------------------
192.168.10.1		50:d4:f7:3e:91:9c	
192.168.10.124		08:00:27:d2:26:79	
192.168.10.143		44:cb:8b:53:b0:b2	
192.168.10.222		34:c9:3d:a2:06:ca	
</pre>

Identify the manufacturer
<pre>
$ sudo ./arp_scanner.py 192.168.10.1 --hw

IP			MAC Address		Vendor
------------------------------------------------------------------------
192.168.10.1		50:d4:f7:3e:91:9c	TP-LINK TECHNOLOGIES CO.,LTD.
</pre>

# To understand better
https://en.wikipedia.org/wiki/Address_Resolution_Protocol
