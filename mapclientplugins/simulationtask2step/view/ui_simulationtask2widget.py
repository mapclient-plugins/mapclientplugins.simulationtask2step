# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulationtask2widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QDoubleSpinBox, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_SimulationTask2Widget(object):
    def setupUi(self, SimulationTask2Widget):
        if not SimulationTask2Widget.objectName():
            SimulationTask2Widget.setObjectName(u"SimulationTask2Widget")
        SimulationTask2Widget.resize(819, 567)
        self.horizontalLayout = QHBoxLayout(SimulationTask2Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dockWidget = QDockWidget(SimulationTask2Widget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setStyleSheet(u"QToolBox::tab {\n"
"         background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                     stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                     stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"         border-radius: 5px;\n"
"         color: black;\n"
"     }\n"
"\n"
"     QToolBox::tab:selected { /* italicize selected tabs */\n"
"         font: bold;\n"
"         color: black;\n"
"     }\n"
"QToolBox {\n"
"    padding : 0\n"
"}")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.dockWidgetContents)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButtonEuler = QRadioButton(self.groupBox)
        self.radioButtonEuler.setObjectName(u"radioButtonEuler")
        self.radioButtonEuler.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButtonEuler)

        self.radioButtonCvode = QRadioButton(self.groupBox)
        self.radioButtonCvode.setObjectName(u"radioButtonCvode")
        self.radioButtonCvode.setChecked(False)

        self.verticalLayout_3.addWidget(self.radioButtonCvode)


        self.horizontalLayout_3.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.stepSizeSpinBox = QDoubleSpinBox(self.dockWidgetContents)
        self.stepSizeSpinBox.setObjectName(u"stepSizeSpinBox")
        self.stepSizeSpinBox.setDecimals(5)
        self.stepSizeSpinBox.setMaximum(10.000000000000000)
        self.stepSizeSpinBox.setSingleStep(0.010000000000000)
        self.stepSizeSpinBox.setValue(0.100000000000000)

        self.horizontalLayout_2.addWidget(self.stepSizeSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.nSpinBox = QSpinBox(self.dockWidgetContents)
        self.nSpinBox.setObjectName(u"nSpinBox")
        self.nSpinBox.setMinimum(2)
        self.nSpinBox.setValue(30)

        self.horizontalLayout_4.addWidget(self.nSpinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.simulateButton = QPushButton(self.dockWidgetContents)
        self.simulateButton.setObjectName(u"simulateButton")

        self.verticalLayout.addWidget(self.simulateButton)

        self.clearButton = QPushButton(self.dockWidgetContents)
        self.clearButton.setObjectName(u"clearButton")

        self.verticalLayout.addWidget(self.clearButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.doneButton = QPushButton(self.dockWidgetContents)
        self.doneButton.setObjectName(u"doneButton")

        self.verticalLayout.addWidget(self.doneButton)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.plotPane = QWidget(SimulationTask2Widget)
        self.plotPane.setObjectName(u"plotPane")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plotPane.sizePolicy().hasHeightForWidth())
        self.plotPane.setSizePolicy(sizePolicy1)
        self.dockWidget.raise_()

        self.horizontalLayout.addWidget(self.plotPane)


        self.retranslateUi(SimulationTask2Widget)

        QMetaObject.connectSlotsByName(SimulationTask2Widget)
    # setupUi

    def retranslateUi(self, SimulationTask2Widget):
        SimulationTask2Widget.setWindowTitle(QCoreApplication.translate("SimulationTask2Widget", u"Heart Transform", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("SimulationTask2Widget", u"Simulation Task 2", None))
        self.groupBox.setTitle(QCoreApplication.translate("SimulationTask2Widget", u"Integration method:", None))
        self.radioButtonEuler.setText(QCoreApplication.translate("SimulationTask2Widget", u"Euler (h=step size)", None))
        self.radioButtonCvode.setText(QCoreApplication.translate("SimulationTask2Widget", u"CVODE (h=max step)", None))
        self.label.setText(QCoreApplication.translate("SimulationTask2Widget", u"h:", None))
        self.label_2.setText(QCoreApplication.translate("SimulationTask2Widget", u"number of points:", None))
        self.simulateButton.setText(QCoreApplication.translate("SimulationTask2Widget", u"Simulate", None))
        self.clearButton.setText(QCoreApplication.translate("SimulationTask2Widget", u"Clear graph", None))
        self.doneButton.setText(QCoreApplication.translate("SimulationTask2Widget", u"Done", None))
    # retranslateUi

