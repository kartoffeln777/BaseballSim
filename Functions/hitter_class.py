#------------------------------------------------------------------------------
#
# Input:  All basic stats tracked for a hitter
# Output: None
#
# Purpose: Creates 3 different classes: MLB_Hitter, MiLB_Hitter, and
#          Hitter_Projections
#
#------------------------------------------------------------------------------

class Hitter:
	
  def __init__(self, MLB, MiLB, Proj, Post):
    self.MLB  = MLB
    self.MiLB = MiLB
    self.Proj = Proj
    self.Post = Post
	
class Hitter_Stats_Base:

  def __init__(self, Year, Team, Games, AB, PA, H, Singles, Doubles, Triples, HR, R, RBI, BB, IBB, SO, HBP, SF, SH, GDP, SB, CS, BA):
    self.year     = Year
    self.team     = Team
    self.GP       = Games
    self.AB       = AB
    self.PA       = PA
    self.H        = H
    self.Singles  = Singles
    self.Doubles  = Doubles
    self.Triples  = Triples
    self.HR       = HR
    self.R        = R
    self.RBI      = RBI
    self.BB       = BB
    self.IBB      = IBB
    self.K        = SO
    self.HBP      = HBP
    self.SF       = SF
    self.SH       = SH
    self.GDP      = GDP
    self.SB       = SB
    self.CS       = CS
    self.BA       = BA
    self.BB_rate  = []
    self.K_rate   = []
    if len(self.BB_rate) > 0 & len(self.K_rate) > 0:
      for i in range (0, len(self.BB)):
        self.BB_rate.append( round(100*(float(self.BB[i]) / float(self.PA[i])),2) )
        self.K_rate.append( round(100*(float(self.K[i]) / float(self.PA[i])), 2) )
"""

class MiLB_Hitter:

  def __init__(self, Year, League, Games, AB, PA, H, Singles, Doubles, Triples, HR, R, RBI, BB, IBB, SO, HBP, SF, SH, GDP, SB, CS, BA):
    self.year     = Year
    self.league   = League
    self.GP       = Games
    self.AB       = AB
    self.PA       = PA
    self.H        = H
    self.Singles  = Singles
    self.Doubles  = Doubles
    self.Triples  = Triples
    self.HR       = HR
    self.R        = R
    self.RBI      = RBI
    self.BB       = BB
    self.IBB      = IBB
    self.K        = SO
    self.HBP      = HBP
    self.SF       = SF
    self.SH       = SH
    self.GDP      = GDP
    self.SB       = SB
    self.CS       = CS
    self.BA       = BA
    self.BB_rate  = []
    self.K_rate   = []
    if len(self.BB_rate) > 0 & len(self.K_rate) > 0:
      for i in range (0, len(self.BB)):
        self.BB_rate.append( round(100*(float(self.BB[i]) / float(self.PA[i])),2) )
        self.K_rate.append( round(100*(float(self.K[i]) / float(self.PA[i])), 2) )

class Hitter_Projections:

  def __init__(self, Year, League, Games, AB, PA, H, Singles, Doubles, Triples, HR, R, RBI, BB, IBB, SO, HBP, SF, SH, GDP, SB, CS, BA):
    self.year     = Year
    self.league   = League
    self.GP       = Games
    self.AB       = AB
    self.PA       = PA
    self.H        = H
    self.Singles  = Singles
    self.Doubles  = Doubles
    self.Triples  = Triples
    self.HR       = HR
    self.R        = R
    self.RBI      = RBI
    self.BB       = BB
    self.IBB      = IBB
    self.K        = SO
    self.HBP      = HBP
    self.SF       = SF
    self.SH       = SH
    self.GDP      = GDP
    self.SB       = SB
    self.CS       = CS
    self.BA       = BA
    self.BB_rate  = []
    self.K_rate   = []
    if len(self.BB_rate) > 0 & len(self.K_rate) > 0:
      for i in range (0, len(self.BB)):
        self.BB_rate.append( round(100*(float(self.BB[i]) / float(self.PA[i])),2) )
        self.K_rate.append( round(100*(float(self.K[i]) / float(self.PA[i])), 2) )

class Hitter_Postseason:

  def __init__(self, Year, League, Games, AB, PA, H, Singles, Doubles, Triples, HR, R, RBI, BB, IBB, SO, HBP, SF, SH, GDP, SB, CS, BA):
    self.year     = Year
    self.league   = League
    self.GP       = Games
    self.AB       = AB
    self.PA       = PA
    self.H        = H
    self.Singles  = Singles
    self.Doubles  = Doubles
    self.Triples  = Triples
    self.HR       = HR
    self.R        = R
    self.RBI      = RBI
    self.BB       = BB
    self.IBB      = IBB
    self.K        = SO
    self.HBP      = HBP
    self.SF       = SF
    self.SH       = SH
    self.GDP      = GDP
    self.SB       = SB
    self.CS       = CS
    self.BA       = BA
    self.BB_rate  = []
    self.K_rate   = []
    if len(self.BB_rate) > 0 & len(self.K_rate) > 0:
      for i in range (0, len(self.BB)):
        self.BB_rate.append( round(100*(float(self.BB[i]) / float(self.PA[i])),2) )
        self.K_rate.append( round(100*(float(self.K[i]) / float(self.PA[i])), 2) )
"""
