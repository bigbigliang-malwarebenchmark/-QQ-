import urllib, urllib2, sys
import ssl
import re

host = 'https://himobile.market.alicloudapi.com'
path = '/query'
method = 'GET'
appcode = 'fd9700aba68f4af4ad0213e716960775'

file = open('telephone.txt')
f = open('write.txt','w+')
patter = '{"ret":\d+'
pattern = '{"ret":200,"data":{"code":\d+'
for line in file:
	line = line.strip('\n') 
	querys = 'number=' + str(line)
	#print querys
	bodys = {}
	url = host + path + '?' + querys

	request = urllib2.Request(url)
	request.add_header('Authorization', 'APPCODE ' + appcode)
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	response = urllib2.urlopen(request, context=ctx)
	content = response.read()
	#print re.match(patter,content).group() == '{"ret":200'
	if (re.match(patter,content).group()== '{"ret":200'):
		#print content
		a = re.match(pattern,content).group()
		#print a
		if ( a == '{"ret":200,"data":{"code":5') or (a == '{"ret":200,"data":{"code":1'):
			f.write(line)
			f.write('\n')
			#print a
file.close()
f.close()