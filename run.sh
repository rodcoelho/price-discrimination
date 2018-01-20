#!/usr/bin/env bash

# builds droplet on digital ocean
#python3 build.py

#python3 shell.py


#
#
## Local: ssh root@$IP_ADDRESS
## Remote: > yes
## Remote: git clone git://github.com/rodcoelho/dotfiles.git
#mv dotfiles/nano/.nanorc .
## Remote: chmod +x dotfiles/run.sh
## Remote: ./dotfiles/run.sh
#adduser --disabled-password --gecos "" $REMOTE_USERNAME
#usermod -aG sudo $REMOTE_USERNAME
#cp .nanorc /home/$REMOTE_USERNAME
#mkdir /etc/ssh/$REMOTE_USERNAME
#
#exit
#
## Local
#
#sh -c 'echo "$REMOTE_USERNAME:$REMOTE_PASSWORD" >> /Users/$LOCAL_USERNAME/.credentials'
#
#scp /Users/$LOCAL_USERNAME/.ssh/id_rsa.pub root@$IP_ADDRESS:/etc/ssh/$REMOTE_USERNAME/authorized_keys
#
#scp .credentials root@$IP_ADDRESS:/home/$REMOTE_USERNAME/
#
#ssh root@$IP_ADDRESS