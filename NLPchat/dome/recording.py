#!/usr/bin/python
# encoding:utf-8
# @lance


import pyaudio  # 这个需要自己下载轮子
import wave
# 初始化语音
from aip import AipSpeech
import speech_recognition as sr
import win32com.client


in_path = "./voices/myvoices.wav"  # 存放录音的路径


# ./voices/myvoices.wav
def get_audio(filepath):
    # aa = str(input("是否开始录音？   （y/n）"))
    # if aa == str("y") :
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # 声道数
    RATE = 16000  # 采样率

    RECORD_SECONDS = 5  # 录音时间
    WAVE_OUTPUT_FILENAME = filepath
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("*" * 5, "开始录音：请在5秒内输入语音", "*" * 5)
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("*" * 5, "录音结束", "*" * 5)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

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
    get_audio(in_path)
    listen()


