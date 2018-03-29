#!/usr/bin/env python3

import os


def send_payload():
    f_read = open("tmp/ip_address.txt", "r")
    ips = f_read.readlines()
    ips = [x[5:] for x in ips]
    for ip in ips:
        os.system('scp -P 6174 /Users/rodrigocoelho/projects/final-project/worker-nodes/tmp/ip_address.txt rodrigocoelho@{ip_address}:/home/rodrigocoelho/dotfiles/tmp'.format(ip_address=ip.strip()))


if __name__ == '__main__':
    send_payload()

