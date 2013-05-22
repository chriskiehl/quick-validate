import os
import sys
import time
import urllib
import urllib2
import inspect
from bs4 import BeautifulSoup
import mechanize

url = 'http://jigsaw.w3.org/css-validator/validator'

params = {
	'text': open('css.css').read(),
	'profile':'css3',
	'usermedium':'all',
	'warning':'1',
	'vextwarning':'',
	'lang':'en'
}

# br = mechanize.Browser()
# br.open(url)
# br.set_handle_robots(False)
# br.select_form(nr=1)
# br.set_all_readonly(False)    
# br.form.set_all_readonly(False)    
# br.form['file'] = open('css.css').read()

# br.submit()

# print br.response().read()


agent = ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.31 '
		'(KHTML, like Gecko) Chrome/26.0.1410.43 Safari/537.31')

headers = {'User-Agent' : agent}
payload = urllib.urlencode(params)
req = urllib2.Request(url, headers=headers, data=payload)
response = urllib2.urlopen(req)
print response.read()
# with open('cssv_invalid.html','wb') as f:
# 	f.write(response.read())

