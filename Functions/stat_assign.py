
def pitcher_stat_assign(stat_array):

  mlb_year_array     = []
  mlb_team_array     = []
  mlb_league_array   = []
  mlb_W_array        = []
  mlb_L_array        = []
  mlb_ERA_array      = []
  mlb_G_array        = []
  mlb_GS_array       = []
  mlb_CG_array       = []
  mlb_ShO_array      = []
  mlb_SV_array       = []
  mlb_HLD_array      = []
  mlb_BS_array       = []
  mlb_IP_array       = []
  mlb_TBF_array      = []
  mlb_H_array        = []
  mlb_R_array        = []
  mlb_ER_array       = []
  mlb_HR_array       = []
  mlb_BB_array       = []
  mlb_IBB_array      = []
  mlb_HBP_array      = []
  mlb_WP_array       = []
  mlb_BK_array       = []
  mlb_SO_array       = []

  milb_year_array     = []
  milb_team_array     = []
  milb_league_array   = []
  milb_W_array        = []
  milb_L_array        = []
  milb_ERA_array      = []
  milb_G_array        = []
  milb_GS_array       = []
  milb_CG_array       = []
  milb_ShO_array      = []
  milb_SV_array       = []
  milb_HLD_array      = []
  milb_BS_array       = []
  milb_IP_array       = []
  milb_TBF_array      = []
  milb_H_array        = []
  milb_R_array        = []
  milb_ER_array       = []
  milb_HR_array       = []
  milb_BB_array       = []
  milb_IBB_array      = []
  milb_HBP_array      = []
  milb_WP_array       = []
  milb_BK_array       = []
  milb_SO_array       = []

  projections_year_array     = []
  projections_team_array     = []
  projections_league_array   = []
  projections_W_array        = []
  projections_L_array        = []
  projections_ERA_array      = []
  projections_G_array        = []
  projections_GS_array       = []
  projections_CG_array       = []
  projections_ShO_array      = []
  projections_SV_array       = []
  projections_HLD_array      = []
  projections_BS_array       = []
  projections_IP_array       = []
  projections_TBF_array      = []
  projections_H_array        = []
  projections_R_array        = []
  projections_ER_array       = []
  projections_HR_array       = []
  projections_BB_array       = []
  projections_IBB_array      = []
  projections_HBP_array      = []
  projections_WP_array       = []
  projections_BK_array       = []
  projections_SO_array       = []

  for i in stat_array[0]:
    if len(i) != 0:
      if type(i[0]) == int:
	mlb_year_array.append(i[0])
        mlb_team_array.append(i[1])
        mlb_W_array.append(i[2])
        mlb_L_array.append(i[3])
        mlb_ERA_array.append(i[4])
        mlb_G_array.append(i[5])
        mlb_GS_array.append(i[6])
        mlb_CG_array.append(i[7])
        mlb_ShO_array.append(i[8])
        mlb_SV_array.append(i[9])
        mlb_HLD_array.append(i[10])
        mlb_BS_array.append(i[11])
        mlb_IP_array.append(i[12])
        mlb_TBF_array.append(i[13])
        mlb_H_array.append(i[14])
        mlb_R_array.append(i[15])
        mlb_ER_array.append(i[16])
        mlb_HR_array.append(i[17])
        mlb_BB_array.append(i[18])
        mlb_IBB_array.append(i[19])
        mlb_HBP_array.append(i[20])
        mlb_WP_array.append(i[21])
	mlb_BK_array.append(i[22])
	mlb_SO_array.append(i[23])

  for i in stat_array[1]:
    milb_year_array.append(i[0])
    milb_team_array.append(i[1])
    milb_W_array.append(i[2])
    milb_L_array.append(i[3])
    milb_ERA_array.append(i[4])
    milb_G_array.append(i[5])
    milb_GS_array.append(i[6])
    milb_CG_array.append(i[7])
    milb_ShO_array.append(i[8])
    milb_SV_array.append(i[9])
    milb_HLD_array.append(i[10])
    milb_BS_array.append(i[11])
    milb_IP_array.append(i[12])
    milb_TBF_array.append(i[13])
    milb_H_array.append(i[14])
    milb_R_array.append(i[15])
    milb_ER_array.append(i[16])
    milb_HR_array.append(i[17])
    milb_BB_array.append(i[18])
    milb_IBB_array.append(i[19])
    milb_HBP_array.append(i[20])
    milb_WP_array.append(i[21])
    milb_BK_array.append(i[22])
    milb_SO_array.append(i[23])

  for i in stat_array[2]:
    projections_year_array.append(i[0])
    projections_team_array.append(i[1])
    projections_W_array.append(i[2])
    projections_L_array.append(i[3])
    projections_ERA_array.append(i[4])
    projections_G_array.append(i[5])
    projections_GS_array.append(i[6])
    projections_CG_array.append(i[7])
    projections_ShO_array.append(i[8])
    projections_SV_array.append(i[9])
    projections_HLD_array.append(i[10])
    projections_BS_array.append(i[11])
    projections_IP_array.append(i[12])
    projections_TBF_array.append(i[13])
    projections_H_array.append(i[14])
    projections_R_array.append(i[15])
    projections_ER_array.append(i[16])
    projections_HR_array.append(i[17])
    projections_BB_array.append(i[18])
    projections_IBB_array.append(i[19])
    projections_HBP_array.append(i[20])
    projections_WP_array.append(i[21])
    projections_BK_array.append(i[22])
    projections_SO_array.append(i[23])


  mlb = [mlb_year_array, mlb_team_array, mlb_league_array,  mlb_W_array, mlb_L_array, mlb_ERA_array, mlb_G_array, mlb_GS_array, mlb_CG_array, mlb_ShO_array, mlb_SV_array, mlb_HLD_array, mlb_BS_array, mlb_IP_array, mlb_TBF_array, mlb_H_array, mlb_R_array, mlb_ER_array, mlb_HR_array, mlb_BB_array, mlb_IBB_array, mlb_HBP_array, mlb_WP_array, mlb_BK_array, mlb_SO_array]

  milb = [milb_year_array, milb_team_array, milb_league_array,  milb_W_array, milb_L_array, milb_ERA_array, milb_G_array, milb_GS_array, milb_CG_array, milb_ShO_array, milb_SV_array, milb_HLD_array, milb_BS_array, milb_IP_array, milb_TBF_array, milb_H_array, milb_R_array, milb_ER_array, milb_HR_array, milb_BB_array, milb_IBB_array, milb_HBP_array, milb_WP_array, milb_BK_array, milb_SO_array]

  projections = [projections_year_array, projections_team_array, projections_league_array,  projections_W_array, projections_L_array, projections_ERA_array, projections_G_array, projections_GS_array, projections_CG_array, projections_ShO_array, projections_SV_array, projections_HLD_array, projections_BS_array, projections_IP_array, projections_TBF_array, projections_H_array, projections_R_array, projections_ER_array, projections_HR_array, projections_BB_array, projections_IBB_array, projections_HBP_array, projections_WP_array, projections_BK_array, projections_SO_array]

