import sys
import json
from typing import Tuple

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize, QTime
from PySide6.QtGui import QPixmap, QMovie, QCursor
from PySide6.QtUiTools import QUiLoader

from compiled.ui_main import Ui_MainWindow
from list_widget import list_widget
from todo import Todo
from datetime import datetime
from edit_popup_widget import Edit_popup_widget
from notification import notification_widget
# from data import app_list
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWebEngineWidgets import QWebEngineView
from hackatime import HackaTime

from config import *

class MainWindow(QMainWindow, Ui_MainWindow):
    """Main window for apps.
    - `todo`, a QListWidget to display items
    - `todo_input`, a QLineEdit used to add new todos
    - `todo_add`, a QPushButton to trigger add
    - `label`, a QLabel used for the animated GIF
    """

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.todo_add.clicked.connect(self.todo_add_function)
        self.todo_input.text()
        self.todoClass = Todo()
        self.todo.itemClicked.connect(self.todo_list_clicked)

        self.dateTimeEdit.setDate(datetime.now())
        self.dateTimeEdit.setTime(QTime.currentTime())

        self.setFixedSize(QSize(1200,485))
        # self.setMaximumSize(996,485)
        self.resize(QSize(1200,485))

        self.setup_app_list()
        self.setup_hackatime()
        self.setup_todo()

        if MAIN_ART_TYPE == "video":
            giv = QMovie(MAIN_ART)
            self.style_1.setMovie(giv)
            giv.start()
        elif MAIN_ART_TYPE == "picture":
            self.style_1.setPixmap(QPixmap(MAIN_ART))
        else:
            raise f'{TypeError}, MAIN_ART_TYPE must be either "image" or "video", check the config.py file'#///////////////////////////
        self._popups = []

        self.list_app.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        # self.hackatime.


    def todo_list_clicked(self, item) -> None:
        """Open an edit popup for the clicked todo list item.
        
        Funtion to show popup for editing the Todo.
        Run automaticaly when a list/object/option is clicked in the qtwidgetlist
        """

        uuid = item.data(Qt.UserRole)
        print(uuid)
        popup = Edit_popup_widget(self.todoClass, uuid)
        self._popups.append(popup)
        popup.popup_closed.connect(self.popup_close)

        cursor_pos = QCursor.pos()
        print(popup.pos(), "start")
        popup.exec()
    def popup_close(self):
        print("close but does it works")
        self.setup_todo()


    def time_left(self, due: datetime) -> Tuple[int, int, int, int]:
        """
        Return the time left until `due` as (days, hours, minutes, seconds).
        """

        now = datetime.now(due.tzinfo)
        delta = due - now

        total_sec = int(delta.total_seconds())
        days = total_sec // 86400
        hours = (total_sec % 86400) // 3600
        minutes = (total_sec % 3600) // 60
        seconds = total_sec % 60
        return days, hours, minutes, seconds


    def todo_add_function(self) -> None: 
        """Function to add todo
        """

        if self.todo_input.text():
            self.todoClass.add_item(
                desc=str(self.todo_input.text()),
                deadline=self.dateTimeEdit.date().toPython(),
                status="pending",
                title=str(self.todo_input.text()),
            )

        self.todo_input.clear()
        self.setup_todo()
            
        

    def setup_todo(self) -> None:
        """Populate the list widget from the .todo file.
        """

        self.todo.clear()
        print("refresh")
        i = 0

        for data in self.todoClass.load_item():
            i += 1
            days, hours, minutes, seconds = self.time_left(data["due"])

            item = QListWidgetItem()
            item.setData(Qt.UserRole, data["uuid"])
            widget = list_widget(
                order=str(i),
                description=str(data["title"]),
                deadline=f"{days} days and {hours} hours left",
                checklist=True,
                status=True,
            )
            item.setSizeHint(widget.sizeHint())
            self.todo.addItem(item)
            self.todo.setItemWidget(item, widget)

            
    def setup_app_list(self) -> None:
        self.list_app.setSpacing(0)
        self.list_app.setGridSize(QSize(50, 50))
        for i in APP_LIST:

            item = QListWidgetItem()
            # print(i)
            widget = notification_widget(
                app=str(i),
                url=APP_LIST[i]["address"],
                app_type=APP_LIST[i]["app_type"]
            )
            widget.setFocusPolicy(Qt.NoFocus)
            widget.setMaximumWidth(50)
            widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            item.setSizeHint(widget.sizeHint())
            self.list_app.addItem(item)
            self.list_app.setItemWidget(item, widget)
            
    def setup_hackatime(self):


        widget = HackaTime(HACKATIME_WIDGET_API)
        widget.setParent(self.hackatime.parentWidget())
        widget.setGeometry(self.hackatime.geometry())
        # self.
        self.hackatime.hide()
        self.hackatime.deleteLater()
        
        self.hackatime = widget
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
