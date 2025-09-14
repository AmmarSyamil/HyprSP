from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
from pathlib import Path
import importlib.util
import sys
from config import *
from compiled.page_main_ui import Ui_Form
from extra.specs import Specs
from extra.web import Web_Engine
# from PySide6.QtWidgets import QVBoxLayout

class list_widget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.resize(800, 400)

        self.flipimages_middle.addImages(PAGE_MAIN_FLIPVIEW)

        self.specs = Specs()
        self.setup()

        # w = Web_Engine("https://id.quora.com/")
        # w.setParent(self.web.parentWidget())
        # w.setGeometry(self.web.geometry())

        # self.web = w

    def setup(self):
        # print(self.specs.device_os())
        self.OS_label.setText(self.specs.device_os())
        self.System_label.setText(self.specs.device_system())
        self.GPU_label.setText(self.specs.device_cpu())
        self.CPU_label.setText(self.specs.device_gpu())

        # Set image or animation to main ImageLabel
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
