from Color import bcolors
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

freq = 44100
duration = 5

print(bcolors.OKBLUE + "Speak anything " + bcolors.ENDC)
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

sd.wait()
write("recording0.wav", freq, recording)
wv.write("recording1.wav", recording, freq, sampwidth=2)


import speech_recognition as sr

filename = "recording1.wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(bcolors.OKGREEN + bcolors.BOLD + 'You said: {}'.format(text) + bcolors.ENDC)
