

# text recognition
import playsound
import pyttsx3
import translators as ts
import goslate
from PIL import Image
import pytesseract
import cv2
im=Image.open("abc.jpg")
text=pytesseract.image_to_string(im,lang="eng")
print("From____________\n"+text)
engine = pyttsx3.init()

print(ts.google(text,from_language='fr',to_language='en'))
engine.say(ts.google(text,from_language='fr',to_language='en'))
engine.runAndWait()





























