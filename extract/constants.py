#constants.py
#Justin Selig, June 30, 2014
#Cornell eRulemaking Initiative

import os
"""xlrd requies that you specify a sheet number."""

SHEET0 = 0

"""This column number is used by cell_value and remains the same because 
of the format of the excel sheets given."""
COL0 = 0
COL1 = 1
COL2 = 2
COL3 = 3

SAVE_PATH = os.path.abspath("output")