#!/usr/bin/env python

from flask import Flask     # 导出falsk类
app = Flask(__name__)       # 生成一个web app对象

@app.route('/')             #注册一个url, 表示当请求 url + '/' 这个网址时，执行 hello_world这个函数
def hello_world():
    #return 'leoguo NB!'    #hello world返回的信息传递到浏览器上
    return 'Leo.G'

if __name__ == '__main__':
    app.run()               #启动 app应用
                            #相关参数：app.run（host=None, port=None, debug=None）
                            # debug：当有代码更新时，不用重启web app