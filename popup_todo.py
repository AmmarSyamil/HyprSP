from PySide6.QtWidgets import QWidget, QDialog
# from compiled.page_main_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize, QDateTime, QDate, Signal
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

class List_widget(QDialog, Ui_Form):
    popup_closed = Signal()
    def __init__(self,todo:Todo, uuid=None, title=None, desc=None, priorities=None, deadline=datetime.now(), completed=False):
        super().__init__()

        self.setupUi(self)
        # self.setup()

        self.todo = todo
        self.uuid = uuid

        if uuid:
            self.current = self.todo.search_todos(uuid)
        


        # self.todo = Todo(DATA)

            self.title_input.setText(self.current["title"])
            self.description_input.setText(self.current["description"])
            self.completed.setChecked(bool(self.current["status"]))

        else:
            # self.title_input.setText()
            # self.description_input.setText()
            # self.completed.setChecked()
            pass

        self.time_deadline_input.setFixedWidth(37)

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
        date_ahh_idk = QDateTime(self.deadline_input.getDate(), self.time_deadline_input.getTime())

        add = self.todo.add_todo(
            title=self.title_input.text(),
            description=self.description_input.toPlainText(),
            # deadline=[self.deadline_input.getDate(), self.time_deadline_input.getTime()],
            deadline=date_ahh_idk.toPython(),
            importance=self.priorities_input.text(),
            status=self.completed.isChecked()
        )

        if add:
            raise add
        
        self.popup_closed.emit()
        self.close()
    
    def del_func(self):
        print(self.priorities_input.text())
        # ?pass
        dell = self.todo.delete(
            id=self.uuid
        )

        if dell:
            raise dell
        self.popup_closed.emit()
        self.close()

    def cancel_func(self):
        self.close()

        # self.

    # def setup(self):

       


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_instance = Todo(DATA)
    w = List_widget(todo_instance)
    w.show()
    sys.exit(app.exec())

