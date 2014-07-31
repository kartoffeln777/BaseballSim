def postseason_assign(mlb_array):

  count = 0 
  temp_postseason_array = []

# If there are two consecutive years that are the same, then the
# second year refers to the player being in the postseason.
# Postseason stats are separated from regular season stats and 
# given their own category.

  for i in range(1, len(mlb_array[0])):
    if mlb_array[0][i-count] == mlb_array[0][i-count-1]:
      temp_array = []
      for j in range(len(mlb_array)):
	if len(mlb_array[j]) > 0:
          temp_array.append(mlb_array[j][i-count])
	  del mlb_array[j][i-count]
      count += 1
      temp_postseason_array.append(temp_array)
  

  
  temp_whole = []
  for i in range(len(temp_postseason_array[0])):
    temp_inner = []
    for j in temp_postseason_array:
      temp_inner.append(j[i])
    temp_whole.append(temp_inner)

  return [temp_whole, mlb_array]
