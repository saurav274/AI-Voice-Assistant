import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import time
from AppOpener import open as open_app, close as close_app
from website import open_site

load_dotenv(".env")

engine = pyttsx3.init()

def speak(text):
    global engine
    try:
        engine.stop()      # Stop any previous speech
    except:
        pass

    engine.say(text)
    engine.runAndWait()

# Load Gemini API key
api_key=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key) 

# OPTIMIZATION: Configure the model to give brief answers quickly
fast_config = types.GenerateContentConfig(
    max_output_tokens=150,     # Limits long-winded answers that take time to generate
    temperature=0.7,           # Standard creativity balance
    system_instruction="You are a fast, concise voice assistant. Keep answers brief (1-2 sentences)."
)

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
           
        # Opens Websites and Apps
        if text.startswith("open "):
            name=text.replace("open ","").strip()
            if open_site(name):
                speak(f"Opening {name}")
            else:
                try:
                    open_app(name)
                    speak(f"Opening {name}")
                except Exception as e:
                    print(f"Error opening {name}: {e}")
                    speak(f"Sorry, I cannot find this app named {name}")

        # Closes Apps           
        elif text.startswith("close "):
            name=text.replace("close ","").strip()
            try:
                close_app(name)
                speak(f"Closing {name}")
            except Exception as e:
                print(f"Error closing {name}: {e}")
                speak(f"Sorry, I cannot close this app named {name}")

        # Exits from system
        elif text in ["goodbye" , "quit" , "exit"]:
            speak("Goodbye sir")
            break

        else:
            try:
                # Send the user's query to Gemini and generate a concise response
                print("Sending request to LLM")
                start = time.perf_counter() #Checks time taken by api for response 

                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=text,
                    config=fast_config
                )
                end = time.perf_counter()

                print(f"LLM call took {end - start:.2f} seconds")

                output_text = response.text

                print(output_text)
                speak(output_text)

            except Exception as e:
                print(f"Gemini Error: {e}")
                speak("Sorry, I cannot answer right now.")
        
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")

    except sr.RequestError as e:
        print("Google Speech Recognition service error:", e)