#Config file
from compiled import resources_rc
from pathlib import Path
import subprocess

# Config file for this project
# Run this code to compile all ui and qrc file

MAIN_ART = ":/images/herta.gif"
MAIN_ART_TYPE = "video"
EDIT_POPUP_ART = ":/images/1.png"
EDIT_POPUP_ART_TYPE = "image"

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
            "icon" : ":/logo/slack.png",
            "app_type": "web"
        },
    "Instagram":
        {
            "address":"https://www.instagram.com",
            "icon" : ":/logo/instagram",
            "app_type": "web"
        },
    "Discord": 
        {
            "address": "https://www.discord.com",
            "icon" : ":/logo/discord.jpg",
            "app_type": "web"
        },
    "Reddit" :
        {
            "address": "https://www.reddit.com",
            "icon" : ":/logo/reddit",
            "app_type": "web"
        },
    "Spotify" :
        {
            "address": r"C:\Users\ASUS\AppData\Roaming\Spotify\Spotify.exe",
            "icon" : ":/logo/spotify.png",
            "app_type": "local"
        }
    }

APP_LIST_EXTENTION_FILE = ["png", "jpg", "jpeg", "gif"]

HACKATIME_WIDGET_API = "https://github-readme-stats.hackclub.dev/api/wakatime?username=2455&api_domain=hackatime.hackclub.com&theme=darcula&custom_title=Hackatime+Stats&layout=compact&cache_seconds=0&langs_count=12"



STRUCTURE = {
    "ui" : {
        "ui/edit_popup.ui": "compiled/edit_popup.py",
        "ui/hackatime.ui": "compiled/hackatime.py",
        "ui/list.ui": "compiled/ui_list.py",
        "ui/main.ui": "compiled/ui_main.py",
        "ui/notification.ui": "compiled/ui_notification.py",
    },

    "qrc" : {
        "resources.qrc" : "compiled/resources_rc.py"
    }
}


if __name__ == '__main__':
    
    for i,v in STRUCTURE.items():
        if i =="ui":
            for u, c in v.items():
                try:
                    run = subprocess.Popen(["pyside6-uic", u, "-o", c])
                    output = run.communicate()[0]
                except Exception as e:
                    raise e
        elif i == "qrc":
            for u, c in v.items():
                try:
                    run = subprocess.Popen(["pyside6-rcc", u, "-o", c])
                    output = run.communicate()[0]
                except Exception as e:
                    raise e
        else:
            raise "WIERD FORMAT FOUND U LIL CUTIE"
