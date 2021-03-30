#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    c4log
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import logging.handlers

def LogInfo(value):
    InfoLog = r''
    handler = logging.handlers.RotatingFileHandler(InfoLog, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')
    fmt = '%(asctime)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)
    logger = logging.getLogger('test')
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.info(value)