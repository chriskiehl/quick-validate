'''
Quick script to validate all the HTML files in current directory
via the W3C validator. 

Current profesor gives zeros for non-validating html... this 
provides a bit of quick, easy final assurance before project 
submittal.
'''


import os
import sys
import css
import time
import html

import inspect
from bs4 import BeautifulSoup


def _save_results_page(filename):
	with open(filename, 'wb') as f:
		f.write(response.read())

def _load_results_to_soup(filename):
	with open('valid.html', 'rb') as f:
		return BeautifulSoup(f.read())

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
		if 'html' not in f and 'css' not in f:
			continue
		filename = f.split('\\')[-1]
		print 'Validating', filename
		if 'html' in filename.split('.')[-1].lower():
			html.validate(f)
		else:
			css.validate(f)

	user_wait = raw_input("Press any key to exit. ")
	if user_wait == '\n':
		sys.exit()
