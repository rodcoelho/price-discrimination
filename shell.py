#!/usr/bin/env python3

import time, json, sys, os
from pprint import pprint
import build

def spin_up():
    timestamp_utc = time.time()
    writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    vendor_choice = 'do'
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass # FIXME include option for AWS Lightsail
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'.format(unix_command=build.create_digital_ocean_vps(),writeout_file=writeout_file))
            time.sleep(60) # Note: waiting for droplets to spin up so that IP Addresses are provisioned and ready
            return harden(writeout_file)
    else:
        pass #FIXME error handler goes here

def harden(writeout_file):
    response = json.load(open(writeout_file))
    print(response)
    payloads = []
    if 'droplets' in response:
        payloads = response['droplets']
    else:
        payloads = [response['droplet']]
    ip_addresses = []
    for payload in payloads:
        ip_addresses.append(build.get_host(payload['id'], writeout_file))
    # for ip_address in ip_addresses:
    #     os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote0.sh'.format(
    #         ip_address=ip_address))
    #     os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote1.sh'.format(
    #         ip_address=ip_address))
    #     os.system('scp /home/kenso/.ssh/id_rsa.pub root@{ip_address}:/etc/ssh/kensotrabing/authorized_keys'.format(
    #         ip_address=ip_address))
    #     os.system('sh -c \'echo "kensotrabing:$w0rdf!$H" > /home/kenso/dotfiles/setup/.credentials\'')
    #     os.system('scp /home/kenso/dotfiles/setup/.credentials root@{ip_address}:/home/kensotrabing/'.format(
    #         ip_address=ip_address))
    #     os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote2.sh'.format(
    #         ip_address=ip_address))
    return ip_addresses

if __name__ == '__main__':
    pprint(spin_up())
