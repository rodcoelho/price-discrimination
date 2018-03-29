#!/usr/bin/env python3

import time, json, sys, os


def spin_and_writeout(regions):
    for region in regions:
        timestamp_utc = time.time()
        writeout_file = 'tmp/aws-{timestamp_utc}.txt'.format(timestamp_utc=timestamp_utc)
        unix_command = "aws lightsail create-instances              \
                        --instance-names 'Lightsail-{}'             \
                        --availability-zone '{}'                    \
                        --blueprint-id 'ubuntu_16_04_1'             \
                        --bundle-id 'nano_1_0'                      \
                        --key-pair-name 'lightsail_demo'".format(region, region)
        os.system('{unix_command}'.format(unix_command=unix_command))
        unix_command = "aws lightsail get-instance --instance-name 'Lightsail-{}' --query 'instance.privateIpAddress' --output text".format(region)
        os.system('{unix_command} > {writeout_file}'.format(unix_command=unix_command, writeout_file=writeout_file))
        # writeout the ip address
        with open(writeout_file) as f:
            ip = f.readline()
        with open("tmp/ip_address_aws.txt", "a") as f:
            f.write(region + ' ' + ip)
            f.close()
    os.system("rm tmp/aws-*")


# Full description of instance
#os.system("aws lightsail get-instance --instance-name 'LightsailDemo'")

# Return only the IP
# os.system("aws lightsail get-instance --instance-name 'LightsailDemo' --query 'instance.privateIpAddress' --output text")

# Connect    ---- currently caught in a hang ----
# os.system("ssh -i /Users/rodrigocoelho/.ssh/rodrigos-MacBook-Pro.pem ec2-user@<IP_ADDRESS>")

if __name__ == '__main__':
    aws_nodes = ['us-east-1a', 'us-east-1b', 'us-east-1c']
    spin_and_writeout(aws_nodes)

