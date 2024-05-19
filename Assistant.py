from pydoc import text
import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
from google_trans_new import google_translator


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print (voices)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    ''' this function will be used in the starting of the assistant. Its a kind of initialisation of the assistant 
    '''
    
    hour = int(datetime.datetime.now().hour)
   

    if hour>=0 and hour<12:
        speak("Good Morning boss, I am David , a bot designed by the Sir Ayush and team!! I can search for queries from wikipedia , tell you the current time and ofcourse run the most complex algorithm that is multilingual translator designed by my creator.!! How may I help you?")
    elif hour>=12 and hour<17:
        speak("Good afternoon boss, I am David , a bot designed by the Sir Ayush and team!! I can search for queries from wikipedia , tell you the current time and ofcourse run the most complex algorithm that is multilingual translator designed by my creator. !! How may I help you?")
    else:
        speak("Good evening boss, I am David , a bot designed by the Sir Ayush and team!! I can search for queries from wikipedia , tell you the current time and ofcourse run the most complex algorithm that is multilingual translator designed by my creator.!! How may I help you?")

def takeCommand():
    ''' this function mainly takes voice command '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Clearing the background noises...")
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)   

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        print("Sorry boss , I didn't understood...Can You say it again please? ")
        return "None"
    return query
    
def translate():
    speak("what do you want to translate?")
    r =sr.Recognizer()
    with sr.Microphone as source:
        audio1= m.listen()
        textDemo = audio1()
        langinput = input("Type the language code in which you want to translate: ")
        translator= google_translator()
        translated_text = translator.translate(str(textDemo), lang_tgt= str(langinput))
        print(translated_text.text)
        speak(translated_text.text)
    

if __name__== "__main__":
    
    wishme()
    #takeQuery()
    #translate()
   
# while True:
    try:
        
        
            query = takeCommand().lower()

            if "search" in query:
                speak("searching wikipedia, keep tighten your seatbelts...")
                query = query.replace("search", "")
                results = wikipedia.summary(query, sentences= 3)
                speak("according to wikipedia...")
                print(results)
                speak(results)

    
            elif "time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(strTime)   

            elif "open translator" in query:
                speak("ok sir , opening translator...")
                translate()

            elif "open google" in query:
                webbrowser.open("google.com")

            elif "open linkedin" in query:
                webbrowser.open("linkedin.com")

            elif "open youtube" in query:
                webbrowser.open("youtube.com")
            
            elif "design" or "made" or "programmed" in query:
                speak("Yes ofcourse ..it would be sort of excitement that i have to tell my programming . So I have been programmed by a series of algorithms and voice prompts. There are certain libraries and packages used while making me which i can't say as i want to remain 1 step ahead of the others! ")

            
            
            
            

    except KeyboardInterrupt:
        speak("Its been a nice time talking with you ... hope you enjoyed... meet you next time.")
        print('interrupted!')   ## after this exit the loop by pressing ctrl+C
