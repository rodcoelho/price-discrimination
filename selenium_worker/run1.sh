#!/usr/bin/env bash

crontab <<EOF
*/30 * * * * /home/rodrigocoelho/dotfiles/selenium_worker/collect.sh > /home/rodrigocoelho/logs/output.log 2>&1

EOF
