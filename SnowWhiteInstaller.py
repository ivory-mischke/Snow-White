import os
if os.path.exists('/SnowWhite.py'):
    FullFileName = os.path.abspath('/SnowWhite.py')
    try:
        import appJar
        print('appJar already installed')
    except:
        try:
            print('Attempting to install appJar module...')
            os.system('pip install appJar')
            print('Successfully installed appJar module')
        except:
            raise Exception("Failed to install 'appJar' module")
    try:
        import googlemaps
        print('googlemaps already installed')
    except:
        try:
            print('Attempting to install googlemaps module...')
            os.system('pip install googlemaps')
            print('Successfully installed googlemaps module')
        except:
            raise Exception("Failed to install 'googlemaps' module")
    try:
        import forecastio
        print('forecastio already installed')
    except:
        try:
            print('Attempting to install python-forecastio module...')
            os.system('pip install python-forecastio')
            print('Successfully installed python-forecastio module')
        except:
            raise Exception("Failed to install 'python-forecastio' module")

    print('Attempting to make SnowWhite.py auto-start at boot up...')
    try:
        os.system("echo '@sudo /usr/bin/python " + FullFileName + "' >> ~/.config/lxsession/LXDE-pi/autostart")
        os.system("sudo chmod +x " + FullFileName)
        os.system("xrandr --output HDMI1 --rotate left")
    except:
            raise Exception("Failed to make SnowWhite.py auto-start at boot up")
    print('Successfully made SnowWhite.py auto-start at boot up')
else:
    raise Exception("Cannot find SnowWhite.py file")