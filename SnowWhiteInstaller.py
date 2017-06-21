import os
if os.path.exists('/SnowWhite.py'):
    FullName = os.path.abspath('/SnowWhite.py')
    try:
        import appJar
        print('appJar already installed')
    except ModuleNotFoundError:
        try:
            print('Attempting to install appJar module...')
            os.system('pip3 install appJar')
            print('Successfully installed appJar module')
        except:
            raise "Failed to install 'appJar' module"
    try:
        import nytimesarticle
        print('nytimesarticle already installed')
    except ModuleNotFoundError:
        try:
            print('Attempting to install nytimesarticle module...')
            os.system('pip3 install nytimesarticle')
            print('Successfully installed nytimesarticle module')
        except:
            raise "Failed to install 'nytimesarticle' module"
    try:
        import googlemaps
        print('googlemaps already installed')
    except ModuleNotFoundError:
        try:
            print('Attempting to install googlemaps module...')
            os.system('pip3 install googlemaps')
            print('Successfully installed googlemaps module')
        except:
            raise "Failed to install 'googlemaps' module"
    try:
        import forecastio
        print('forecastio already installed')
    except ModuleNotFoundError:
        try:
            print('Attempting to install python-forecastio module...')
            os.system('pip3 install python-forecastio')
            print('Successfully installed python-forecastio module')
        except:
            raise "Failed to install 'python-forecastio' module"

    print('Attempting to create crontab entry...')
    os.system("crontab -l > /tmp/cronfile.txt")
    os.system("echo '@reboot python " + FullName + "' >> /tmp/cronfile.txt")
    os.system("crontab < /tmp/cronfile.txt")
    os.system("rm /tmp/cronfile.txt")
    print('Successfully created crontab entry')
else:
    raise "Cannot find SnowWhite.py file"