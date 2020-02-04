import speech_recognition as sr
from Color import bcolors
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything: ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(bcolors.OKGREEN + bcolors.BOLD + 'You said: {}'.format(text) + bcolors.ENDC)
    except:
        print("Sorry could not recognize your input voice")