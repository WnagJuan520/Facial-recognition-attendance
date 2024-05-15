from PyQt5.QtGui import QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QDateTime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 637)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 771, 301))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 340, 521, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 20, 251, 221))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(0, 20, 251, 221))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(560, 500, 197, 63))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget1)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.verticalLayout.addWidget(self.dateEdit)
        self.verticalLayout.addWidget(self.dateEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(540, 420, 251, 71))
        self.label_2.setStyleSheet("color:rgb(255, 0, 0)")
        self.label_2.setObjectName("label_2")
        # 创建定时器对象，用于实时显示时间
        self.datetime = QTimer()
        # 每500ms获取一次系统时间
        self.datetime.start(500)
        self.datetime.timeout.connect(self.get_datetime)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionaddclass = QtWidgets.QAction(MainWindow)
        self.actionaddclass.setObjectName("actionaddclass")
        self.actiondelclass = QtWidgets.QAction(MainWindow)
        self.actiondelclass.setObjectName("actiondelclass")
        self.actionfindclass = QtWidgets.QAction(MainWindow)
        self.actionfindclass.setObjectName("actionfindclass")
        self.actionaddStu = QtWidgets.QAction(MainWindow)
        self.actionaddStu.setObjectName("actionaddStu")
        self.actiondelStu = QtWidgets.QAction(MainWindow)
        self.actiondelStu.setObjectName("actiondelStu")
        self.actionfindStu = QtWidgets.QAction(MainWindow)
        self.actionfindStu.setObjectName("actionfindStu")
        self.menu.addAction(self.actionaddclass)
        self.menu.addAction(self.actiondelclass)
        self.menu.addAction(self.actionfindclass)
        self.menu_2.addAction(self.actionaddStu)
        self.menu_2.addAction(self.actiondelStu)
        self.menu_2.addAction(self.actionfindStu)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别考勤机"))
        MainWindow.setWindowIcon(QIcon("./image/huang.png"))
        self.label.setText(_translate("MainWindow", " "))
        self.groupBox.setTitle(_translate("MainWindow", "成员签到信息"))
        self.groupBox_2.setTitle(_translate("MainWindow", "成员检测信息"))
        self.pushButton.setText(_translate("MainWindow", "开始签到"))
        self.pushButton_2.setText(_translate("MainWindow", "停止签到"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "小组信息管理"))
        self.menu_2.setTitle(_translate("MainWindow", "成员信息管理"))
        self.actionaddclass.setText(_translate("MainWindow", "添加小组"))
        self.actiondelclass.setText(_translate("MainWindow", "删除小组"))
        self.actionfindclass.setText(_translate("MainWindow", "小组查找"))
        self.actionaddStu.setText(_translate("MainWindow", "增加成员"))
        self.actiondelStu.setText(_translate("MainWindow", "删除成员"))
        self.actionfindStu.setText(_translate("MainWindow", "成员查找"))
