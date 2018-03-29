#!/usr/bin/env bash

mkdir logs

sudo apt-get install python-pip

sudo pip3 install selenium yagmail

sudo pip3 install pyvirtualdisplay

wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz

tar -xvzf geckodriver-v0.18.0-linux64.tar.gz

chmod a+x geckodriver

chmod 755 geckodriver

sudo apt-get install cron

#export PATH=$PATH:/usr/bin/env/geckodriver
#sudo mv geckodriver /usr/bin/
sudo mv geckodriver /usr/local/bin

sudo apt-get install dbus-x11

sudo apt-add-repository ppa:mozillateam/firefox-next

sudo apt-get install firefox xvfb

chmod a+x /home/rodrigocoelho/dotfiles/selenium_worker/collect.sh

if [[ ! -f /tmp/.X10-lock ]]; then
    Xvfb :10 -ac
else
    echo "INFO: $(date) - X Server already running" 1>&2
fi
export DISPLAY=:10

#
##!/usr/bin/env bash
##cat dotfiles/setup/.sudop | sudo -S
#
#mkdir data
#
#apt-get install python-pip
#
#pip install selenium
#
#pip install pyvirtualdisplay
#
#wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
#
#tar -xvzf geckodriver-v0.18.0-linux64.tar.gz
#
#chmod +x geckodriver
#
#chmod 755 geckodriver
#
#mv geckodriver /usr/local/bin
#
#apt-get install dbus-x11
#
#apt-add-repository ppa:mozillateam/firefox-next
#
#apt-get install firefox xvfb
#
#Xvfb :10 -ac &
#
#export DISPLAY=:10
