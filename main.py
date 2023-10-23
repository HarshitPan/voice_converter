import tkinter as tk
from speech import speechRecongnition
from translate import toHindi

desLang_array={"hindi":"hi","english":"en","malyalam":"ml"}
srcLang_array={"english":"","hindi":"hi-IN","malyalam":"ml"}

englishText=""
desLang="hi"
srcLang=""
TranslatedText=""
def reset():
    global englishText,desLang,srcLang,TranslatedText
    englishText=srcLang=TranslatedText=""
    desLang="hi"
    text_speech.config(state=tk.NORMAL)
    text_speech.delete(1.0, tk.END)
    text_speech.config(state=tk.DISABLED)
    text_trans.config(state=tk.NORMAL)
    text_trans.delete(1.0, tk.END)
    text_trans.config(state=tk.DISABLED)
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

    text_trans.config(state=tk.NORMAL)
    text_trans.insert(tk.END, TranslatedText.text)
    text_trans.config(state=tk.DISABLED)

    text_pronun.config(state=tk.NORMAL)
    text_pronun.insert(tk.END, TranslatedText.pronunciation)
    text_pronun.config(state=tk.DISABLED)

root = tk.Tk()
label_width=500
root.title("Basic Window")
button1 = tk.Button(root, text="Microphone", command=readFromSpeech)
button1.pack(pady=20)
text_speech = tk.Text(root,height=5, width=100, wrap=tk.WORD,state=tk.DISABLED)
text_speech.pack(expand=True, fill='both', padx=10, pady=10)
button2 = tk.Button(root, text="Translate", command=TranslateText)
button2.pack(pady=20)
text_trans = tk.Text(root,height=5, width=100, wrap=tk.WORD,state=tk.DISABLED)
text_trans.pack(expand=True, fill='both', padx=10, pady=10)
text_pronun = tk.Text(root,height=5, width=100, wrap=tk.WORD,state=tk.DISABLED)
text_pronun.pack(expand=True, fill='both', padx=10, pady=10)
root.geometry("400x300")
root.mainloop()