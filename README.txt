To run the program change your directory to the file containing CeRI-FederalRegister-Extraction, and type into your terminal/command line:
	
	python extract

When prompted, specify the file path of the excel spreadsheet containing the URLs to visit. There is a test file included in this package called 'Example URLs.xlsx'. The program will print to the terminal when files are being written. It will create an excel speadsheet similar to the input spreadsheet but containing the titles of the 'Executive Summary' sections alongside the urls. It is also necessary to keep a folder entitled 'output' in the repository. This is where the text files with the summary content will be stored.

It takes about 1-2 seconds for each url to be opened, the html to be read, and the files to be formatted and written to. So be patient. 

Have fun!