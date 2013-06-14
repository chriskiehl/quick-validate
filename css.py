import os
import sys
import time
import urllib
import urllib2
import inspect
from bs4 import BeautifulSoup
import mechanize

def post_css_to_validator(f):
	url = 'http://jigsaw.w3.org/css-validator/#validate_by_upload'

	br = mechanize.Browser()
	br.addheaders = [('User-agent', 
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22' 
		'(KHTML, like Gecko) Chrome/25.0.1364.172 Safari/537.22')]
	br.set_handle_robots(False)
	br.open(url)
	br.select_form(nr=1)
	br.set_all_readonly(False)    
	br.form.set_all_readonly(False)    
	br.form.add_file(open(f), 'text/css')

	return br.submit()

def is_valid(soup):
	results_container = soup.find('div', {'id':'results_container'})
	results = results_container.find('div', {'id':'errors'})
	return True if results is None else False

def validate(f):
	filename = f.split('\\')[-1]
	results = post_css_to_validator(filename)
	soup = BeautifulSoup(results.read())

	if is_valid(soup):
		print 'Passed all checks! No issues found with', filename
		print 
		return
	# Errors found
	print
	print 'Errors found with file', filename
	print
	print 'File location:', f
	for error in get_errors(soup):
		print error
		print
	print 
	time.sleep(.6)

def get_errors(soup):
	LINE_NUM, CODE, ERROR = range(3)
	error_msgs = []
	table_rows = soup.find('div', {'class':'error-section'}).find('table').find_all('tr')
	for row in table_rows:
		data = row.find_all('td')

		line = data[LINE_NUM].get_text().encode('ascii')
		code = data[CODE].get_text().encode('ascii')
		error =  ' '.join(data[ERROR].get_text().encode('ascii').split())
		
		error_msgs.append(''.join([line, code, error]))
	return error_msgs



if __name__ == '__main__':
	# result = post_css_to_validator('css.css')
	# with open('CSS_RESULTS.html', 'wb') as f:
	# 	f.write(result.read())

	with open('CSS_RESULTS.html') as f:
		soup = BeautifulSoup(f.read())





















