#!/bin/bash
docker ps | grep "healthy)" > grep.txt
python ubuntu_server_1/restart_script.py
