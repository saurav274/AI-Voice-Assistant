# 🎙️ AI Voice Assistant

A simple AI-powered voice assistant built with Python that can recognize voice commands, open websites and desktop applications, and answer general questions using the Google Gemini API.

## 👨‍💻 Author

Developed by **Saurav** as a personal project to practice Python, APIs, and AI development.

## ✨ Features

- 🎤 Voice recognition using SpeechRecognition
- 🔊 Text-to-Speech using pyttsx3
- 🤖 AI responses powered by Google Gemini
- 🌐 Open websites with voice commands
- 💻 Launch desktop applications

 Note: app paths in apps.py are hardcoded to my machine — update apps.py with your own shortcut paths to use app-opening commands

- 🔒 Secure API key using environment variables (.env)
- 📦 Modular project structure

## 🛠️ Technologies Used

- Python
- Google Gemini API
- SpeechRecognition
- pyttsx3
- sounddevice
- scipy
- python-dotenv

## 📂 Project Structure

```
AI-Voice-Assistant/
│
├── main.py
├── apps.py
├── website.py
├── requirements.txt
├── .gitignore
├── README.md
└── API.env (not included)
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Voice-Assistant.git
```

### 2. Navigate to the project

```bash
cd AI-Voice-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create an environment file

Create a file named:

```
API.env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### 5. Run the assistant

```bash
python main.py
```

## 🎤 Example Commands

- Open Google
- Open YouTube
- Open GitHub
- Open Notepad
- Open Calculator
- What is Artificial Intelligence?
- Tell me a joke
- Exit

## 📌 Future Improvements

- Wake word support
- Local LLM support
- GUI interface
- Weather integration
- Music controls
- Better speech formatting
- Conversation memory

## 🤝 Contributing

Suggestions and improvements are always welcome.

## 📄 License

This project is licensed under the MIT License.