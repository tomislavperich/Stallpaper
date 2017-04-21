import ctypes, time, sys, os
from bs4 import BeautifulSoup
try: import urllib.request as ul
except ImportError: import urllib as ul


updateInterval = 10
imageName = "Stallpaper.jpg"
imageDir = os.getenv("APPDATA")+"\\Stallpaper"
saveLocation = os.path.join(imageDir, imageName)

def checkDir():
    if not os.path.exists(imageDir):
        os.makedirs(imageDir)

def updateImage():
    baseUrl = "https://rms.sexy"
    try:
        html = BeautifulSoup(ul.urlopen(baseUrl).read(), "html.parser")
        imageUrl = html.findAll("img",{"class":"stallman"})[0].get("src")
        ul.urlretrieve(baseUrl + imageUrl, saveLocation)
        print("[*] Downloaded image")
    except:
        print("[x] Unable to download image\n    Attempting again in 10 seconds...")
        time.sleep(10)
        updateImage()

def setWallpaper():
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, saveLocation, 0)
        print("[*] Wallpaper changed")
    except:
        print("[x] Unable to set wallpaper")


# Run script
while True:
    checkDir()
    updateImage()
    setWallpaper()
    time.sleep(updateInterval)
