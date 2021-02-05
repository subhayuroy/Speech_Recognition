import speech_recognition as sr
from Color import bcolors

r = sr.Recognizer()
with sr.Microphone() as source:
    print(bcolors.OKBLUE + "Speak anything: " + bcolors.ENDC)
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(bcolors.OKGREEN + bcolors.BOLD + 'You said: {}'.format(text) + bcolors.ENDC)
    except:
        print("Sorry could not recognize your input voice. Please retry")
        
        
        
##Another method

import speech_recognition as sr 
import pyttsx3  

r = sr.Recognizer()  
 
def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 

while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2) 
             
            audio2 = r.listen(source2) 
            
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
  
            print("Did you say: "+MyText) 
            SpeakText(MyText) 
              
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured")
