'''
创建类对象
open函数完成摄像头的配置打开
'''
import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap


class camera():
    '''
    类初始化，相当于构造函数
    '''

    def __init__(self):
        self.open_camera()

    '''
        以下函数通过opencv打开笔记本电脑默认摄像头
    '''

    def open_camera(self):
        # 因此我们需要得到它，并且将他返回
        # 0通常表示内置默认摄像头,但有时设备排序顺序会导致0表示外置摄像头。self.capture为全局变量
        # 在上面的self.capture得到结果中，我们需要进行结果的读取，通过self.capture.read()
        self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        # isopend()函数返回一个布尔值，来判断是否打开摄像头
        if self.capture.isOpened():
            print("摄像头打开成功")
        # 定义一个多维数组，用来存储获取的画面数据
        self.currentframe = np.array([])

    '''
        获取摄像头数据
    '''

    def read_camera(self):
        # 读取摄像头画面，并且实现按帧读取，每一帧就是一副图像，当这些图像连接起来，就是一条视频图像，返回的结果为ret,
        # pic_data，pic_data就是我们需要的结果，而ret主要用来判断去取状态，如果摄像头有数据，返回True，没有则返回Flase;
        ret, pic_data = self.capture.read()
        face_detect = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')
        face = face_detect.detectMultiScale(pic_data, scaleFactor=1.3, minNeighbors=10)
        for x, y, w, h in face:
            cv2.rectangle(pic_data, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)

        if not ret:
            print("获取摄像头数据失败")
            return None
        return pic_data

    '''
        摄像头图像格式转换
    '''

    # 因为在界面Label框中进行显示的图像格式是QPixmap的图像格式，而OpenCV读取的图像格式为像素数组格式的图像，
    # 因此需要进行转换才能在Label上进行显示：返回参数为qpix(用于Label框显示的格式图像)
    def camera_to_pic(self):
        pic = self.read_camera()
        # 摄像头是BGR需要转换为RGB
        # image 转 cv2 格式
        self.currentframe = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        # 设置宽高

        # self.currentframe=cv2.cvtColor(self.currentframe,(521,411))
        height, width = self.currentframe.shape[:2]
        # 转换格式（界面能够显示的格式）
        # 先转换为QImage图片（画面）
        # QImage(data,width,height,format)创建：数据、快读、高度、格式
        qimg = QImage(self.currentframe, width, height, QImage.Format_RGB888)
        qpix = QPixmap.fromImage(qimg)
        return qpix

    '''
        关闭摄像头
    '''

    def colse_camera(self):
        # 释放摄像头
        self.capture.release()
