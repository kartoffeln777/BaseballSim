from optparse import OptionParser

parser = OptionParser()
parser.add_option("-w", "--web", action="store_false", dest="webgrab", default=True, help="Connect to web to get updated stats")

(options, args) = parser.parse_args()

print options.webgrab
