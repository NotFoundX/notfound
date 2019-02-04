#!/usr/bin/env python
#
#LXNotFound
import urllib, urllib2

aut_h = urllib2.HTTPBasicAuthHandler()
aut_h.add_password("real", "host", "usuario", "password")

opener = urllib2.build_opener(aut_h)
urllib2.install_opener(opener)

f = urllib2.urlopen("http://www.python.org"
)
proxy_h = urllib2.ProxyHandler({"http" : "http://miproxy.net:123"})

opener = urllib2.build_opener(proxy_h)
urllib2.install_opener(opener)

f = urllib2.urlopen("http://www.python.org")

cookie_h = urllib2.HTTPCookieProcessor()

opener = urlliv2.build_opener(cookie_h)
urllib2.install_opener(opener)

f = urllib2.urlopen("http://www.python.org")

