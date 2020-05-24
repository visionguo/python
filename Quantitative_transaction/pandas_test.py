#!/usr/bin/env python
# -*- encoding:UTF-8 -*-

import numpy as np
import pandas as pd

#s = pd.Series([-1.0,-1.5,1,1.5],index=["a","b","c","d"])
s = pd.Series(["a",-1.5,1,1.5],index=["a","b","c","d"])

#dtype 指定为int8
s = pd.Series([-1.0,-1.5,1,1.5],index=["a","b","c","d"],dtype='int8')

#ndarray 数据类型创建Series对象
s = pd.Series(np.random.randn(4),index=["a","b","c","d"])

#以字典作为数据类型创建Series对象
s = pd.Series({'a':0,'b':1,'c':2},index=["a","b","e","a"])

#以常量值为数据类型创建Series对象
s = pd.Series(5.,index=["a","b","c","d"])
print (s)
