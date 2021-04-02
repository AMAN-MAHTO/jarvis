import speech_recognition as sr
def listning():
    print('listning')
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        print('recog')
        try:
            return r.recognize_google(audio)
        except:
            return "didn't recognized"
