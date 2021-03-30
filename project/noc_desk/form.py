#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/03/22
# Brief:
#    form
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

"""
定义一个类：noc格式版本
"""
class EditForm(FlaskForm):
    case_id = StringField(u'故障编号', validators=[
                DataRequired(message= u'编号不能为空'), Length(1, 64)])
    case_title = StringField(u'故障标题', validators=[
                DataRequired(message= u'编号不能为空'), Length(1, 256)])
    case_desc = StringField(u'事件概述')
    case_time = StringField(u'故障时间')
    case_level = StringField(u'故障级别')
    case_affect = StringField(u'故障影响')
    case_process = StringField(u'故障过程回顾')
    improve = StringField(u'改进计划')
    submit = SubmitField(u'提交')