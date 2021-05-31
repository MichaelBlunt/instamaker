#!/bin/bash

#get prereqs
apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4

apt install python3
apt install pip3
pip3 install selenium

#get chromium-browser
curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
apt-get -y update
apt-get -y install google-chrome-stable

#chromedriver
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver

#get account code 
mkdir /tmp/mikel
wget https://raw.githubusercontent.com/MichaelBlunt/instamaker/main/instagram_account_maker.py > /tmp/mikel/instagram_account_maker.py
