import os, shutil
import random
import time
import getpass

USERNAME = getpass.getuser() #Gets the username for the location.
PICTURE = "/home/"+ USERNAME +"/Pictures/"
PATH = PICTURE + "Wallpaper/"
USEDWALLPAPER = PICTURE + "UsedWallpaper/"

def reuseWallpaper(): # this function reuses all used wallpaper if the wallpaper folder is empty
    os.chdir(PICTURE)
    os.rmdir(PATH)
    os.rename(USEDWALLPAPER, PATH)
    os.mkdir(USEDWALLPAPER)


def moveUsedWallpaper(filename): #This function is to move the used wallpaper to usedwallpaper folder as not to repeat the used wallpaper.
    if not os.path.isdir(USEDWALLPAPER):
        os.chdir(PICTURE)
        os.mkdir("UsedWallpaper")
    path = PATH +"/" + filename
    usedWallpaperPath = USEDWALLPAPER +"/" + filename
    try:
        shutil.move(path, usedWallpaperPath)
    except Exception as e:
        print("Move failed.!!>> "+ e)



def main():
    os.chdir(PATH)
    wallpapers = os.listdir()
    try:
        wallpaper = random.choice(wallpapers)
    except:
        reuseWallpaper()
        wallpaper = random.choice(wallpapers)
    moveUsedWallpaper(wallpaper)
    path = USEDWALLPAPER + "\'" + wallpaper + "\'"
    cmd = "gsettings set org.gnome.desktop.background picture-uri file:////" + path
    print(cmd)
    os.system(cmd)
    #time.sleep(0.5)
    

if __name__ == "__main__":
	main()
