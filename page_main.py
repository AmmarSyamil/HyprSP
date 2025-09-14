from PySide6.QtWidgets import QWidget
# from compiled.page_main_ui import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QLabel, QWidget
from PySide6.QtCore import Qt, QFile, QIODevice, QObject, QSize
from PySide6.QtGui import QPixmap, QMovie
from PySide6.QtUiTools import QUiLoader
import sys
from pathlib import Path
import importlib.util
import sys
from qfluentwidgets.components.widgets.line_edit import TextEdit
# import config
# from config import *

# #WTF IS PYTHON IMPORTING IDK NOSFFNOIWAIBUASDASBFABF
# mod_path = (Path(__file__).resolve().parents[1] / "compiled" / "page_main_ui.py")
# spec = importlib.util.spec_from_file_location("compiled.page_main_ui", str(mod_path))
# module = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(module)

# ROOT = Path(__file__).resolve().parents[1]
# if str(ROOT) not in sys.path:
#     sys.path.insert(0, str(ROOT))

# def _load_module(name, relative_path):
#     path = ROOT / relative_path
#     spec = importlib.util.spec_from_file_location(name, str(path))
#     module = importlib.util.module_from_spec(spec)
#     spec.loader.exec_module(module)
#     sys.modules[name] = module
#     return module

# _compiled = _load_module("compiled.page_main_ui", Path("compiled") / "page_main_ui.py")
# Ui_Form = _compiled.Ui_Form

# _specs_mod = _load_module("extra.specs", Path("extra") / "specs.py")
# Specs = _specs_mod.Specs

# _config_mod = _load_module("config", Path("") / "config.py")
# config = _config_mod

from compiled.page_main_ui import Ui_Form
from config import *
from extra.specs import Specs
from extra.web import Web_Engine
# from extra.web import Wen_ENgine

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

