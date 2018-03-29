#!/usr/bin/env python3

import os

regions = ['us-east-1a', 'us-east-1b', 'us-east-1c']
for region in regions:
    os.system("aws lightsail delete-instance --instance-name Lightsail-{}".format(region))

os.system("rm tmp/ip_address_aws.txt")

