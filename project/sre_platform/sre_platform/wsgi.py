#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/07/15
# Brief:
#    wsgi
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

"""
WSGI config for sre_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sre_platform.settings")
application = get_wsgi_application()
