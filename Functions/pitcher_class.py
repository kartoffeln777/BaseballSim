#------------------------------------------------------------------------------
#
# Input:  All basic stats tracked for a hitter
# Output: None
#
# Purpose: Creates 3 different classes: MLB_Hitter, MiLB_Hitter, and
#          Hitter_Projections
#
#------------------------------------------------------------------------------

class Pitcher:
	
  def __init__(self, MLB, MiLB, Proj, Post):
    self.MLB  = MLB
    self.MiLB = MiLB
    self.Proj = Proj
    self.Post = Post
	
class Pitcher_Stats_Base:

  def __init__(self, Year, Team, W, L, ERA, G, GS, CG, ShO, SV, HLD, BS, IP, TBF, H, R, ER, HR, BB, IBB, HBP, WP, BK, SO):
    self.year     = Year
    self.team     = Team
    self.W        = W
    self.L        = L
    self.ERA      = ERA
    self.G        = G
    self.GS       = GS
    self.CG       = CG
    self.ShO      = ShO
    self.SV       = SV
    self.HLD      = HLD
    self.BS       = BS
    self.IP       = IP
    self.TBF      = TBF
    self.H        = H
    self.R        = R
    self.ER       = ER
    self.HR       = HR
    self.BB       = BB
    self.IBB      = IBB
    self.HBP      = HBP
    self.WP       = WP
    self.BK       = BK
    self.SO       = SO


