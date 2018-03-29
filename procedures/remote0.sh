#!/usr/bin/env bash

sh -c 'echo "set const" >> .nanorc'

sh -c 'echo "set tabsize 4" >> .nanorc'

sh -c 'echo "set tabstospaces" >> .nanorc'

adduser --disabled-password --gecos "" rodrigocoelho

usermod -aG sudo rodrigocoelho

echo 'rodrigocoelho ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo

cp .nanorc /home/rodrigocoelho/

mkdir -p /etc/ssh/rodrigocoelho/
