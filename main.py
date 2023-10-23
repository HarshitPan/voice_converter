import tkinter as tk
from speech import speechRecongnition
from translate import convertTo

desLang_array={"hindi":"hi","english":"en","malyalam":"ml"}
srcLang_array={"english":"","hindi":"hi-IN","malyalam":"ml-IN"}

englishText=""
desLang="hindi"
srcLang="english"
TranslatedText=""
def reset():
    global englishText,desLang,srcLang,TranslatedText
    englishText=TranslatedText=""
    text_speech.config(state=tk.NORMAL)
    text_speech.delete(1.0, tk.END)
    text_speech.config(state=tk.DISABLED)
    text_trans.config(state=tk.NORMAL)
    text_trans.delete(1.0, tk.END)
    text_trans.config(state=tk.DISABLED)

    text_pronun.config(state=tk.NORMAL)
    text_pronun.delete(1.0, tk.END)
    text_pronun.config(state=tk.DISABLED)
def readFromSpeech():
    # label1.config(text="speak in microphone")
    print("button clicked...")
    reset()
    global englishText
    print(desLang)
    print(srcLang)
    englishText=speechRecongnition(srcLang_array[srcLang])
    print(desLang)
    print(srcLang)
    text_speech.config(state=tk.NORMAL)
    text_speech.insert(tk.END, englishText)
    text_speech.config(state=tk.DISABLED)

def TranslateText():

    global englishText  
    global TranslatedText
    TranslatedText=convertTo(englishText,desLang_array[srcLang],desLang_array[desLang])

    text_trans.config(state=tk.NORMAL)
    text_trans.delete(1.0, tk.END)
    text_trans.config(state=tk.DISABLED)

    text_pronun.config(state=tk.NORMAL)
    text_pronun.delete(1.0, tk.END)
    text_pronun.config(state=tk.DISABLED)

    text_trans.config(state=tk.NORMAL)
    text_trans.insert(tk.END, TranslatedText.text)
    text_trans.config(state=tk.DISABLED)

    text_pronun.config(state=tk.NORMAL)
    text_pronun.insert(tk.END, TranslatedText.pronunciation)
    text_pronun.config(state=tk.DISABLED)

root = tk.Tk()
label_width=500
root.title("Translator")
canvas=tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL,command=canvas.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

for i in srcLang_array:
    rbtn=tk.Radiobutton(canvas,text=i, variable=srcLang, value=i)
    rbtn.pack(anchor=tk.W)
button1 = tk.Button(canvas, text="Microphone", command=readFromSpeech)
button1.pack(pady=20)
text_speech = tk.Text(canvas,height=5, width=100, wrap=tk.WORD,state=tk.DISABLED)
text_speech.pack(expand=True, fill='both', padx=10, pady=10)
for i in desLang_array:
    rbtn=tk.Radiobutton(canvas,text=i, variable=desLang, value=i)
    rbtn.pack(anchor=tk.W)
button2 = tk.Button(canvas, text="Translate", command=TranslateText)
button2.pack(pady=20)
text_trans = tk.Text(canvas,height=5, width=100, wrap=tk.WORD,state=tk.DISABLED)
text_trans.pack(expand=True, fill='both', padx=10, pady=10)
text_pronun = tk.Text(canvas,height=5, width=100, wrap=tk.WORD,state=tk.DISABLED)
text_pronun.pack(expand=True, fill='both', padx=10, pady=10)
reset_button=tk.Button(canvas,text="Reset",command=reset)
reset_button.pack(pady=20)
root.mainloop()