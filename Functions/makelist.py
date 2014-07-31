from bs4 import BeautifulSoup

#------------------------------------------------------------------------------
#
# Input:  table
# Output: result (Returns a list of tables)
#
# Purpose: Takes tables written in HTML and returns a list of the contents of
#          the tables.
#
#------------------------------------------------------------------------------


def makelist(table):
  import BeautifulSoup
  
  result = []
  allrows = table.findAll('tr')
  for row in allrows:
    result.append([])
    allcols = row.findAll('td')
    for col in allcols:
      thestrings = [unicode(s) for s in col.findAll(text=True)]
      thetext = ''.join(thestrings)
      result[-1].append(thetext)
    if not result[-1]:
      del result[-1]

  return result
  
