#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2021/03/22
# Brief:
#    noclist
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

from mysql import query_db, modify_db
import re
from models.models import User, NocImprovement, NocAffected, NocNoc, NocPriority, NocReasons
from models.models import db
import json

def finish_rate(case_id):
    """
    完成速率
    """
    sql="select * FROM noc WHERE `serial_number` = '"+str(case_id)+"'"
    try:
        finish_field_num = 0
        noc_info = db.session.query(NocNoc).filter(NocNoc.serial_number == case_id).first().as_dict()
        print(noc_info)
        affected_info = db.session.query(NocAffected).filter(NocAffected.nid == noc_info["id"]).all()
        if len(affected_info) != 0:
            finish_field_num += 1
        imp_info = db.session.query(NocImprovement).filter(NocImprovement.nid == noc_info["id"]).all()
        if len(imp_info) != 0:
            finish_field_num += 1
        del noc_info["id"]
        del noc_info["status"]

        for i in noc_info:
            if not re.match(r'None|0000-00-00', str(noc_info[i])):
                finish_field_num+=1
        print(finish_field_num)

    except Exception as e:
        db.session.rollback()
        print(e)
        raise
    finally:
        db.session.close()

    finish_rate=finish_field_num/16*100
    return finish_rate