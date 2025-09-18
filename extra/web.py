from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QSizePolicy, QFrame
from PySide6.QtCore import QUrl, QSize, Qt
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6 import QtCore
import markdown
import sys
import logging

logging.basicConfig(level=logging.INFO)

from qframelesswindow.webengine import FramelessWebEngineView

class Web_Engine(QFrame):
    # def __init__(self, url, markdown=False, mode="fit", parent=None):
    #     super().__init__(parent=parent)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("homeInterface")

        # 1. Replace QWebEngineView with FramelessWebEngineView
        self.webView = FramelessWebEngineView(self)
        self.webView.setAttribute(Qt.WA_TranslucentBackground)
        self.webView.setAttribute(Qt.WA_NoSystemBackground, True)
        self.webView.setStyleSheet("background: transparent;")
        self.webView.load(QUrl("https://id.quora.com/"))
        self.webView.page().runJavaScript(
            "document.body.style.backgroundColor = 'transparent';"
        )

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 48, 0, 0)
        self.vBoxLayout.addWidget(self.webView)
    #     self.web = FramelessWebEngineView(self)
    #     self.url = url
    #     self.mode = mode
    #     logging.info(f"Initializing Web_Engine with URL: {url}")

    #     layout = QVBoxLayout(self)
    #     layout.setContentsMargins(0,0,0,0)
    #     layout.setSpacing(0)
    #     # Removed adjustSize, frameless, and translucent for better placement in layouts
    #     # self.adjustSize()
    #     # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #     # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    #     # self.web.loadFinished.connect(self.resize)

    #     self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #     self.web.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #     layout.addWidget(self.web)

    #     try:
    #         self.web.page().contentsSizeChanged.connect(self.setup)
    #     except Exception as e:
    #         pass

    #     self.web.loadFinished.connect(self.setup_after)
    #     self.web.urlChanged.connect(lambda url: logging.info(f"URL changed to: {url.toString()}"))

    #     if markdown:
    #         self.net = QNetworkAccessManager(self)
    #         self.net.finished.connect(self._connect)
    #         self.net.get(QNetworkRequest(QUrl(url)))
    #     else:
    #         # self.web.setUrl(QUrl(url))
    #         self.web.load(QUrl(url))
    #         logging.info(f"Set URL: {url}")


    # def _connect(self, reply):
    #     if reply:
    #         data = reply.readAll()
    #         md =    bytes(data).decode('utf-8', 'ignore')
    #         html = markdown.markdown(md)
    #         self.web.setHtml(html, QUrl(self.url))
    #         logging.info(f"Set HTML for markdown URL: {self.url}")

    # def setup(self, current_size):
    #     try:
    #         size = QSize(int(current_size.width()), int(current_size.height()))
    #     except Exception as e:
    #         size = self.size()

    #     if self.mode == "compact":
    #         self.web.setFixedSize(size)
    #         # Removed self.setFixedSize(size) to allow proper placement in layouts
    #     else:
    #         self.web.resize(self.size())

    # def setup_after(self):
    #     # if self.mode == "fit":
    #     #     self.web.resize(self.size())
    #     # else:
    #         page = self.web.page()
    #         try:
    #             size = page.contentsSize()
    #             self.setup(size)

    #         except Exception as e:
    #             pass

    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     # if self.mode == "fit":
    #     #     self.web.resize(self.size())

    # def sizeHint(self): 
    #     return self.web.sizeHint()

    # def resize(self):
    #     # self.
    #     self.setFixedSize(self.web.page().contentsSize())
    #     # miaw = True
    #     # while miaw:
    #     #     current = self.size()
    #     #     # current.setHeight
    #     #     self.setFixedSize(current.width()+1,current.height()+1 )
    #     #     # if self.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # w = HackaTime("https://github-readme-stats.hackclub.dev/api/wakatime?username=2455&api_domain=hackatime.hackclub.com&theme=darcula&custom_title=Hackatime+Stats&layout=compact&cache_seconds=0&langs_count=8")
    w = Web_Engine()
    # w = Web_Engine.load("https://www.instagram.com/explore/")
    # w = HackaTime("https://github.com/AmmarSyamil/AmmarSyamil/blob/main/README.md?plain=1")
    w.setFixedSize(QSize(400,400))
    w.show()
    app.exec()