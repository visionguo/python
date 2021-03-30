#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    models/__init__.py
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

__all__ = ['User', 'Groups', 'Department']

from .user import User
from .group import Groups
from .department import Department
