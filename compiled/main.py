# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
# import resources_rc
import compiled.resources_rc as resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 161, 161))
        self.label.setPixmap(QPixmap(u":/images/images/herta.gif"))
        self.label.setScaledContents(True)
        self.todo = QListWidget(self.centralwidget)
        self.todo.setObjectName(u"todo")
        self.todo.setGeometry(QRect(30, 210, 341, 241))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 450, 459, 51))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.todo_add = QPushButton(self.layoutWidget)
        self.todo_add.setObjectName(u"todo_add")

        self.gridLayout.addWidget(self.todo_add, 0, 2, 1, 1)

        self.todo_input = QLineEdit(self.layoutWidget)
        self.todo_input.setObjectName(u"todo_input")

        self.gridLayout.addWidget(self.todo_input, 0, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.list_app = QListWidget(self.centralwidget)
        self.list_app.setObjectName(u"list_app")
        self.list_app.setGeometry(QRect(300, 30, 509, 59))
        self.list_app.setFlow(QListView.Flow.LeftToRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.todo_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

