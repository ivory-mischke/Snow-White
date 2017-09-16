import os
import fileinput
#ScreenOrientation = 'Landscape'
#ScreenOrientation = 'Portrait'

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

ScreenSaverCheck = os.system('cat /etc/lightdm/lightdm.conf | grep "xserver-command=X -s 0 -dpms"')
if ScreenSaverCheck != "xserver-command=X -s 0 -dpms":
    os.system('sudo echo "xserver-command=X -s 0 -dpms" >> /etc/lightdm/lightdm.conf')
    print('Successfully turned off screen saver')
else:
    print('Screen saver already turned off')

if ScreenOrientation == 'Portrait':
    ScreenOrientationCheck = os.system('cat /boot/config.txt | grep "display_rotate"')
    if "dispay_rotate" in ScreenOrientationCheck:
        for line in fileinput.input('/boot/config.txt', inplace = True):
            print line.replace("*display_rotate*", "display_rotate=3")
    else:
        os.system('sudo echo "display_rotate=3" >> /boot/config.txt')
        print("Portrait display has been set.")