
# Python Project 2 : Weather App


print("------- Weather APP 1.1------- ..... Created by Rohit Pawale\n")

import pyttsx3
import requests
import json


engine = pyttsx3.init()

city = input("Enter name of the city : \n")

# xml format
# url = f"http://api.weatherapi.com/v1/current.xml?key=0f9c81af3c4847ccb75114838250406&q={city}"

# json form
url = f"http://api.weatherapi.com/v1/current.json?key=0f9c81af3c4847ccb75114838250406&q={city}"


r = requests.get(url)

# print(r.text)
# print(type(r.text))

wdic = json.loads(r.text)


# Temperature in celcius
temp = wdic["current"]["temp_c"]

y = f"Current Temperature in {city} is {temp} Celcius"
print(y)
engine.say(y)
engine.runAndWait()


# fahrenheit
temp1 = wdic["current"]["temp_f"]

y1 = f"Current Temperature in {city} is {temp1} fahrenheit"
print(y1)
engine.say(y1)
engine.runAndWait()


# Condition
c = wdic["current"]["condition"]["text"]

y2= f"Current Cindition in {city} is {c}"
print(y2)
engine.say(y2)
engine.runAndWait()







