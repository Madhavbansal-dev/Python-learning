**Jarvis – AI Voice Assistant**

*Python- 3.10+
License- MIT*

Jarvis is a Python-based AI voice assistant that can perform various tasks using voice commands.
It integrates speech recognition, text-to-speech, AI responses, music playback, and news updates.

This project is part of my **Python learning journey.**

---

**Features**

- Voice recognition using "speech_recognition"
- Text-to-speech responses using "pyttsx3"
- AI responses using Gemini API
- Fetch latest news using NewsAPI
- Play music from a JSON-based music library
- Open popular websites like Google, YouTube, Instagram, LinkedIn, etc.

---

**Installation**

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Python-learning.git

Go to the project folder:

cd Python-learning/Jarvis

Install required libraries:

pip install pyttsx3 speechrecognition requests google-generativeai

---

**API Setup**

This project requires two API keys:

**Gemini API**

Replace this line in "jarvis.py":

genai.configure(api_key="YOUR_GEMINI_API_KEY")

with your own Gemini API key.

**News API**

Replace this line in "jarvis.py":

newsapi="YOUR_NEWS_API_KEY"

with your own NewsAPI key.

---

**How to Run**

Run the program:

python jarvis.py

Say "Jarvis" to activate the assistant.

Example commands:

- Open Google
- Open YouTube
- Play shape of you
- Tell me the news

Jarvis will listen and respond using voice.

---

**Music Library**

Jarvis uses a "music.json" file to store song names and their YouTube links.

Example:

{
  "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
  "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ"
}

You can add more music in "music.json" to play your favorite songs.

To add a new song:

"song name": "youtube link"

Example:

"believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc"

---

**Project Structure**

Python-learning
│
├── password_generator.py
│
└── Jarvis
    ├── jarvis.py
    ├── music.json
    └── README.md

---

**Requirements**

- Python 3.10+
- Internet connection
- Python libraries:
  - pyttsx3
  - speechrecognition
  - requests
  - google-generativeai

---

**Author**

Madhav Bansal
Class 9 Student | Learning Python & Electronics
Aspiring Developer & Inventor

GitHub: https://github.com/madhavbansal-dev
