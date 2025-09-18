# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_todo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QWidget)

from qfluentwidgets import (BodyLabel, CheckBox)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(255, 20)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 311, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_label = BodyLabel(self.layoutWidget)
        self.title_label.setObjectName(u"title_label")

        self.horizontalLayout.addWidget(self.title_label)

        self.due_in_label = BodyLabel(self.layoutWidget)
        self.due_in_label.setObjectName(u"due_in_label")

        self.horizontalLayout.addWidget(self.due_in_label)

        self.prioritize_label = BodyLabel(self.layoutWidget)
        self.prioritize_label.setObjectName(u"prioritize_label")

        self.horizontalLayout.addWidget(self.prioritize_label)

        self.completed_label = CheckBox(self.layoutWidget)
        self.completed_label.setObjectName(u"completed_label")

        self.horizontalLayout.addWidget(self.completed_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Title", None))
        self.due_in_label.setText(QCoreApplication.translate("Form", u"Due in", None))
        self.prioritize_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.completed_label.setText("")
    # retranslateUi

