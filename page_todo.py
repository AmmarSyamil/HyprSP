from PySide6.QtWidgets import QWidget
# from compiled.page_main_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
from pathlib import Path
import importlib.util
import sys
from qfluentwidgets.components.widgets.line_edit import TextEdit

from compiled.page_todo_ui import Ui_Form
from config import *
from extra.specs import Specs
from extra.web import Web_Engine
# from compiled.ui_notification import
from notification import notification_widget

class list_widget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.todo_add.isPressed.connect(self.button_add)
        
    def button_add(self):
        #open up 
        pass

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = list_widget()
    w.show()
    sys.exit(app.exec())

