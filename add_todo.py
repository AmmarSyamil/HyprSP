from PySide6.QtWidgets import QWidget
from compiled.ui_add_todo import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys

class list_widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        print("status_input type:", type(getattr(self, "status_input", None)))
        # self.title.setTextColor
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = list_widget()
    w.show()
    sys.exit(app.exec())

