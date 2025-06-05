
#  Python Project 1: Robo Speaker

# import os

# if __name__ == '__main__':
    
#     print("Welcome to Robo Speaker 1.1 ...... Created By Rohit")
#     while True:    
#         x= input("Enter what do you want me to speak: ")
#         if(x=='q'):
#             print("Bye Bye!!")
#             break

#         command = f' powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
#         os.system(command)




# Using an pyttsx3

import pyttsx3

engine = pyttsx3.init()

print("Welcome to Robo Speaker 2.1 ...... Created By Rohit")
while True:
    x = input("Enter what do you want me to speak (or 'q' to quit): ")
    if x.lower() == 'q':
        y = "Good by my Friend"
        engine.say(y)
        engine.runAndWait()
        print("Bye Bye !!")
        break
    engine.say(x)
    engine.runAndWait()
