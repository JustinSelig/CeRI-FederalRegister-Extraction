#extract.py
#Justin Selig, June 30, 2014
#Cornell eRulemaking Initiative

from constants import *
import xlrd
import xlwt
import xlutils
import urllib2

"""Returns html contents of a web page as a list.
Precondition: url is a url string or unicode."""
def get_webpage(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	result = []
	while True:
		line = response.readline()
		if '</html>' in line: #at end of site
			break
		result.append(line)
	return result
	
"""Returns a list of html lines containing the string 'Executive Summary'
Precondition: webpage is a list of html elements."""
def find_string(webpage):
	matching = []
	matching = [line for line in webpage if 'Executive Summary' in line]
	return matching
	
"""Returns a list with only html elements containing headers.
Precondition: html_list is a list of html elements scrubbed to contain
the string 'Executive Summary'"""
def clean_info(html_list):
	result = []
	for element in html_list:
		if 'h1' in element or \
			'h2' in element or \
			'h3' in element or \
			'h4' in element or \
			'h5' in element or \
			'h6' in element:
			result.append(element)
	return result
	
"""Returns a list containing the starting locations (line numbers) of each 
relevant heading.
Precondition: html_list is a cleaned list of html elements with only headers,
site is a Webpage object containing the entire webpage content"""
def get_line_numbers(html_list, site):
	result = []
	for element in html_list:
		line_number = site.content.index(element)
		result.append(line_number)
	return result
	
############################### Sections Found ################################

"""Given a list of html tags representing a site (content), method extracts the
relevant text in subsections under the 'Executive Summary' heading.
Precondition: content is a list of html tags representing the web page, 
start_line is an integer."""
def get_relevant_text(content, start_line):
	result = []
	heading_num = get_heading_num(content[start_line])
	for line in range(start_line+1, len(content)):
		element = content[line]
		if ('[' in element and ']' in element) and (element.strip().index('[') == 0) :
			result.append(element)
		if '<h' in element or \
			'<p' in element or \
			'<s' in element or \
			'<i' in element or \
			'<li' in element:
			if '<h' in element:
				if heading_num < get_heading_num(element):
					result.append(element)
				else:
					break
			elif '<p' in element or \
				'<s' in element or \
				'<i' in element or \
				'<li' in element:
				result.append(element)
		else:
			continue
	return result

"""Returns the heading number of an html tag given an element.
Precondition: element is a string representing an html tag with a header."""
def get_heading_num(element):
	return int(element[element.index('<h')+2])