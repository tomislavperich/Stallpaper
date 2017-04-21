# Use urllib2 for Python 2.x
import urllib.request, ctypes, os
from bs4 import BeautifulSoup


baseUrl = "https://rms.sexy"
# Update/download wallpaper
try:
    html = BeautifulSoup(urllib.request.urlopen(baseUrl).read(), "html.parser")
    imageUrl = html.findAll("img",{"class":"stallman"})[0].get("src")
    urllib.request.urlretrieve(baseUrl + imageUrl, "Stallpaper.jpg")
    print("[*] Downloaded image")
except:
    print("[x] Unable to download image")

# Set wallpaper
try:
    # Windows
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "Stallpaper.jpg", 0)
    print("[*] Wallpaper changed")
else:
    # Linux
    import commands
    command = "gconftool-2 --set /desktop/gnome/background/picture_filename --type string 'stallpaper.jpg'"
    status, output = commands.getstatusoutput(command)  # status=0 if success
    print("[*] Wallpaper changed")
except:
    print("[x] Unable to set wallpaper")