# Remove empty arrays from each of the lists

  count = 0
  for i in range(len(mlb)):
    if len(mlb[i-count]) == 0:
      del mlb[i-count]
      count += 1
  
  count = 0
  for i in range(len(milb)):
    if len(milb[i-count]) == 0:
      del milb[i-count]
      count += 1
  
  count = 0
  for i in range(len(projections)):
    if len(projections[i-count]) == 0:
      del projections[i-count]
      count += 1

  return [mlb, milb, projections] 



def hitter_stat_assign(stat_array):

  mlb_year_array     = []
  mlb_team_array     = []
  mlb_league_array   = []
  mlb_GP_array       = []
  mlb_AB_array       = []
  mlb_PA_array       = []
  mlb_H_array        = []
  mlb_1B_array       = []
  mlb_2B_array       = []
  mlb_3B_array       = []
  mlb_HR_array       = []
  mlb_R_array        = []
  mlb_RBI_array      = []
  mlb_BB_array       = []
  mlb_IBB_array      = []
  mlb_K_array        = []
  mlb_HBP_array      = []
  mlb_SF_array       = []
  mlb_SH_array       = []
  mlb_GDP_array      = []
  mlb_SB_array       = []
  mlb_CS_array       = []
  mlb_BA_array       = []

  milb_year_array    = []
  milb_team_array    = []
  milb_league_array  = []
  milb_GP_array      = []
  milb_AB_array      = []
  milb_PA_array      = []
  milb_H_array       = []
  milb_1B_array      = []
  milb_2B_array      = []
  milb_3B_array      = []
  milb_HR_array      = []
  milb_R_array       = []
  milb_RBI_array     = []
  milb_BB_array      = []
  milb_IBB_array     = []
  milb_K_array       = []
  milb_HBP_array     = []
  milb_SF_array      = []
  milb_SH_array      = []
  milb_GDP_array     = []
  milb_SB_array      = []
  milb_CS_array      = []
  milb_BA_array      = []

  projections_year_array    = []
  projections_team_array    = []
  projections_league_array  = []
  projections_GP_array      = []
  projections_AB_array      = []
  projections_PA_array      = []
  projections_H_array       = []
  projections_1B_array      = []
  projections_2B_array      = []
  projections_3B_array      = []
  projections_HR_array      = []
  projections_R_array       = []
  projections_RBI_array     = []
  projections_BB_array      = []
  projections_IBB_array     = []
  projections_K_array       = []
  projections_HBP_array     = []
  projections_SF_array      = []
  projections_SH_array      = []
  projections_GDP_array     = []
  projections_SB_array      = []
  projections_CS_array      = []
  projections_BA_array      = []

  for i in stat_array[0]:
    if len(i) != 0:
      if type(i[0]) == int:
	mlb_year_array.append(i[0])
        mlb_team_array.append(i[1])
        mlb_GP_array.append(i[2])
        mlb_AB_array.append(i[3])
        mlb_PA_array.append(i[4])
        mlb_H_array.append(i[5])
        mlb_1B_array.append(i[6])
        mlb_2B_array.append(i[7])
        mlb_3B_array.append(i[8])
        mlb_HR_array.append(i[9])
        mlb_R_array.append(i[10])
        mlb_RBI_array.append(i[11])
        mlb_BB_array.append(i[12])
        mlb_IBB_array.append(i[13])
        mlb_K_array.append(i[14])
        mlb_HBP_array.append(i[15])
        mlb_SF_array.append(i[16])
        mlb_SH_array.append(i[17])
        mlb_GDP_array.append(i[18])
        mlb_SB_array.append(i[19])
        mlb_CS_array.append(i[20])
        mlb_BA_array.append(i[21])
  
  for i in stat_array[1]:
    milb_year_array.append(i[0])
    milb_team_array.append(i[1])
    milb_GP_array.append(i[2])
    milb_AB_array.append(i[3])
    milb_PA_array.append(i[4])
    milb_H_array.append(i[5])
    milb_1B_array.append(i[6])
    milb_2B_array.append(i[7])
    milb_3B_array.append(i[8])
    milb_HR_array.append(i[9])
    milb_R_array.append(i[10])
    milb_RBI_array.append(i[11])
    milb_BB_array.append(i[12])
    milb_IBB_array.append(i[13])
    milb_K_array.append(i[14])
    milb_HBP_array.append(i[15])
    milb_SF_array.append(i[16])
    milb_SH_array.append(i[17])
    milb_GDP_array.append(i[18])
    milb_SB_array.append(i[19])
    milb_CS_array.append(i[20])
    milb_BA_array.append(i[21])

  for i in stat_array[2]:
    projections_year_array.append(i[0])
    projections_team_array.append(i[1])
    projections_GP_array.append(i[2])
    projections_AB_array.append(i[3])
    projections_PA_array.append(i[4])
    projections_H_array.append(i[5])
    projections_1B_array.append(i[6])
    projections_2B_array.append(i[7])
    projections_3B_array.append(i[8])
    projections_HR_array.append(i[9])
    projections_R_array.append(i[10])
    projections_RBI_array.append(i[11])
    projections_BB_array.append(i[12])
    projections_IBB_array.append(i[13])
    projections_K_array.append(i[14])
    projections_HBP_array.append(i[15])
    projections_SF_array.append(i[16])
    projections_SH_array.append(i[17])
    projections_GDP_array.append(i[18])
    projections_SB_array.append(i[19])
    projections_CS_array.append(i[20])
    projections_BA_array.append(i[21])

  mlb = [mlb_year_array, mlb_team_array, mlb_league_array,  mlb_GP_array, mlb_AB_array, mlb_PA_array, mlb_R_array, mlb_H_array, mlb_1B_array, mlb_2B_array, mlb_3B_array, mlb_HR_array, mlb_R_array, mlb_RBI_array, mlb_BB_array, mlb_IBB_array, mlb_K_array, mlb_HBP_array, mlb_SF_array, mlb_SH_array, mlb_GDP_array, mlb_SB_array, mlb_CS_array, mlb_BA_array]

  milb = [milb_year_array, milb_team_array, milb_league_array,  milb_GP_array, milb_AB_array, milb_PA_array, milb_R_array, milb_H_array, milb_1B_array, milb_2B_array, milb_3B_array, milb_HR_array, milb_R_array, milb_RBI_array, milb_BB_array, milb_IBB_array, milb_K_array, milb_HBP_array, milb_SF_array, milb_SH_array, milb_GDP_array, milb_SB_array, milb_CS_array, milb_BA_array]

  projections = [projections_year_array, projections_team_array, projections_league_array,  projections_GP_array, projections_AB_array, projections_PA_array, projections_R_array, projections_H_array, projections_1B_array, projections_2B_array, projections_3B_array, projections_HR_array, projections_R_array, projections_RBI_array, projections_BB_array, projections_IBB_array, projections_K_array, projections_HBP_array, projections_SF_array, projections_SH_array, projections_GDP_array, projections_SB_array, projections_CS_array, projections_BA_array]
  
  count = 0
  for i in range(len(mlb)):
    if len(mlb[i-count]) == 0:
      del mlb[i-count]
      count += 1
  
  count = 0
  for i in range(len(milb)):
    if len(milb[i-count]) == 0:
      del milb[i-count]
      count += 1
  
  count = 0
  for i in range(len(projections)):
    if len(projections[i-count]) == 0:
      del projections[i-count]
      count += 1

  return [mlb, milb, projections] 
