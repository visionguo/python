#!/usr/bin/env python

import re
import subprocess

def check_alive(ip,count=1,timeout=1):
    cmd ='ping -c %d -w %d %s' % (count,timeout,ip)
    p = subprocess.Popen(cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
 
    result = p.stdout.read()
    regex = re.findall('100% packet loss',result)
    if len(regex) == 0:
        print "\033[31m%s UP\033[0m" % (ip)
    else:
        print "\033[32m%s DOWN\033[0m" % (ip)
 
 
if __name__ == "__main__":
 
        with file('/Users/guoshaogang/ping.txt','r') as f:
                for line in f.readlines():
                        ip = line.strip()
                        check_alive(ip)

#for example
#ping.txt
#10.16.208.1
