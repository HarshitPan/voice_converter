import tkinter as tk
from speech import speechRecongnition
c=0
i=1


root = tk.Tk()
label_height=400
label_width=500
label = tk.Label(root, text="", height=label_height, width=label_width)
def button_click():
    label.config(text="speak in microphone")
    global c
    c=1
    global i
    i+=1
    print("button clicked...")

if(c==1):
    print("inside c")
    c=0
    englishText=speechRecongnition()
    label.config(text=englishText)

root.title("Basic Window")
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack(pady=20)
label.pack()
root.geometry("400x300")
root.mainloop()