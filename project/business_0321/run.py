#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    run
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import os
from flask_bootstrap import Bootstrap
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

bootstrap = Bootstrap(app)

if __name__ == '__main__':
    print("app-start")
    app.run() 




