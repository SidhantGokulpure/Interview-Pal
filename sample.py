import warnings
warnings.filterwarnings('ignore')
import pyttsx3 #text-to-speech
import speech_recognition as sr #enable microphone
import wikipedia

engine = pyttsx3.init('sapi5') #sapi5 helps in synthesis and recognition of voice
rate = engine.getProperty('rate')
voices = engine.getProperty('voices') #to get details for current voice
engine.setProperty('voice', voices[0].id) # 0 = male and 1 = female
engine.setProperty('rate', 150)

def speak(audio): #function to convert text 2 speech
    engine.say(audio)
    engine.runAndWait() #speech will not be audible without this command

def takeCommandMic():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  #Using google for voice recognition.
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please...")
        return "None"  
    return query

if __name__ == "__main__":
    while True:
        query = takeCommandMic().lower()

        #an example for ai giving the info in both speech and text
        #say "What are computers on wikipedia" for example
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2) #wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
