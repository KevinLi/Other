#!/usr/bin/env python

import urllib

IP = []
Ports = []
Ports2 = []

html = urllib.urlopen("http://sockslist.net/").readlines()

for i in html:
	if "<td class=\"t_ip\">" in i:
		IP.append(i.split("<td class=\"t_ip\">")[1].split("</td>")[0])
	elif "<td class=\"t_port\">" in i:
		i = i.split("<td class=\"t_port\">")[1].split("</td>")[0]
		Ports.append(i)
	elif "fromCharCode" in i:
		num = int(i.split("Code(")[1].split("+parseInt")[0])

# Decrypting? the port numbers
for port in Ports:
	ps = port.split(",")
	ostr = ""
	for x in range(0,len(ps)):
		ostr += chr(num+int(ps[x]))
	Ports2.append(ostr)

for x in range(0,len(IP)):
	print(IP[x])
	print(Ports2[x])
	print("")
