import speech_recognition as sr
speech=sr.Recognizer()
i=0
while i<20:
    try:
       with sr.Microphone() as mic:
           print("here");
           speech.adjust_for_ambient_noise(mic,duration=0.2)
           audio = speech.listen(mic)
           text = speech.recognize_google(audio)
           text = text.lower()
           print(f"Recongnized {text}")
    except sr.UnknownValueError():
        speech=sr.Recognizer()
        continue
    except:
        print("error")
        break
    i+=1
