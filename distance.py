# import googletrans
# import speech_recognition as sr
# import gtts
# import playsound
#
# recognizer = sr.Recognizer()
# translator = googletrans.Translator()
# input_lang = 'fr-FR'
# output_lang = 'en'
# try:
#     with sr.Microphone() as source:
#         print('Speak Now')
#         voice = recognizer.listen(source)
#         text = recognizer.recognize_google(voice, language=input_lang)
#         print(text)
# except:
#     pass
#
# translated = translator.translate(text, dest=output_lang)
# print(translated.text)
# converted_audio = gtts.gTTS(translated.text, lang=output_lang)
# converted_audio.save('romantic.mp3')
# playsound.playsound('romantic.mp3')
# import speech_recognition as sr
# import pyttsx3
# import translators as ts
#
# listener = sr.Recognizer()
# engine = pyttsx3.init()
#
# text = 'Bonjour mes amis'
# engine.say(text)
# # talk('To Whom you want to send email')
# engine.say(ts.google(text,from_language='fr',to_language='en'))
#
# engine.runAndWait()


# import speech_recognition as sr
#
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Speak Anything :")
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print("You said : {}".format(text))
#     except:
#         print("Sorry could not recognize what you said")

# import speech_recognition as sr
#
# # Record Audio
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
#
# # Speech recognition using Google Speech Recognition
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("You said: " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))


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



# text = "hello"

# gs = goslate.Goslate()
# translatedText = gs.translate(text, 'en')

# print(translatedText)


# print("TO\n"+text)

print(ts.google(text,from_language='fr',to_language='en'))
engine.say(ts.google(text,from_language='fr',to_language='en'))
engine.runAndWait()





























