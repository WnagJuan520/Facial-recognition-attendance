import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from function_window import function_window

if __name__ == '__main__':
    # 创建应用程序对象
    app =QApplication(sys.argv)
    widgets =QMainWindow()
    #创建窗口
    ui = function_window()
    #显示窗口
    ui.show()
    #应用执行
    app.exec_()
    #关闭应用
    sys.exit(0)