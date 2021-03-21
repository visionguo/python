#!/usr/bin/python
#coding:utf-8
import StringIO
import pycurl
import sys
import os
class urlpass:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + buf
def urlgzip(input_url):
    t = urlpass()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)#响应代码
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)#远程服务器连接时间
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)#连接上后开始传输的时间
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)#接收第一个字节的时间
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)#上一请求总时间
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)#下载数据大小
    #print 'http_code http_size conn_time pre_tran start_tran total_time'
    return "http_code:%d,http_size:%d,conn_time:%f,pre_tran:%f,start_tran:%f,total_time:%f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time)
if __name__ == '__main__':
    #input_url = sys.argv[1]
    input_url='http://www.testurl.com'
    urlinfo=urlgzip(input_url)
    print type(urlinfo)
    print urlinfo
pycurl.NAMELOOKUP_TIME 域名解析时间
pycurl.CONNECT_TIME 远程服务器连接时间
pycurl.PRETRANSFER_TIME 连接上后到开始传输时的时间
pycurl.STARTTRANSFER_TIME 接收到第一个字节的时间
pycurl.TOTAL_TIME 上一请求总的时间
pycurl.REDIRECT_TIME 如果存在转向的话，花费的时间
 
pycurl.EFFECTIVE_URL
pycurl.HTTP_CODE HTTP 响应代码
pycurl.REDIRECT_COUNT 重定向的次数
pycurl.SIZE_UPLOAD 上传的数据大小
pycurl.SIZE_DOWNLOAD 下载的数据大小
pycurl.SPEED_UPLOAD 上传速度
pycurl.HEADER_SIZE 头部大小
pycurl.REQUEST_SIZE 请求大小
pycurl.CONTENT_LENGTH_DOWNLOAD 下载内容长度
pycurl.CONTENT_LENGTH_UPLOAD 上传内容长度
pycurl.CONTENT_TYPE 内容的类型
pycurl.RESPONSE_CODE 响应代码
pycurl.SPEED_DOWNLOAD 下载速度
pycurl.SSL_VERIFYRESULT
pycurl.INFO_FILETIME 文件的时间信息
 
pycurl.HTTP_CONNECTCODE HTTP 连接代码
pycurl.HTTPAUTH_AVAIL
pycurl.PROXYAUTH_AVAIL
pycurl.OS_ERRNO
pycurl.NUM_CONNECTS
pycurl.SSL_ENGINES
pycurl.INFO_COOKIELIST
pycurl.LASTSOCKET
pycurl.FTP_ENTRY_PATH
 
发微信告警
#!/usr/bin/python
#coding:utf-8
import StringIO
import pycurl
import sys
import os
import requests
import json
class urlpass:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + buf
def urlgzip(input_url):
    t = urlpass()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)#响应代码
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)#远程服务器连接时间
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)#连接上后开始传输的时间
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)#接收第一个字节的时间
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)#上一请求总时间
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)#下载数据大小
    #print 'http_code http_size conn_time pre_tran start_tran total_time'
    return "状态码:%d,页面下载大小KB:%d,连接时间秒:%f,开始传输时间:%f,总时长秒:%f"%(http_code,http_size,http_conn_time,http_start_tran,http_total_time)
 
def get_token():
 
  url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
  values = {'corpid' : 'weixin corpid' ,
      'corpsecret':'weixin token',
       }#asia monitor
  req = requests.post(url, params=values)
  data = json.loads(req.text)
  return data["access_token"]
 
def send_msg(info01):
  url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
  values = """{"touser" : "1" ,
      "toparty":"1",
      "msgtype":"text",
      "agentid":"1",
      "text":{
        "content": "新加坡API:{%s}"
      },
      "safe":"0"
      }""" %(info01)
 
  data = json.loads(values)
  req = requests.post(url, values)
 
if __name__ == '__main__':
    #input_url = sys.argv[1]
    input_url='http://www.test.com'
 
    urlinfo=urlgzip(input_url)
    send_msg(urlinfo)
    print type(urlinfo)
    print urlinfo

##
g1-g3-op-v01
/home/sa
g1-g3-op-v02

#!/usr/bin/env python
#coding:utf-8

import StringIO
import pycurl
import sys
import os
import time
import json
import socket
import urllib
import traceback

class urlpass:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + buf

def urlgzip(input_url):
    t = urlpass()
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.PROXY, 'g1-g3-op-v01:7000/healthcheck')
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()


    http_code      = c.getinfo(pycurl.HTTP_CODE)          #响应代码

    url_monitor = {
        'http_code':      [http_code, 'GAUGE'],
    }

    output = []
    for key in url_monitor:
        s = {}
        s['endpoint'] = socket.gethostname()
        s['timestamp'] = int(time.time())
        s['step'] = 60
        s['counterType'] = url_monitor[key][1]
        s['metric'] = 'g1-g3-op-v01:7000/healthcheck'
        s['value'] = url_monitor[key][0]
        output.append(s)
    return output

if __name__ == "__main__":
    input_url ='http://g1-g3-op-v01:7000/healthcheck'
    urlinfo=urlgzip(input_url)
    print json.dumps(urlinfo)
    sys.stdout.flush()

