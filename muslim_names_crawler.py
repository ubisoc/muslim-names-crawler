#!/usr/bin/env python
import urllib2
from bs4 import BeautifulSoup

def main():
	boys_limit = 265
	boys_url = 'http://www.muslimnames.info/baby-boys/islamic-boys-names-'
	girls_limit = 243
	girls_url = 'http://www.muslimnames.info/baby-girls/islamic-girls-names-'
	output_file = open('names.txt', 'a')
	selector = 'boys'

	c = 1
	c_url = boys_url
	for i in range(1, girls_limit + boys_limit):
		if c > boys_limit:
			c = 1
			c_url = girls_url
			selector = 'girls'

		response = urllib2.urlopen(c_url + str(c) + '/')
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		for link in [link.string for link in soup.select('div.nrow_name.' + selector + ' a')]:
			output_file.write('%s\n' % link)

		c = c + 1
		

if __name__ == '__main__':
	main()