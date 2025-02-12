#!/usr/bin/env python3
# https://github.com/posixfan/arp-keeper
from argparse import ArgumentParser
from mac_vendor_lookup import MacLookup
from ipaddress import IPv4Network
from os import getuid
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp

parser = ArgumentParser(description='Search for live hosts by arp responses.',
                        usage='arp_scan target [options]')
parser.add_argument('target', type=str,
                    help='Target IPv4 addresses. You can also use CIDR notation'
                         ' 10.0.0.0/24')
args = parser.parse_args()

def is_running_as_root():
    return getuid() == 0

def is_valid_ipv4_cidr(cidr):
    try:
        IPv4Network(cidr, strict=False)
        return True
    except ValueError:
        return False

def arp_scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst='FF:FF:FF:FF:FF:FF')
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def get_vendor_by_mac(mac_address):
    try:
        return MacLookup().lookup(mac_address)
    except:
        return f'Manufacturer not found'

def print_result(results_list):
    print(f'\nIP\t\t\tMAC Address\t\tManufacturer\n{"-" * 78}')

    for client in results_list:
        print(f'{client["ip"]}\t\t{client["mac"]}\t{get_vendor_by_mac(client["mac"])}')

def main():
    if not is_running_as_root():
        print('Root rights are required')
        return

    if not is_valid_ipv4_cidr(args.target):
        print('Invalid ip address format\n'
             'An example of the correct format: 192.168.1.10, 10.205.100.0/24,'
             ' 192.168.255.0/33')
        return

    result = arp_scan(args.target)

    try:
        print_result(result)
    except KeyboardInterrupt:
        print('\nTurning off the program\n')

if __name__ == '__main__':
    main()
