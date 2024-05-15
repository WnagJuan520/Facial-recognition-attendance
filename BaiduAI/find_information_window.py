import xlwt
from PyQt5.QtWidgets import QDialog, QAbstractItemView, QTableWidgetItem, QHeaderView, QFileDialog, QMessageBox
from PyQt5.QtCore import QTime
from find_information import Ui_Dialog
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
import datetime
import pymysql
import mysql.connector

class find_information_window(Ui_Dialog,QDialog):
    def __init__(self,sign_data,parent=None):
        super(find_information_window,self).__init__(parent)
        self.setupUi(self)
        self.sign_data = sign_data#接收签到数据
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)#设置表格不可更改
        #设置表格为指定长度
        self.tableWidget.setColumnWidth(0, 55)#第一列格子大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(1, 85)#第二列格子大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(2, 65)#第三列格子大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(3, 105)#第四列格子大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(4, 85)#第五列格子大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tableWidget.setColumnWidth(5, 85)#第六列格子大小
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)

        for i in self.sign_data.values():
            row=self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row,0,QTableWidgetItem(i['user_id']))
            self.tableWidget.setItem(row,1, QTableWidgetItem(i['user_info']))
            self.tableWidget.setItem(row,2, QTableWidgetItem(i['group_id']))
            self.tableWidget.setItem(row,3, QTableWidgetItem(i['datetime']))
            time = QTime.currentTime()  # 获取人脸打开时间
            time = time.toString()  # 将获取到的时间转为字符串
            # # 例如： 周日 3月 5 09:46:46 2023


            checkin_start = datetime.time(8, 0, 0)
            checkin_end = datetime.time(12, 0, 0)
            checkout_start = datetime.time(13, 0, 0)
            checkout_end = datetime.time(17, 0, 0)
            current_time = datetime.datetime.now().time()
            arr = '非签到时间'
            quit = '未到签退时间'
            arr_time = '非签到时间'
            quit_time = '非签退时间'
            if current_time > checkin_start and current_time < checkin_end:  # 8点到12点
                arr = "迟到"
                quit = '未到签退时间'
            elif current_time < checkin_start:  # 早于8点
                arr = "没迟到"
                quit = '未到签退时间'
            elif current_time < checkout_end and current_time > checkout_start:  # 下午一点到五点
                quit = '早退'

            else:
                quit = '正常下班'
            self.tableWidget.setItem(row, 4, QTableWidgetItem(arr))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(quit))
            self.tableWidget.resizeColumnToContents(6)
        self.pushButton_2.clicked.connect(self.export)#绑定按钮事件为导出为Excel
        self.pushButton_2.clicked.connect(self.mykuku)#绑定按钮事件为导出数据库
        self.pushButton.clicked.connect(self.closewindow)#取消按钮事件绑定为取消方法
    #表格数据导出
    def export(self): #打开保存文件弹窗
        try:
            path, ret = QFileDialog.getSaveFileName(self, "选择导出文件路径", ".", "文件格式(*.xls)")
            row = self.tableWidget.rowCount()  # 获取行
            column = self.tableWidget.columnCount()  # 获取列
            # 创建一个workbook 设置编码
            workbook = xlwt.Workbook(encoding='utf-8')
            # 创建一个表的名称，不是文件名称
            worksheet = workbook.add_sheet('成员签到信息')
            for j in range(column):
                table = self.tableWidget.horizontalHeaderItem(j).text()  # 获取表头
                worksheet.write(0, j, table)  # 写入表头
            for i in range(row):
                for j in range(column):
                    data = self.tableWidget.item(i, j).text()  # 获取签到数据
                    # 写入excel 参数对应 行, 列, 值
                    worksheet.write(i + 1, j, data)  # 写入签到数据
            workbook.save(path)# 保存
            QMessageBox.about(self, "提示", "数据导出成功！")
            self.accept()
        except:
            QMessageBox.about(self, "提示", "数据导出异常！")

        #         #表的数据为：
        #         #iD,name,group_name,time,early,late
    def mykuku(self):
        # 打开数据库连接，参数1：主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名
        db = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='mykuku')
        # 使用cursor()创建一个cursor对象
        cursor = db.cursor()
        time = QDateTime.currentDateTime()
        #time = QTime.currentTime()  # 获取人脸打开时间
        time = time.toString()
        checkin_start = datetime.time(8, 0, 0)
        checkin_end = datetime.time(12, 0, 0)
        checkout_start = datetime.time(13, 0, 0)
        checkout_end = datetime.time(17, 0, 0)
        current_time = datetime.datetime.now().time()
        early = '非签到时间'
        late = '未到签退时间'
        for i in self.sign_data.values():
            user_id = i['user_id']
            name = i['user_info']  # 根据需求自行修改
            group_name = i['group_id']  # 根据需求自行修改
            time = time
            if current_time > checkin_start and current_time < checkin_end:  # 8点到12点
                early = "迟到"
                quit = '未到签退时间'
            elif current_time < checkin_start:  # 早于8点
                early = "没迟到"
                quit = '未到签退时间'
            elif current_time < checkout_end and current_time > checkout_start:  # 下午一点到五点
                late = '早退'
            else:
                late = '正常下班'
            data = (user_id, name, group_name,time,early,late)
            cursor.execute("insert into Record(user_id,name,group_name,time,early,late) values (%s,%s,%s,%s,%s,%s)", data)
            # 提交数据
            db.commit()
        # 关闭数据库连接
        db.close()


        #
        # # 插入数据的SQL语句
        # add_data = ("INSERT INTO table_name "
        #             "(id, name, group_name, time, early, late) "
        #             "VALUES (%s, %s, %s, %s, %s, %s)")
        # # 数据库操作指针
        # cursor = cnx.cursor()
        # # 待插入的数据
        # data = (1, 'John', 'Group A', '2021-10-01 08:00:00', '08:00:00', '18:00:00')
        # # 执行插入数据操作
        # cursor.execute(add_data, data)
        # # 确认数据插入
        # cnx.commit()
        # # 关闭数据库连接
        # cursor.close()
        # cnx.close()


    #取消按钮
    def closewindow(self):
        self.close()



            # if (int(time[0] + time[1] + time[3] + time[4]) > 900 ):
            #     out = '是'
            # else:
            #     out = '否'

            # 日期双数
            # if ((int(datetime[9] + datetime[10] + datetime[12] + datetime[13])) < 900 and int(
            #         datetime[9]) == 0):
            #     out = '否'
            # else:
            #     out = '是'







        # 打开数据库连接，参数1：主机名或IP；参数2：用户名；参数3：密码；参数4：数据库名
        #         # db = {
        #         #     'user': 'root',
        #         #     'password': '123456',
        #         #     'host': '127.0.0.1',
        #         #     'database': 'mykuku',
        #         #     'charset': 'utf8'
        #         # }
        #         # cnx = mysql.connector.connect(db)
        #         # # 使用cursor()创建一个cursor对象
        #         # cursor = cnx.cursor()
        #         # 使用execute()方法执行SQL语句，如果表存在删除
        #
        #         # cursor.execute("DROP TABLE IF EXISTS Record")
        #         # # 使用预处理语句创建表
        #         # sql = """CREATE TABLE Record(
        #         # id INT(11) NOT NULL AUTO_INCREMENT,
        #         # name VARCHAR(50) NOT NULL,
        #         # group_name VARCHAR(50) NOT NULL,
        #         # time DATETIME NOT NULL,
        #         # early varchar(50) NOT NULL,
        #         # late varchar (50) NOT NULL,
        #         # PRIMARY KEY (id)
        #         # )DEFAULT CHARSET=utf8;
        #         # """
        #         #表的数据为：
        #         #iD,name,group_name,time,early,late
        #         # 执行SQL语句
        #         #cursor.execute(sql)
        #         # 建立MySQL数据库连接