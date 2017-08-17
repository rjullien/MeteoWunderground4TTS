#!/usr/bin/env python
# coding: utf8
import json
import urllib2
def TranslateDay(DayEnglish):
    if DayEnglish == "Monday":
        DayFrench = "Lundi"
    elif DayEnglish == "Tuesday":
        DayFrench = "Mardi"
    elif DayEnglish == "Wednesday":
        DayFrench = "Mercredi"
    elif DayEnglish == "Thursday":
        DayFrench = "Jeudi"
    elif DayEnglish == "Friday":
        DayFrench = "Vendredi"
    elif DayEnglish == "Saturday":
        DayFrench = "Samedi"
    elif DayEnglish == "Sunday":
        DayFrench = "Dimanche"
    else:
        DayFrench = DayEnglish   # If french requested
    return DayFrench

def TranslateMonth(MonthEnglish):
    if MonthEnglish == "January":
        MonthFrench = "Janvier"
    elif MonthEnglish == "Fevrier":
        MonthFrench = "Mardi"
    elif MonthEnglish == "Mars":
        MonthFrench = "Mercredi"
    elif MonthEnglish == "Avril":
        MonthFrench = "Jeudi"
    elif MonthEnglish == "May":
        MonthFrench = "Mai"
    elif MonthEnglish == "June":
        MonthFrench = "Juin"
    elif MonthEnglish == "July":
        MonthFrench = "Juillet"
    elif MonthEnglish == "August":
        MonthFrench = "Aout"
    elif MonthEnglish == "September":
        MonthFrench = "Septembre"
    elif MonthEnglish == "October":
        MonthFrench = "Octobre"
    elif MonthEnglish == "November":
        MonthFrench = "Novembre"
    elif MonthEnglish == "December":
        MonthFrench = "Decembre"
    else:
        MonthFrench = MonthEnglish  # If french requested
    return MonthFrench

def calculatePluie(ModeMeteo,FilenamePluie):
    # Open json file
    with open(FilenamePluie) as data_file:
        data = json.load(data_file)

    # test if API return error
    try:
        a=data["response"]["error"]
        print data["response"]["error"]["type"] + ": " + data["response"]["error"]["description"]
        ErrorParsing=True
        exit()
    except KeyError:
        pass
        # Test if alert present
    try:
        a=data["response"]["features"]["forecast10day"]
        pass
    except KeyError:
        print "Error: keyword forecast10day not found"
        ErrorParsing=True
        exit()

        # Test if alert data vide
        a=data["forecast"]
    if a:
        pass
    else:
        print "forecast data empty"
        ErrorParsing=True
        exit()

    # get data
    PluieDetecte=False
    MessagePluie=""
    for i in range(len(data["forecast"]["simpleforecast"]["forecastday"])):

        if ModeMeteo == "full":
            if data["forecast"]["txt_forecast"]["forecastday"][i*2]["fcttext_metric"] == "":
                textMeteoJour = data["forecast"]["txt_forecast"]["forecastday"][i*2]["fcttext"]
                textMeteoNuit = data["forecast"]["txt_forecast"]["forecastday"][i*2+1]["fcttext"]
            else:
                textMeteoJour = data["forecast"]["txt_forecast"]["forecastday"][i*2]["fcttext_metric"]
                textMeteoNuit = data["forecast"]["txt_forecast"]["forecastday"][i*2+1]["fcttext_metric"]

            MessagePluie = MessagePluie \
            + str(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["weekday"])\
            + " " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["day"])\
            + " " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["monthname"])\
            + ", " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["conditions"])\
            + ", " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_allday"]["mm"])\
            + ' mm de pluie sur 24h'\
            + "\nJour:" + str(textMeteoJour)\
            + "\nNuit:" + str(textMeteoNuit)\
            + "\n\n"
        elif ModeMeteo == "neige":
        # snow_allday
            if data["forecast"]["simpleforecast"]["forecastday"][i]["snow_allday"]["cm"] != 0:

                if PluieDetecte:
                    MessagePluie = MessagePluie + ", "
                MessagePluie = MessagePluie \
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["snow_allday"]["mm"])\
                + ' mm de pluie prevu le '\
                + str(TranslateDay(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["weekday"]))\
                + " " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["day"])\
                + " " + unicode(TranslateMonth(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["monthname"]))\
                + ' dont '\
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["snow_night_day"]["cm"])\
                + ' cm le jour et '\
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["snow_night"]["cm"])\
                + ' cm la nuit'

        elif ModeMeteo == "pluie":
            if data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_allday"]["mm"] != 0:

                if PluieDetecte:
                    MessagePluie = MessagePluie + ", "
                MessagePluie = MessagePluie \
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_allday"]["mm"])\
                + ' mm de pluie prevu le '\
                + str(TranslateDay(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["weekday"]))\
                + " " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["day"])\
                + " " + unicode(TranslateMonth(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["monthname"]))\
                + ' dont '\
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_day"]["mm"])\
                + ' mm le jour et '\
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_night"]["mm"])\
                + ' mm la nuit'
                PluieDetecte=True
        else:
            MessagePluie="Error"
    if ModeMeteo == "pluie" or ModeMeteo == "neige":
        if PluieDetecte:
            pass
        else:
            MessagePluie="Pas de "+ModeMeteo+" prevu dans les 10 jours a venir"
    return MessagePluie

def calculateAlert(FilenameAlert):
    pass
    # Open json file
    with open(FilenameAlert) as data_file:
        data = json.load(data_file)

    # test if API return error
    try:
        a=data["response"]["error"]
        print data["response"]["error"]["type"] + ": " + data["response"]["error"]["description"]
        ErrorParsing=True
        exit()
    except KeyError:
        pass

    # Test if alert present
    try:
        a=data["response"]["features"]["alerts"]
        pass
    except KeyError:
        print "Error: keyword alerts not found"
        ErrorParsing=True
        exit()

    # Test if alert data vide
    a=data["alerts"]
    if a:
       pass
    else:
        print "alert data empty"
        ErrorParsing=True
        exit()

    #get data
    Alerte=data["response"]["features"]["alerts"]
    TypeAlerte=data["alerts"][0]["wtype_meteoalarm_name"]
    NiveauAlerte=data["alerts"][0]["level_meteoalarm"]
    CouleurAlerte=data["alerts"][0]["level_meteoalarm_name"]
    DescriptionAlerte=data["alerts"][0]["level_meteoalarm_description"]
    DebutAlerte=data["alerts"][0]["date"]
    FinAlerte=data["alerts"][0]["expires"]

    if False:
        pprint(Alerte)
        pprint(TypeAlerte)
        pprint(NiveauAlerte)
        pprint(CouleurAlerte)
        pprint(DescriptionAlerte)
        pprint(DebutAlerte)
        pprint(FinAlerte)

    return str(TypeAlerte) + str(NiveauAlerte) + str(CouleurAlerte) + str(DescriptionAlerte) + str(DebutAlerte) + str(FinAlerte)

def getDataMeteo(APIKey,requestType,RequestCity,debug):

    if requestType == "alerts":
        req="http://api.wunderground.com/api/" + APIKey + "/alerts/lang:FR/q/" + RequestCity + ".json"
    elif requestType == "forecast":
        req="http://api.wunderground.com/api/" + APIKey + "/forecast10day/lang:FR/q/" + RequestCity + ".json"
    else:
        print usage
        exit()

    if (debug):
        print req
        return req
    else:
        handler = urllib2.urlopen(req)
        return handler.read()
