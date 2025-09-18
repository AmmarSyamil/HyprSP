# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_settings.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidgetItem,
    QSizePolicy, QVBoxLayout, QWidget)

from qfluentwidgets import (CheckBox, FlipView, SubtitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 400)
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 340, 221, 41))
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.settings = CheckBox(self.frame_4)
        self.settings.setObjectName(u"settings")
        self.settings.setGeometry(QRect(10, 10, 211, 20))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 781, 271))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget1 = QWidget(self.frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 10, 221, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.wuwa_label = SubtitleLabel(self.layoutWidget1)
        self.wuwa_label.setObjectName(u"wuwa_label")

        self.verticalLayout.addWidget(self.wuwa_label)

        self.wuwa_flipview = FlipView(self.layoutWidget1)
        self.wuwa_flipview.setObjectName(u"wuwa_flipview")

        self.verticalLayout.addWidget(self.wuwa_flipview)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget2 = QWidget(self.frame_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 221, 251))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.car_label = SubtitleLabel(self.layoutWidget2)
        self.car_label.setObjectName(u"car_label")

        self.verticalLayout_2.addWidget(self.car_label)

        self.car_flipview = FlipView(self.layoutWidget2)
        self.car_flipview.setObjectName(u"car_flipview")

        self.verticalLayout_2.addWidget(self.car_flipview)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.layoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget_2 = QWidget(self.frame_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 221, 251))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.default_label = SubtitleLabel(self.layoutWidget_2)
        self.default_label.setObjectName(u"default_label")

        self.verticalLayout_3.addWidget(self.default_label)

        self.default_flipview = FlipView(self.layoutWidget_2)
        self.default_flipview.setObjectName(u"default_flipview")

        self.verticalLayout_3.addWidget(self.default_flipview)


        self.horizontalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.settings.setText(QCoreApplication.translate("Form", u"dark/ light", None))
        self.wuwa_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.car_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.default_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

