#!/bin/bash
mkdir datasets
mkdir tempaudio
mkdir data
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get install python3
sudo apt-get -y install python3-pip
sudo pip3 install -r requirements.txt
sudo apt-get install python-matplotlib
sudo apt-get install python3-pyaudio
sudo pip3 install opencv-python
sudo pip3 install opencv-contrib-python