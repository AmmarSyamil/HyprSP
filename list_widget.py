from PySide6.QtWidgets import QWidget
from compiled.ui_list import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys

class list_widget(QWidget, Ui_Form):
    def __init__(self, order, description, deadline,status):
        super().__init__()

        self.setupUi(self)
        self.order.setText(order)
        self.description.setText(description)
        # self.checklist.setChecked(checklist)
        # self.checklist.stateChanged.connect(self.on_mark)
        self.deadlne.setText(deadline)
        # self.checklist.statusTip()
        
        

    def on_mark(self):
        print("ciki")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = list_widget(str(1), "tes", True)
    w.show()
    sys.exit(app.exec())

