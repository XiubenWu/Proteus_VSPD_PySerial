# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MyUI(object):
    def setupUi(self, MyUI):
        MyUI.setObjectName("MyUI")
        MyUI.resize(621, 446)
        self.gridLayout = QtWidgets.QGridLayout(MyUI)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(MyUI)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(MyUI)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.time = QtWidgets.QLineEdit(MyUI)
        self.time.setObjectName("time")
        self.verticalLayout_6.addWidget(self.time)
        self.saveCount = QtWidgets.QComboBox(MyUI)
        self.saveCount.setObjectName("saveCount")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.saveCount.addItem("")
        self.verticalLayout_6.addWidget(self.saveCount)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.label_3 = QtWidgets.QLabel(MyUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.start = QtWidgets.QPushButton(MyUI)
        self.start.setObjectName("start")
        self.verticalLayout_5.addWidget(self.start)
        self.save = QtWidgets.QPushButton(MyUI)
        self.save.setObjectName("save")
        self.verticalLayout_5.addWidget(self.save)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Channal0 = QtWidgets.QLabel(MyUI)
        self.Channal0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal0.setObjectName("Channal0")
        self.verticalLayout_3.addWidget(self.Channal0)
        self.Channal2 = QtWidgets.QLabel(MyUI)
        self.Channal2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal2.setObjectName("Channal2")
        self.verticalLayout_3.addWidget(self.Channal2)
        self.Channal4 = QtWidgets.QLabel(MyUI)
        self.Channal4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal4.setObjectName("Channal4")
        self.verticalLayout_3.addWidget(self.Channal4)
        self.Channal6 = QtWidgets.QLabel(MyUI)
        self.Channal6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal6.setObjectName("Channal6")
        self.verticalLayout_3.addWidget(self.Channal6)
        self.Channal2_4 = QtWidgets.QLabel(MyUI)
        self.Channal2_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal2_4.setObjectName("Channal2_4")
        self.verticalLayout_3.addWidget(self.Channal2_4)
        self.Channal2_5 = QtWidgets.QLabel(MyUI)
        self.Channal2_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal2_5.setObjectName("Channal2_5")
        self.verticalLayout_3.addWidget(self.Channal2_5)
        self.Channal12 = QtWidgets.QLabel(MyUI)
        self.Channal12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal12.setObjectName("Channal12")
        self.verticalLayout_3.addWidget(self.Channal12)
        self.Channal14 = QtWidgets.QLabel(MyUI)
        self.Channal14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channal14.setObjectName("Channal14")
        self.verticalLayout_3.addWidget(self.Channal14)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit0 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit0.setObjectName("lineEdit0")
        self.verticalLayout.addWidget(self.lineEdit0)
        self.lineEdit2 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit2.setObjectName("lineEdit2")
        self.verticalLayout.addWidget(self.lineEdit2)
        self.lineEdit4 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit4.setObjectName("lineEdit4")
        self.verticalLayout.addWidget(self.lineEdit4)
        self.lineEdit6 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit6.setObjectName("lineEdit6")
        self.verticalLayout.addWidget(self.lineEdit6)
        self.lineEdit8 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit8.setObjectName("lineEdit8")
        self.verticalLayout.addWidget(self.lineEdit8)
        self.lineEdit10 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit10.setObjectName("lineEdit10")
        self.verticalLayout.addWidget(self.lineEdit10)
        self.lineEdit12 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit12.setObjectName("lineEdit12")
        self.verticalLayout.addWidget(self.lineEdit12)
        self.lineEdit14 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit14.setObjectName("lineEdit14")
        self.verticalLayout.addWidget(self.lineEdit14)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Channel1 = QtWidgets.QLabel(MyUI)
        self.Channel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel1.setObjectName("Channel1")
        self.verticalLayout_4.addWidget(self.Channel1)
        self.Channel3 = QtWidgets.QLabel(MyUI)
        self.Channel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel3.setObjectName("Channel3")
        self.verticalLayout_4.addWidget(self.Channel3)
        self.Channel3_2 = QtWidgets.QLabel(MyUI)
        self.Channel3_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel3_2.setObjectName("Channel3_2")
        self.verticalLayout_4.addWidget(self.Channel3_2)
        self.Channel3_3 = QtWidgets.QLabel(MyUI)
        self.Channel3_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel3_3.setObjectName("Channel3_3")
        self.verticalLayout_4.addWidget(self.Channel3_3)
        self.Channel3_4 = QtWidgets.QLabel(MyUI)
        self.Channel3_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel3_4.setObjectName("Channel3_4")
        self.verticalLayout_4.addWidget(self.Channel3_4)
        self.Channel3_5 = QtWidgets.QLabel(MyUI)
        self.Channel3_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel3_5.setObjectName("Channel3_5")
        self.verticalLayout_4.addWidget(self.Channel3_5)
        self.Channel3_6 = QtWidgets.QLabel(MyUI)
        self.Channel3_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel3_6.setObjectName("Channel3_6")
        self.verticalLayout_4.addWidget(self.Channel3_6)
        self.Channel3_7 = QtWidgets.QLabel(MyUI)
        self.Channel3_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Channel3_7.setObjectName("Channel3_7")
        self.verticalLayout_4.addWidget(self.Channel3_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit1 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit1.setObjectName("lineEdit1")
        self.verticalLayout_2.addWidget(self.lineEdit1)
        self.lineEdit3 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit3.setObjectName("lineEdit3")
        self.verticalLayout_2.addWidget(self.lineEdit3)
        self.lineEdit5 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit5.setObjectName("lineEdit5")
        self.verticalLayout_2.addWidget(self.lineEdit5)
        self.lineEdit7 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit7.setObjectName("lineEdit7")
        self.verticalLayout_2.addWidget(self.lineEdit7)
        self.lineEdit9 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit9.setObjectName("lineEdit9")
        self.verticalLayout_2.addWidget(self.lineEdit9)
        self.lineEdit11 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit11.setObjectName("lineEdit11")
        self.verticalLayout_2.addWidget(self.lineEdit11)
        self.lineEdit13 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit13.setObjectName("lineEdit13")
        self.verticalLayout_2.addWidget(self.lineEdit13)
        self.lineEdit15 = QtWidgets.QLineEdit(MyUI)
        self.lineEdit15.setObjectName("lineEdit15")
        self.verticalLayout_2.addWidget(self.lineEdit15)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(MyUI)
        QtCore.QMetaObject.connectSlotsByName(MyUI)

    def retranslateUi(self, MyUI):
        _translate = QtCore.QCoreApplication.translate
        MyUI.setWindowTitle(_translate("MyUI", "Form"))
        self.label.setText(_translate("MyUI", "???????????????"))
        self.label_2.setText(_translate("MyUI", "???????????????????????????"))
        self.saveCount.setItemText(0, _translate("MyUI", "10"))
        self.saveCount.setItemText(1, _translate("MyUI", "20"))
        self.saveCount.setItemText(2, _translate("MyUI", "30"))
        self.saveCount.setItemText(3, _translate("MyUI", "40"))
        self.saveCount.setItemText(4, _translate("MyUI", "50"))
        self.saveCount.setItemText(5, _translate("MyUI", "100"))
        self.saveCount.setItemText(6, _translate("MyUI", "200"))
        self.saveCount.setItemText(7, _translate("MyUI", "1000"))
        self.saveCount.setItemText(8, _translate("MyUI", "5000"))
        self.saveCount.setItemText(9, _translate("MyUI", "10000"))
        self.start.setText(_translate("MyUI", "????????????"))
        self.save.setText(_translate("MyUI", "????????????"))
        self.Channal0.setText(_translate("MyUI", "??????0???"))
        self.Channal2.setText(_translate("MyUI", "??????2???"))
        self.Channal4.setText(_translate("MyUI", "??????4???"))
        self.Channal6.setText(_translate("MyUI", "??????6???"))
        self.Channal2_4.setText(_translate("MyUI", "??????8???"))
        self.Channal2_5.setText(_translate("MyUI", "??????10???"))
        self.Channal12.setText(_translate("MyUI", "??????12???"))
        self.Channal14.setText(_translate("MyUI", "??????14???"))
        self.Channel1.setText(_translate("MyUI", "??????1???"))
        self.Channel3.setText(_translate("MyUI", "??????3???"))
        self.Channel3_2.setText(_translate("MyUI", "??????5???"))
        self.Channel3_3.setText(_translate("MyUI", "??????7???"))
        self.Channel3_4.setText(_translate("MyUI", "??????9???"))
        self.Channel3_5.setText(_translate("MyUI", "??????11???"))
        self.Channel3_6.setText(_translate("MyUI", "??????13???"))
        self.Channel3_7.setText(_translate("MyUI", "??????15???"))


