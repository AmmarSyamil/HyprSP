from PySide6.QtWidgets import QWidget
# from compiled.ui_list_widget import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
from compiled.edit_popup import Ui_Form
from todo import Todo
from datetime import datetime

class Edit_popup_widget(QWidget, Ui_Form):
    def __init__(self, Todo_Class, uuid=None, title=None, desc=None, due=None):
        super().__init__()
        self.setupUi(self)
        giv = QMovie(":/images/images/herta.gif")
        if giv:
            # print("sd
            # print(giv)
            self.extra.setMovie(giv)
        else:
            pass
            # print("ded")
        giv.start()


        if uuid:
            self.todo = Todo_Class
            self.current = self.todo.find_item(uuid)
            # self.current = self.todo..filter(uuid=uuid)
            # print(type(self.current))
            days, hours, minutes, seconds = self.time_left(self.current["due"])

            # print(dict(self.current))
            self.title.setText(self.current["title"])
            self.description.setText(self.current["description"])
            self.due.setText(f'{days} days and {hours} hours left')
        else:
            self.title.setText(title)
            self.description.setText(desc)
            self.due.setText(due)

        self.save.clicked.connect(self.save_button)
        self.delete_2.clicked.connect(self.delete_button)
        self.cancel.clicked.connect(self.cancel_button)
        

        # self.order.setText(order)
        # self.description.setText(description)
        # self.checklist.setChecked(checklist)
        # self.checklist.stateChanged.connect(self.on_mark)
        # self.deadlne.setText(deadline)
        # self.checklist.statusTip()

    def time_left(self, data):
        now = datetime.now(data.tzinfo)
        delta = data-now

        total_sec = int(delta.total_seconds())
        days = total_sec // 86400 
        hours = (total_sec % 86400) // 3600
        minutes = (total_sec % 3600) // 60
        seconds = total_sec % 60
        return days, hours, minutes, seconds
        
    def save_button(self):
        print("save")

    def cancel_button(self):
        print("canvel")

    def delete_button(self):
        print("delete")
        

    def on_mark(self):
        print("ciki")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_popup_widget(str(1), "tes", True)
    w.show()
    sys.exit(app.exec())