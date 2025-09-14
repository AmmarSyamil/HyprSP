# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_hackatime.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ImageLabel, StrongBodyLabel, TitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        self.title = TitleLabel(Form)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 20, 371, 41))
        self.title.setBaseSize(QSize(10, 10))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 391, 311))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.total_time_label = StrongBodyLabel(self.frame)
        self.total_time_label.setObjectName(u"total_time_label")
        self.total_time_label.setGeometry(QRect(10, 10, 49, 16))
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 361, 21))

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.widget1 = QWidget(self.frame_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 0, 371, 241))
        self.verticalLayout_3 = QVBoxLayout(self.widget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.hackatime = StrongBodyLabel(self.widget1)
        self.hackatime.setObjectName(u"hackatime")

        self.verticalLayout_3.addWidget(self.hackatime)

        self.today_time_widget = QWidget(self.widget1)
        self.today_time_widget.setObjectName(u"today_time_widget")

        self.verticalLayout_3.addWidget(self.today_time_widget)

        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 4)
        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(410, 9, 381, 221))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.layoutWidget1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.longest_project_label = StrongBodyLabel(self.frame_3)
        self.longest_project_label.setObjectName(u"longest_project_label")
        self.longest_project_label.setGeometry(QRect(10, 10, 161, 16))
        self.longest_project_widget = QWidget(self.frame_3)
        self.longest_project_widget.setObjectName(u"longest_project_widget")
        self.longest_project_widget.setGeometry(QRect(10, 30, 361, 31))

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.layoutWidget1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.average_coding_label = StrongBodyLabel(self.frame_4)
        self.average_coding_label.setObjectName(u"average_coding_label")
        self.average_coding_label.setGeometry(QRect(10, 10, 161, 16))
        self.average_coding_widget = QWidget(self.frame_4)
        self.average_coding_widget.setObjectName(u"average_coding_widget")
        self.average_coding_widget.setGeometry(QRect(10, 30, 361, 101))

        self.verticalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.side_style = ImageLabel(Form)
        self.side_style.setObjectName(u"side_style")
        self.side_style.setGeometry(QRect(420, 240, 361, 141))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u"Hackatime", None))
        self.total_time_label.setText(QCoreApplication.translate("Form", u"Total time", None))
        self.hackatime.setText(QCoreApplication.translate("Form", u"Today time", None))
        self.longest_project_label.setText(QCoreApplication.translate("Form", u"Longest project", None))
        self.average_coding_label.setText(QCoreApplication.translate("Form", u"Average Coding", None))
        self.side_style.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

