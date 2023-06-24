import win32com.client as wincom
print("Welcome to WinTTS 1.0 by Aston")
while True:
    speak = wincom.Dispatch("SAPI.SpVoice")
    text = input("What do you want to say: ")
    speak.Speak (text)