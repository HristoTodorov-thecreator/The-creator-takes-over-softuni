import speech_recognition as sr


recoginzer = sr.Recognizer()

with sr.Microphone() as source:
    print('starting...')

    audio = recoginzer.listen(source)


try:
    text = recoginzer.recognize_google(audio,language='bg-BG') #'en-US'
    print(text)

except sr.UnknownValueError:
    print(f'Try again your voice was not recognized')