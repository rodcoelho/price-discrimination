#!/usr/bin/env python3

import json
import os
import re
import sys
import time


def create_digital_ocean_vps():
    endpoint = 'https://api.digitalocean.com/v2/droplets'
    hostname = 'node'
    api_data = {}
    mac_pa_token = open('/Users/{username}/.pat/.digitalocean'.format(username=('rodrigocoelho'))).read() #FIXME
    a_header = 'Authorization: Bearer {pa_token}'.format(pa_token=mac_pa_token)
    c_header = 'Content-Type: application/json'
    vm_count = 1
    if vm_count < 2:
        api_data['name'] = hostname
    else:
        api_data['names'] = ['{hostname} {_}'
                                .format(hostname=hostname,
                                        _=_)
                                .replace(' ', '-')
                                for _ in range(vm_count)]
    api_data['region'] = 'nyc3'
    api_data['size']   = '1gb'
    api_data['image']  = 'ubuntu-16-04-x64'
    api_data['ssh_keys'] = ['{ssh_key_id}'.format(ssh_key_id=17337718)] #FIXME
    api_data['tags'] = ['test']
    endstate = 'curl -X POST "{endpoint}"              \
                -d \'{api_data}\'                      \
                -H "{a_header}"                        \
                -H "{c_header}"'                       \
                .format(endpoint=endpoint,
                        api_data=json.dumps(api_data),
                        a_header=a_header.strip(),
                        c_header=c_header)
    return re.sub(' +', ' ', endstate)

def build_single_vps():
    timestamp_utc = time.time()
    writeout_file = 'build-{timestamp_utc}.json'.format(timestamp_utc=timestamp_utc)
    aws_lightsail = ['awsl', 'aws lightsail']
    digital_ocean = ['do', 'digital ocean']
    iaas_platform = aws_lightsail + digital_ocean
    vendor_choice = 'do' # FIXME
    if vendor_choice in iaas_platform:
        if vendor_choice in aws_lightsail:
            pass # FIXME
        elif vendor_choice in digital_ocean:
            os.system('{unix_command} > {writeout_file}'                 \
                        .format(unix_command=create_digital_ocean_vps(),
                                writeout_file=writeout_file))
            sys.exit(0)
    else:
        pass # FIXME

if __name__ == '__main__':
    build_single_vps()