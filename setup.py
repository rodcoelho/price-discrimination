#!/usr/bin/env python3

import os
import re

path_to_token = '/Users/rodrigocoelho/.pat/.digitalocean'
with open('{path_to_token}'.format(path_to_token=path_to_token), 'r') as f:
    token = f.read().rsplit()[0]

scheme                   = 'https'
authority                = 'api.digitalocean.com'
path                     = '/v2/droplets'
endpoint                 = '{scheme}://{authority}{path}'.format(
                                scheme=scheme,
                                path = path,
                                authority = authority,
                                )

data                     = '{"name": "newchain","region": "nyc3","size": "512mb","image": "ubuntu-16-04-x64","ssh_keys": ["17337718"],"backups": false,"ipv6": false,"user_data": null,"private_networking": null,"volumes": null,"tags": ["tagtest"]}'

create_droplet_command = "curl -X POST -d \'{data}\'                            \
                            -H \"Authentication: Bearer {token}\"               \
                            -H \"Content-Type: application/json\"               \
                             \"{endpoint}\"".format(data = data,
                                                token = token,
                                                endpoint = endpoint)
os.system(create_droplet_command)

#print(re.sub(' +', ' ', create_droplet_command))
#os.system(create_droplet_command)

# Then, we need to wait fot the droplet to be created
#os.system()

# Then we need to get the IP address of the droplet that we created
#os.system()

# Finally, we need to clone our dotfiles to the droplet
#host =
#os.system('ssh -o "StrictHostKeyChecking no" root@{host}\'bash -s\' < dotfiles/run.sh'.format(host=host)')

# if __name__ == "__main__":
#     token = '/Users/rodrigocoelho/.pat/.digitalocean'
