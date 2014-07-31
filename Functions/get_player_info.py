#------------------------------------------------------------------------------
#
# Input:  playerName, url
# Output: [player_dict[mlb], player_dict[milb], player_dict[proj], 
#         player_dict[post]] (mlb, milb, projected, and postseason stats)
#
# Purpose: Sorts the data in into MLB, MiLB, projected, and postseason stats
#
#------------------------------------------------------------------------------

from webgrab                 import webgrab
from player_stats            import player_stats
from array_parser            import array_parser
from stat_assign             import pitcher_stat_assign
from stat_assign             import hitter_stat_assign
from postseason_assign       import postseason_assign
from pitcher_class           import Pitcher
from pitcher_class           import Pitcher_Stats_Base
from hitter_class            import Hitter
from hitter_class            import Hitter_Stats_Base
from makelist                import makelist
from get_tables              import get_tables
from generalize_player_name  import generalize_player_name
from stat_write              import stat_write

def get_player_info(name, url, web_bool):

  basic_stats_dict = {'Year': 0, 'Age': 1, 'Team': 2, 'League': 3, 'Games': 4, 'PA': 5, 'AB':6, 'R': 7, 'H': 8, '2B': 9, '3B': 10, 'HR': 11, 'RBI': 12, 'SB': 13, 'CS': 14, 'BB': 15, 'SO': 16, 'BA': 17, 'OBP': 18, 'SLG': 19, 'OPS': 20, 'OPS+': 21, 'TB': 22, 'GDP': 23, 'HBP': 24, 'SH': 25, 'SF': 26, 'IBB': 27, 'Pos': 28, 'Awards': 29}

  #First, we want to make the name generic 

  playerName = generalize_player_name(name)

# Check if the player is a pitcher or hitter

  if url[-1] == "P":
    player_type = "Pitcher"
  else:
    player_type = "Hitter"
 
# If specified, get player data from the web. 
# Otherwise, use what is already saved to the computer.

  if web_bool:
    webgrab(playerName, url)

  array = player_stats(playerName)

  stats = array_parser(array)

#######
  stat_write(stats, playerName)
#######

  if player_type == "Hitter":
    [mlb_and_post_stats, milb_stats, projection_stats] = hitter_stat_assign(stats)
    del mlb_and_post_stats[5]
    del milb_stats[5]
    del projection_stats[5]

    [postseason_stats, mlb_stats] = postseason_assign(mlb_and_post_stats)

    MLB = Hitter_Stats_Base(mlb_stats[0], mlb_stats[1], mlb_stats[2], mlb_stats[3], mlb_stats[4], mlb_stats[5], mlb_stats[6], mlb_stats[7], mlb_stats[8], mlb_stats[9], mlb_stats[10], mlb_stats[11], mlb_stats[12], mlb_stats[13], mlb_stats[14], mlb_stats[15], mlb_stats[16], mlb_stats[17], mlb_stats[18], mlb_stats[19], mlb_stats[20], mlb_stats[21] )

    MiLB = Hitter_Stats_Base(milb_stats[0], milb_stats[1], milb_stats[2], milb_stats[3], milb_stats[4], milb_stats[5], milb_stats[6], milb_stats[7], milb_stats[8], milb_stats[9], milb_stats[10], milb_stats[11], milb_stats[12], milb_stats[13], milb_stats[14], milb_stats[15], milb_stats[16], milb_stats[17], milb_stats[18], milb_stats[19], milb_stats[20], milb_stats[21] )

    Proj = Hitter_Stats_Base(projection_stats[0], projection_stats[1], projection_stats[2], projection_stats[3], projection_stats[4], projection_stats[5], projection_stats[6], projection_stats[7], projection_stats[8], projection_stats[9], projection_stats[10], projection_stats[11], projection_stats[12], projection_stats[13], projection_stats[14], projection_stats[15], projection_stats[16], projection_stats[17], projection_stats[18], projection_stats[19], projection_stats[20], projection_stats[21] )
  
    Post = Hitter_Stats_Base(postseason_stats[0], postseason_stats[1], postseason_stats[2], postseason_stats[3], postseason_stats[4], postseason_stats[5], postseason_stats[6], postseason_stats[7], postseason_stats[8], postseason_stats[9], postseason_stats[10], postseason_stats[11], postseason_stats[12], postseason_stats[13], postseason_stats[14], postseason_stats[15], postseason_stats[16], postseason_stats[17], postseason_stats[18], postseason_stats[19], postseason_stats[20], postseason_stats[21] )

    player = Hitter(MLB, MiLB, Proj, Post) 
 
 
  elif player_type == "Pitcher":
    
    [mlb_and_post_stats, milb_stats, projection_stats] = pitcher_stat_assign(stats)

    [postseason_stats, mlb_stats] = postseason_assign(mlb_and_post_stats)
   
    MLB = Pitcher_Stats_Base(mlb_stats[0], mlb_stats[1], mlb_stats[2], mlb_stats[3], mlb_stats[4], mlb_stats[5], mlb_stats[6], mlb_stats[7], mlb_stats[8], mlb_stats[9], mlb_stats[10], mlb_stats[11], mlb_stats[12], mlb_stats[13], mlb_stats[14], mlb_stats[15], mlb_stats[16], mlb_stats[17], mlb_stats[18], mlb_stats[19], mlb_stats[20], mlb_stats[21], mlb_stats[22], mlb_stats[23] )

    MiLB = Pitcher_Stats_Base(milb_stats[0], milb_stats[1], milb_stats[2], milb_stats[3], milb_stats[4], milb_stats[5], milb_stats[6], milb_stats[7], milb_stats[8], milb_stats[9], milb_stats[10], milb_stats[11], milb_stats[12], milb_stats[13], milb_stats[14], milb_stats[15], milb_stats[16], milb_stats[17], milb_stats[18], milb_stats[19], milb_stats[20], milb_stats[21], milb_stats[22], milb_stats[23] )

    Proj = Pitcher_Stats_Base(projection_stats[0], projection_stats[1], projection_stats[2], projection_stats[3], projection_stats[4], projection_stats[5], projection_stats[6], projection_stats[7], projection_stats[8], projection_stats[9], projection_stats[10], projection_stats[11], projection_stats[12], projection_stats[13], projection_stats[14], projection_stats[15], projection_stats[16], projection_stats[17], projection_stats[18], projection_stats[19], projection_stats[20], projection_stats[21], projection_stats[22], projection_stats[23] )
  
    Post = Pitcher_Stats_Base(postseason_stats[0], postseason_stats[1], postseason_stats[2], postseason_stats[3], postseason_stats[4], postseason_stats[5], postseason_stats[6], postseason_stats[7], postseason_stats[8], postseason_stats[9], postseason_stats[10], postseason_stats[11], postseason_stats[12], postseason_stats[13], postseason_stats[14], postseason_stats[15], postseason_stats[16], postseason_stats[17], postseason_stats[18], postseason_stats[19], postseason_stats[20], postseason_stats[21], postseason_stats[22], postseason_stats[23] )

    player = Pitcher(MLB, MiLB, Proj, Post) 

  
  return player
  
  #return [player_dict[mlb], player_dict[milb], player_dict[proj], player_dict[post]]
 
