# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python_sandbox\pysimplegui_designer\untitled - Copy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(541, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(240, 5, 298, 166))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.r2 = QtWidgets.QRadioButton(self.groupBox)
        self.r2.setObjectName("r2")
        self.gridLayout.addWidget(self.r2, 2, 0, 1, 1)
        self.r1 = QtWidgets.QRadioButton(self.groupBox)
        self.r1.setChecked(True)
        self.r1.setObjectName("r1")
        self.gridLayout.addWidget(self.r1, 0, 0, 1, 1)
        self.r3 = QtWidgets.QRadioButton(self.groupBox)
        self.r3.setObjectName("r3")
        self.gridLayout.addWidget(self.r3, 3, 0, 1, 1)
        self.r4 = QtWidgets.QRadioButton(self.groupBox)
        self.r4.setObjectName("r4")
        self.gridLayout.addWidget(self.r4, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rr3 = QtWidgets.QRadioButton(self.groupBox_3)
        self.rr3.setAutoRepeat(False)
        self.rr3.setObjectName("rr3")
        self.gridLayout_3.addWidget(self.rr3, 2, 0, 1, 1)
        self.rr1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.rr1.setObjectName("rr1")
        self.gridLayout_3.addWidget(self.rr1, 0, 0, 1, 1)
        self.rr2 = QtWidgets.QRadioButton(self.groupBox_3)
        self.rr2.setChecked(True)
        self.rr2.setAutoRepeat(False)
        self.rr2.setObjectName("rr2")
        self.gridLayout_3.addWidget(self.rr2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 1, 0, 1, 1)
        self.stat = QtWidgets.QPushButton(self.frame)
        self.stat.setObjectName("stat")
        self.gridLayout_2.addWidget(self.stat, 1, 2, 1, 1)
        self.dasf = QtWidgets.QVBoxLayout()
        self.dasf.setObjectName("dasf")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.dasf.addWidget(self.label_2)
        self.r1_2 = QtWidgets.QRadioButton(self.frame)
        self.r1_2.setChecked(True)
        self.r1_2.setObjectName("r1_2")
        self.dasf.addWidget(self.r1_2)
        self.r4_2 = QtWidgets.QRadioButton(self.frame)
        self.r4_2.setObjectName("r4_2")
        self.dasf.addWidget(self.r4_2)
        self.r2_2 = QtWidgets.QRadioButton(self.frame)
        self.r2_2.setObjectName("r2_2")
        self.dasf.addWidget(self.r2_2)
        self.r3_2 = QtWidgets.QRadioButton(self.frame)
        self.r3_2.setObjectName("r3_2")
        self.dasf.addWidget(self.r3_2)
        self.gridLayout_2.addLayout(self.dasf, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(11, 11, 211, 73))
        self.groupBox_2.setObjectName("groupBox_2")
        self.q4 = QtWidgets.QPushButton(self.groupBox_2)
        self.q4.setGeometry(QtCore.QRect(109, 49, 99, 21))
        self.q4.setObjectName("q4")
        self.q3 = QtWidgets.QPushButton(self.groupBox_2)
        self.q3.setGeometry(QtCore.QRect(109, 22, 99, 21))
        self.q3.setObjectName("q3")
        self.q1 = QtWidgets.QPushButton(self.groupBox_2)
        self.q1.setGeometry(QtCore.QRect(3, 22, 100, 21))
        self.q1.setObjectName("q1")
        self.q2 = QtWidgets.QPushButton(self.groupBox_2)
        self.q2.setGeometry(QtCore.QRect(3, 49, 100, 21))
        self.q2.setObjectName("q2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(87, 3, 37, 16))
        self.label.setObjectName("label")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(25, 195, 476, 396))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_3)
        self.timeEdit.setGeometry(QtCore.QRect(245, 230, 106, 20))
        self.timeEdit.setObjectName("timeEdit")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(245, 4, 37, 16))
        self.label_3.setObjectName("label_3")
        self.q1_2 = QtWidgets.QPushButton(self.tab_3)
        self.q1_2.setGeometry(QtCore.QRect(245, 23, 75, 23))
        self.q1_2.setObjectName("q1_2")
        self.radioButton = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton.setGeometry(QtCore.QRect(245, 52, 82, 18))
        self.radioButton.setObjectName("radioButton")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_3)
        self.horizontalSlider.setGeometry(QtCore.QRect(245, 152, 84, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 103, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget.setGeometry(QtCore.QRect(14, 393, 181, 106))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab_3)
        self.dateTimeEdit.setGeometry(QtCore.QRect(245, 282, 106, 20))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalSlider = QtWidgets.QSlider(self.tab_3)
        self.verticalSlider.setGeometry(QtCore.QRect(289, 174, 16, 50))
        self.verticalSlider.setMinimumSize(QtCore.QSize(0, 50))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(34, 508, 120, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_3)
        self.dateEdit.setGeometry(QtCore.QRect(245, 256, 106, 20))
        self.dateEdit.setObjectName("dateEdit")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox.setGeometry(QtCore.QRect(245, 126, 91, 20))
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.spinBox = QtWidgets.QSpinBox(self.tab_3)
        self.spinBox.setGeometry(QtCore.QRect(245, 100, 91, 20))
        self.spinBox.setObjectName("spinBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_2.setGeometry(QtCore.QRect(245, 76, 71, 18))
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 13, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(24, 193, 160, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.rewr = QtWidgets.QGroupBox(self.tab_3)
        self.rewr.setGeometry(QtCore.QRect(24, 288, 120, 80))
        self.rewr.setObjectName("rewr")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.q1_3 = QtWidgets.QPushButton(self.tab_4)
        self.q1_3.setObjectName("q1_3")
        self.gridLayout_7.addWidget(self.q1_3, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.q2_2 = QtWidgets.QPushButton(self.tab_4)
        self.q2_2.setObjectName("q2_2")
        self.gridLayout_7.addWidget(self.q2_2, 2, 0, 1, 1)
        self.q4_2 = QtWidgets.QPushButton(self.tab_4)
        self.q4_2.setObjectName("q4_2")
        self.gridLayout_7.addWidget(self.q4_2, 2, 1, 1, 1)
        self.q3_2 = QtWidgets.QPushButton(self.tab_4)
        self.q3_2.setObjectName("q3_2")
        self.gridLayout_7.addWidget(self.q3_2, 1, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(55, 95, 104, 64))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "car method"))
        self.r2.setText(_translate("MainWindow", "second"))
        self.r1.setText(_translate("MainWindow", "none"))
        self.r3.setText(_translate("MainWindow", "third"))
        self.r4.setText(_translate("MainWindow", "first"))
        self.groupBox_3.setTitle(_translate("MainWindow", "jet method"))
        self.rr3.setText(_translate("MainWindow", "third"))
        self.rr1.setText(_translate("MainWindow", "first"))
        self.rr2.setText(_translate("MainWindow", "second"))
        self.checkBox.setText(_translate("MainWindow", "cool flag"))
        self.stat.setText(_translate("MainWindow", "дай статус"))
        self.label_2.setText(_translate("MainWindow", "human method"))
        self.r1_2.setText(_translate("MainWindow", "1"))
        self.r4_2.setText(_translate("MainWindow", "2"))
        self.r2_2.setText(_translate("MainWindow", "3"))
        self.r3_2.setText(_translate("MainWindow", "4"))
        self.q4.setText(_translate("MainWindow", "q4 button"))
        self.q3.setText(_translate("MainWindow", "q3 button"))
        self.q1.setText(_translate("MainWindow", "q1 button"))
        self.q2.setText(_translate("MainWindow", "q2 button"))
        self.label.setText(_translate("MainWindow", "Кнопки"))
        self.label_3.setText(_translate("MainWindow", "Кнопки"))
        self.q1_2.setText(_translate("MainWindow", "q1 button"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.rewr.setTitle(_translate("MainWindow", "GroupBox3123"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Tab 1"))
        self.q1_3.setText(_translate("MainWindow", "q1 button"))
        self.label_4.setText(_translate("MainWindow", "Кнопки"))
        self.q2_2.setText(_translate("MainWindow", "q2 button"))
        self.q4_2.setText(_translate("MainWindow", "q4 button"))
        self.q3_2.setText(_translate("MainWindow", "q3 button"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">greg</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">greg</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

