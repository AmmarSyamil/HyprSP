# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_main.ui'
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
from PySide6.QtWidgets import (QApplication, QListView, QListWidgetItem, QSizePolicy,
    QWidget)

from qfluentwidgets import (FlipView, ImageLabel, TextEdit)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(773, 401)
        self.main = ImageLabel(Form)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(10, 20, 201, 181))
        self.flipimages_middle = FlipView(Form)
        self.flipimages_middle.setObjectName(u"flipimages_middle")
        self.flipimages_middle.setGeometry(QRect(220, 10, 256, 381))
        self.app_list = QListView(Form)
        self.app_list.setObjectName(u"app_list")
        self.app_list.setGeometry(QRect(490, 10, 271, 71))
        self.web = QWidget(Form)
        self.web.setObjectName(u"web")
        self.web.setGeometry(QRect(500, 90, 261, 301))
        self.specs_label = TextEdit(Form)
        self.specs_label.setObjectName(u"specs_label")
        self.specs_label.setGeometry(QRect(10, 210, 201, 171))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.main.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

