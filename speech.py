import speech_recognition as sr
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

