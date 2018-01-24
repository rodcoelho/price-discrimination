#!/usr/bin/env python3

import time, json, sys, os
from pprint import pprint
import digitalocean

def spin_up():
    timestamp_utc = time.time()
    writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    # vendor_choice = input('vendor_choice: ')
    vendor_choice = 'do'
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'             \
                        .format(unix_command=digitalocean.builder(), \
                                writeout_file=writeout_file))
            time.sleep(60)
            return harden(writeout_file)
    else:
        pass # TODO 2

def harden(writeout_file):
    response = json.load(open(writeout_file))
    if 'droplets' in response:
        payloads = response['droplets']
    else:
        payloads = [response['droplet']]
    ip_addresses = []
    for payload in payloads:
        ip_addresses.append(digitalocean.get_host(payload['id'], writeout_file))
    for ip_address in ip_addresses:
        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote0.sh'.format(ip_address=ip_address))
        os.system('scp /Users/rodrigocoelho/.ssh/id_rsa.pub root@{ip_address}:/etc/ssh/rodrigocoelho/authorized_keys'.format(ip_address=ip_address))
        os.system('sh -c \'echo "rodrigocoelho:swordfish" > /Users/rodrigocoelho/dotfiles/setup/.credentials\'')
        os.system('scp /Users/rodrigocoelho/projects/dotfiles/setup/.credentials root@{ip_address}:/home/rodrigocoelho/'.format(ip_address=ip_address))
        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote1.sh'.format(ip_address=ip_address))
    return ip_addresses


if __name__ == '__main__':
    pprint(spin_up())
