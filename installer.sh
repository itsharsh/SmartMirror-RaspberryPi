#!/bin/bash
mkdir datasets
mkdir tempaudio
mkdir data
sudo apt autoremove -y
sudo apt-get update -y
sudo apt update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install python3 -y
sudo apt-get -y install python3-dev python3-pip
sudo pip3 install -r requirements.txt
sudo apt-get install python-matplotlib -y
sudo apt-get install python3-pyaudio -y
sudo apt-get install libhdf5-dev libhdf5-serial-dev -y
sudo apt-get install libqtwebkit4 libqt4-test -y
sudo apt-get install python3-opencv -y