#!/usr/bin/env python3

import os, re

os.system('curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer d902bef3397deb0a587ee028b75c587019790924046767a3227fb435bd01131e" "https://api.digitalocean.com/v2/droplets?tag_name=test"')
os.system('rm tmp/ip_address.txt')
os.system('rm logs/build*')

