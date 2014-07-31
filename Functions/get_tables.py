from bs4 import BeautifulSoup

#------------------------------------------------------------------------------
#
# Input:  html_doc
# Output: table (All the HTML code for tables from the html_doc)
#
# Purpose: Reads the previously written source code and extracts only the code 
#          relating to HTML tables
#
#------------------------------------------------------------------------------

def get_tables(html_doc):
  soup = BeautifulSoup.BeautifulSoup(html_doc)
  return soup.findAll('table')

