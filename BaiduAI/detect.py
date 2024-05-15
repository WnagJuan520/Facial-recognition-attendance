import requests
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtCore import QTime
import datetime
class detect_thread(QThread):
    transmit_data = pyqtSignal(dict)#定义信号，用于子线程与主线程中的人脸检测数据交互
    transmit_data1 = pyqtSignal(str)  # 定义信号，用于子线程与主线程中的人脸识别数据交互
    # 字典用来存储签到数据
    sign_data_list = {}
    def __init__(self,access_token):
        super(detect_thread,self).__init__()# super()函数是用于调用父类的一个方法。
        self.ok=True#循环控制变量
        self.condition = False#人脸检测控制变量，是否进行人脸检测
        self.access_token=access_token#主线程获取的access_token信息传递给子线程并设置为全局变量
    #run函数执行结束代表线程结束
    def run(self):
        while self.ok==True:
            if self.condition==True:
                self.detect_face(self.imageData)# 人脸检测
                self.condition=False
    '''
        接收主线程传递过来的图像
    '''
    # 主线程每隔500毫秒会向线程中发送一帧图像，因此线程中需要有一个函数接收传递过来的图像
    def get_imgdata(self,data):
        #当窗口调用这个槽函数，就把传递的数据存放在线程的变量中
        self.imageData=data#将接收到图像数据赋值给全局变量
        self.condition=True#主线程有图像传递过来，改变condition的状态，run函数中运行人脸检测函数
    '''
        人脸检测
    '''
    def detect_face(self,base64_image):
        '''
        以下代码是套用百度API文档提供的模板
        '''
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        # 请求参数是一个字典，在字典中存储了，要识别的内容
        params = {
            "image": base64_image,  # 图片信息字符串
            "image_type": "BASE64",  # 图片信息的格式
            "face_field": "gender,age,beauty,mask,emotion,expression,glasses,face_shape",  # 请求识别人脸的属性，各个属性在字符中用逗号隔开
            "max_face_num": 10#能够检测的最多人脸数
        }
        # 访问令牌
        access_token = self.access_token
        request_url = request_url + "?access_token=" + access_token
        # 设置请求的格式体
        headers = {'content-type': 'application/json'}
        # 发送post网络请求,请求百度AI进行人脸检测
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            data = response.json()
            self.face_search()
            self.transmit_data.emit(dict(data))#如果返回结果正确，则将返回信息传递给主线程


    # 人脸识别搜索检测，只识别一个人
    def face_search(self):
        request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
        params = {
            "image": self.imageData,
            "image_type": "BASE64",
            "group_id_list": "class1,Dianxin193,Dianxin192,Dianxin191",
        }
        access_token = self.access_token
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            data = response.json()
            if data['error_msg'] == 'SUCCESS':
                #查错用
                #print('人脸签到：')
                #print(data)
                if data['result']['user_list'][0]['score'] > 90: #大于90分，意味人脸识别成功
                    del [data['result']['user_list'][0]['score']]
                    time = QTime.currentTime()#获取人脸打开时间
                    time = time.toString()#将获取到的时间转为字符串
                    datatime = QDateTime.currentDateTime()
                    datatime = datatime.toString()
                    # 测试代码 print(time)
                    checkin_start = datetime.time(8, 0, 0)
                    checkin_end = datetime.time(12, 0, 0)
                    checkout_start = datetime.time(13, 0, 0)
                    checkout_end = datetime.time(17, 0, 0)
                    current_time = datetime.datetime.now().time()
                    arr = '非签到时间'
                    quit = '未到签退时间'
                    arr_time = '非签到时间'
                    quit_time = '非签退时间'
                    if current_time > checkin_start and current_time < checkin_end:#8点到12点
                        arr = "迟到"
                        quit = '未到签退时间'
                        arr_time = time
                    elif current_time < checkin_start: #早于8点
                        arr = "没迟到"
                        quit = '未到签退时间'
                        arr_time = time
                    elif current_time < checkout_end and current_time > checkout_start: # 下午一点到五点
                        quit = '早退'
                        quit_time = time
                    else:
                        quit_time = time
                        quit = '正常下班'



                    data['result']['user_list'][0]['datetime'] = datatime#将获取到的时间添加到返回的数据中
                    # 测试是否迟到 print(out)
                    key = data['result']['user_list'][0]['group_id'] + data['result']['user_list'][0]['user_info']#在变量中键入值，包括小组名称和成员编号
                    if key not in self.sign_data_list.keys():
                        self.sign_data_list[key] = data['result']['user_list'][0]
                    list1 = [data['result']['user_list'][0]['user_info'],data['result']['user_list'][0]['group_id']]
                    self.transmit_data1.emit("成员签到成功\n成员信息如下:\n" + "姓名:" + list1[0] + "\n" + "组号:" + list1[1]+ "\n"+ "是否迟到:"+ arr  +  "\n" + "签到时间:" + arr_time + "\n"+ "是否早退:" + quit + "\n"+ "签退时间:" + quit_time)#将信号发送给主线程

                # print(datetime[9],datetime[11],datetime[12])
               # if (int(time[0] + time[1] + time[3] + time[4]) > 900):#             判断迟到 已经迟到
                    #     out='是'
                    #     arr_time = time
                    #     if(int(time[0] + time[1] + time[3] + time[4]) < 1400):#         判断早退 没到签到时间
                    #         quit='未到签退时间'
                    #     else:
                    #         if(int(time[0] + time[1] + time[3] + time[4]) < 1700):#     早退
                    #             quit='是'
                    #             quit_time = time
                    #         else:#没早退
                    #             quit='否'
                    #             quit_time = time
                    # else:    #                                                          没迟到
                    #     out='否'
                    #     arr_time = time
                    #     if (int(time[0] + time[1] + time[3] + time[4]) < 1400):#        没到签到时间
                    #         quit = '未到签退时间'
                    #     else:
                    #         if (int(time[0] + time[1] + time[3] + time[4]) < 1700):#    早退
                    #             quit = '是'
                    #             quit_time = time
                    #         else:
                    #             quit = '否'
                    #             quit_time = time

                    #例如： 周日 3月 5 09:46:46 2023
                    # # 日期单数
                    # if ((int(datetime[8]+datetime[9]+datetime[11]+datetime[12]))<900 and int(datetime[8])==0):
                    #     out='否'
                    # else:
                    #     out='是'
                    # # 日期双数
                    # if ((int(datetime[9] + datetime[10] + datetime[12] + datetime[13])) < 900 and int(datetime[9]) == 0):
                    #     out = '否'
                    # else:
                    #     out = '是'
