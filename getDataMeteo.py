import urllib2
import sys
import lib.MeteoLib
usage="usage: " + sys.argv[0] + " APIKey alerts|forecast [Country/City] \nExample: " + sys.argv[0] + " xxxx forecast FR/Roquefort-les-Pins"
debug=False
#debug=True
# API doc: https://www.wunderground.com/weather/api/d/docs?d=index

if len(sys.argv) < 3:
        print usage
        exit()

APIKey = sys.argv[1]
requestType=sys.argv[2]
if len(sys.argv) == 4:
    RequestCity=sys.argv[3]
else:
    RequestCity="FR/Roquefort-les-Pins"
if debug:
    print "Requested City:"+ RequestCity

print lib.MeteoLib.getDataMeteo(APIKey,requestType,RequestCity,debug)
