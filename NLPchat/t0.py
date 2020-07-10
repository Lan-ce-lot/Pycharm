# 文字转音频程序and联合文字处理程序
# encoding:utf-8
# coding by Mufasa 2018.11.09

'''
功能说明：
1，文本标记功能整合进程序中；
2，联网的http API接口整合；
  1，网络检查；
  2，断网异常检测；
  3，网络传数据、接数据；
3，文本转语音的baidu-api接口整合
  1，语速，取值0-9，默认为5中语速；
  2，音调，取值0-9，默认为5中语调；
  3，音量，取值0-15，默认为5中音量；
  4，发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女；
4，音频保存自主设置；
'''

import os
import tkinter.filedialog
import shutil
import tkinter as tk
from aip import AipSpeech


def audio_out(string_, path, audio_set=None):
    # 百度云网络网络配置
    APP_ID = '14636839'
    API_KEY = 'u34cdKCsR61tzM0r20Qnp3YM'
    SECRET_KEY = 'Rehs5G02EqbrRDDgGdPY9NKY2ZlCX8Oq'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    if len(string_) > 500:
        num = int(len(string_) / 500)
        # 第一段音频
        result = client.synthesis(string_[0:500], 'zh', 1,
                                  {'spd': audio_set[0], 'pit': audio_set[1], 'vol': audio_set[2], 'per': audio_set[3]})
        open(path, 'wb').write(result)
        # 中间段落的音频
        for i in range(1, num):
            result = client.synthesis(string_[i * 500:(i + 1) * 500], 'zh', 1,
                                      {'spd': audio_set[0], 'pit': audio_set[1], 'vol': audio_set[2],
                                       'per': audio_set[3]})
            open(path, 'ab').write(result)
        # 最后一段音频
        result = client.synthesis(string_[num * 500:], 'zh', 1,
                                  {'spd': audio_set[0], 'pit': audio_set[1], 'vol': audio_set[2], 'per': audio_set[3]})
        open(path, 'ab').write(result)
    else:
        result = client.synthesis(string_, 'zh', 1,
                                  {'spd': audio_set[0], 'pit': audio_set[1], 'vol': audio_set[2], 'per': audio_set[3]})
        open(path, 'wb').write(result)


def isConnected():
    import requests
    try:
        html = requests.get("http://www.baidu.com", timeout=2)
    except:
        return False
    return True


def out_comma(data, num_1, num_2):
    txt = ''
    if isinstance(data, (list)):  # 有不止一段
        for i in data:
            for n in range(num_1):
                txt = txt + i
        for n in range(num_2):
            for i in data:
                txt = txt + i
    else:  # 如果不是数组，即只有一个字符串
        for n in range(num_2):
            txt = txt + data
    return txt


def code_a(path, data, set, audio_set):
    txt_mid = data.split('...')
    for i in range(len(txt_mid)):
        txt_mid[i] = txt_mid[i].split(',,,')
    # 上面是对文本进行切片，下面进行相关处理
    txt = ''
    for i in txt_mid:
        txt = txt + out_comma(i, set[0], set[1])
    for i in range(set[2]):
        for j in txt_mid:
            for k in j:
                txt = txt + k
    # import pyperclip
    # pyperclip.copy(txt)
    if path == '':
        import pyperclip
        pyperclip.copy(txt)
    else:
        fobj = open(path + '.txt', 'w')
        fobj.write(txt)
        fobj.close()
        # 音频生成，需要额外读取audio_set数据

        audio_out(txt, path + '.mp3', audio_set)


