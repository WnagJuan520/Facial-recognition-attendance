
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 500)#对话框调整大小
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.tableWidget)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "成员签到信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "组号"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "时间"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "是否迟到"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "是否早退"))
        self.pushButton_2.setText(_translate("Dialog", "导出为Excel"))
        self.pushButton.setText(_translate("Dialog", "取消"))