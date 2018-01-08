#!/usr/bin/env python3

import os
import re

path_to_token = input("Path to token: ")
#token = path_to_token
with open('{path_to_token}'.format(path_to_token=path_to_token), 'r') as f:
    token = f.read().rsplit()[0]
print(token)

scheme                   = 'https'
authority                = 'api.digitalocean.com'
path                     = '/v2/droplets'
endpoint                 = '{scheme}://{authority}{path}'.format(
                                scheme=scheme,
                                path = path,
                                authority = authority,
                                )
#token                    = 'smoken'
data                     = 'sata'

# FIXME - Format the following string
create_droplet_command = "curl -X POST -d \'{data}\'                            \
                            -H \"Authentication: Bearer {token}\"               \
                            -H \"Content-Type: application/json\"               \
                             \"{endpoint}\"".format(data = data,
                                                token = token,
                                                endpoint = endpoint)
print(re.sub(' +', ' ', create_droplet_command))
#os.system(create_droplet_command)

# Then, we need to wait fot the droplet to be created
#os.system()

# Then we need to get the IP address of the droplet that we created
#os.system()

# Finally, we need to clone our dotfiles to the droplet
#host =
#os.system('ssh -o "StrictHostKeyChecking no" root@{host}\'bash -s\' < dotfiles/run.sh'.format(host=host)')
