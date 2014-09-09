import urllib

str1 = "this is sample string"

print urllib.quote_plus("http://www.yahoo.com/")
print urllib.quote_plus("Kruder & Dorfmeister")


q_str = urllib.quote_plus(str1)

print q_str


print urllib.unquote_plus(q_str)


# -*- coding: utf-8 -*-

s1 = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

print s1

s2 = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

print s2
