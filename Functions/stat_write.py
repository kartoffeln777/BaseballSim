def stat_write(stat_array, name):

  ftemp = open("C:\\Python27\\Scripts\\baseball\\Fangraphs\\player_stats\\" + name + "_stats.txt", 'w')

  for i in stat_array:
    for j in i:
      for k in j:
        ftemp.write(str(k) + "   ")
      ftemp.write("\n\n")

