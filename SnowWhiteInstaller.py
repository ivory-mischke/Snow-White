import os
import fileinput
import subprocess
import re
#ScreenOrientation = 'Landscape'
ScreenOrientation = 'Portrait'

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
    except:
            raise Exception("Failed to make SnowWhite.py auto-start at boot up")
    print('Successfully made SnowWhite.py auto-start at boot up')
else:
    raise Exception("Cannot find SnowWhite.py file")

ScreenSaverCheck = subprocess.Popen(['grep','xserver-command=X -s 0 -dpms', '/etc/lightdm/lightdm.conf'], stdout=subprocess.PIPE).communicate()[0]
if not re.search('xserver-command=X -s 0 -dpms', ScreenSaverCheck):
    os.system('sudo echo "xserver-command=X -s 0 -dpms" >> /etc/lightdm/lightdm.conf')
    print('Successfully turned off screen saver')
else:
    print('Screen saver already turned off')

if ScreenOrientation == 'Portrait':
    ScreenOrientationCheck = subprocess.Popen(['grep','display_rotate', '/boot/config.txt'], stdout=subprocess.PIPE).communicate()[0]
    if re.search('display_rotate', ScreenOrientationCheck):
        for line in fileinput.input('/boot/config.txt', inplace = True):
            if re.search('display_rotate', line):
                DisplayRotateLine = (re.search('display_rotate', line)).string
                print line.replace(DisplayRotateLine, "display_rotate=3")
            else:
                print line
    else:
        os.system('sudo echo "display_rotate=3" >> /boot/config.txt')
    print("Portrait display has been set.")
