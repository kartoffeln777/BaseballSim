from player_stats import player_stats
from array_parser import array_parser

def getAverage(PlayerName):
  mlb_avg_array = []
  mlb_year_array = []
  milb_avg_array = []
  milb_year_array = []
  player_array = player_stats(PlayerName + "_output.txt", PlayerName)[1]
# print player_array
  stats = array_parser(player_array)
# print "MLB averages by year:\n"
  sum_AB_mlb = 0
  sum_H_mlb = 0
  sum_AB_milb = 0
  sum_H_milb = 0
#  print "Here are stats[0] \n", stats[0]
  dict = {'Year': 0, 'Age': 1, 'Team': 2, 'League': 3, 'Games': 4, 'PA': 5, 'AB':6, 'R': 7, 'H': 8, '2B': 9, '3B': 10, 'HR': 11, 'RBI': 12, 'SB': 13, 'CS': 14, 'BB': 15, 'SO': 16, 'BA': 17, 'OBP': 18, 'SLG': 19, 'OPS': 20, 'OPS+': 21, 'TB': 22, 'GDP': 23, 'HBP': 24, 'SH': 25, 'SF': 26, 'IBB': 27, 'Pos': 28, 'Awards': 29}
  for i in stats[0]:
    if type(i[0]) == int:
#      print i[dict['AB']]
      sum_AB_mlb += float(i[dict['AB']])
      sum_H_mlb += float(i[dict['H']])
      mlb_avg_array.append(i[dict['BA']])
      mlb_year_array.append(i[dict['Year']])
#     print "%d: %.3f\n" % (i[dict['Year']], float(i[dict['BA']]))
# print "MiLB averages by year:\n"
  for i in stats[1]:
    if type(i[0]) == int:
      sum_AB_milb += float(i[dict['AB']])
      sum_H_milb += float(i[dict['H']])
      milb_avg_array.append(i[dict['BA']])
      milb_year_array.append(i[dict['Year']])
#     print "%d: %.3f\n" % (i[dict['Year']], float(i[dict['BA']]))
  mlb_BA = sum_H_mlb/sum_AB_mlb 
  milb_BA = sum_H_milb/sum_AB_milb

  print "MLB career avg: %.3f\n" %mlb_BA
  print "MiLB career avg: %.3f\n" %milb_BA

  return [[milb_avg_array, mlb_avg_array],[milb_year_array, mlb_year_array]]
 

