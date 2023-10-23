from googletrans import Translator
translate=Translator()

def convertTo(text,s,d):
    global translate
    return translate.translate(text,dest=d,src=s)