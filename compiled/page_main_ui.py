# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QListView, QListWidget, QListWidgetItem,
    QSizePolicy, QWidget)

from qfluentwidgets import (ImageLabel, TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(773, 401)
        self.main = ImageLabel(Form)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(20, 20, 191, 171))
        self.specs_label = TextEdit(Form)
        self.specs_label.setObjectName(u"specs_label")
        self.specs_label.setGeometry(QRect(10, 200, 701, 161))
        self.app_list = QListWidget(Form)
        self.app_list.setObjectName(u"app_list")
        self.app_list.setGeometry(QRect(240, 20, 471, 61))
        self.app_list.setMovement(QListView.Movement.Free)
        self.app_list.setFlow(QListView.Flow.LeftToRight)
        self.app_list.setProperty(u"isWrapping", False)
        self.app_list.setResizeMode(QListView.ResizeMode.Adjust)
        self.app_list.setLayoutMode(QListView.LayoutMode.Batched)
        self.app_list.setViewMode(QListView.ViewMode.IconMode)
        self.main_2 = ImageLabel(Form)
        self.main_2.setObjectName(u"main_2")
        self.main_2.setGeometry(QRect(0, 0, 821, 421))
        self.main_2.raise_()
        self.main.raise_()
        self.specs_label.raise_()
        self.app_list.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.main_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

