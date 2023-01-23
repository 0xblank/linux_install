#!/bin/bash

apt update -y
apt install python3 -y
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
python3 $SCRIPT_DIR/install.py
apt upgrade -y
apt autoremove -y