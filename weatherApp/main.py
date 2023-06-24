import requests
import json
import win32com.client as wincom
print("Welcome to WeatherApp 1.0 by Aston")
city = input("Enter City: ")
url = f"http://api.weatherapi.com/v1/current.json?key=c1366dfe2c2647df956145946232306&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak(temp)

