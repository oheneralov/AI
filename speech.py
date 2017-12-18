#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
from gtts import gTTS
from nltk.chat.util import Chat, reflections
import win32com.client as wincl

pairs = [
    [
        r"My name is (.*)",
        ['hello %1', '%1 mabuhay ka'],
    ],
	[
        r"What is your name(.*)",
        ['My name is Olha', 'Olha'],
    ], 
	[
        r"George|Steven|Brian|Anthony|Kevin|Alex|Bob|Clark|David|Edward|James|John|Robert|Michael|William|Richard|Charles|Joseph|Thomas|Christopher|Daniel|Paul|Mark|Donald",
        ['hello', 'Hi'],
    ], 
	[
        r"Who are you?(.*)",
        ['I am Robot35908', 'Robot35908'],
    ],
    [
        r'hello|hi|Good morning|Good afternoon|Good evening|Good night',
        ['hello', 'kamusta', 'mabuhay', 'hi', "%1"],
    ],
	[
        r'(.*)How do you do?(.*)',
        ['Pleased to meet you', 'hello', 'kamusta', 'mabuhay', 'hi', "%1"],
    ],
	[
        r'(.*)How are you?(.*)',
        ['I am fine thanks. And you?'],
    ],
	[
        r'(.*)fine|well|nice|cool|good(.*)',
        ['So any other questtion s?', 'Would you like to ask me something else?'],
    ],
	[
        r'(.*)Really?(.*)',
        ['Yes'],
    ],
    [
        r'(.*) (hungry|sleepy|groot)',
        [
            "%1 %2"
        ]
    ],
    [
        r'(.*)(mahal|love)(.*)',
        [
            "https://goo.gl/ndTZVq",
            "I always thought Love was a static class until you made an instance of it.",
            "I love user interfaces it's because that's where U and I are always together.",
        ],
    ],
    [
        r'(.*)(relationship)(.*)',
        [
            "Mabuti pa sa database may relationship. Eh tayo, wala.",
        ],
    ],
    [
        r'(meron|mayron|ano|does|is there|what) (.*) (forever)(.*)',
        [
            "Loading...",
            "None",
            "while True: pass",
        ],
    ],
    [
        r'(.*)', # default response if no patterns from above is found
        [
            "I know nothing about %1",
            "Sorry I don't know what `%1` is?",
        ],
    ],
]

class Speech2Text():
    def getText(self):
        r = sr.Recognizer()
        with sr.Microphone(device_index = 0) as source:
            audio = r.record(source, duration = 5)
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
	
        with sr.AudioFile("microphone-results.wav") as source:
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I do not understand"
        except sr.RequestError as e:
            return "Sorry, something wrong with me"


class Olha(Chat):
    def start(self, quit, speech):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try: user_input = speech.getText()
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.": user_input = user_input[:-1]
                result = self.respond(user_input)
                print(result)
                speak.Speak(text = result)

def Olhabot():
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text='Hi, what is your name?', lang='en')
    
    speech = Speech2Text()
    chat = Olha(pairs, reflections)
    chat.start('quit', speech)

if __name__ == "__main__":
    Olhabot()

