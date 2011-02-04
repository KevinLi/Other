#!usr/bin/env python

#- Challenge/socklist.py -#
#- Written by Cam1337    -#
#- Revised Feb.1.2011    -#
#- Congrats banhammer :) -#

import urllib2

_url = "http://sockslist.net/"
_page =  urllib2.urlopen(_url).read()
_inc_num = int(_page.split("{ostr+=String.fromCharCode(")[1].split("+parseInt")[0])
_data_page = _page.split("<div id=\"proxylist\"></div>")[1].split("<!-- <th>Whois</th> -->")[1].split("</table>")[0].split("<tr>")[1:]

IP = "IPs"
PORT = "PORTs"

decrypt = lambda _string_: "".join([chr(int(i)+_inc_num) for i in _string_.split(",")])

DATA = {
		IP : [i.split('<td class="t_ip">')[1].split("</td>")[0] for i in _data_page],
		PORT : [decrypt(i.split('<td class="t_port">')[1].split("</td>")[0]) for i in _data_page]
		}

for i in DATA[IP]:
	mIP, mPORT = i, DATA[PORT][DATA[IP].index(i)]
	print "%s:%s" % (mIP, mPORT)