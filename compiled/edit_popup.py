# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_popup.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
from compiled import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(671, 300)
        self.extra = QLabel(Form)
        self.extra.setObjectName(u"extra")
        self.extra.setGeometry(QRect(330, 10, 161, 161))
        self.extra.setPixmap(QPixmap(u":/images/images/herta.gif"))
        self.extra.setScaledContents(True)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 10, 261, 143))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.layoutWidget)
        self.title.setObjectName(u"title")

        self.verticalLayout.addWidget(self.title)

        self.title_input = QLineEdit(self.layoutWidget)
        self.title_input.setObjectName(u"title_input")

        self.verticalLayout.addWidget(self.title_input)

        self.description = QLabel(self.layoutWidget)
        self.description.setObjectName(u"description")

        self.verticalLayout.addWidget(self.description)

        self.description_input = QLineEdit(self.layoutWidget)
        self.description_input.setObjectName(u"description_input")

        self.verticalLayout.addWidget(self.description_input)

        self.due = QLabel(self.layoutWidget)
        self.due.setObjectName(u"due")

        self.verticalLayout.addWidget(self.due)

        self.due_input = QLineEdit(self.layoutWidget)
        self.due_input.setObjectName(u"due_input")

        self.verticalLayout.addWidget(self.due_input)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 180, 239, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.save = QPushButton(self.layoutWidget1)
        self.save.setObjectName(u"save")

        self.horizontalLayout.addWidget(self.save)

        self.delete_2 = QPushButton(self.layoutWidget1)
        self.delete_2.setObjectName(u"delete_2")

        self.horizontalLayout.addWidget(self.delete_2)

        self.cancel = QPushButton(self.layoutWidget1)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.extra.setText("")
        self.title.setText(QCoreApplication.translate("Form", u"Title", None))
        self.description.setText(QCoreApplication.translate("Form", u"Description", None))
        self.due.setText(QCoreApplication.translate("Form", u"Due", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.delete_2.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

