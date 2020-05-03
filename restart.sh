#!/bin/bash
docker ps | grep "healthy)" > grep.txt
python restart_script.py
