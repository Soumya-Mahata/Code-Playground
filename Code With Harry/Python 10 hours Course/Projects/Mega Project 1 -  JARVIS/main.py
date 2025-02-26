import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ProcesCommand(command):
    if "open google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open linkedIn" in command.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open whatsApp" in command.lower():
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")
    elif "open gmail" in command.lower():
        speak("Opening Gmail")
        webbrowser.open("https://www.gmail.com")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Google Speech Recognition
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout = 3, phrase_time_limit = 5)
            word = r.recognize_google(audio)
            print(word)
            if (word.lower() == "jarvis"):
                speak("yeah!")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    ProcesCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))