import pyttsx3
import speech_recognition as sr
import webbrowser

#provide access to TTS 
engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)

def main():
    speak_audio("Hello, I'm Jalith's voice assistant.")
    speak_audio("How can I help you?")
    while True:
        #recognize the words
        query = take_command().lower()

        #commands to recognize
        if "are you in" in query:
            speak_audio("Yes, I am here.")

        elif "open google" in query:
            speak_audio("Please wait, I am opening Google.")
            webbrowser.open("https://www.google.com")

        elif "open github" in query:
            speak_audio("Please wait I'll open github")
            webbrowser.open("https://github.com/")

#for speak the words
def speak_audio(audio):
    engine.say(audio)
    engine.runAndWait()

#get the commands from microphone
def take_command():

    #defining recognizer
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print("User said: " + query + "\n")
    except Exception as e:
        print(e)
        speak_audio("I didn't understand.")
        return "None"
    return query

if __name__ == "__main__":
    main()
