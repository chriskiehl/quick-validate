import urllib
import urllib2
from bs4 import BeautifulSoup


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

def get_errors(soup):
	error_loop = soup.find('ol', {'id':'error_loop'})
	errors = [i.get_text().replace('\n', '').encode('ascii', 'ignore') 
		for i in error_loop.find_all('li')]
	
	return [' '.join(i.split()) for i in errors]


def validate(f):
	filename = f.split('\\')[-1]
	result = post_html_to_validator(f)
	soup = BeautifulSoup(result.read())

	if is_valid(soup):
		print 'Passed all checks! No issues found with', filename
		print 
		return
	# Errors found
	print 
	print 'Errors found with file', filename
	print 'File location:', f
	print
	for error in show_errors(soup):
		print error
	print 
	time.sleep(.6)







