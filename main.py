import tkinter as tk
from speech import speechRecongnition
from translate import toHindi
c=0
i=1



englishText=""
TranslatedText=""
def readFromSpeech():
    # label1.config(text="speak in microphone")
    global i
    i+=1
    print("button clicked...")
    global englishText
    englishText=speechRecongnition()
    label1.config(text=englishText)

def TranslateText():
    global englishText
    global TranslatedText
    TranslatedText=toHindi(englishText)
    label2.config(text=TranslatedText.text)
    label3.config(text=TranslatedText.pronunciation)

root = tk.Tk()
label_width=500
label1 = tk.Label(root, text="", width=label_width)
root.title("Basic Window")
button1 = tk.Button(root, text="Microphone", command=readFromSpeech)
button1.pack(pady=20)
label1.pack()
button2 = tk.Button(root, text="Translate", command=TranslateText)
button2.pack(pady=20)
label2 = tk.Label(root, text="", width=label_width)
label2.pack()
label3 = tk.Label(root, text="", width=label_width)
label3.pack()
root.geometry("400x300")
root.mainloop()