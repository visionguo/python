#!/bin/bash
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    prepare
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

if [[ -d venv ]]; then
    rm -rf venv
fi
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r pip-req.txt

