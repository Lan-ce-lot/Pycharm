#!/usr/bin/python
# encoding:utf-8
# @lance


import pyaudio # 这个需要自己下载轮子
import wave
in_path = "./audios/input.wav" # 存放录音的路径

def get_audio(filepath):
    aa = str(input("是否开始录音？   （y/n）"))
    if aa == str("y") :
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1                # 声道数
        RATE = 11025                # 采样率
        RECORD_SECONDS = 5          # 录音时间
        WAVE_OUTPUT_FILENAME = filepath
        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("*"*5, "开始录音：请在5秒内输入语音", "*"*5)
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("*"*5, "录音结束\n")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
    elif aa == str("否"):
        exit()
    else:
        print("语音录入失败，请重新开始")
        get_audio(in_path)

if __name__ == '__main__':
    get_audio("./audios/input.wav")