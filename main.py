import tkinter as tk
from speech import speechRecongnition,speakerText
from translate import convertTo

desLang_array={"hindi":"hi","english":"en","malyalam":"ml","tamil":"ta","telugu":"te","urdu":"ur","punjabi":"pa"}
srcLang_array={"english":"","hindi":"hi-IN","malyalam":"ml-IN","tamil":"ta-IN","telugu":"te-IN","urdu":"ur-PK","punjabi":"pa-IN"}

englishText=""
TranslatedText=""
def reset():
    global englishText,TranslatedText
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
    global englishText,desLang,srcLang          
    print(desLang.get())
    print(srcLang.get())
    try:
        englishText=speechRecongnition(srcLang_array[srcLang.get()])
    except Exception as e:
        text_speech.config(state=tk.NORMAL)
        text_speech.insert(tk.END, "some error occured... try again")
        text_speech.config(state=tk.DISABLED)
    else:
        text_speech.config(state=tk.NORMAL)
        text_speech.insert(tk.END, englishText)
        text_speech.config(state=tk.DISABLED)
    print(desLang.get())
    print(srcLang.get())
def TranslateText():

    global englishText  
    global TranslatedText
    TranslatedText=convertTo(englishText,desLang_array[srcLang.get()],desLang_array[desLang.get()])

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
    if(TranslatedText.pronunciation != None):
        text_pronun.insert(tk.END, TranslatedText.pronunciation)
    else:
        text_pronun.insert(tk.END, "No pronunciation...")
    text_pronun.config(state=tk.DISABLED)
def speakerFunc():
    speakerText(TranslatedText.text,desLang.get())
root = tk.Tk()
label_width=500

desLang=tk.StringVar()
desLang.set("hindi")
srcLang=tk.StringVar()
srcLang.set("english")

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
speakerButton=tk.Button(canvas,text="Speaker",command=speakerFunc)
speakerButton.pack(pady=20)
reset_button=tk.Button(canvas,text="Reset",command=reset)
reset_button.pack(pady=20)
root.mainloop()