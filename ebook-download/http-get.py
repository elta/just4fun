#! /usr/bin/python3.3

import urllib.request,io,os,sys
from html.parser import HTMLParser
from optparse import OptionParser  

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.values = []
        self.cache_tag = 0

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                self.cache_tag = 1
                for (variable, value)  in attrs:
                    if variable == "href":
                        self.links.append(value)

    def handle_data(self, data):
        if self.cache_tag == 1:
            self.values.append(data)

        self.cache_tag = 0

def log(log=str()):
    f = open("http-get.log", "a", 1, "gbk")
    f.write(log + "\n")
    f.close()


def download(opener, site=str(), href=str(), fullname=str()):
    log("Current url is " + site + "/" + href)

    try:
        x = opener.open(site + "/" + href)
        s=x.read()
    except:
        log("Web access error, url is " + site + "/" + href)
        log("Web access error, fullname is " + fullname)
        return

    if href[-1:] == '/':    # Floder
        s=s.decode('utf-8','ignore')

        hp = MyHTMLParser()
        hp.feed(s)
        hp.close()

        # Create dir path
        # mkdir 'fullname'
        os.makedirs(fullname)
        log("Create dir: " + fullname)

        for i in range(0, len(hp.links)):
            if hp.values[i].startswith('[To'):
                continue
            else:
                download(opener, site, hp.links[i].strip(), fullname + "/" + hp.values[i].strip())
    else:
        log("Save file: " + fullname)
        f = open(fullname, "ab")
        f.write(s)
        f.close()

if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options]")  
    parser.add_option("-s", "--site",  
                    action = "store",  
                    type = 'string',  
                    dest = "site",  
                    default = None,  
                    help="Specify site you want to download"  
                    )  
    parser.add_option("-u", "--username",  
                    action = "store",  
                    type = 'string',  
                    dest = "user",  
                    default = None,  
                    help="Specify username"  
                    )  
    parser.add_option("-p", "--password",  
                    action = "store",  
                    type = 'string',  
                    dest = "passwd",  
                    default = None,  
                    help="Specify password"  
                    )  
    (options, args) = parser.parse_args()  
    site=options.site
    username=options.user
    password=options.passwd

    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, site, username, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

    opener = urllib.request.build_opener(handler)

    site_parser = site.split("://")
    top_dir = ""
    
    if len(site_parser) == 1:
        top_dir = site_parser[0]
    else:
        top_dir = site_parser[1]


    download(opener, site, "/", sys.path[0]+'/' + top_dir)

