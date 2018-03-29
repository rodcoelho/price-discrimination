#!/usr/bin/env bash
##cat dotfiles/setup/.sudop | sudo -S
#echo 'a'
#cat dotfiles/setup/.sudop | sudo -S mkdir data
#echo 'b'
#cat dotfiles/setup/.sudop | sudo -S apt-get install python-pip
#echo 'c'
#cat dotfiles/setup/.sudop | sudo -S pip install selenium
#echo 'd'
#cat dotfiles/setup/.sudop | sudo -S pip install pyvirtualdisplay
#echo 'e'
#cat dotfiles/setup/.sudop | sudo -S wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
#echo 'f'
#cat dotfiles/setup/.sudop | sudo -S tar -xvzf geckodriver-v0.18.0-linux64.tar.gz
#echo 'g'
#cat dotfiles/setup/.sudop | sudo -S chmod +x geckodriver
#echo 'h'
#cat dotfiles/setup/.sudop | sudo -S chmod 755 geckodriver
#echo 'i'
#cat dotfiles/setup/.sudop | sudo -S mv geckodriver /usr/local/bin
#echo 'j'
#cat dotfiles/setup/.sudop | sudo -S apt-get install dbus-x11
#echo 'k'
#cat dotfiles/setup/.sudop | sudo -S apt-add-repository ppa:mozillateam/firefox-next
#echo 'l'
#cat dotfiles/setup/.sudop | sudo -S apt-get install firefox xvfb
#echo 'm'
#Xvfb :10 -ac &
#echo 'n'
#export DISPLAY=:10

##!/usr/bin/env bash
#cat dotfiles/setup/.sudop | sudo -S
#echo 'a'
##cat dotfiles/setup/.sudop | sudo -S mkdir data
#echo 'b'
##cat dotfiles/setup/.sudop | sudo -S apt-get install python-pip
#echo 'c'
##cat dotfiles/setup/.sudop | sudo -S pip install selenium
#echo 'd'
##cat dotfiles/setup/.sudop | sudo -S pip install pyvirtualdisplay
#echo 'e'
##cat dotfiles/setup/.sudop | sudo -S wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
#echo 'f'
##cat dotfiles/setup/.sudop | sudo -S tar -xvzf geckodriver-v0.18.0-linux64.tar.gz
#echo 'g'
##cat dotfiles/setup/.sudop | sudo -S chmod +x geckodriver
##echo 'h'
##cat dotfiles/setup/.sudop | sudo -S chmod 755 geckodriver
#echo 'i'
##cat dotfiles/setup/.sudop | sudo -S mv geckodriver /usr/local/bin
#echo 'j'
##cat dotfiles/setup/.sudop | sudo -S apt-get install dbus-x11
#echo 'k'
##cat dotfiles/setup/.sudop | sudo -S apt-add-repository ppa:mozillateam/firefox-next
#echo 'l'
##cat dotfiles/setup/.sudop | sudo -S apt-get install firefox xvfb
#echo 'm'
Xvfb :10 -ac &
#echo 'n'
export DISPLAY=:10