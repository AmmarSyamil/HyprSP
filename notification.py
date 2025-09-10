from PySide6.QtWidgets import QWidget
# from compiled.ui_list_widget import Ui_Form?
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
import webbrowser
import platform
from pathlib import Path
from compiled.ui_notification import Ui_Form
import compiled.resources_rc as resources_rc
from data import app_list
from config import *

class notification_widget(QWidget, Ui_Form):
    def __init__(self, app, app_type, url=None):
        super().__init__()

        self.setupUi(self)
        self.url = url
        self.type = type
        self.app_type = app_type
        self.setFixedSize(50,50)
        self.setMaximumSize(QSize(50,50))
        self.setup()
        
    def wsl(self):
        try:
            if "Microsofst" in platform.release() or "microsoft-standard-WSL" in platform.release():
                print("Python is running in WSL.")
                return True

            
        except Exception as e:
            return False
            # else:
                # print("Python is not running in WSL.")
    

    def setup(self):
        # done = False
        for i in APP_LIST_EXTENTION_FILE:
            try:
                path = f":/logo/{self.app.lower()}.{i}"
                if i == "gif": #//////////////////////////////////////////////////////////////////////////////////////
                    movie = QMovie(path)
                    if movie:
                        self.logo.setMovie(movie)
                        movie.start()
                        break
                else:
                    logo = QPixmap(path)
                    if not logo.isNull():
                        self.logo.setPixmap(logo)
                        break
            except Exception as e:
                pass

            
        # for i, u in app_list.items():
            
            # if self.wsl():
            #     print("womp womp")
            # if self.os_name == "Windows":
            #     webbrowser.open(self.url, new=2)
            # elif self.os_name == "Linux":
            #     webbrowser.open(self.url, new=2)
            # elif self.os_name == "Darwin":
            #     webbrowser.open(self.url, new=2)
            pass
        

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print(self.url)
            if self.app_type == "web":
                webbrowser.open(self.url, new=2)
            elif self.app_type == "local":
                try:
                    subprocess.Popen(self.url)
                except Exception as e:
                    raise e
                
        # super().mousePressEvent(event)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = notification_widget("Discord", "https://www.discord.com")
    w.show()
    sys.exit(app.exec())


# os_name = platform.system()
# print(f"Operating System: {os_name}")




