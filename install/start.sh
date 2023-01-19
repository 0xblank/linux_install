#!/bin/bash

apt update -y
apt install python3 -y
python3 /install/install.py
apt upgrade -y
apt autoremove -y