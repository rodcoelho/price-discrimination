#!/usr/bin/env python3

import os


def set_up(ip):
    os.system('ssh -p 6174 -o "StrictHostKeyChecking no" rodrigocoelho@{ip_address} \'bash -s\' < /selenium_worker/setup.sh'.format(
            ip_address=ip))


def run_it(ip):
    os.system('ssh -p 6174 -o "StrictHostKeyChecking no" rodrigocoelho@{ip_address} \'bash -s\' < /selenium_worker/run1.sh'.format(ip_address=ip))


def main():
    f = open("tmp/ip_address.txt", "r")
    ips = f.readlines()
    address_list = [ip[5:].strip() for ip in ips]
    address_list = address_list[1:]
    # for _ in address_list:
    #     set_up(_)
    for _ in address_list:
        run_it(_)


if __name__ == '__main__':
    main()

