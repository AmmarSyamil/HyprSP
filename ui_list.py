# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 130, 351, 41))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checklist = QCheckBox(self.gridLayoutWidget)
        self.checklist.setObjectName(u"checklist")

        self.gridLayout.addWidget(self.checklist, 0, 2, 1, 1)

        self.order = QLabel(self.gridLayoutWidget)
        self.order.setObjectName(u"order")

        self.gridLayout.addWidget(self.order, 0, 0, 1, 1)

        self.description = QLabel(self.gridLayoutWidget)
        self.description.setObjectName(u"description")

        self.gridLayout.addWidget(self.description, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checklist.setText(QCoreApplication.translate("Form", u"Done", None))
        self.order.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.description.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

