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
        Form.resize(372, 38)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.description = QLabel(Form)
        self.description.setObjectName(u"description")

        self.gridLayout.addWidget(self.description, 0, 1, 1, 1)

        self.checklist = QCheckBox(Form)
        self.checklist.setObjectName(u"checklist")

        self.gridLayout.addWidget(self.checklist, 0, 3, 1, 1)

        self.order = QLabel(Form)
        self.order.setObjectName(u"order")

        self.gridLayout.addWidget(self.order, 0, 0, 1, 1)

        self.deadlne = QLabel(Form)
        self.deadlne.setObjectName(u"deadlne")

        self.gridLayout.addWidget(self.deadlne, 0, 2, 1, 1)

        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.description.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.checklist.setText(QCoreApplication.translate("Form", u"Done", None))
        self.order.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.deadlne.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

