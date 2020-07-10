#!/usr/bin/python
# encoding:utf-8
# @lance
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re
import pyttsx3 as pyttsx
import newtuling
import recording
import qtawesome
import threading
import idiom
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout
from win32com.client import Dispatch

td = newtuling.TuringDome(json_path=newtuling.json_path, api_url=newtuling.api_url)

class MainUi(QtWidgets.QMainWindow):
    flag = 0
    sound_flag = 0 # 语音，默认开启
    keyWord = ['黄昌盛', '文字模式', '语音模式', '成语接龙', '讲个笑话', '帮助']

    def __init__(self):
        super().__init__()
        self.setWindowTitle('HCS的机器人')
        self.init_ui()

    def inputBord(self, str):
        self.right_bar_widget.setText(str)

    def r_setBord(self, str):
        self.right_recommend_widget.setText(self.right_recommend_widget.toPlainText() + '机器人：' + str + '\n')

    def p_setBord(self, str):
        self.right_recommend_widget.setText(self.right_recommend_widget.toPlainText() + '我    ：' + str + '\n')

    def slot_max_or_recv(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def cbutton_1(self):
        self.inputBord('文字模式')
        self.submited()
        str = self.right_bar_widget.toPlainText()

    def cbutton_2(self):
        self.inputBord('语音模式')
        self.submited()
        str = self.right_bar_widget.toPlainText()

    def cbutton_3(self):
        self.inputBord('成语接龙')
        self.submited()
        str = self.right_bar_widget.toPlainText()
        # self.idiom_start(start=1, mode=2, opt=1)

    def cbutton_4(self):
        self.inputBord('讲个笑话')
        self.submited()
        str = self.right_bar_widget.toPlainText()


    def cbutton_5(self):
        self.inputBord('使用帮助')
        self.submited()
        str = self.right_bar_widget.toPlainText()

    def res(self, str):
        ans = ''
        return ans

    def reply(self, str):

        if re.match('.*帮助.*?', str, flags=0):
            str = '''欢迎使用HCS智能机器人！
        我可以聊天
        输入关键字解锁新功能
        '文字模式', '语音模式', '成语接龙', '讲个笑话', '帮助', '退出'  '''
        elif str == '文字模式':
            self.sound_flag = 1
            str = '开启文字模式'
        elif str == '语音模式':
            self.sound_flag = 0
            str = '开启语音模式'

        elif str == '讲个笑话':
            pass
        # elif str == '成语接龙':
        #     pass
        elif re.match('.*退出.*?', str, flags=0):
            str = '再见'
            self.r_setBord(str)
            thread1 = threading.Thread(target=self.read, args=(str,))
            thread1.start()
            thread1.join()
            self.close()
            exit()
        else:
            str = td.talkToTheTuring(str)
        self.r_setBord(str)
        thread1 = threading.Thread(target=self.read, args=(str,))
        thread1.start()

    def read(self, str):
        if self.sound_flag == 0:
            en = pyttsx.init()
            en.say(str)
            rate = en.getProperty('rate')
            en.setProperty('rate', rate + 150)
            en.runAndWait()

    def submited(self):
        self.p_setBord(self.right_bar_widget.toPlainText())
        str = self.right_bar_widget.toPlainText()
        self.right_bar_widget.clear()

        self.reply(str)

    def clc(self):
        self.right_recommend_widget.clear()
        self.right_bar_widget.clear()

    def listening(self):
        recording.get_audio("./voices/myvoices.wav")
        self.inputBord(recording.listen())
        self.submited()

    # 回车
    def keyPressEvent(self, event):
        # 这里event.key（）显示的是按键的编码
        if str(event.key()) == '16777220':  # 回车
            print("按下回车")
            self.submited()

    # ==============================================================================

    def init_ui(self):
        self.setFixedSize(728, 450)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        # ===========================================================================

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_close.clicked.connect(self.close)
        # self.left_visit.clicked.connect(self.slot_max_or_recv)
        self.left_mini.clicked.connect(self.showMinimized)

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "文字模式")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "语音模式")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), "成语接龙")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "讲个笑话")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), "使用帮助")
        self.left_button_5.setObjectName('left_button')
        self.left_button_1.clicked.connect(self.cbutton_1)
        self.left_button_2.clicked.connect(self.cbutton_2)
        self.left_button_3.clicked.connect(self.cbutton_3)
        self.left_button_4.clicked.connect(self.cbutton_4)
        self.left_button_5.clicked.connect(self.cbutton_5)
        # self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "我的收藏")
        # self.left_button_6.setObjectName('left_button')

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        # self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        # self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        # ============================================================


        self.right_recommend_widget = QtWidgets.QTextBrowser()  # 推荐封面部件
        self.right_recommend_widget.setFixedSize(605, 250)
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)


        # self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 1, 0, 1, 9)

        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + ' HCS的智能机器人')
        self.search_icon.setFont(qtawesome.font('fa', 16))

        self.right_layout.addWidget(self.search_icon, 0, 0, 1, 2)
        # ============================================================

        self.right_bar_widget = QtWidgets.QTextEdit()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)

        self.right_layout.addWidget(self.right_bar_widget, 2, 0, 1, 9)

        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.submit = QtWidgets.QPushButton(qtawesome.icon('fa.bug', color='white'), "发送")  # 提交
        self.submit.setObjectName('left_button')
        self.submit.clicked.connect(self.submited)

        self.right_layout.addWidget(self.submit, 3, 8, 1, 1)

        self.clearbutton = QtWidgets.QPushButton(qtawesome.icon('fa.magic', color='white'), "清空")  # 清空
        self.clearbutton.setObjectName('left_button')
        self.clearbutton.clicked.connect(self.clc)

        self.right_layout.addWidget(self.clearbutton, 3, 0, 1, 1)


        self.recbutton = QtWidgets.QPushButton(qtawesome.icon('fa.magic', color='white'), "录音")  # 录音
        self.recbutton.setObjectName('left_button')
        self.recbutton.clicked.connect(self.listening)

        self.right_layout.addWidget(self.recbutton, 3, 4, 1, 1)
        # =======================================================

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}

            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')
        self.right_widget.setStyleSheet('''
                    QWidget#right_widget{
                        color:#232C51;
                        background:white;
                        border-top:1px solid darkGray;
                        border-bottom:1px solid darkGray;
                        border-right:1px solid darkGray;
                        border-top-right-radius:10px;
                        border-bottom-right-radius:10px;
                    }
                    QLabel#right_lable{
                        border:none;
                        font-size:16px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                ''')
        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_layout.setSpacing(0)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    os.system("pause")