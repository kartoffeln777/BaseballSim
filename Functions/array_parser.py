#------------------------------------------------------------------------------
#
# Input:  array (Array of player's stats)
# Output: [mlb_temp_list, milb_temp_list, projections_temp_list] (This is a 
#         list of MLB, MiLB, and projected stats)
#
# Purpose: Sorts the data in array into MLB, MiLB, and projected stats
#
#------------------------------------------------------------------------------


def array_parser(array):
  #array is an array containing stats 

  
  milb_temp_list = []
  mlb_temp_list = []
  projections_temp_list = []
  for i in array[0]:
    if len(i) > 0:
      league_check = str(i[1])

# Check if the stats are for when the player was in the minor leagues

      if league_check.find("A") >=0 or (league_check.find("(R)") >= 0 and not (league_check.find("Steamer") >= 0 or league_check.find("ZiPS") >= 0)):
        templist_milb = []
	for j in i:
	  if len(j) > 0:
            k = str(j)
	    try:
	      m = int(k)
	      k = m
	    except StandardError:
	      pass 
	    except ValueError:
	      m = float(k)
	      k = m
	    templist_milb.append(k)
	milb_temp_list.append(templist_milb)
      elif league_check.find("Steamer") >= 0 or league_check.find("ZiPS") >= 0 or league_check.find("Bill James") >= 0 or league_check.find("Oliver") >= 0 or league_check.find("Fans") >= 0:
	templist_proj = []
        for j in i:
	  if len(j) > 0:
            k = str(j)
# Check if k is an int, float, or string	
	    try:
	      m = int(k)
	      k = m
	    except StandardError:
	      pass   
            except ValueError:
	      m = float(k)
	      k = m	
	    templist_proj.append(k)	
	projections_temp_list.append(templist_proj)
# If not assigned to any of the other lists, it is
# mlb statistics
      else:
	templist_mlb = []
	for j in i:
	  if len(j) > 0:
            k = str(j)
	    try:
	      m = int(k)
	      k = m
	    except StandardError:
	      pass   
            except ValueError:
	      m = float(k)
	      k = m	
	    templist_mlb.append(k)	
	mlb_temp_list.append(templist_mlb)
    
  return [mlb_temp_list, milb_temp_list, projections_temp_list]

  
