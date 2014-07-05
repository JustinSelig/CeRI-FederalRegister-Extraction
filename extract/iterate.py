#iterate.py
#Justin Selig, June 30, 2014
#Cornell eRulemaking Initiative

from extract import *
from constants import *
import xlrd
import xlwt
import xlutils
import urllib2
import sys
from HTMLParser import HTMLParser
import xlutils.copy
import os.path

#Opens excel spreadsheet containing urls
FILE = raw_input("Enter File: ").replace('"', '') #quotes must be removed to read file
WORKBOOK = xlrd.open_workbook(FILE)
READ_SHEET = WORKBOOK.sheet_by_index(SHEET0)

#Opens excel spreadsheet for editing
WORKSHEET = xlutils.copy.copy(WORKBOOK)
WRITE_SHEET = WORKSHEET.get_sheet(0)
	
def main():
	file_count = 0
	for row in range(1, READ_SHEET.nrows):
		#opens webpage, finds 'Executive Summary' content
		url = READ_SHEET.cell_value(row, COL0)
		webpage = get_webpage(url)
		site = Webpage()
		site.setContent(webpage)
		info = find_string(webpage)
		cleaned_info = clean_info(info)
		start_lines = get_line_numbers(cleaned_info, site)
		#iterates through starting lines, and writes content to text file
		text_file_name = READ_SHEET.cell_value(row, COL2).replace(u'\xa0', ' ')
		file_number = 1
		excel_col_num = COL3
		for line in start_lines:
			file_name = text_file_name
			section_heading = strip_tags(site.content[line]).strip()
			write_to_excel(row, excel_col_num, section_heading)
			if len(start_lines) > 1:
				file_name += "_" + `file_number`
			relevant_text = get_relevant_text(site.content, line)
			file_count += 1
			print "Writing File " + `file_count`
			produce_text_file(file_name, relevant_text)
			file_number += 1
			excel_col_num += 1
	WORKSHEET.save('ProgramOutput.xls')
		
"""Given a row, column, and datum, method writes datum to excel sheet
Precondition: row, col are integers, and datum is a string."""
def write_to_excel(row, col, datum):
	print "Writing to excel file"
	datum = datum.replace('Back to Top', '')
	WRITE_SHEET.write(row, col, datum)

"""Given a name and content, method creates and writes to a text file.
Precondition: name is a string, content is a list of html tags."""
def produce_text_file(name, content):
	print "Creating new text file"
	complete_name = os.path.join(SAVE_PATH, name+".txt")
	file = open(complete_name, 'w')
	for line in content:
		if '<h' in line:
			line = strip_tags(line).strip()
			file.write('\n'+line+'\n\n')
		elif '</p' in line or '<i' in line or '<li' in line:
			line = strip_tags(line).strip()
			file.write(line+'\n\n')
		elif ('[' in line and ']' in line) and (line.strip().index('[') == 0):
			line = strip_tags(line).strip()
			file.write(' ' + line + ' ')
		else:
			line = strip_tags(line).strip()
			file.write(line)
	file.close()

"""A webpage object which contains a list of html tags representing the site's
content"""
class Webpage:
	def __init__(self):
		self.content = []
	
	def setContent(self, content):
		self.content = content
		
	def getContent():
		return self.content

"""A class to handle the stripping of html tags in website's content."""
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
		
    def handle_data(self, d):
        self.fed.append(d)
		
    def get_data(self):
        return ''.join(self.fed)

"""Parses line of html"""
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()