#!/usr/bin/env python3

import os
import re


scheme                   = 'https'
authority                = 'api.digitalocean.com'
path                     = '/v2/droplets'
tag                      = 'test'
query_string             = '?tag_name={tag}'.format(tag=tag)

endpoint                 = '{scheme}://{authority}{path}{query_string}'.format(
                                scheme=scheme,
                                path = path,
                                authority = authority,
                                query_string=query_string)
token                    = 'smoken'

teardown_droplet_command = "curl -X DETETE\                                     \
                            -H \"Content-Type: application/json\"               \
                            -H \"Authentication: Bearer {token}\"               \
                             \"{endpoint}\"".format(
                                                token = token,
                                                endpoint = endpoint)
teardown_droplet_command = (re.sub(' +',' ', teardown_droplet_command))

print(teardown_droplet_command)