import pyttsx3


def set_property(voice=1, print_prop=False):
    global engine
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    if print_prop:
        print(voices[voice].id)
    engine.setProperty('voice', voices[voice].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
