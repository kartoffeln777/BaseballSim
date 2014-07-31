import BeautifulSoup
import string
import sys
import urllib
import os

sys.path.append("C:\\Python27\\Scripts\\baseball\\Fangraphs\\Functions")

from array_parser      import array_parser
from get_tables        import get_tables
from player_stats      import player_stats
from webgrab           import webgrab
from stat_assign       import pitcher_stat_assign
from stat_assign       import hitter_stat_assign
from hitter_class      import Hitter
from hitter_class      import Hitter_Stats_Base
from postseason_assign import postseason_assign
from get_player_info   import get_player_info
from sorter            import sorter
from optparse          import OptionParser
from time              import clock, time

parser = OptionParser()
parser.add_option("-w", "--web", action="store_true", dest="webgrab", default=False, help="Connect to web to get updated stats")
parser.add_option("-t", "--time", action="store_true", dest="time_check", default=False, help="Print time program takes to run")

(options, args) = parser.parse_args()

webgrab_switch = options.webgrab
time_check     = options.time_check

start_time = clock()

stat_dict = {'mlb': 0, 'milb': 1, 'proj': 2, 'post': 3}
"""
matt_carpenter = get_player_info("matt carpenter", "http://www.fangraphs.com/statss.aspx?playerid=8090&position=1B/3B", webgrab_switch)
print matt_carpenter.MLB.PA
print matt_carpenter.MLB.BA

paul_konerko = get_player_info("Paul Konerko", "http://www.fangraphs.com/statss.aspx?playerid=242&position=1B", webgrab_switch)
print "\ngetting stats\n"
print paul_konerko.MLB.RBI
print ""
print paul_konerko.MLB.HR
print ""
print paul_konerko.MiLB.BA
print ""
"""
"""
david_price = get_player_info("David Price", "http://www.fangraphs.com/statss.aspx?playerid=3184&position=P", webgrab_switch)
print "\nprice stats\n"
print david_price.MLB.year
print david_price.MLB.ERA
print david_price.MLB.SO
print ""
print david_price.MiLB.ERA
print david_price.MiLB.IP
"""

adam_jones = get_player_info("Adam Jones", "http://www.fangraphs.com/statss.aspx?playerid=6368&position=OF", webgrab_switch)
print adam_jones.MLB.PA
print adam_jones.MLB.BA
print adam_jones.MLB.Doubles
print adam_jones.MLB.SB
print adam_jones.MiLB.H
print ""


#get_player_info("Wil Myers", "http://www.fangraphs.com/statss.aspx?playerid=sa501214&position=OF")

#player_array = [matt_carpenter, paul_konerko, adam_jones]

#sorter(matt_carpenter.MLB.PA)

"""
import numpy
#from pylab import *
from matplotlib import pyplot
x1 = adam_jones.MLB.year
y1 = adam_jones.MLB.BA
x2 = matt_carpenter.MLB.year
y2 = matt_carpenter.MLB.BA
#locs,labels = xticks()
#xticks(locs, map(lambda x1: "%" %x1, locs)
pyplot.xlabel('Year')
pyplot.ylabel('Batting Average')
pyplot.title('BA by year')
pyplot.plot(x1,y1, 'orange', x2, y2, 'r')
pyplot.show()
"""

end_time = clock()
total_time = end_time - start_time
if time_check:
  print "\nThis took %f.2 seconds to run" % total_time
