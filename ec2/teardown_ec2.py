#!/usr/bin/env python3

import os, json
import credentials

access_id = credentials.aws_access_key['AWS Access Key ID']
access_key = credentials.aws_access_key['AWS Secret Access Key']

dir_location = "/Users/rodrigocoelho/projects/final-project/worker-nodes/ec2/tmp"
dir = os.listdir(dir_location)

for item in dir:
    if item.endswith("ec2-instance_id_payload.txt"):
        try:
            data = json.load(open('tmp/'+str(item)))
            instance_id = data[0]['InstanceId']
            region = data[0]["Placement"]["AvailabilityZone"]
            region = region[:-1]
            unix_command = '(echo {access_id}; echo {access_key}; echo {region}; echo json;) | aws configure'.format(
                access_id=access_id, access_key=access_key, region=region)
            os.system('{unix_command}'.format(unix_command=unix_command))
            os.system("aws ec2 terminate-instances --instance-ids {instance_id}".format(instance_id=instance_id))
            os.remove(os.path.join(dir_location, item))
        except:
            print("Error reading Json OR no file exists")

os.system("rm tmp/us*")
