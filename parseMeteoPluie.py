import json
import sys
from pprint import pprint
debug=True
import lib.MeteoLib
# ----- Debut du programme principal
usage="usage: " + sys.argv[0] + " ModeMeteo filename \nExample: " + sys.argv[0] + " full|pluie|neige filename.json"
if len(sys.argv) < 3:
    print usage
    exit()

FilenamePluie=sys.argv[2]
ModeMeteo=sys.argv[1]

MessageMeteo =  lib.MeteoLib.calculatePluie(ModeMeteo,FilenamePluie)
if debug:
    print MessageMeteo
