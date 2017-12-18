#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone(device_index = 0) as source:
    audio = r.record(source, duration = 10)
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())
	
r = sr.Recognizer()
with sr.AudioFile("microphone-results.wav") as source:
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
