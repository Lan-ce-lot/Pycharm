# import pyttsx3 as pyttsx
# en = pyttsx.init()
# en.say('好好学习')
# en.runAndWait()

# from win32com.client import Dispatch
# speaker = Dispatch('SAPI.SpVoice')
# speaker.Speak('好好学习')
# del speaker


from aip import AipSpeech

""" 你的 APPID AK SK """

# APP_ID = '20611530'
# API_KEY = '66adOyD9ADvQqx2bUnErIwVv'
# SECRET_KEY = 'gxyRQ7gTzBa0oQaMI067AqXM2OXRt4Xq'
# =============可以用的
APP_ID = '15422825'
API_KEY = 'DhXGtWHYMujMVZZGRI3a7rzb'
SECRET_KEY = 'PbyUvTL31fImGthOOIP5ZbbtEOGwGOoT'
# APP_ID = '20315758'
# API_KEY = 'pPMQbHo7ccNrGo7XvLjyupEi'
# SECRET_KEY = 'MfFOtlK8m9SFUIlrUpCRl7bZl65datG3'
# APP_ID = '14636839'
# API_KEY = 'u34cdKCsR61tzM0r20Qnp3YM'
# SECRET_KEY = 'Rehs5G02EqbrRDDgGdPY9NKY2ZlCX8Oq'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('你好吗', 'zh', 1, {
    'vol': 5,
    'apd': 3,
    'pit': 9,
    'per': 4 # 0, 1, 3, 4
})
print(result)

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
        print(f)
