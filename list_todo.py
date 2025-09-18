from PySide6.QtWidgets import QWidget
# from compiled.page_main_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize, Signal
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
from pathlib import Path
import importlib.util
import sys
from qfluentwidgets import *
from config import *
from extra.specs import Specs
from extra.web import Web_Engine
# from compiled.ui_notification import
from notification import notification_widget
from todo_class import Todo
from datetime import datetime

from compiled.list_todo_ui import Ui_Form

class AppCard(QWidget, Ui_Form):
    clicked = Signal()

    def __init__(self , title, due_in, completed, priorities, parent=None, is_list=False):
            super().__init__(parent)
            print(f"AppCard: Initializing with title={title}, due_in={due_in}, completed={completed}, priorities={priorities}, is_list={is_list}")
            self.setupUi(self)
            print("AppCard: setupUi called")
            self.title_label.setText(title)
            self.due_in_label.setText(due_in)
            self.prioritize_label.setText(str(priorities))
            self.completed_label.setChecked(bool(completed))

            if is_list:
                print("AppCard: is_list True, adjusting layout")
                self.layoutWidget.setParent(None)
                self.setLayout(self.horizontalLayout)
                self.layoutWidget.deleteLater()
                self.setMinimumHeight(60)
                self.setMaximumHeight(80)
                self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            else:
                self.setMinimumHeight(19)
                self.setMaximumHeight(22)
                self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AppCard(title="TS PMO", due_in="sybau", priorities="41", completed=True)
    w.show()
    sys.exit(app.exec())
