# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_edt.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

from qfluentwidgets import (BodyLabel, CalendarPicker, CheckBox, ComboBox,
    LineEdit, PushButton, TextEdit, TimePicker)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(349, 400)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 281, 381))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 350, 239, 26))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.save = PushButton(self.layoutWidget)
        self.save.setObjectName(u"save")

        self.horizontalLayout.addWidget(self.save)

        self.dell = PushButton(self.layoutWidget)
        self.dell.setObjectName(u"dell")

        self.horizontalLayout.addWidget(self.dell)

        self.cancel = PushButton(self.layoutWidget)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 258, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = BodyLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.title_input = LineEdit(self.layoutWidget1)
        self.title_input.setObjectName(u"title_input")

        self.verticalLayout.addWidget(self.title_input)

        self.label_2 = BodyLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.description_input = TextEdit(self.layoutWidget1)
        self.description_input.setObjectName(u"description_input")

        self.verticalLayout.addWidget(self.description_input)

        self.label_3 = BodyLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.priorities_input = ComboBox(self.layoutWidget1)
        self.priorities_input.setObjectName(u"priorities_input")

        self.verticalLayout.addWidget(self.priorities_input)

        self.label_4 = BodyLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.deadline_input = CalendarPicker(self.layoutWidget1)
        self.deadline_input.setObjectName(u"deadline_input")

        self.verticalLayout.addWidget(self.deadline_input)

        self.time_deadline_input = TimePicker(self.layoutWidget1)
        self.time_deadline_input.setObjectName(u"time_deadline_input")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_deadline_input.sizePolicy().hasHeightForWidth())
        self.time_deadline_input.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.time_deadline_input)

        self.completed = CheckBox(self.layoutWidget1)
        self.completed.setObjectName(u"completed")

        self.verticalLayout.addWidget(self.completed)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.dell.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Form", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Priorities", None))
        self.priorities_input.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Deadline", None))
        self.deadline_input.setText("")
        self.time_deadline_input.setText("")
        self.completed.setText(QCoreApplication.translate("Form", u"Completed", None))
    # retranslateUi

