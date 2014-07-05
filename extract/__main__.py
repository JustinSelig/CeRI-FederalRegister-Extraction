#__main__.py
#Justin Selig, June 30, 2014
#Cornell eRulemaking Initiative

"""This is the module with the script code to start up the app.  Make
sure that this module is in a folder with the following files, and that
you install xlrd, xlwt, and xlutils on your computer using the given libraries:
	
	iterate.py
	extract.py 
	constants.py 
	xlrd-0.9.3 (folder)
	xlwt-0.7.5 (folder)
	xlutils (folder)"""

from iterate import *	

if __name__ == "__main__":
	print "Starting main"
	main()
	print "Finished!"