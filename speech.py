import speech_recognition as sr
import pyttsx3
def speechRecongnition(ln):
    speech=sr.Recognizer()
    try:
        with sr.Microphone() as mic:
            print("here");
            speech.adjust_for_ambient_noise(mic,duration=5)
            audio = speech.listen(mic)
            text = speech.recognize_google(audio,language=ln)
            text = text.lower()
            print(f"Recongnized {text}")
            return text
    except sr.UnknownValueError():
        speech=sr.Recognizer()
        return "error"
    except TypeError:
        return "error"
def speakerText(text,ln):
    speaker=pyttsx3.init()
    speaker.setProperty('rate',150)
    voice=speaker.getProperty('voices')
    # for i in voice:
    #     if i.gender==None:
    #         print(i)
    speaker.setProperty('voice',ln)
    speaker.say(text)
    speaker.runAndWait()
#testing 
#speakerText("hello this is harshit and i just want to enter","hindi")
