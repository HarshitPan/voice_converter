import speech_recognition as sr
import os
def speechRecongnition():
    speech=sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            print("here");
            speech.adjust_for_ambient_noise(mic,duration=1)
            audio = speech.listen(mic)
            text = speech.recognize_google(audio)
            text = text.lower()
            os.system("clear")
            print(f"Recongnized {text}")
            return text
    except sr.UnknownValueError():
        speech=sr.Recognizer()
        return "error"
    except TypeError:
        return "error"
