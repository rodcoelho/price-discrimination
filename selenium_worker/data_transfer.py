#!/usr/env/bin python3

import os, time

if __name__ == "__main__":
    # get ip address of Master Node
    f = open("../tmp/ip_address.txt", "r")
    ips = f.readlines()
    address_list = [ip[5:].strip() for ip in ips]
    for _ in address_list:
        os.system('scp -P 6174 rodrigocoelho@{ip}:/home/rodrigocoelho/dotfiles/data/* /Users/rodrigocoelho/projects/final-project/worker-nodes/data'.format(ip=_))
        time.sleep(5)

