from PySide6.QtWidgets import QWidget
# from compiled.ui_list_widget import Ui_Form?
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
import platform
from pathlib import Path
from compiled.ui_notification import Ui_Form
import compiled.resources_rc as resources_rc
# from data import app_list
from config import *
from extra.web import Web_Engine

from compiled.page_hackatime_ui import Ui_Form
# import requests

class notification_widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        # self.setup_widget(self.total_time_label, "")

        # self.side_style.setpixmap(PAGE_HACKATIME_FLIPVIEW)

        if MAIN_ART_TYPE == "video":
            movie = QMovie(MAIN_ART)
            self.side_style.setMovie(movie)
            movie.start()
        else:
            pixmap = QPixmap(MAIN_ART)
            self.side_style.setPixmap(pixmap)
            self.side_style.setScaledContents(True)

        
    def setup_widget(self, widget_setup,  url):
        w = Web_Engine(url) 
        w.setParent(widget_setup.parentWidget())
        w.setGeometry(widget_setup.geometry())

        widget_setup.hide()
        widget_setup.deleteLater()

        widget_setup = w
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = notification_widget()
    w.show()
    sys.exit(app.exec())




