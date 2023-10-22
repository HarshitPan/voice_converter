import tkinter as tk
from speech import speechRecongnition
from translate import toHindi

desLang_array={"hindi":"hi"}
srcLang_array=[["English",]]

englishText=""
desLang="hi"
srcLang=""
TranslatedText=""
def reset():
    global englishText,desLang,srcLang,TranslatedText
    englishText=srcLang=TranslatedText=""
    desLang="hi"
    text_speech.config(state=tk.NORMAL)
    text_speech.insert(tk.END, "")
    text_speech.config(state=tk.DISABLED)

def readFromSpeech():
    # label1.config(text="speak in microphone")
    print("button clicked...")
    reset()
    global englishText

    englishText=speechRecongnition(srcLang)
    text_speech.config(state=tk.NORMAL)
    text_speech.insert(tk.END, englishText)
    text_speech.config(state=tk.DISABLED)

def TranslateText():
    global englishText
    global TranslatedText
    TranslatedText=toHindi(englishText)
    label2.config(text=TranslatedText.text)
    label3.config(text=TranslatedText.pronunciation)

root = tk.Tk()
label_width=500
root.title("Basic Window")
button1 = tk.Button(root, text="Microphone", command=readFromSpeech)
button1.pack(pady=20)
text_speech = tk.Text(root,height=5, width=100, wrap=tk.WORD,state=tk.DISABLED)
text_speech.pack(expand=True, fill='both', padx=10, pady=10)
button2 = tk.Button(root, text="Translate", command=TranslateText)
button2.pack(pady=20)

label2 = tk.Label(root, text="", width=label_width)
label2.pack()
label3 = tk.Label(root, text="", width=label_width)
label3.pack()
root.geometry("400x300")
root.mainloop()