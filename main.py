import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from google import genai
from apps import open_app
from website import open_site
import time

load_dotenv("API.env")

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Load Gemini API key
api_key=os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

FS = 16000
DURATION = 5
r = sr.Recognizer()

while True:

    # Record user's voice
    print("Speak now...")

    recording = sd.rec(
        int(DURATION * FS),
        samplerate=FS,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write("voice.wav", FS, recording)

    print("Recording saved!")

    with sr.AudioFile("voice.wav") as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio).lower()
        print("You said:", text)

        #Opens Websites and Apps
        if text.startswith("open "):
            name=text.replace("open ","").strip()
            if open_site(name):
                speak(f"Opening {name}")
            elif open_app(name):
                    speak(f"Opening {name}")
            else:
                speak("Sorry sir i can't open this, it's not added in system")

        #Exits from system
        elif text in ["goodbye" , "quit" , "exit"]:
            speak("Goodbye sir")
            break

        else:
            try:
                #Using LLM API 
                print("Sending request to LLM")
                start = time.perf_counter() #Checks time taken by api for response 

                interaction = client.interactions.create(
                    model="gemini-3.5-flash",
                    input=text
                )
                end = time.perf_counter()

                print(f"LLM call took {end - start:.2f} seconds")

                print(interaction.output_text)
                speak(interaction.output_text)

            except Exception as e:
                print(f"Gemini Error: {e}")
                speak("Sorry, I cannot answer right now.")
        
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")

    except sr.RequestError as e:
        print("Google Speech Recognition service error:", e)