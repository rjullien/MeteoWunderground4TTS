import json
import sys
from pprint import pprint
import lib.MeteoLib

usage="usage: " + sys.argv[0] + " filename"
if len(sys.argv) < 2:
        print usage
        exit()

FilenameAlert=sys.argv[1]
print lib.MeteoLib.calculateAlert(FilenameAlert)
