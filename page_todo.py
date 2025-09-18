from PySide6.QtWidgets import QWidget, QVBoxLayout
# from compiled.page_main_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QFrame
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie, QCursor
from PySide6.QtUiTools import QUiLoader
import sys
from pathlib import Path
import importlib.util
import sys
from qfluentwidgets.components.widgets.line_edit import TextEdit
from qfluentwidgets import NavigationItemPosition, FluentWindow, SubtitleLabel, setFont
from compiled.page_todo_ui import Ui_Form
from config import *
from extra.specs import Specs
from extra.web import Web_Engine
# from compiled.ui_notification import
from notification import notification_widget
from todo_class import Todo
from datetime import datetime
from list_todo import AppCard
from popup_todo import List_widget
# from 

# from typing import

class list_widget(QFrame, Ui_Form):
    def __init__(self):     
        super().__init__()

        self.setupUi(self)
        self.todoClass = Todo(DATA)

        self.todo_list.itemClicked.connect(self.todo_list_clicked)
        self.todo_priorities.itemClicked.connect(self.todo_list_clicked)
        self.setup_todo()
        self.setup_closest()
        self.setup_prioritise()

        if PAGE_TODO_BAGROUND == "video":
            movie = QMovie()
            self.main_2.setMovie(movie)
            movie.start()
        else:
            pixmap = QPixmap(PAGE_TODO_BAGROUND)
            self.main_2.setPixmap(pixmap)
            self.main_2.setScaledContents(True)

        # self.style.setAspectRatioMode(Qt.KeepAspectRatio)
        # # self.style.setScaledContents(True)
        
        # self.style.setItemSize(QSize(361, 131))
        # self.style.addImages(PAGE_TODO_FLIPVIEW)

        self.todo_add.clicked.connect(self.todo_list_pressed)

        self._popups = []

    def time_left(self, due: datetime):
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


    def setup_todo(self) -> None:
        """
        Populate the list widget from the .todo file.
        """

        self.todo_list.clear()
        print("refresh")
        i = 0

        for id, data in self.todoClass.list_todos().items():
            i += 1

            days, hours, minutes, seconds = self.time_left(data["deadline"])

            item = QListWidgetItem()
            item.setData(Qt.UserRole, id)
            widget = AppCard(
                # order=str(i),
                title=str(data["title"]),
                due_in=f"{days} D and {hours} H left",
                completed=data["status"],
                priorities=data["importance"],
                is_list=True
            )
            item.setSizeHint(widget.sizeHint())
            self.todo_list.addItem(item)
            self.todo_list.setItemWidget(item, widget)
            # Ensure widget is properly sized within the item
            widget.resize(item.sizeHint())
            widget.show()

    def setup_closest(self):
        closest = self.todoClass.find_closest()

        if closest is None:
            return

        self.closest_uuid, closest_data = closest

        days, hours, minutes, seconds = self.time_left(closest_data["deadline"])
        closest_widget = AppCard(
            title=str(closest_data["title"]),
            due_in=f"{days} and {hours} left",
            completed=closest_data["status"],
            priorities=closest_data["importance"],
            is_list=False
        )

        closest_widget.setParent(self.frame_6)
        closest_widget.setGeometry(self.todo_closest.geometry())

        self.todo_closest.setParent(None)
        self.todo_closest.deleteLater()
        self.todo_closest = closest_widget

        self.todo_closest.clicked.connect(self.closest_clicked)

        pass

    def setup_prioritise(self):
        # prioriti = self.todoClass.get_top_priority()

        # for i in 


        for id, data in self.todoClass.get_top_priority().items():

            days, hours, minutes, seconds = self.time_left(data["deadline"])

            item = QListWidgetItem()
            item.setData(Qt.UserRole, id)
            widget = AppCard(
                # order=str(i),
                title=str(data["title"]),
                due_in=f"{days} and {hours} left",
                completed=data["status"],
                priorities=data["importance"],
                is_list=True
            )
            item.setSizeHint(widget.sizeHint())
            self.todo_priorities.addItem(item)
            self.todo_priorities.setItemWidget(item, widget)
            # Ensure widget is properly sized within the item
            widget.resize(item.sizeHint())
            widget.show()
        
        pass

    def todo_list_pressed(self):
        popup = List_widget(
            self.todoClass)
        self._popups.append(popup)
        popup.popup_closed.connect(self.popup_close)

        popup.exec()


    def todo_list_clicked(self, item):

        uuid = item.data(Qt.UserRole)
        # print(uuid)
        popup = List_widget(
            self.todoClass, uuid)
        self._popups.append(popup)
        popup.popup_closed.connect(self.popup_close)

        # cursor_pos = QCursor.pos()
        # print(popup.pos(), "start")
        popup.exec()

        pass

    def closest_clicked(self):
        popup = List_widget(
            self.todoClass, self.closest_uuid)
        self._popups.append(popup)
        popup.popup_closed.connect(self.popup_close)

        popup.exec()

        pass

    def popup_close(self):
        self.setup_todo()
        self.setup_closest()
        pass

    def button_add(self):
        #open up

        pass

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = list_widget()
    w.show()
    sys.exit(app.exec())





































# may god bles me with a bmw f90 m5 cs, plssss