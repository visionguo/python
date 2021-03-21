#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Auther:VisionGuo
# Date:2018/08/29
# Brief:
#    mythread
# Globals:
#    None
# Returns:
#    succ:0
#    fail:1

import threading

class MyThread(threading.Thread):
    """
    Define MyThread
    """
    def __init__(self,func,args=()):
        super(MyThread,self).__init__()
        self.func = func
        self.args = args

    def run(self):
        """
        Define run
        """
        self.result = self.func(*self.args)

    def get_result(self):
        """
        Get result
        """
        try:
            return self.result    #如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception:
            return None