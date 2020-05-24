#!/usr/bin/env python
#coding:utf-8

import socket

def URL2IP():
   for oneurl in urllist.readlines():
       url=str(oneurl.strip())[7:]
       print url
       try:
           ip =socket.gethostbyname(url)
           print ip
           iplist.writelines(str(ip)+"\n")
       except:
           print "this URL 2 IP ERROR "

try:
    urllist=open("/Users/guoshaogang/ping.txt_dns_1","r")
    iplist=open("/Users/guoshaogang/ping.txt","w")
    URL2IP()
    urllist.close()
    iplist.close()
    print "complete !"
except:
    print "ERROR !"

#for example
#ping_domain.txt 
#http://m-jrpre.guazi.com

