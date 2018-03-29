#!/usr/bin/env bash

python3 shell.py; sleep 1m; python3 send_ip_address.py

# to SSH:
# ssh -p 6174 rodrigocoelho@IP.ADDRESS.0.0

# to configure each VM for selenium:
# ./dotfiles/selenium_worker/manual_setup.sh

# to begin cron jobs:
# python3 activate

# to list cron jobs in each VM:
# crontab -l

# to push updated code to each VM:
# python3 gitupdate.py

# to delete droplets by tags:
# curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer d902bef3397deb0a587ee028b75c587019790924046767a3227fb435bd01131e" "https://api.digitalocean.com/v2/droplets?tag_name=test"
