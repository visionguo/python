#!/bin/bash
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    entrypoint
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

function run
    """
    run
    """
{
    gunicorn -c gunicorn_conf.py run:app
}

function stop
    """
    stop
    """
{
    kill -9 `ps aux |grep gunicorn |grep treant |awk '{ print $2 }'`
}

if [ "$1" = "run" ]; then
    run
fi

if [ "$1" = "stop" ]; then
    stop
fi

