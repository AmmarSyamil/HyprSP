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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDateTimeEdit, QGridLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

from qfluentwidgets import PushButton
from compiled import resources_rc
# import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1163, 485)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.style_1 = QLabel(self.centralwidget)
        self.style_1.setObjectName(u"style_1")
        self.style_1.setGeometry(QRect(30, 30, 201, 201))
        self.style_1.setPixmap(QPixmap(u":/images/images/herta.gif"))
        self.style_1.setScaledContents(True)
        self.todo = QListWidget(self.centralwidget)
        self.todo.setObjectName(u"todo")
        self.todo.setGeometry(QRect(280, 110, 341, 241))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(280, 360, 459, 51))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.todo_add = PushButton(self.layoutWidget)
        self.todo_add.setObjectName(u"todo_add")

        self.gridLayout.addWidget(self.todo_add, 0, 2, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.gridLayout.addWidget(self.dateTimeEdit, 0, 1, 1, 1)

        self.todo_input = QLineEdit(self.layoutWidget)
        self.todo_input.setObjectName(u"todo_input")

        self.gridLayout.addWidget(self.todo_input, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 3)
        self.list_app = QListWidget(self.centralwidget)
        self.list_app.setObjectName(u"list_app")
        self.list_app.setGeometry(QRect(280, 30, 871, 59))
        self.list_app.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_app.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.list_app.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.list_app.setFlow(QListView.Flow.LeftToRight)
        self.list_app.setProperty(u"isWrapping", False)
        self.list_app.setResizeMode(QListView.ResizeMode.Adjust)
        self.list_app.setLayoutMode(QListView.LayoutMode.Batched)
        self.list_app.setViewMode(QListView.ViewMode.IconMode)
        self.list_app.setUniformItemSizes(False)
        self.list_app.setSelectionRectVisible(False)
        self.hackatime = QWidget(self.centralwidget)
        self.hackatime.setObjectName(u"hackatime")
        self.hackatime.setGeometry(QRect(630, 110, 521, 241))
        self.style_2 = QLabel(self.centralwidget)
        self.style_2.setObjectName(u"style_2")
        self.style_2.setGeometry(QRect(30, 260, 201, 141))
        self.style_2.setPixmap(QPixmap(u":/images/images/herta.gif"))
        self.style_2.setScaledContents(True)
        self.style_3 = QLabel(self.centralwidget)
        self.style_3.setObjectName(u"style_3")
        self.style_3.setGeometry(QRect(760, 380, 391, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1163, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.style_1.setText("")
        self.todo_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.style_2.setText("")
        self.style_3.setText("")
    # retranslateUi

