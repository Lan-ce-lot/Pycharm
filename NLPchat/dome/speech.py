#!/usr/bin/python
# encoding:utf-8
# @lance




import speech_recognition as sr
r = sr.Recognizer()    #调用识别器
test = sr.AudioFile("F:\\work\\git-base\\piano\\MyPiano\\NLPchat\\dome\\voices\\myvoices.wav")   #导入语音文件
with test as source:
    audio = r.record(source)
type(audio)
c=r.recognize_sphinx(audio, language='zh-cn')     #识别输出
print(c)

# if __name__ =="__main__":
#     speech_to_text("./voices/myvoices.wav")
