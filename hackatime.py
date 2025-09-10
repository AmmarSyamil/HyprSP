from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtCore import QUrl, QSize
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6 import QtCore
import markdown
import sys


class HackaTime(QWidget):
    def __init__(self, url, markdown=False, mode="fit"):
        super().__init__()
        self.web = QWebEngineView()
        self.url = url
        self.mode = mode

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)    
        layout.addWidget(self.web)
        self.adjustSize()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # self.web.loadFinished.connect(self.resize)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.web.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        try:
            self.web.page().contentsSizeChanged.connect(self.setup)
        except Exception as e:
            pass

        self.web.loadFinished.connect(self.setup_after)

        if markdown:
            self.net = QNetworkAccessManager(self)
            self.net.finished.connect(self._connect)
            self.net.get(QNetworkRequest(QUrl(url)))
        else:
            self.web.setUrl(QUrl(url))


    def _connect(self, reply):
        if reply:
            data = reply.readAll()
            md =    bytes(data).decode('utf-8', 'ignore')
            html = markdown.markdown(md)
            self.web.setHtml(html, QUrl(self.url))

    def setup(self, current_size):
        try:
            size = QSize(int(current_size.width(), int(size.height())))
        except Exception as e:
            size = self.size()

        if self.mode == "compact":
            self.web.setFixedSize(size)
            self.setFixedSize(size)
        else:
            self.web.resize(self.size())

    def setup_after(self):
        if self.mode == "fit":
            self.web.resize(self.size())
        else:
            page = self.web.page()
            try:
                size = page.contentsSize()
                self.setup(size)

            except Exception as e:
                pass

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.mode == "fit":
            self.web.resize(self.size())

    def sizeHint(self): 
        return self.web.sizeHint()

    def resize(self):
        # self.
        self.setFixedSize(self.web.page().contentsSize())
        # miaw = True
        # while miaw:
        #     current = self.size()
        #     # current.setHeight
        #     self.setFixedSize(current.width()+1,current.height()+1 )
        #     # if self.


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = HackaTime("https://github-readme-stats.hackclub.dev/api/wakatime?username=2455&api_domain=hackatime.hackclub.com&theme=darcula&custom_title=Hackatime+Stats&layout=compact&cache_seconds=0&langs_count=8")
    # w = HackaTime("https://github.com/AmmarSyamil/AmmarSyamil/blob/main/README.md?plain=1")
    w.show()
    app.exec()