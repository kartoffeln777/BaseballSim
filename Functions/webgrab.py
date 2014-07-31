import urllib
import os

#------------------------------------------------------------------------------
#
# Input: player_name, url to player's fangraphs page
# Output: No output
#
# Purpose: Reads the source code of the player's fangraphs page and dumps it
#          in a file called "player_name_output.txt"
#
#------------------------------------------------------------------------------

def webgrab(player_name, url):
  
  #get the file
  f = urllib.urlopen(url)
  s = f.read()
  f.close()

  #replaces all instances of the pattern with a newline, then writes it into the file 'refined.txt'
  ff = open("C:\\Python27\\Scripts\\baseball\\Fangraphs\\player_info\\" + player_name + "_output.txt", 'w')
  ff.write(s)
  ff.close()


