# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_todo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CalendarPicker, ComboBox, LineEdit,
    PushButton, TextEdit, TimePicker)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(669, 458)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 348, 321))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = BodyLabel(self.layoutWidget)
        self.title.setObjectName(u"title")

        self.verticalLayout.addWidget(self.title)

        self.title_input = LineEdit(self.layoutWidget)
        self.title_input.setObjectName(u"title_input")

        self.verticalLayout.addWidget(self.title_input)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.description = BodyLabel(self.layoutWidget)
        self.description.setObjectName(u"description")

        self.verticalLayout_2.addWidget(self.description)

        self.description_input = TextEdit(self.layoutWidget)
        self.description_input.setObjectName(u"description_input")

        self.verticalLayout_2.addWidget(self.description_input)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.due = BodyLabel(self.layoutWidget)
        self.due.setObjectName(u"due")

        self.verticalLayout.addWidget(self.due)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.due_input = CalendarPicker(self.layoutWidget)
        self.due_input.setObjectName(u"due_input")

        self.horizontalLayout.addWidget(self.due_input)

        self.dateTimeEdit = TimePicker(self.layoutWidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout.addWidget(self.dateTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.status = BodyLabel(self.layoutWidget)
        self.status.setObjectName(u"status")

        self.verticalLayout.addWidget(self.status)

        self.status_input = ComboBox(self.layoutWidget)
        self.status_input.addItem("")
        self.status_input.addItem("")
        self.status_input.setObjectName(u"status_input")
        self.status_input.setFlat(True)

        self.verticalLayout.addWidget(self.status_input)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(410, 310, 239, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.save = PushButton(self.layoutWidget_2)
        self.save.setObjectName(u"save")

        self.horizontalLayout_2.addWidget(self.save)

        self.delete_2 = PushButton(self.layoutWidget_2)
        self.delete_2.setObjectName(u"delete_2")

        self.horizontalLayout_2.addWidget(self.delete_2)

        self.cancel = PushButton(self.layoutWidget_2)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout_2.addWidget(self.cancel)

        self.extra = QLabel(Form)
        self.extra.setObjectName(u"extra")
        self.extra.setGeometry(QRect(400, 10, 241, 221))
        self.extra.setPixmap(QPixmap(u":/images/images/herta.gif"))
        self.extra.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Title", None))
        self.description.setText(QCoreApplication.translate("Form", u"Description", None))
        self.due.setText(QCoreApplication.translate("Form", u"Due", None))
        self.status.setText(QCoreApplication.translate("Form", u"Status", None))
        self.status_input.setItemText(0, QCoreApplication.translate("Form", u"Completed", None))
        self.status_input.setItemText(1, QCoreApplication.translate("Form", u"Not Completed", None))

        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.delete_2.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.extra.setText("")
    # retranslateUi

