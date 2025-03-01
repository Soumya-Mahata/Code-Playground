import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "news_Api_key"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()  # Initialize pygame mixer
    pygame.mixer.music.load("temp.mp3")  # Load the MP3 file
    pygame.mixer.music.play()  # Play the audio file
    # Keep the program running so the music can play
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Small delay to prevent excessive CPU usage
    pygame.mixer.music.unload()  # Unload the file from the mixer
    os.remove("temp.mp3")  # Remove the file after playing

def aiprocess(command):
    client = OpenAI(api_key="OpenAI_Api_Key",)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like opening websites, playing music, and fetching news."},
            {
                "role": "user",
                "content": command
            }
        ]
    )

    return (completion.choices[0].message['content'])

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
    elif "open ai" in command.lower():
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com/")
    elif command.lower().startswith("play"):
        song = command[command.find(" ") + 1:].lower()
        if song in musicLibrary.music:
            speak("Playing " + song)
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Song not found")
    elif "news" in command.lower():
        speak("Here are the top news")
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
        response = requests.get(url)
        # Checking if the request was successful. In HTTP, 200 means success.
        if response.status_code == 200:
            news = response.json()
            # Extracting and displaying headlines
            if "articles" in news:
                for i, article in enumerate(news["articles"], 1):
                    speak(f"{i}. {article['title']}")
            else:
                print("No articles found.")
        else:
            print(f"Error: Unable to fetch news (Status Code: {response.status_code})")
    else:
        # Let OpenAI handle the command
        output = aiprocess(command)
        speak(output)

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
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)
            print(word)
            if ("jarvis" in word.lower()):
                speak("yeah!")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Processing...{command}")
                    ProcesCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))