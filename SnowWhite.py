from appJar import gui
from nytimesarticle import articleAPI
import time,googlemaps,forecastio

NYTAPIKey = ''
GoogleMapsAPIKey = ''
DarkSkyAPIKey = ''
Latitude = ''
Longitude =''
WeatherUpdateTime = time.time()
NewsUpdateTime = time.time()

ListOfIcons = {
    'clear-day': ".\Icons\Sun.gif",
    'wind': ".\Icons\Wind.gif",
    'cloudy': ".\Icons\Cloud.gif",
    'partly-cloudy-day': ".\Icons\PartlySunny.gif",
    'rain': ".\Icons\Rain.gif",
    'snow': ".\Icons\Snow.gif",
    'snow-thin': ".\Icons\Snow.gif",
    'fog': ".\Icons\Haze.gif",
    'clear-night': ".\Icons\Moon.gif",
    'partly-cloudy-night': ".\Icons\PartlyMoon.gif",
    'thunderstorm': ".\Icons\Storm.gif",
    'tornado': ".\Icons\Tornado.gif",
    'hail': ".\Icons\Hail.gif"
}
Weather = forecastio.load_forecast(DarkSkyAPIKey,Latitude,Longitude)
WeatherIcon = Weather.currently().icon
if WeatherIcon in ListOfIcons:
    WeatherIconImage = ListOfIcons[Weather.currently().icon]
else:
    WeatherIconImage = ''
Temperature = round(Weather.currently().temperature)

NYTAPIClient = articleAPI(NYTAPIKey)
NYTArticles = NYTAPIClient.search()
NYTHeadline = NYTArticles['response']['docs'][0]['headline']['print_headline']

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
            MagicMirror.setImage("TempIcon", UpdatedIconImage)
            WeatherIcon = UpdatedWeatherIcon
        UpdatedTemperature = round(Weather.currently().temperature)

        if UpdatedTemperature != Temperature:
            MagicMirror.setLabel("TempDegree", ' ' + str(UpdatedTemperature) + u'\u00B0')
            Temperature = UpdatedTemperature
        WeatherUpdateTime = time.time()

    if (time.time() - NewsUpdateTime) >= 3600:
        NewNYTHeadline = NYTArticles['response']['docs'][0]['headline']['print_headline']
        MagicMirror.setLabel("NYTHeadline",NewNYTHeadline)
        NewsUpdateTime = time.time()

MagicMirror = gui()
MagicMirror.setFullscreen()
MagicMirror.hideTitleBar()
MagicMirror.setBg("black")

MagicMirror.setSticky("nw")
MagicMirror.startPanedFrame("WeatherPane",0,0)
MagicMirror.setBg("black")
MagicMirror.addImage("TempIcon",WeatherIconImage)
MagicMirror.addLabel("TempDegree",' ' + str(Temperature) + u'\u00B0')
MagicMirror.getLabelWidget("TempDegree").config(font="Helvetica 98 bold")
MagicMirror.setLabelFg("TempDegree","White")
MagicMirror.stopPanedFrame()

MagicMirror.setSticky("ne")
MagicMirror.startPanedFrame("DateTimePane",0,1)
MagicMirror.setBg("black")
MagicMirror.addLabel("Time",time.strftime("%H:%M"))
MagicMirror.getLabelWidget("Time").config(font="Helvetica 98 bold")
MagicMirror.setLabelFg("Time","White")
MagicMirror.addLabel("Date",time.strftime("%m/%d/%y"))
MagicMirror.getLabelWidget("Date").config(font="Helvetica 38 bold")
MagicMirror.setLabelFg("Date","White")
MagicMirror.stopPanedFrame()

MagicMirror.setSticky("sw")
MagicMirror.startPanedFrame("NYTHeadlinePane",1,0)
MagicMirror.setBg("black")
MagicMirror.addLabel("NYTHeadline",NYTHeadline)
MagicMirror.getLabelWidget("NYTHeadline").config(font="Helvetica 38 bold")
MagicMirror.setLabelFg("NYTHeadline","White")
MagicMirror.stopPanedFrame()

MagicMirror.setSticky("se")
MagicMirror.startPanedFrame("GoogleMapsPane",1,1)
MagicMirror.setBg("black")
MagicMirror.addLabel("GoogleMapsDestination","Say: 'Set Destination (Destination)'")
MagicMirror.getLabelWidget("GoogleMapsDestination").config(font="Helvetica 38 bold")
MagicMirror.setLabelFg("GoogleMapsDestination","White")
MagicMirror.stopPanedFrame()

MagicMirror.registerEvent(Update_Labels)

MagicMirror.go()