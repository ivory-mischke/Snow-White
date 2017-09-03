import os
if os.path.exists('SnowWhite.py'):
    FullFileName = os.path.abspath('SnowWhite.py')
    try:
        import appJar
        print('appJar already installed')
    except:
        try:
            print('Attempting to install appJar module...')
            os.system('sudo pip install appJar')
            print('Successfully installed appJar module')
        except:
            raise Exception("Failed to install 'appJar' module")
    try:
        import forecastio
        print('forecastio already installed')
    except:
        try:
            print('Attempting to install python-forecastio module...')
            os.system('sudo pip install python-forecastio')
            print('Successfully installed python-forecastio module')
        except:
            raise Exception("Failed to install 'python-forecastio' module")

    print('Attempting to make SnowWhite.py auto-start at boot up...')
    try:
        os.system("echo '@sudo /usr/bin/python " + FullFileName + "' >> ~/.config/lxsession/LXDE-pi/autostart")
        os.system("sudo chmod +x " + FullFileName)
        #modify /boot/config.txt add display_rotate=3
        os.system("xrandr --output HDMI1 --rotate left")
    except:
            raise Exception("Failed to make SnowWhite.py auto-start at boot up")
    print('Successfully made SnowWhite.py auto-start at boot up')
else:
    raise Exception("Cannot find SnowWhite.py file")