def code_b(path, data, set, audio_set):
    txt_mid = data.split('...')
    for i in range(len(txt_mid)):
        txt_mid[i] = txt_mid[i].split(',,,')
    txt_last = []
    for i in txt_mid:
        for j in i:
            txt_last.append(j)
    # print(txt_last)
    # for i in txt_last:
    # print(i)
    # print('文本输出完毕')#这里是有。标点的
    txt_mark = []
    txt_midd = data[:2]
    for i in data[2:]:
        txt_midd = txt_midd + i
        if txt_midd == ',,,':
            txt_mark.append(0)
        elif txt_midd == '...':
            txt_mark.append(1)
        txt_midd = txt_midd[1:]
    # print(len(txt_last))#98
    # print(len(txt_mark))#97
    txt = ''
    for circle in range(set[2]):
        for i in range(len(txt_mark)):
            if txt_mark[i] == 0:
                for j in range(set[0]):
                    txt += txt_last[i]

            elif txt_mark[i] == 1:
                for j in range(set[1]):
                    txt += txt_last[i]

    if path == '':
        import pyperclip
        pyperclip.copy(txt)
    else:
        fobj = open(path + '.txt', 'w')
        fobj.write(txt)
        fobj.close()
        # 音频生成，需要额外读取audio_set数据
        audio_out(txt, path + '.mp3', audio_set)


class assist():
    def write_txt_data(data, path):
        ls = os.linesep
        # data 为数组类型
        fobj = open(path, 'w')
        fobj.writelines(['%s%s' % (x, ls) for x in data])
        fobj.close()

    def read_txt_data(path):
        fobj = open(path, 'r')
        string = []
        for eachline in fobj:
            if eachline[:-1] != '':
                string.append(eachline[:-1])
        fobj.close()
        return string


