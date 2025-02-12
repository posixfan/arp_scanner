# ARP Scanner

This is a simple ARP (Address Resolution Protocol) scanner written in Python 3. The tool scans a given IPv4 network range and identifies live hosts by their ARP responses. It also retrieves the MAC address and manufacturer information for each discovered device.

## Features

- Scans a specified IPv4 address or CIDR range for live hosts.
- Retrieves MAC addresses of discovered devices.
- Looks up the manufacturer of the device using the MAC address.
- Requires root privileges to run (due to the use of raw sockets).

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `scapy` library (`pip install scapy`)
- `mac-vendor-lookup` library (`pip install mac-vendor-lookup`)

## Usage

1. Clone the repository or download the script.
2. Ensure the script has executable permissions:
   ```bash
   chmod +x arp_scan.py
3. Run the script with root privileges:
   ```bash
   sudo ./arp_scan.py <target>
Replace `<target>` with the IPv4 address or CIDR range you want to scan (e.g., `192.168.1.0/24`).

## New versions of Ubuntu and Debian use VENV
[What is VENV](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)

### Quick Start Guide
<pre>bash
~/arp_scanner$ sudo apt install python3-venv
~/arp_scanner$ python3 -m venv venv
~/arp_scanner$ source venv/bin/activate
~/arp_scanner$ pip install scapy
~/arp_scanner$ pip install mac_vendor_lookup
~/arp_scanner$ sudo venv/bin/python3 arp_scanner.py target </pre>
Replace `target` with the IPv4 address or CIDR range you want to scan (e.g., `192.168.1.0/24`).

## Example
<pre>sudo ./arp_scan.py 192.168.1.0/24</pre>
**Output**
The script will display a table with the following columns:
- IP: The IP address of the discovered device.
- MAC Address: The MAC address of the device.
- Manufacturer: The manufacturer of the network interface (if found).

Example output:
<pre>
IP                     MAC Address              Manufacturer
------------------------------------------------------------------------------
192.168.1.1          00:11:22:33:44:55         Cisco Systems, Inc
192.168.1.10         AA:BB:CC:DD:EE:FF         Intel Corporate
</pre>

## Code Overview
- ARP Scanning: The script sends ARP requests to the specified IP range and listens for responses.
- MAC Vendor Lookup: It uses the mac-vendor-lookup library to retrieve the manufacturer information based on the MAC address.
- Root Check: The script ensures it is run with root privileges to access raw sockets.
- Input Validation: It validates the provided IP address or CIDR range before scanning.

## Limitations
- The script requires root privileges to run.
- It only supports IPv4 addresses.
- The manufacturer lookup depends on the accuracy of the mac-vendor-lookup database.

# Author
Andrew Razuvaev - [GitHub](https://github.com/posixfan) | <posixfan87@yandex.ru>
