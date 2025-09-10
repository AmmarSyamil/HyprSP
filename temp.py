from qfluentwidgets import FluentWindow, PrimaryPushButton
from PySide6.QtWidgets import QApplication

app = QApplication([])

win = FluentWindow()
btn = PrimaryPushButton("Hello Fluent", win)
win.resize(400, 250)
win.show()

app.exec()