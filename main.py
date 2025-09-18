import sys
import json
from typing import Tuple

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QSizePolicy
# from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize, QTime, QColor
from PySide6.QtGui import QPixmap, QMovie, QCursor, QColor
# from PySide6.QtUiTools import QUiLoader

# from compiled.ui_main import Ui_MainWindow
# from list_widget import list_widget
# from todo import Todo
# from datetime import datetime
# from edit_popup_widget import Edit_popup_widget
# from notification import notification_widget
# # from data import app_list
# from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
# from PySide6.QtWebEngineWidgets import QWebEngineView
# from extra.web import Web_Engine as HackaTime

from config import *
from qfluentwidgets.components.widgets.line_edit import TextEdit
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont, Theme, setTheme
from qfluentwidgets import FluentIcon as FIF
# from qfluentwidgets import 

from page_main import list_widget as main_page
from page_todo import list_widget as todo_page

class Main(FluentWindow):
    def __init__(self):
        super().__init__()
        

        # self.setupUi(self)

        self.homePage = main_page()
        self.todoPage = todo_page()

        # self.homePage.setObjectName("home")
        self.todoPage.setObjectName("todo")

    
        self.initNavigation()
        self.setup()



    def initNavigation(self):
        self.addSubInterface(self.homePage, FIF.HOME, 'Home')
        self.addSubInterface(self.todoPage, FIF.LABEL, 'Todo')
        pass
    
    def setup(self):
        self.resize(850,450)
        self.titleBar.maxBtn.hide()
        self.titleBar.setDoubleClickEnabled(False)
        self.setCustomBackgroundColor(QColor(30, 30, 30), QColor(20, 20, 20))
        self.setWindowTitle('HypSP')





if __name__ == "__main__":
    setTheme(Theme.DARK)
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    w.setMicaEffectEnabled(True)
    sys.exit(app.exec())
