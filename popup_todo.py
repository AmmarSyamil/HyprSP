from PySide6.QtWidgets import QWidget
# from compiled.page_main_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize, QDateTime, QDate
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
from pathlib import Path
import importlib.util
import sys
from qfluentwidgets.components.widgets.line_edit import TextEdit

from compiled.popup_edt_ui import Ui_Form
from config import *
from extra.specs import Specs
from extra.web import Web_Engine
# from compiled.ui_notification import
from notification import notification_widget
from todo_class import Todo
from datetime import datetime

class list_widget(QMainWindow, Ui_Form):
    def __init__(self, title=None, desc=None, priorities=None, deadline=datetime.now(), completed=False):
        super().__init__()

        self.setupUi(self)
        # self.setup()



        self.todo = Todo(DATA)

        self.title_input.setText(title)
        self.description_input.setText(desc)
        self.completed.setChecked(completed)

        self.date = QDateTime(
            deadline.year, 
            deadline.month, 
            deadline.day, 
            deadline.hour,
            deadline.minute,
            deadline.second
        )

        self.deadline_input.setDate(self.date.date())
        self.time_deadline_input.setTime(self.date.time())



        self.save.clicked.connect(self.save_func)
        self.dell.clicked.connect(self.del_func)
        self.cancel.clicked.connect(self.cancel_func)

        self.priorities_input.addItems(["Important", "Normal", "Not important"])


    
    # def _priorities(self):

    # def setup(self):


    




    def save_func(self):
        # print(self.title_input.text())
        add = self.todo.add_todo(
            title=self.save.text(),
            description=self.description_input.toPlainText(),
            deadline=[self.deadline_input.getDate(), self.time_deadline_input.getTime()],
            importance=self.priorities_input.text(),
            status=self.completed.isChecked()
        )

        if add:
            raise add
        self.close()
    
    def del_func(self, id):
        print(self.priorities_input.text())
        # ?pass
        dell = self.todo.delete(
            id=id
        )

        if dell:
            raise dell
        self.close()

    def cancel_func(self):
        self.close()

        # self.

    # def setup(self):

       


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = list_widget()
    w.show()
    sys.exit(app.exec())

