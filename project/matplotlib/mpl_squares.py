#!/usr/bin/env python
# -*- coding:utf-8 -*-

import matplotlib
matplotlib.use('TkAgg')

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import matplotlib.pyplot as plt     #导入模块pyplot,并指定别名plt

# squares = [1,4,9,16,25]
# plt.plot(squares)
# plt.show()

import numpy as np
import pandas as pd
import matplotlib
import pylab
from matplotlib.font_manager import FontManager, FontProperties
import subprocess
import matplotlib.pyplot as plot


def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')


if __name__ == '__main__':
    plot.title(u"你大爷就是你大爷", fontproperties=getChineseFont())
    plot.show()


