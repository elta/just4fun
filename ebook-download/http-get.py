#! /usr/bin/python3.3

import urllib.request,io,os,sys

site=''
url=site
username=''
password=''

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, site, username, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(handler)
x = opener.open(site)
s=x.read()
s=s.decode('utf-8','ignore')
print(s)

file=open('a.html', 'a', 1, 'gbk')
file.write(str(s))
file.close()
