#!/usr/bin/env python3

import time, json, sys, os
import digitalocean
import lightsail
from send_messages import sendtext


def spin_up(_):
    timestamp_utc = time.time()
    writeout_file = 'logs/build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    # vendor_choice = input('vendor_choice: ')
    vendor_choice = 'do'
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass    # TODO
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'               \
                        .format(unix_command=digitalocean.builder(_),  \
                                writeout_file=writeout_file))
            time.sleep(60)
            return harden(writeout_file, _)
    else:
        pass  # TODO


def harden(writeout_file, region):



    response = json.load(open(writeout_file))
    if 'droplets' in response:
        payloads = response['droplets']
    else:
        payloads = [response['droplet']]
    ip_addresses = []
    for payload in payloads:
        ip_addresses.append(digitalocean.get_host(payload['id'], writeout_file))
    for ip_address in ip_addresses:
        print(ip_addresses)
        with open("tmp/ip_address.txt", "a") as f:
            f.write(region + ' ' + ip_address +'\n')
            f.close()
        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote0.sh'.format(ip_address=ip_address))
        os.system('scp /Users/rodrigocoelho/.ssh/id_rsa.pub root@{ip_address}:/etc/ssh/rodrigocoelho/authorized_keys'.format(ip_address=ip_address))
        os.system('sh -c \'echo "rodrigocoelho:swordfish" > /Users/rodrigocoelho/projects/final-project/worker-nodes/setup/.credentials\'')
        os.system('scp /Users/rodrigocoelho/projects/final-project/worker-nodes/setup/.credentials root@{ip_address}:/home/rodrigocoelho/'.format(ip_address=ip_address))
        os.system('ssh -o "StrictHostKeyChecking no" root@{ip_address} \'bash -s\' < procedures/remote1.sh'.format(ip_address=ip_address))
        print('\n\n\n')
        os.system('ssh -p 6174 -o "StrictHostKeyChecking no" rodrigocoelho@{ip_address} \'bash -s\' < procedures/remote2.sh'.format(ip_address=ip_address))
        print('\n\n\n')
    return ip_addresses


if __name__ == '__main__':
    master = 'nyc1'
    do_nodes = ['nyc1', 'nyc3', 'sfo2']
    # aws_nodes = ['us-east-1a', 'us-east-1b', 'us-east-1c']

    # single thread for digitalocean master
    spin_up(master)
    time.sleep(60)

    # multi-processing for digitalocean worker nodes
    from functools import partial
    from multiprocessing.pool import Pool

    work = partial(spin_up)
    with Pool(3) as p:
        p.map(work, do_nodes)

    # # aws lightsail worker nodes
    # lightsail.spin_and_writeout(aws_nodes)

    print('Work has been tasked to Pool')
    sendtext('4154307857', 'ATT', 'Droplets Are Up', 'Go get to work!')