class out_setconfig(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('参数设置')  # 弹窗界面
        self.data_set_path = os.path.dirname(os.path.realpath(__file__)) + "\\data_set.txt"
        isExists = os.path.exists(self.data_set_path)
        if isExists == False:  # bug,之前没有设置
            self.setup_eror()
        else:
            self.setup_UI()

    def setup_eror(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='程序第一次运行！\n\n已进行参数初始化操作\n').pack(side=tk.LEFT)
        row4 = tk.Frame(self)
        row4.pack(fill="x")
        assist.write_txt_data(['1', '2', '2', '2', '1', '3', '1', '2', '5', '5', '5', '0'], self.data_set_path)

        tk.Button(row4, text="关闭窗口", command=self.cancel).pack(side=tk.RIGHT)

    def setup_UI(self):

        self.A1 = tk.StringVar()
        self.A2 = tk.StringVar()
        self.A3 = tk.StringVar()
        self.A0 = tk.IntVar()

        self.B1 = tk.StringVar()
        self.B2 = tk.StringVar()
        self.B3 = tk.StringVar()
        self.B0 = tk.IntVar()

        self.C0 = tk.StringVar()
        self.C1 = tk.StringVar()
        self.C2 = tk.StringVar()
        self.C3 = tk.StringVar()

        data = assist.read_txt_data(self.data_set_path)
        self.A1.set(data[1])
        self.A2.set(data[2])
        self.A3.set(data[3])
        d = int(data[0])
        self.A0.set(d)

        self.B1.set(data[5])
        self.B2.set(data[6])
        self.B3.set(data[7])
        d = int(data[4])
        self.B0.set(d)

        self.C0.set(data[8])
        self.C1.set(data[9])
        self.C2.set(data[10])
        self.C3.set(data[11])

        row1 = tk.Frame(self)
        row1.pack(fill="x")

        tk.Label(row1, text='程序A', width=30).grid(row=0, column=0, columnspan=2)
        tk.Label(row1, text='逗号次数：', width=15).grid(row=1, column=0)
        tk.Label(row1, text='句号次数：', width=15).grid(row=2, column=0)
        tk.Label(row1, text='全部文本次数', width=15).grid(row=3, column=0)
        tk.Label(row1, text='是否生成文本', width=15).grid(row=4, column=0)

        tk.Entry(row1, textvariable=self.A1, width=13).grid(row=1, column=1)
        tk.Entry(row1, textvariable=self.A2, width=13).grid(row=2, column=1)
        tk.Entry(row1, textvariable=self.A3, width=13).grid(row=3, column=1)
        checkA = tk.Checkbutton(row1, text="播放", variable=self.A0)
        checkA.select()
        checkA.grid(column=1, row=4, sticky=tk.W)

        tk.Label(row1, text='程序B', width=30).grid(row=0, column=2, columnspan=2)
        tk.Label(row1, text='逗号次数：', width=15).grid(row=1, column=2)
        tk.Label(row1, text='句号次数：', width=15).grid(row=2, column=2)
        tk.Label(row1, text='全部文本次数', width=15).grid(row=3, column=2)
        tk.Label(row1, text='是否生成文本', width=15).grid(row=4, column=2)

        tk.Entry(row1, textvariable=self.B1, width=13).grid(row=1, column=3)
        tk.Entry(row1, textvariable=self.B2, width=13).grid(row=2, column=3)
        tk.Entry(row1, textvariable=self.B3, width=13).grid(row=3, column=3)
        checkB = tk.Checkbutton(row1, text="播放", variable=self.B0)
        checkB.select()
        checkB.grid(column=3, row=4, sticky=tk.W)

        self.A0.set(int(data[0]))
        self.B0.set(int(data[4]))

        # 这个是音频合成设置界面的
        tk.Label(row1, text='音频合成参数设置', width=30).grid(row=0, column=4, columnspan=2)
        tk.Label(row1, text='语速：', width=15).grid(row=1, column=4)
        tk.Label(row1, text='音调：', width=15).grid(row=2, column=4)
        tk.Label(row1, text='音量', width=15).grid(row=3, column=4)
        tk.Label(row1, text='发音人', width=15).grid(row=4, column=4)

        tk.Entry(row1, textvariable=self.C0, width=13).grid(row=1, column=5)
        tk.Entry(row1, textvariable=self.C1, width=13).grid(row=2, column=5)
        tk.Entry(row1, textvariable=self.C2, width=13).grid(row=3, column=5)
        tk.Entry(row1, textvariable=self.C3, width=13).grid(row=4, column=5)

        tk.Button(row1, text="取消", command=self.cancel, width=13).grid(row=9, column=0)
        tk.Button(row1, text="确定", command=self.ok, width=13).grid(row=9, column=4)
        tk.Button(row1, text="重置", command=self.reset, width=13).grid(row=9, column=5)

    def ok(self):
        self.userinfo_A = [self.A0.get(), self.A1.get(), self.A2.get(), self.A3.get()]  # 设置数据
        self.userinfo_B = [self.B0.get(), self.B1.get(), self.B2.get(), self.B3.get()]  # 设置数据
        self.userinfo_C = [self.C0.get(), self.C1.get(), self.C2.get(), self.C3.get()]

        self.userinfo_A[0] = str(self.userinfo_A[0])
        self.userinfo_B[3] = str(self.userinfo_B[3])

        data = self.userinfo_A + self.userinfo_B + self.userinfo_C
        # print(data)
        assist.write_txt_data(data, os.path.dirname(os.path.realpath(__file__)) + "\\data_set.txt")
        self.destroy()  # 销毁窗口

    def cancel(self):
        self.userinfo = None  # 空！
        self.destroy()

    def reset(self):
        assist.write_txt_data(['1', '2', '2', '2', '1', '3', '1', '2', '5', '5', '5', '0'], self.data_set_path)
        self.destroy()


################################
class main_code(tk.Tk):
    def __init__(self):
        super().__init__()
        self.audio_path = ""
        self.run = True
        self.vartext = tk.StringVar()

        self.txt = ''
        networkisok = isConnected()
        if networkisok:
            self.mark_text = '网络连接正常！\n欢迎使用！'
        else:
            self.mark_text = '无网络连接！\n请确认网络连接是否完好\n无法连接百度云服务器'

        self.insert_text = ''
        self.vartext.set(self.mark_text)
        self.audio_path = ""
        self.title('音频标记')
        self.setupUI()

    def setupUI(self):

        row4 = tk.Frame(self)
        row4.pack(fill="x")

        tk.Button(row4, text='导入文本', width=27, command=self.select).grid(row=0, column=0)
        tk.Button(row4, text='设置文本', width=27, command=self.setup_config).grid(row=0, column=1)
        tk.Button(row4, text='生成文本', width=27, command=lambda: self.lay(entry1.get())).grid(row=0, column=2)

        label = tk.Label(row4, height=3, textvariable=self.vartext, bg='white', font=('黑体', 10), anchor='w').grid(row=1,
                                                                                                                  column=0,
                                                                                                                  columnspan=3)

        entry1 = tk.Entry(row4, width=85)
        entry1.grid(row=2, column=0, columnspan=3)

    def select(self):  # 获取audio_path和audio_len
        self.audio_path = tk.filedialog.askopenfilename(initialdir='C:\\Users\\Administrator\\Desktop', filetypes=(
        ("txt or docx files", "*.txt;*.docx"), ("All files", "*.*")))
        if self.audio_path == "":
            self.vartext.set('未导入任何文件')
        else:
            p, f = os.path.split(self.audio_path)
            path = os.path.dirname(os.path.realpath(__file__)) + '\\data\\' + str(os.path.splitext(f)[0])
            # print(path)
            isExists = os.path.exists(path)
            if not isExists:  # 如果不存在这个目录
                os.makedirs(path)  # 创建一个新的路径
                shutil.copyfile(self.audio_path, path + '\\' + f)

            if str(os.path.splitext(f)[1]) == '.txt':
                file_object = open(self.audio_path, 'r', encoding='UTF-8')
                try:
                    file_context = file_object.read()
                finally:
                    file_object.close()
                self.txt = file_context
                self.vartext.set('已导入txt文本')
            # print(1)
            elif str(os.path.splitext(f)[1]) == '.docx':
                import docx
                document = docx.Document(self.audio_path)
                txt = ''
                for paragraph in document.paragraphs:
                    txt += paragraph.text
                self.txt = txt
                self.vartext.set('已导入docx文本')

            self.audio_path = path + '\\' + f  # 更新数据路径
            # print(self.audio_path)

    def lay(self, txt=''):
        mark_set = assist.read_txt_data(os.path.dirname(os.path.realpath(__file__)) + "\\data_set.txt")
        # print(mark_set)

        for i in range(len(mark_set)):
            mark_set[i] = int(mark_set[i])

        # mark_set=[1,1,0,1,0,0,1,4]
        if txt == '':
            if self.audio_path != '':
                p, f = os.path.split(self.audio_path)
                # print(p)
                if mark_set[0] == 1:
                    # code_a(p+'\\'+str(os.path.splitext(f)[0])+'_A'+'.txt',self.txt,mark_set[1:4])
                    code_a(p + '\\' + str(os.path.splitext(f)[0]) + '_A', self.txt, mark_set[1:4], mark_set[8:12])
                    # self.vartext.set('已生成文本标记文件A')
                if mark_set[4] == 1:
                    # code_b(p+'\\'+str(os.path.splitext(f)[0])+'_B'+'.txt',self.txt,mark_set[5:])
                    code_b(p + '\\' + str(os.path.splitext(f)[0]) + '_B', self.txt, mark_set[5:], mark_set[8:12])
                    # self.vartext.set('已生成文本标记文件B')
                if mark_set[0] == 1 and mark_set[4] == 1:
                    self.vartext.set('已生成文本标记文件A、B和相应的音频')
                elif mark_set[0] == 1 and mark_set[4] == 0:
                    self.vartext.set('已生成文本标记文件A和相应的音频')
                elif mark_set[0] == 0 and mark_set[4] == 1:
                    self.vartext.set('已生成文本标记文件B和相应的音频')
                elif mark_set[0] == 0 and mark_set[4] == 0:
                    self.vartext.set('设置中未确定生成何种文件\n请在设置文本中调整参数！')
            else:
                self.vartext.set('未导入任何文件')
        else:
            # print(txt)
            if mark_set[0] == 1:
                code_a('', txt, mark_set[1:4])
                self.vartext.set('已将A程序处理后的文字复制到剪切板\n直接粘贴即可\n如果想使用B程序处理请在设置中将程序A取消，并勾选程序B')
            elif mark_set[4] == 1:
                code_b('', txt, mark_set[5:])
                self.vartext.set('已将B程序处理后的文字复制到剪切板\n直接粘贴即可\n如果想使用A程序处理请在设置中将程序B取消，并勾选程序A')

    def setup_config(self):
        res = self.ask_userinfo()
        if res is None: return

    def ask_userinfo(self):
        inputDialog = out_setconfig()
        self.wait_window(inputDialog)  # 这一句很重要！！！


if __name__ == '__main__':
    app = main_code()
    app.mainloop()