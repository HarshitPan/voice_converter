from googletrans import Translator
translate=Translator()

def toHindi(text):
    global translate
    return translate.translate(text,dest="hi")