#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/06/01
# Brief:
#    raidtype
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = ['RaidType']

class RaidType(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('Raid类型'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

    class Meta:
        db_table = 'raidtype'
        ordering = ['name']