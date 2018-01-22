#!/usr/bin/env bash
# builds droplet on digital ocean
#python3 build.py
python3 shell.py

# curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer d902bef3397deb0a587ee028b75c587019790924046767a3227fb435bd01131e" "https://api.digitalocean.com/v2/droplets?tag_name=test"