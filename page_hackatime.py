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
# from data import app_list
from config import *

from compiled.page_hackatime_ui import Ui_Form

class notification_widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = notification_widget()
    w.show()
    sys.exit(app.exec())




