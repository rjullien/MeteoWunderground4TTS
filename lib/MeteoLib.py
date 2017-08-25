#!/usr/bin/env python
# coding: utf8
import json
from datetime import datetime
import urllib2
# import urllib
def splitPluieJourneeNuit(pluieJour,pluieNuit):
    if pluieJour == None:
        pluieJour=0
    if pluieNuit == None:
        pluieNuit=0
    if pluieJour !=0 and pluieNuit !=0:
        MessagePluie = ", "\
        + 'dont '\
        + str(pluieJour)\
        + ' millimetre le jour et '\
        + str(pluieNuit)\
        + ' millimetre la nuit'
    elif pluieJour !=0:
        MessagePluie = u", durant la journée"
    else: # pluieJour =0 pluieNuit !0
        MessagePluie = ", durant la nuit"
    return MessagePluie
def test_answer():
    assert splitPluieJourneeNuit(0,1) == ", durant la nuit"
    assert splitPluieJourneeNuit(None,1) == ", durant la nuit"
    assert splitPluieJourneeNuit(1,0) == u", durant la journée"
    assert splitPluieJourneeNuit(1,None) == u", durant la journée"
    assert splitPluieJourneeNuit(1,2) == ", dont 1 millimetre le jour et 2 millimetre la nuit"

def splitNeigeJourneeNuit(pluieJour,pluieNuit):
    if pluieJour == None:
        pluieJour=0
    if pluieNuit == None:
        pluieNuit=0
    if pluieJour !=0 and pluieNuit !=0:
        MessagePluie = ", "\
        + 'dont '\
        + str(pluieJour).rstrip('0').rstrip('.')\
        + ' centimetre le jour et '\
        + str(pluieNuit).rstrip('0').rstrip('.')\
        + ' centimetre la nuit'
    elif pluieJour !=0:
        MessagePluie = u", durant la journée"
    else: # pluieJour =0 pluieNuit !0
        MessagePluie = ", durant la nuit"
    return MessagePluie
def test_answer():
    assert splitNeigeJourneeNuit(0,1) == ", durant la nuit"
    assert splitNeigeJourneeNuit(None,1) == ", durant la nuit"
    assert splitNeigeJourneeNuit(1,0) == u", durant la journée"
    assert splitNeigeJourneeNuit(1,None) == u", durant la journée"
    assert splitNeigeJourneeNuit(1,2) == ", dont 1 centimetre le jour et 2 centimetre la nuit"

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
def test_answer():
    assert TranslateDay("Monday") == "Lundi"
    assert TranslateDay("Tuesday") == "Mardi"
    assert TranslateDay("Wednesday") == "Mercredi"
    assert TranslateDay("Thursday") == "Jeudi"
    assert TranslateDay("Friday") == "Vendredi"
    assert TranslateDay("Saturday") == "Samedi"
    assert TranslateDay("Sunday") == "Dimanche"
    assert TranslateDay("Mardi") == "Mardi"

def TranslateMonth(MonthEnglish):
    if MonthEnglish == "January":
        MonthFrench = "Janvier"
    elif MonthEnglish == "February":
        MonthFrench = "Fevrier"
    elif MonthEnglish == "March":
        MonthFrench = "Mars"
    elif MonthEnglish == "April":
        MonthFrench = "Avril"
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
def test_answer():
    assert TranslateMonth("January") == "Janvier"
    assert TranslateMonth("February") == "Fevrier"
    assert TranslateMonth("March") == "Mars"
    assert TranslateMonth("April") == "Avril"
    assert TranslateMonth("May") == "Mai"
    assert TranslateMonth("June") == "Juin"
    assert TranslateMonth("July") == "Juillet"
    assert TranslateMonth("August") == "Aout"
    assert TranslateMonth("September") == "Septembre"
    assert TranslateMonth("October") == "Octobre"
    assert TranslateMonth("November") == "Novembre"
    assert TranslateMonth("December") == "Decembre"
    assert TranslateMonth("Decembre") == "Decembre"

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
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["snow_allday"]["cm"]).rstrip('0').rstrip('.')\
                + ' centimetre de neige prevu le '\
                + str(TranslateDay(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["weekday"]))\
                + " " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["day"])\
                + " " + unicode(TranslateMonth(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["monthname"]))\
                + splitNeigeJourneeNuit(data["forecast"]["simpleforecast"]["forecastday"][i]["snow_day"]["cm"],data["forecast"]["simpleforecast"]["forecastday"][i]["snow_night"]["cm"])
                PluieDetecte=True
        elif ModeMeteo == "pluie":
            if data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_allday"]["mm"] != 0:

                if PluieDetecte:
                    MessagePluie = MessagePluie + "... "
                MessagePluie = MessagePluie \
                + str(data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_allday"]["mm"])\
                + ' millimetre de pluie prevu le '\
                + str(TranslateDay(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["weekday"]))\
                + " " + str(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["day"])\
                + " " + unicode(TranslateMonth(data["forecast"]["simpleforecast"]["forecastday"][i]["date"]["monthname"]))\
                + splitPluieJourneeNuit(data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_day"]["mm"],data["forecast"]["simpleforecast"]["forecastday"][i]["qpf_night"]["mm"])
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

    DebutAlerteDate=datetime.strptime(DebutAlerte, '%Y-%m-%d %H:%M:%S GMT')
    DebutAlerte=datetime.strftime(DebutAlerteDate,'le %A %d %B a %H heures GMT').replace(' 0', ' ')
    FinAlerteDate=datetime.strptime(FinAlerte, '%Y-%m-%d %H:%M:%S GMT')
    FinAlerte=datetime.strftime(FinAlerteDate,'le %A %d %B a %H heures GMT').replace(' 0', ' ')
    if False:
        pprint(Alerte)
        pprint(TypeAlerte)
        pprint(NiveauAlerte)
        pprint(CouleurAlerte)
        pprint(DescriptionAlerte)
        pprint(DebutAlerte)
        pprint(FinAlerte)

    return "Alerte "+ str(TypeAlerte) + " de niveau " + str(CouleurAlerte) + "..." + str(DescriptionAlerte) + "..."  + str(DebutAlerte) + "..." + str(FinAlerte)

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
        # handler = urllib.urlopen(req)
        handler = urllib2.urlopen(req)
        return handler.read()
