import time
import speech_recognition as sr
import webbrowser
import pyttsx3
from multiprocessing import Process
import requests
import google.generativeai as genai
import json

# ---- Speech ----
def worker(text):
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()

def speak(text):
    p = Process(target=worker, args=(text,))
    p.start()
    p.join()

# ---- Music ----
try:
    with open("music.json", "r") as f:
        music_library = json.load(f)
except FileNotFoundError:
    music_library = {}
    print("music.json not found. Music feature will be disabled.")

# ---- AI ----
genai.configure(api_key="YOUR_GEMINI_API_KEY")

def ai(c):
    try:
        prompt = f"You are Jarvis. Answer in Hindi/English casually. User said: {c.lower()}"
        response = genai.Models.generate_text(model="gemini-2.5-flash", prompt=prompt)
        return getattr(response, "text", str(response))
    except Exception as e:
        print(f"AI error: {e}")
        return "Sorry, I couldn't process that right now"

# ---- Voice Recognizer ----
r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
newsapi = "YOUR_NEWS_API_KEY"
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)

# ---- Commands ----
def processCommand(c):
    c_lower = c.lower()
    if "open google" in c_lower:
        webbrowser.open("https://google.com")
    elif "open facebook" in c_lower:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c_lower:
        webbrowser.open("https://youtube.com")
    elif "open chatgpt" in c_lower or "open chat gpt" in c_lower:
        webbrowser.open("https://chatgpt.com")
    elif "open instagram" in c_lower:
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c_lower:
        webbrowser.open("https://linkedin.com")
    elif "open jiohotstar" in c_lower:
        webbrowser.open("https://jiohotstar.com")
    elif c_lower.startswith("play"):
        song = " ".join(c_lower.split(" ")[1:]).strip()
        link = music_library.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find {song} in my music library.")
    elif "news" in c_lower:
        try:
            r = requests.get(f"https://newsapi.org/v2/everything?q=India&language=en&sortBy=publishedAt&apiKey={newsapi}")
            if r.status_code == 200:
                speak("Here are today's news")
                time.sleep(0.5)
                data = r.json()
                articles = data.get("articles", [])
                for article in articles:
                    print(article["title"])
                    speak(article["title"])
        except Exception:
            speak("Sorry, I couldn't fetch the news right now")
    else:
        output = ai(c)
        print(output)
        speak(output)

# ---- Main ----
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        try:
            print("Call me by saying Jarvis")
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening....")
                audio = r.listen(source, timeout=7, phrase_time_limit=7)
                print("Recognizing....")
                word = r.recognize_google(audio)
            
            if "jarvis" not in word.lower():
                print(f"You said: {word}")
            
            if "jarvis" in word.lower():
                with sr.Microphone() as source:
                    try:
                        r.adjust_for_ambient_noise(source, duration=1)
                        speak("Yaa, speak I am activated")
                        print("Speak I am activated")
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        command = r.recognize_google(audio)
                        print(f"Your command: {command}")
                        speak(f"Your command is {command}")
                        processCommand(command)
                    except sr.UnknownValueError:
                        speak("Could not understand audio")
                        speak("Call me by saying Jarvis")
                    except sr.WaitTimeoutError:
                        speak("No speech detected, try again...")
                        speak("Call me by saying Jarvis")
        except sr.WaitTimeoutError:
            print("No speech detected, try again...")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError:
            print("Could not request results, check internet")
        except Exception as e:
            print(f"Error: {e}")
