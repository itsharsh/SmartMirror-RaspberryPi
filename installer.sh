#!/bin/bash
sudo mkdir datasets
sudo mkdir tempaudio
sudo mkdir data
sudo apt autoremove -y
sudo apt-get update -y
sudo apt update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install python3 -y
sudo apt-get -y install python3-dev python3-pip
sudo apt-get install python-matplotlib -y
sudo apt-get install python3-pyaudio -y
sudo apt-get install libhdf5-dev libhdf5-serial-dev -y
sudo apt-get install libqtwebkit4 libqt4-test -y
sudo apt install libjasper1 -y
sudo apt-get install libatlas-base-dev -y
sudo apt-get install python3-opencv -y
sudo apt-get install libatlas-base-dev -y
sudo apt install virtualenv python3-virtualenv -y

sudo pip3 install -r requirements.txt
