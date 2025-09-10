from PySide6.QtWidgets import QDialog, QCompleter
# from compiled.ui_list_widget import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QComboBox
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize, Signal, QPoint, QTimer, QDate, QDateTime
from PySide6.QtGui import QPixmap, QMovie, QCursor, QGuiApplication
from PySide6.QtUiTools import QUiLoader
import sys
from compiled.edit_popup import Ui_Form
from todo import Todo
from datetime import datetime
from config import *

class Edit_popup_widget(QDialog, Ui_Form):
    popup_closed = Signal()

    def __init__(self, Todo_Class, uuid=None, title=None, desc=None, due=None):
        super().__init__()
        self.setupUi(self)



        self.setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        original_showPopup = self.status_input.showPopup
        
        def custom_showPopup():
            original_showPopup()
            popup = self.status_input.view().window()
            if popup:
                pos = self.status_input.mapToGlobal(QPoint(0, self.status_input.height()))
                pos.setX(self.status_input.mapToGlobal(QPoint(0,0)).x())
                popup.move(pos)
        self.status_input.showPopup = custom_showPopup

        # print(self.pos(), "heh")
        self.show_near_pointer()

        if EDIT_POPUP_ART_TYPE == "video":
            giv = QMovie(EDIT_POPUP_ART)
            self.extra.setMovie(giv)
            giv.start()
        elif EDIT_POPUP_ART_TYPE == "image":
            self.extra.setPixmap(QPixmap(EDIT_POPUP_ART))
        else:
            raise f'{TypeError}, EDIT_POPUP_ART_TYPE must be either "image" or "video", check the config.py file'#///////////////////////////
        # giv = QMovie(":/images/images/herta.gif")

        # if giv:

        #     self.extra.setMovie(giv)
        # else:
        #     pass
        # giv.start()


        if uuid:
            self.todo = Todo_Class
            self.current = self.todo.find_item(uuid)

            self.days, self.hours, self.minutes, self.seconds = self.time_left(self.current["due"])

            self.title_input.setText(self.current["title"])
            self.description_input.setText(self.current["description"])
            self.due_input.setDate(self.current["due"])
        else:
            self.title_input.setText(title)
            self.description_input.setText(desc)
            self.due_input.setText(due)

        # print(self.pos(), "after uuid")


        if self.current["status"]=="pending":
            temp = "Not Completed"
        else:
            temp = "Completed"
        self.status_input.setCurrentText(temp)
        self.status_input.currentTextChanged.connect(self.dropdown_status)
        self.status_input.setFocus()
        self.save.clicked.connect(self.save_button)
        self.delete_2.clicked.connect(self.delete_button)
        self.cancel.clicked.connect(self.cancel_button)

        

    def dropdown_status(self, text):
        # print(self.pos(), "at dropdown")
        if self.status_input.currentText() == "Completed":
            self.current["status"] = "completed"
        else:
            self.current["status"] = "pending"
        self.status_input.view().window().close()
        # print(self.current["status"])
        
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
        # print(self.current)
        date = self.due_input.dateTime().toPython()
        self.todo.edit_item(
            task=self.current,
            title=self.title_input.text(),
            description=self.description_input.toPlainText(),
            due=date,
            status=self.current["status"]
        )
        # print("save")
        self.popup_closed.emit()
        self.close()

    def cancel_button(self):
        # print("cancel")
        self.close()

    def delete_button(self):
        # print("delete")
        self.todo.delete_item(task=self.current)
        self.popup_closed.emit()
        self.close()


        

    def on_mark(self):
        print("ciki") #/////////////////////////////////////////////////////////////////

    def showEvent(self, event):
        super().showEvent(event)
        if hasattr(self, 'desired_pos'):
            self.move(self.desired_pos)


    def show_near_pointer(self):
        offfset = QPoint(-300,-150)
        global_pos = QCursor.pos()+offfset
        parent = self.parentWidget()


        print(parent, self.isWindow())

        if parent and not self.isWindow():
            local = parent.mapFromGlobal(global_pos)
            self.move(local)

        else:
            screen = QGuiApplication.primaryScreen()
            rect = screen.availableGeometry()
            global_pos.setX(max(0, min(global_pos.x(), rect.width() - self.width())))
            global_pos.setY(max(0, min(global_pos.y(), rect.height() - self.height())))

            self.desired_pos = global_pos


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Edit_popup_widget(str(1), "tes", True)
    w.show()
    sys.exit(app.exec())
    