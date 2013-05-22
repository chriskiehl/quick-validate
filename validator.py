import os
import sys
import time
import urllib
import urllib2
import inspect
from bs4 import BeautifulSoup


def _save_results_page(filename):
	with open(filename, 'wb') as f:
		f.write(response.read())

def _load_results_to_soup(filename):
	with open('valid.html', 'rb') as f:
		return BeautifulSoup(f.read())

def post_html_to_validator(html_file):
	url = 'http://validator.w3.org/check'

	params = {
		'uploaded_file': open(html_file).read(),
		'charset':'(detect automatically)',
		'doctype':'Inline',
		'group':'0'
	}

	payload = urllib.urlencode(params)
	req = urllib2.Request(url, data=payload)
	return urllib2.urlopen(req)

def is_valid(soup):
	result = soup.find('h2', {'class':'valid'}) 
	return True if result is not None else False

def show_errors(soup):
	error_loop = soup.find('ol', {'id':'error_loop'})
	errors = [i.get_text().replace('\n', '').encode('ascii', 'ignore') 
		for i in error_loop.find_all('li')]
	
	return [' '.join(i.split()) for i in errors]


def get_file_list(files = None, directory=os.getcwd()):
	if files is None: files = []
	for i in os.listdir(directory):
		if os.path.isdir(os.path.abspath(directory + '\\'  + i)):
			get_file_list(files, os.path.abspath(directory + '\\' + i))
			continue
		if '.html' in i: #eventually support css
			files.append(os.path.abspath(directory) + '\\' + i)
	return files

if __name__ == '__main__':
	if len(sys.argv) > 1:
		file_list = sys.argv[1:]
	else:
		file_list = get_file_list()

	for f in file_list:
		if 'html' not in f:
			continue
		filename = f.split('\\')[-1]
		print 'Validating', filename
		result = post_html_to_validator(f)
		soup = BeautifulSoup(result.read())

		if is_valid(soup):
			print 'Passed all checks! No issues found with', filename
			print 
			continue 
		# Errors found
		print 'Errors found with file', filename
		print 'File location:', f
		for error in show_errors(soup):
			print error
		print 
		time.sleep(.6)
