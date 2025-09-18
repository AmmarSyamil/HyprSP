from PySide6.QtWidgets import QApplication, QVBoxLayout, QFrame
from PySide6.QtCore import QUrl, Qt, QSize
from PySide6.QtWebEngineWidgets import QWebEngineView
from qframelesswindow.webengine import FramelessWebEngineView
import sys

class TestPlainWebEngine(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("TestPlainWebEngine")
        self.webView = QWebEngineView(self)
        self.webView.setAttribute(Qt.WA_TranslucentBackground)
        self.webView.setAttribute(Qt.WA_NoSystemBackground, True)
        self.webView.setStyleSheet("background: transparent;")
        self.webView.load(QUrl("https://id.quora.com/"))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.webView)

class TestFramelessWebEngine(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("TestFramelessWebEngine")
        self.webView = FramelessWebEngineView(self)
        self.webView.setAttribute(Qt.WA_TranslucentBackground)
        self.webView.setAttribute(Qt.WA_NoSystemBackground, True)
        self.webView.setStyleSheet("background: transparent;")
        self.webView.load(QUrl("https://id.quora.com/"))
        self.webView.page().runJavaScript("document.body.style.backgroundColor = 'transparent';")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.webView)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Test 1: Plain QWebEngineView with transparency
    w1 = TestPlainWebEngine()
    w1.setWindowTitle("Test Plain QWebEngineView")
    w1.resize(600, 400)
    w1.show()

    # Test 2: FramelessWebEngineView with transparency
    w2 = TestFramelessWebEngine()
    w2.setWindowTitle("Test FramelessWebEngineView")
    w2.resize(600, 400)
    w2.show()

    sys.exit(app.exec())
