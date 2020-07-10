#!/usr/bin/python
# encoding:utf-8
# @lance

# 初始化语音
from aip import AipSpeech
import speech_recognition as sr
import win32com.client

# 1、语音生成音频文件,录音并以当前时间戳保存到voices文件中
# Use SpeechRecognition to record 使用语音识别录制
def my_record(rate=16000):

    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio = r.listen(source)

    with open("voices/myvoices.wav", "wb") as f:
        f.write(audio.get_wav_data())


# 2、音频文件转文字：采用百度的语音识别python-SDK
# 导入我们需要的模块名，然后将音频文件发送给出去，返回文字。
# 百度语音识别API配置参数



# 将语音转文本STT
def listen():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    APP_ID = '14636839'
    API_KEY = 'u34cdKCsR61tzM0r20Qnp3YM'
    SECRET_KEY = 'Rehs5G02EqbrRDDgGdPY9NKY2ZlCX8Oq'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    path = 'voices/myvoices.wav'
    # 读取录音文件
    with open(path, 'rb') as fp:
        voices = fp.read()
    try:
        # 参数dev_pid：1536普通话(支持简单的英文识别)、1537普通话(纯中文识别)、1737英语、1637粤语、1837四川话、1936普通话远场
        result = client.asr(voices, 'wav', 16000, {'dev_pid': 1537, })
        result_text = result["result"][0]
        print("you said: " + result_text)
        return result_text
    except KeyError:
        print("KeyError")
        speaker.Speak("我没有听清楚，请再说一遍...")

if __name__ == "__main__":
    my_record()
    listen()
    print(111)