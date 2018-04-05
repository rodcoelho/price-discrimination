#!/usr/bin/env python3

import os
import json
from credentials import credential
access_id = credential.aws_access_key['AWS Access Key ID']
access_key = credential.aws_access_key['AWS Secret Access Key']


regions = {'us-east-1': 'ami-43a15f3e',
           'us-east-2': 'ami-916f59f4',
           'us-west-1': 'ami-925144f2',
           'us-west-2': 'ami-4e79ed36'}


# spin up ec2 instance
for region, image_id in regions.items():
    try:
        # aws configure
        unix_command = '(echo {access_id}; echo {access_key}; echo {region}; echo json;) | aws configure'.format(access_id=access_id, access_key=access_key, region=region)
        os.system('{unix_command}'.format(unix_command=unix_command))

        # spin up VM
        writeout_file = 'tmp/{region}-ec2-instance_id_payload.txt'.format(region=region)
        unix_command = "aws ec2 run-instances               \
                        --image-id {image_id}               \
                        --region {region}                   \
                        --count 1 --instance-type t2.micro  \
                        --key-name rodcoelho_key            \
                        --query 'Instances'".format(image_id=image_id, region=region)
        os.system('{unix_command} > {writeout_file}'.format(unix_command=unix_command, writeout_file=writeout_file))
        # returns an "instance id" for the instance
    except:
        print("Spin up error - {}\n".format(region))

    try:
        # we need that "instance id" to get the public IP address (the output only gives us private ip)
        data = json.load(open('tmp/{region}-ec2-instance_id_payload.txt'.format(region=region)))
        instance_id = data[0]['InstanceId']
    except:
        print("Fail reading JSON - {}\n\n".format(region))

    try:
        # get public IP address
        writeout_file = 'tmp/{region}-ec2-ip_address.txt'.format(region=region)
        unix_command = "aws ec2 describe-instances                              \
                        --instance-ids {instance_id}                            \
                        --query 'Reservations[0].Instances[0].PublicIpAddress'".format(instance_id=instance_id)
        os.system('{unix_command} > {writeout_file}'.format(unix_command=unix_command, writeout_file=writeout_file))
    except:
        print("Error writing out IP address - {}\n\n\n\n".format(region))


# clean up tmp directory and create one location that stores all of the public ip addresses
dir_location = "/Users/rodrigocoelho/projects/final-project/worker-nodes/ec2/tmp"
dir = os.listdir(dir_location)
for item in dir:
    if item.endswith("ec2-ip_address.txt"):
        item = 'tmp/' + item
        file_data = open(item, 'r')
        ip = file_data.readline()[1:-2]

        # FIXME
        # we need to come back at a later point and create a data structure (perhaps a dict) to store ip, region, etc
        # so that this next line can do this:
        # enable security group to ssh via the public ip address
        # os.system('aws ec2 authorize-security-group-ingress --group-name rodcoelho --protocol tcp --port 22 --cidr ' + ip + '/24')

        # append each ip into one text file
        with open("tmp/ip_address.txt", "a") as f:
            f.write(ip + '\n')
            f.close()

        # delete old files
        os.system('rm ' + item)
##################       ##################
##################  ssh  ##################
##################       ##################
# east 1
# ssh -i /Users/rodrigocoelho/.ssh/devenv-key-east1.pem ubuntu@<IPADDRESS>

# east 2
# ssh -i /Users/rodrigocoelho/.ssh/devenv-key-east2.pem ubuntu@<IPADDRESS>

# west 1
# ssh -i /Users/rodrigocoelho/.ssh/devenv-key-west1.pem ubuntu@<IPADDRESS>

# west 2
# ssh -i /Users/rodrigocoelho/.ssh/devenv-key-west2.pem ubuntu@<IPADDRESS>

