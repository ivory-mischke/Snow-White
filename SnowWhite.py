from appJar import gui
import time,googlemaps,forecastio,requests,random

GoogleMapsAPIKey = ''
NYTAPIKey = ''
DarkSkyAPIKey = ''
Latitude = ''
Longitude = ''
WeatherUpdateTime = time.time()
NewsUpdateTime = time.time()

ListOfIcons = {
    'clear-day': "./Icons/Sun.gif",
    'wind': "./Icons/Wind.gif",
    'cloudy': "./Icons/Cloud.gif",
    'partly-cloudy-day': "./Icons/PartlySunny.gif",
    'rain': "./Icons/Rain.gif",
    'snow': "./Icons/Snow.gif",
    'snow-thin': "./Icons/Snow.gif",
    'fog': "./Icons/Haze.gif",
    'clear-night': "./Icons/Moon.gif",
    'partly-cloudy-night': "./Icons/PartlyMoon.gif",
    'thunderstorm': "./Icons/Storm.gif",
    'tornado': "./Icons/Tornado.gif",
    'hail': "./Icons/Hail.gif"
}
Weather = forecastio.load_forecast(DarkSkyAPIKey,Latitude,Longitude)
WeatherIcon = Weather.currently().icon
WeatherSummary = Weather.hourly().summary
if WeatherIcon in ListOfIcons:
    WeatherIconImage = ListOfIcons[Weather.currently().icon]
else:
    WeatherIconImage = ''
Temperature = round(Weather.currently().temperature)

NYTAPIRequest = requests.get("https://api.nytimes.com/svc/topstories/v2/home.json?api-key=" + NYTAPIKey)
NYTArticles = NYTAPIRequest.json()
NYTHeadline1 = NYTArticles['results'][random.randrange(0,NYTArticles['num_results'])]['title']
NYTHeadline2 = NYTArticles['results'][random.randrange(0,NYTArticles['num_results'])]['title']
while NYTHeadline2 == NYTHeadline1:
    NYTHeadline2 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']
NYTHeadline3 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']
while NYTHeadline3 == NYTHeadline1 or NYTHeadline3 == NYTHeadline2:
    NYTHeadline3 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']

def Update_Labels():
    CurrentTime = time.strftime("%H:%M")
    CurrentDate = time.strftime("%m/%d/%y")
    global WeatherUpdateTime
    global NewsUpdateTime
    global WeatherIcon
    global Temperature

    if CurrentDate != MagicMirror.getLabel("Date"):
        MagicMirror.setLabel("Date",CurrentDate)
    if CurrentTime != MagicMirror.getLabel("Time"):
        MagicMirror.setLabel("Time",CurrentTime)

    if (time.time() - WeatherUpdateTime) >= 1800:
        #Update the weather every 30 minutes
        Weather.update()
        UpdatedWeatherIcon = Weather.currently().icon
        if UpdatedWeatherIcon != WeatherIcon:
            if UpdatedWeatherIcon in ListOfIcons:
                UpdatedIconImage = ListOfIcons[UpdatedWeatherIcon]
            else:
                UpdatedIconImage = ''
            MagicMirror.setImage("TempIcon",UpdatedIconImage)
            WeatherIcon = UpdatedWeatherIcon
        UpdatedTemperature = round(Weather.currently().temperature)

        if UpdatedTemperature != Temperature:
            MagicMirror.setLabel("TempDegree",str(UpdatedTemperature) + u'\u00B0')
            Temperature = UpdatedTemperature
        WeatherUpdateTime = time.time()

    if (time.time() - NewsUpdateTime) >= 3600:
        NYTAPIRequest = requests.get("https://api.nytimes.com/svc/topstories/v2/home.json?api-key=" + NYTAPIKey)
        NYTArticles = NYTAPIRequest.json()
        NewNYTHeadline1 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']
        NewNYTHeadline2 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']
        while NewNYTHeadline2 == NewNYTHeadline1:
            NewNYTHeadline2 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']
        NewNYTHeadline3 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']
        while NewNYTHeadline3 == NewNYTHeadline1 or NewNYTHeadline3 == NewNYTHeadline2:
            NewNYTHeadline3 = NYTArticles['results'][random.randrange(0, NYTArticles['num_results'])]['title']
        MagicMirror.setLabel("NYTHeadline1",NewNYTHeadline1)
        MagicMirror.setLabel("NYTHeadline2", NewNYTHeadline2)
        MagicMirror.setLabel("NYTHeadline3", NewNYTHeadline3)
        NewsUpdateTime = time.time()

MagicMirror = gui()
MagicMirror.setFullscreen()
MagicMirror.setBg("black")

MagicMirror.setSticky("nw")
MagicMirror.startPanedFrame("WeatherPane",0,0)
MagicMirror.setBg("black")
MagicMirror.addImage("TempIcon",WeatherIconImage)
MagicMirror.addLabel("TempDegree",str(Temperature) + u'\u00B0')
MagicMirror.getLabelWidget("TempDegree").config(font="Helvetica 40 bold")
MagicMirror.setLabelFg("TempDegree","White")
MagicMirror.addLabel("TempSummary",WeatherSummary)
MagicMirror.getLabelWidget("TempSummary").config(font="Helvetica 20 bold")
MagicMirror.setLabelFg("TempSummary","White")
MagicMirror.setLabelAlign("TempSummary","left")
MagicMirror.stopPanedFrame()

MagicMirror.setSticky("ne")
MagicMirror.startPanedFrame("DateTimePane",0,1)
MagicMirror.setBg("black")
MagicMirror.addLabel("Time",time.strftime("%H:%M"))
MagicMirror.getLabelWidget("Time").config(font="Helvetica 40 bold")
MagicMirror.setLabelFg("Time","White")
MagicMirror.addLabel("Date",time.strftime("%m/%d/%y"))
MagicMirror.getLabelWidget("Date").config(font="Helvetica 30 bold")
MagicMirror.setLabelFg("Date","White")
MagicMirror.stopPanedFrame()
MagicMirror.setSticky("sw")
MagicMirror.startPanedFrame("NYTHeadlinePane",1,0)
MagicMirror.setBg("black")
MagicMirror.addLabel("NYTHeadline1",NYTHeadline1)
MagicMirror.getLabelWidget("NYTHeadline1").config(font="Helvetica 8 bold")
MagicMirror.setLabelFg("NYTHeadline1","White")
MagicMirror.setLabelAlign("NYTHeadline1","left")
MagicMirror.addLabel("NYTHeadline2",NYTHeadline2)
MagicMirror.getLabelWidget("NYTHeadline2").config(font="Helvetica 8 bold")
MagicMirror.setLabelFg("NYTHeadline2","White")
MagicMirror.setLabelAlign("NYTHeadline2","left")
MagicMirror.addLabel("NYTHeadline3",NYTHeadline3)
MagicMirror.getLabelWidget("NYTHeadline3").config(font="Helvetica 8 bold")
MagicMirror.setLabelFg("NYTHeadline3","White")
MagicMirror.setLabelAlign("NYTHeadline3","left")
MagicMirror.stopPanedFrame()

MagicMirror.setSticky("se")
MagicMirror.startPanedFrame("GoogleMapsPane",1,1)
MagicMirror.setBg("black")
MagicMirror.addLabel("GoogleMapsDestination","Say: 'Set Destination (Destination)'")
MagicMirror.getLabelWidget("GoogleMapsDestination").config(font="Helvetica 8 bold")
MagicMirror.setLabelFg("GoogleMapsDestination","White")
MagicMirror.stopPanedFrame()

MagicMirror.registerEvent(Update_Labels)

MagicMirror.go()