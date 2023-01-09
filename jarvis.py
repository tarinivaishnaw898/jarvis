import speech_recognition as SR
import pyttsx3
listener=SR.Recognizer()
engine=pyttsx3.init()
## to change the voice of the alexa
## voices=engine.getProperty('voices')
##engine.setProperty('voice',voices[1].id)
def say(text):
    
    engine.say(text)
    engine.runAndWait()

    
def take_command():  
    try:
        with SR.Microphone() as source:
            print("listening.....")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
     #   command=command.lower()
    #if 'alexa' in command:
        print(command)
        
except:
    pass
return command