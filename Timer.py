import pyttsx3
engine = pyttsx3.init()
import time
timer=float(input("After how much time do you want to get alerted(in minutes)? "))
timerinsecs=timer*60
time.sleep(timerinsecs)
prompt="Time over!"
print(prompt)
engine.say(prompt)
engine.runAndWait()
