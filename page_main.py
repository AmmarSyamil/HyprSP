from PySide6.QtWidgets import QWidget
# from compiled.page_main_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget, QSizePolicy
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
from pathlib import Path
import importlib.util
import sys
from qfluentwidgets.components.widgets.line_edit import TextEdit

from compiled.page_main_ui import Ui_Form
from config import *
from extra.specs import Specs
from extra.web import Web_Engine
# from compiled.ui_notification import
from notification import notification_widget

class list_widget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.resize(800, 401)

        self.flipimages_middle.setAspectRatioMode(Qt.KeepAspectRatio)
        self.flipimages_middle.setItemSize(QSize(263, 399))
        self.flipimages_middle.addImages(PAGE_MAIN_FLIPVIEW)
        self.specs = Specs()
        self.setup() 
        
        w = Web_Engine("https://id.quora.com/")
        w.setParent(self.web.parentWidget())
        w.setGeometry(self.web.geometry())
        self.web.hide()
        self.web.deleteLater()
        self.web = w

        self.app_list.setSpacing(0)
        self.app_list.setGridSize(QSize(50,50))
        for i in APP_LIST:
            item = QListWidgetItem()
            widget = notification_widget(
                app=str(i),
                url=APP_LIST[i]["address"],
                icon=APP_LIST[i]["icon"],
                app_type=APP_LIST[i]["app_type"]
            )

            widget.setFocusPolicy(Qt.NoFocus)
            widget.setMaximumWidth(50)
            widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
            item.setSizeHint(widget.sizeHint())
            self.app_list.addItem(item)
            self.app_list.setItemWidget(item, widget)






        
        

    def setup(self):
        self.specs_label.setLineWrapMode(TextEdit.NoWrap)
        self.specs_label.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.specs_label.setText(
            self.specs.device_os() + "\n" + self.specs.device_system() + "\n" + self.specs.device_cpu() + "\n" + self.specs.device_gpu()
        )
        # self.OS_label.setText(self.specs.device_os())
        # self.System_label.setText(self.specs.device_system())
        # self.GPU_label.setText(self.specs.device_cpu())
        # self.CPU_label.setText(self.specs.device_gpu())

        from PySide6.QtGui import QPixmap, QMovie
        import config

        if config.MAIN_ART_TYPE == "video":
            movie = QMovie(config.MAIN_ART)
            self.main.setMovie(movie)
            movie.start()
        else:
            pixmap = QPixmap(config.MAIN_ART)
            self.main.setPixmap(pixmap)
            self.main.setScaledContents(True)


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = list_widget()
    w.show()
    sys.exit(app.exec())

