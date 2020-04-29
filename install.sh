#!/usr/bin/env bash

echo "CREATING VENV"
sudo apt-get install -y software-properties-common \
  python-pip python3.7 python3 python-dev python3-dev \
  python-pip python3.7-dev virtualenv gunicorn
virtualenv -p python3.7 venv

# echo "SOURCE ACTIVATE AND PIP INSTALL REQUIREMENTS"
# source venv/bin/activate

pip install -r requirements.txt

echo "DONE"
