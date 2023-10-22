from googletrans import Translator
translate=Translator()

def toHindi(text):
    global translate
    return translate.translate(text,dest="hi")

def toMalyalam(text):
    global translate
    return translate.translate(text,dest="ml")