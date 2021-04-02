import time
t= time.time()
import pyttsx3
import os
import sys

current_path=os.path.dirname(sys.argv[0].replace('/','\\'))
# os.system("cd 'C:\\Users\\ashok mahato\\Desktop\\programing\\files\\Python_learning\\jarvis\\'")

from jarvis_speech import listning
engine= pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def say(audio):
    engine.say(audio)
    engine.runAndWait()
print(time.time()-t)

if __name__=='__main__':
    n=0
    while n<3:
        quary=listning().lower()
        quary.replace('jarvis','')
        if 'open youtube' in quary:
            # if 
            os.system(f'pythonw .\\multi_task_test.py {}')
            print(time.time()-t)
        elif 'play' in quary:
            quary.replace('play','')
            os.system(f'pythonw "C:\\Users\\ashok mahato\\Desktop\\programing\\files\\Python_learning\\jarvis\\jarvis_play.py" {quary}')
        
        n+=1
