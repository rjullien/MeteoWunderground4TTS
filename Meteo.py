# Meteo est un clone de MeteoRene sans l'APIKey
import lib.MeteoLib
import tempfile
import sys

usage="usage: " + sys.argv[0] + " alert|forecast [simulation|debug|Roquefort|Isola|Eyguians] (def:Roquefort)"
if len(sys.argv) > 3 or len(sys.argv) < 2:
        print usage
        exit()

requestType=sys.argv[1]

if len(sys.argv) == 3:
    ModeMeteoRoquefort=sys.argv[2]
    if ModeMeteoRoquefort == "simulation":
        RequestCity="FR/Roquefort-les-Pins"
        RequestCityName="Roquefort"
        Simul=True
        debug=False
    elif ModeMeteoRoquefort == "debug":
        RequestCity="FR/Roquefort-les-Pins"
        RequestCityName="Roquefort"
        Simul=False
        debug=True
    elif ModeMeteoRoquefort == "Eyguians":
        RequestCity="FR/Eyguians"
        RequestCityName=ModeMeteoRoquefort
        debug=False
        Simul=False
    elif ModeMeteoRoquefort == "Roquefort":
        RequestCity="FR/Roquefort-les-Pins"
        RequestCityName=ModeMeteoRoquefort
        debug=False
        Simul=False
    elif ModeMeteoRoquefort == "Isola":
        RequestCity="FR/Isola%202000"
        RequestCityName=ModeMeteoRoquefort
        debug=False
        Simul=False
    else:
        print usage
        exit()

else:
    RequestCity="FR/Roquefort-les-Pins"
    debug=False
    Simul=False

meteopath=tempfile.mkdtemp("meteo")
if debug:
    print meteopath
# ------------
# Insert your APIKeybelow
APIKey="xxxx"
if requestType == "forecast":
    FilenameMeteo= meteopath + "/Meteo" + RequestCityName + ".json"

    if debug:
        print FilenameAlert
        print FilenameMeteo

    if not Simul:
        MeteoResults= lib.MeteoLib.getDataMeteo(APIKey,requestType,RequestCity,debug)
        if debug:
            print MeteoResults
            exit()

        handlerFMeteo = open(FilenameMeteo, 'w')
        handlerFMeteo.write(MeteoResults)
        handlerFMeteo.close()

    if Simul:
        MessageMeteo="2 mm de pluie prevu le Mardi 15 Aout dont 0 mm le jour et 2 mm la nuit ...\nPas de neige prevu dans les 10 jours a venir"
        print MessageMeteo
    else:
        MessageMeteo =  lib.MeteoLib.calculatePluie("pluie",FilenameMeteo)
        print MessageMeteo + "..."
        MessageMeteo =  lib.MeteoLib.calculatePluie("neige",FilenameMeteo)
        print MessageMeteo
elif requestType == "alert":
    FilenameAlert= meteopath + "/Alert" + RequestCityName + ".json"
    if not Simul:
        MeteoResults= lib.MeteoLib.getDataMeteo(APIKey,requestType,RequestCity,debug)
        if debug:
            print MeteoResults
            exit()

        handlerFMeteo = open(FilenameAlert, 'w')
        handlerFMeteo.write(MeteoResults)
        handlerFMeteo.close()

    MessageMeteo =  lib.MeteoLib.calculateAlert(FilenameAlert)
    print unicode(MessageMeteo)
    
else:
    print usage
    exit()
