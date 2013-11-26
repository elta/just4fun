#! /usr/bin/python3.3

# Download ebook from website
# Only support http://www.yi-see.com/
# Two arguments, 1st is the web-url of chaptor list .

import urllib.request,io,os,sys

if len(sys.argv) < 3:
    print("Usage: cmd website output-file [,startchap [,endchap]]")
    exit(-1)

site = sys.argv[1]
ofile = sys.argv[2]

startchap = 0
endchap = 100000

if len(sys.argv) >= 4:
    startchap = int(sys.argv[3]) - 1
if len(sys.argv) >= 5:
    endchap = int(sys.argv[4])

if startchap >= endchap:
    print("Start chap should less than endchap")
    exit(-1)

req=urllib.request.Request(site)
site = site[:site.rfind("/")]
f=urllib.request.urlopen(req)
s=f.read()
s=s.decode('gbk','ignore')

str1 = str(s)
str1 = str.lower(str1)

lists = list()

while str1.find("<a href") != -1:
    if str1[str1.find("<a href"):str1.find("</a>")].find("read") != -1:
        str2 = str1[str1.find("<a href"):str1.find("</a>")]
        strurl = str2[str2.find("read"):str2.find("html") + 4]
        strchap = str2[str2.find(">") + 2:-1] # Chaptor number

        lists = lists.__add__([[int(strchap),strurl]])

    str1 = str1[(str1.find("</a>") + 4):]

# Sort list, then download each chaptor as you wish.
lists = sorted(lists)

mdir=sys.path[0]+'/'
file=open(mdir+ofile,'a',1,'gbk')

if endchap > len(lists):
    endchap = len(lists)

if startchap >= endchap:
    print("Start chap should less than endchap")
    exit(-1)

for i in range(startchap, endchap, 1):
    print("Loading 第" + str(lists[i][0]) + "章 : " + site + "/" + lists[i][1])
    req=urllib.request.Request(site + "/" + lists[i][1])
    f=urllib.request.urlopen(req)
    s=f.read()
    s=s.decode('gbk','ignore')
    strsep = s.splitlines()
    s = strsep[41]
    s = str.lower(s)
    s = s.replace("<br>", "\n")
    s = s.replace("</td>", "")
    s = s.replace("</tr>", "")
    s = s.replace("</table>", "")
    file.write("第" + str(lists[i][0]) + "章\n")
    file.write(s)
    file.write("\n")

file.write(s)
file.close()
