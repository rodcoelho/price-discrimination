#!/usr/bin/env python3

import os
import json
import credentials

regions = {'us-east-1': 'ami-43a15f3e',
           'us-east-2': 'ami-916f59f4',
           'us-west-1': 'ami-925144f2',
           'us-west-2': 'ami-4e79ed36'}

access_id = credentials.aws_access_key['AWS Access Key ID']
access_key = credentials.aws_access_key['AWS Secret Access Key']

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
                        --key-name devenv-key               \
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

