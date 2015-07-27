# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulationtask2widget.ui'
#
# Created: Tue Jul 28 00:37:32 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SimulationTask2Widget(object):
    def setupUi(self, SimulationTask2Widget):
        SimulationTask2Widget.setObjectName("SimulationTask2Widget")
        SimulationTask2Widget.resize(819, 567)
        self.horizontalLayout = QtGui.QHBoxLayout(SimulationTask2Widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QtGui.QDockWidget(SimulationTask2Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setStyleSheet("QToolBox::tab {\n"
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
        self.dockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(self.dockWidgetContents)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButtonEuler = QtGui.QRadioButton(self.groupBox)
        self.radioButtonEuler.setChecked(True)
        self.radioButtonEuler.setObjectName("radioButtonEuler")
        self.verticalLayout_3.addWidget(self.radioButtonEuler)
        self.radioButtonCvode = QtGui.QRadioButton(self.groupBox)
        self.radioButtonCvode.setChecked(False)
        self.radioButtonCvode.setObjectName("radioButtonCvode")
        self.verticalLayout_3.addWidget(self.radioButtonCvode)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.stepSizeSpinBox = QtGui.QDoubleSpinBox(self.dockWidgetContents)
        self.stepSizeSpinBox.setDecimals(5)
        self.stepSizeSpinBox.setMaximum(10.0)
        self.stepSizeSpinBox.setSingleStep(0.01)
        self.stepSizeSpinBox.setProperty("value", 0.1)
        self.stepSizeSpinBox.setObjectName("stepSizeSpinBox")
        self.horizontalLayout_2.addWidget(self.stepSizeSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.nSpinBox = QtGui.QSpinBox(self.dockWidgetContents)
        self.nSpinBox.setMinimum(2)
        self.nSpinBox.setProperty("value", 30)
        self.nSpinBox.setObjectName("nSpinBox")
        self.horizontalLayout_4.addWidget(self.nSpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.simulateButton = QtGui.QPushButton(self.dockWidgetContents)
        self.simulateButton.setObjectName("simulateButton")
        self.verticalLayout.addWidget(self.simulateButton)
        self.clearButton = QtGui.QPushButton(self.dockWidgetContents)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.doneButton = QtGui.QPushButton(self.dockWidgetContents)
        self.doneButton.setObjectName("doneButton")
        self.verticalLayout.addWidget(self.doneButton)
        self.dockWidget.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.dockWidget)
        self.plotPane = QtGui.QWidget(SimulationTask2Widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotPane.sizePolicy().hasHeightForWidth())
        self.plotPane.setSizePolicy(sizePolicy)
        self.plotPane.setObjectName("plotPane")
        self.horizontalLayout.addWidget(self.plotPane)

        self.retranslateUi(SimulationTask2Widget)
        QtCore.QMetaObject.connectSlotsByName(SimulationTask2Widget)

    def retranslateUi(self, SimulationTask2Widget):
        SimulationTask2Widget.setWindowTitle(QtGui.QApplication.translate("SimulationTask2Widget", "Heart Transform", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("SimulationTask2Widget", "Simulation Task 2", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SimulationTask2Widget", "Integration method:", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonEuler.setText(QtGui.QApplication.translate("SimulationTask2Widget", "Euler (h=step size)", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCvode.setText(QtGui.QApplication.translate("SimulationTask2Widget", "CVODE (h=max step)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SimulationTask2Widget", "h:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SimulationTask2Widget", "number of points:", None, QtGui.QApplication.UnicodeUTF8))
        self.simulateButton.setText(QtGui.QApplication.translate("SimulationTask2Widget", "Simulate", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("SimulationTask2Widget", "Clear graph", None, QtGui.QApplication.UnicodeUTF8))
        self.doneButton.setText(QtGui.QApplication.translate("SimulationTask2Widget", "Done", None, QtGui.QApplication.UnicodeUTF8))

