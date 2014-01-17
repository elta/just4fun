#! /usr/bin/python3.3

# Download ebook from website
# Only support http://www.yi-see.com/
# Two arguments, 1st is the web-url of chaptor list .

import urllib.request,io,os,sys

def get_cleanContent(s=str):
    while s.find("<embed") != -1:
        em_s = s[s.find("<embed"):s.find("</embed>") + len("</embed>")]
        s = s.replace(em_s, "")
    while s.find("<em") != -1:
        em_s = s[s.find("<em"):s.find("</em>") + len("</em>")]
        s = s.replace(em_s, "")
    while s.find("<a") != -1:
        em_s = s[s.find("<a"):s.find("</a>") + len("</a>")]
        s = s.replace(em_s, "")
    s = s.replace("<br />", "")
    return s

def get_content(s=str):
    str1 = s.replace(">", ">\n")
    cont = str("")
    p = ""
    while str1.find("<p>") != -1:
        p = str1[str1.find("<p>") + len("<p>"):str1.find("</p>")]
        str1 = str1[str1.find("</p>") + len("</p>"):]
        p = get_cleanContent(p)
        if p.__contains__("&#169;"):
            break
        cont = cont + p
    return cont

def get_item(s=str):
    item_s = s[s.find("<item>"):s.find("</item>") + len("</item>")]
    title = item_s[item_s.find("<title>")+len("<title>"):item_s.find("</title>")]
    content = item_s[item_s.find("<content:encoded>") + len("<content:encoded>"):item_s.find("</content:encoded>")]
    print("=====" + title + "=====")
    content = get_content(content)
    print(content)
    return item_s


req=urllib.request.Request("http://feeds.feedburner.com/jandan/vip")
f=urllib.request.urlopen(req)
s=f.read()
s=s.decode('utf-8','ignore')

str1 = str(s)
item_s = get_item(str1)
while item_s != None and not item_s.__eq__(""):
    str1 = str1.replace(item_s, "")
    item_s = get_item(str1)

file = open("jandan.html", "a", 1, 'utf-8')
file.write(str1)
file.close()
