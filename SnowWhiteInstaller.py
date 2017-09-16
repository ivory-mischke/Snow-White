import os
import fileinput
import subprocess
import re
ScreenOrientation = 'Landscape'
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
    AutoStartCheck = subprocess.Popen(['grep','@/usr/bin/python ' + FullFileName, '/home/pi/.config/lxsession/LXDE-pi/autostart'], stdout=subprocess.PIPE).communicate()[0]
    if not re.search('@/usr/bin/python', AutoStartCheck):
        os.system("echo '@/usr/bin/python " + FullFileName + "' >> /home/pi/.config/lxsession/LXDE-pi/autostart")
        os.system("sudo chmod +x " + FullFileName)
        print('Snow White Application has been set to Auto Start')
    else:
        print('Snow White Application has already been set to Auto Start')
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
                    print(line.replace(DisplayRotateLine, "display_rotate=3"))
                else:
                    print(line,)
            print("Portrait display has been set.")
        else:
            os.system('sudo echo "display_rotate=3" >> /boot/config.txt')
            print("Portrait display has been set.")        
    else:
        ScreenOrientationCheck = subprocess.Popen(['grep','display_rotate', '/boot/config.txt'], stdout=subprocess.PIPE).communicate()[0]
        if re.search('display_rotate', ScreenOrientationCheck):
            for line in fileinput.input('/boot/config.txt', inplace = True):
                if re.search('display_rotate', line):
                    DisplayRotateLine = (re.search('display_rotate', line)).string
                    print(line.replace(DisplayRotateLine, "display_rotate=0"))
                else:
                    print(line,)
            print("Landscape display has been set.")
        else:
            os.system('sudo echo "display_rotate=0" >> /boot/config.txt')
            print("Landscape display has been set.")        
        
else:
    raise Exception("Cannot find SnowWhite.py file")

