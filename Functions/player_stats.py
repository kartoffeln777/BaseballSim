from get_tables import get_tables
from makelist import makelist

#------------------------------------------------------------------------------
#
# Input:  name
# Output: array (Gives an array containing the player's desired statistics)
#
# Purpose: Reads the previously written source code and uses the functions 
#          get_tables() and makelist()to extract the tables from the file and 
#          put them in a list/array.
#
#------------------------------------------------------------------------------

import sys

def player_stats(name):
  
# Read the page source that was previously written by webgrab(). If webgrab_switch is toggled
# off and the page source doesn't exist, the program will exist and print an error message

  try:
    f1 = open("C:\\Python27\\Scripts\\baseball\\Fangraphs\\player_info\\" + name + "_output.txt")
  except IOError:
    print "Error: The file C:\\Python27\\Scripts\\baseball\\Fangraphs\\player_info\\%s_output.txt does not exist." %name
    sys.exit() 

  pageSource = f1.read()
  f1.close()

  table = get_tables(pageSource)
  
  ftemp = open("C:\\Python27\\Scripts\\baseball\\Fangraphs\\temp_player_info\\" + name + "_table_temp.txt", 'w')
  for i in table:
    ftemp.write(str(i))
  
# See if they are in the middle of the game 
# (Contents of Table 18 change if there is a game ongoing)
  
  live_test = makelist(table[18])

  if str(live_test[0][0]).find("Today") >= 0:
    print "live game in progress\n"
    player_list = makelist(table[24])                # This table stores basic stats
  else:
    print "No live game in progress\n"
    player_list = makelist(table[23])                # This table stores basic stats
    

  return [player_list]

