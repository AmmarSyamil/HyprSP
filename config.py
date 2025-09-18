# Helper for resource paths (PyInstaller compatible)
def resource_path(relative_path):
    import sys, os
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path
#Config file
from compiled import resources_rc
from pathlib import Path
import subprocess
from data import DATA
import os
from itertools import chain

# Config file for this project
# Run this code to compile all ui and qrc file


MAIN_ART = resource_path("images/herta.gif")
MAIN_ART_TYPE = "video"
EDIT_POPUP_ART = resource_path("images/1.png")
EDIT_POPUP_ART_TYPE = "image"
DATA = DATA

PAGE_MAIN_FLIPVIEW = [resource_path("images/bg3.png"), resource_path('images/bg4.png')]
PAGE_HACKATIME_FLIPVIEW = [resource_path("images/herta.gif")]
PAGE_TODO_FLIPVIEW = [resource_path("images/1.png")]

PAGE_MAIN_BAGROUND = resource_path("images/bg.jpg")
PAGE_TODO_BAGROUND = resource_path("images/bg5.jpg")



APP_LIST = {
    #Example
    #APP_NAME :
        # {
        #     "address":"web address for web or exe address for local",
        #     "icon" : "APP_ICON_PATH",
        #     "app_type": "web/local"
        # }

    "Slack": 
        {
            "address":"https://www.slack.com",
            "icon" : resource_path("images/logo/slack.png"),
            "app_type": "web"
        },
    "Instagram": 
        {
            "address":"https://www.instagram.com",
            "icon" : resource_path("images/logo/instagram.png"),
            "app_type": "web"
        },
    "Discord": 
        {
            "address": "https://www.discord.com",
            "icon" : resource_path("images/logo/discord.jpg"),
            "app_type": "web"
        },
    "Reddit" :
        {
            "address": "https://www.reddit.com",
            "icon" : resource_path("images/logo/reddit.png"),
            "app_type": "web"
        },
    "Spotify" :
        {
            "address": r"C:\Users\ASUS\AppData\Roaming\Spotify\Spotify.exe",
            "icon" : resource_path("images/logo/spotify.png"),
            "app_type": "local"
        }
    }

APP_LIST_EXTENTION_FILE = ["png", "jpg", "jpeg", "gif"]


HACKATIME_WIDGET_API = "https://github-readme-stats.hackclub.dev/api/wakatime?username=2455&api_domain=hackatime.hackclub.com&theme=darcula&custom_title=Hackatime+Stats&layout=compact&cache_seconds=0&langs_count=12"

import sys
import os
from pathlib import Path
if hasattr(sys, '_MEIPASS'):
    UI_FOLDER_PATH = Path(os.path.join(sys._MEIPASS, 'ui'))
else:
    UI_FOLDER_PATH = Path('./ui')
UI_FILE = [f for f in os.listdir(UI_FOLDER_PATH) if f.endswith('.ui')]
QRC_FILE = "resources.qrc"
COMPILED_AT = Path('./compiled')

if __name__ == '__main__':
    
    for name in chain(UI_FILE, (QRC_FILE,)):
        src = UI_FOLDER_PATH / name
        if not src.exists():
            continue

        try:
            if name.endswith(".ui"):
                out = COMPILED_AT / f"{src.stem}_ui.py" 
                subprocess.run(["pyside6-uic", str(src), "-o", str(out)], check=True)

            elif name.endswith(".qrc"):
                out = COMPILED_AT / f"{src.stem}_rc.py"   
                subprocess.run(["pyside6-rcc", str(src), "-o", str(out)], check=True)

        except subprocess.CalledProcessError as e:
            raise e