# todo_list_simple.py
import sys, json
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader

from ui_main import Ui_MainWindow
from list_widget import list_widget
import resources_rc

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.path = path
        # self.label = QLabel()
        
        # self.setMinimumSize(600, 400)
        
        giv = QMovie(":/images/images/herta.gif")
        if giv:
            print("sd")
            print(giv)
            self.label.setMovie(giv)
        else:
            print("ded")
        giv.start()
        

        print("object names:", [n for n in dir(self) if "list" in n.lower()])
        self.setup()

    def setup(self):
        for i in range(5):
            item = QListWidgetItem()
            # item.setSizeHint(QSize(300, 48))
            widget = list_widget(str(i+1),"miaw",True)
            item.setSizeHint(widget.sizeHint())
            self.todo.addItem(item)
            self.todo.setItemWidget(item, widget)



    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
