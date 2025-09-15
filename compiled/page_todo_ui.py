# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_todo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (FlipView, ListWidget, PushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 384)
        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 10, 331, 371))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.todo_list = ListWidget(self.frame_5)
        self.todo_list.setObjectName(u"todo_list")
        self.todo_list.setGeometry(QRect(10, 11, 311, 321))
        self.layoutWidget = QWidget(self.frame_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 340, 131, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.todo_add = PushButton(self.layoutWidget)
        self.todo_add.setObjectName(u"todo_add")

        self.horizontalLayout.addWidget(self.todo_add)

        self.style = FlipView(Form)
        self.style.setObjectName(u"style")
        self.style.setGeometry(QRect(410, 240, 361, 131))
        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(390, 10, 401, 211))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.layoutWidget1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 49, 16))
        self.todo_closest = QWidget(self.frame_6)
        self.todo_closest.setObjectName(u"todo_closest")
        self.todo_closest.setEnabled(False)
        self.todo_closest.setGeometry(QRect(10, 30, 371, 31))

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.layoutWidget1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 49, 16))
        self.todo_priorities = QListWidget(self.frame_7)
        self.todo_priorities.setObjectName(u"todo_priorities")
        self.todo_priorities.setGeometry(QRect(10, 30, 381, 101))

        self.verticalLayout.addWidget(self.frame_7)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.todo_add.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Closest", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Priorities", None))
    # retranslateUi

