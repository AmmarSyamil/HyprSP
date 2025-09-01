import sys
import json
from typing import Tuple

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader

from compiled.ui_main import Ui_MainWindow
from list_widget import list_widget
import compiled.resources_rc as resources_rc
from todo import Todo
from datetime import datetime
from edit_popup_widget import Edit_popup_widget

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

        # Connect UI signals
        self.todo_add.clicked.connect(self.todo_add_function)
        # Accessing `text()` here is unnecessary but harmless; left as-is
        self.todo_input.text()

        # Model holding todo items
        self.todoClass = Todo()

        # Open edit popup when a list item is clicked
        self.todo.itemClicked.connect(self.todo_list_clicked)

        # Animated gif for the label (resource path)
        giv = QMovie(":/images/images/herta.gif")
        if giv:
            self.label.setMovie(giv)
        giv.start()

        # Keep references to popup windows so they aren't garbage collected
        self._popups = []

        # Populate the UI from model
        self.setup()

    def todo_list_clicked(self, item) -> None:
        """Open an edit popup for the clicked todo list item.
        
        Funtion to show popup for editing the Todo.
        Run automaticaly when a list/object/option is clicked in the qtwidgetlist
        """

        uuid = item.data(Qt.UserRole)
        print(uuid)
        popup = Edit_popup_widget(self.todoClass, uuid)
        self._popups.append(popup)
        popup.show()


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
        """Function to add todo (not completed)
        """

        if self.todo_input.text():
            print(self.todo_input.text())
            # Todo.add_item signature is (desc, deadline, status, title)
            # use keyword args so values are assigned correctly
            self.todoClass.add_item(
                desc=str(self.todo_input.text()),
                deadline=datetime(year=2014, month=1, day=5),
                status="pending",
                title=str(self.todo_input.text()),
            )
        # Refresh UI after adding
        self.setup()
            
        
        # self.todo.addItem()

    def setup(self) -> None:
        """Populate the list widget from the .todo file.
        """

        self.todo.clear()
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

        # for i in range(5):
        #     item = QListWidgetItem()
        #     # item.setSizeHint(QSize(300, 48))
        #     widget = list_widget(str(i+1),"miaw",True)
        #     item.setSizeHint(widget.sizeHint())
        #     self.todo.addItem(item)
        #     self.todo.setItemWidget(item, widget)
            



    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
