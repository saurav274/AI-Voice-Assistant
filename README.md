# 🎙️ AI Voice Assistant

A Python-based voice assistant powered by **Google Gemini AI**. It can understand voice commands, answer questions using AI, open websites from a MySQL database, and launch or close desktop applications.

This project was built to practice **Python, APIs, MySQL, Git/GitHub, modular programming, and AI application development.**

---

## ✨ Features

- 🎤 Voice Recognition using SpeechRecognition
- 🔊 Text-to-Speech using pyttsx3
- 🤖 AI-powered responses with Google Gemini
- 🌐 Open websites stored in a MySQL database
- 📂 Open and close desktop applications
- 🔒 Secure configuration using environment variables (.env)
- 📦 Clean and modular project structure

---

## 🛠️ Technologies Used

- Python
- Google Gemini API
- MySQL
- AppOpener
- SpeechRecognition
- pyttsx3
- sounddevice
- scipy
- python-dotenv

---

## 📂 Project Structure

```text
AI-Voice-Assistant/
│
├── main.py              # Main voice assistant
├── database.py          # MySQL connection and database functions
├── website.py           # Opens websites using MySQL
├── requirements.txt     # Project dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Git ignored files
└── README.md            # Project documentation
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/saurav274/AI-Voice-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd AI-Voice-Assistant
```

### 3. Create a virtual environment (Recommended)

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a file named:

```text
.env
```

Add the following variables:

```env
# Google Gemini API
GEMINI_API_KEY=YOUR_API_KEY

# MySQL Database
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_PASSWORD
DB_NAME=WebSites_db
```

---

## 🗄️ Database Setup

Create the database:

```sql
CREATE DATABASE WebSites_db;
```

Select the database:

```sql
USE WebSites_db;
```

Create the required table:

```sql
CREATE TABLE sites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    site_name VARCHAR(100) UNIQUE NOT NULL,
    url VARCHAR(255) NOT NULL
);
```

Insert some websites:

```sql
INSERT INTO sites (site_name, url)
VALUES
('google', 'https://google.com'),
('youtube', 'https://youtube.com'),
('github', 'https://github.com'),
('chatgpt', 'https://chatgpt.com');
```

---

## ▶️ Run the Assistant

```bash
python main.py
```

---

## 🎤 Example Commands

### 🌐 Websites

- Open Google
- Open YouTube
- Open GitHub
- Open ChatGPT

### 📂 Applications

- Open Chrome
- Open Spotify
- Open Calculator
- Close Chrome
- Close Spotify

### 🤖 AI

- What is Artificial Intelligence?
- Tell me a joke.
- Explain Machine Learning.
- Who invented Python?

### 🚪 Exit

- Exit
- Quit
- Goodbye

---

## 📌 Future Improvements

- 🖥️ GUI Interface
- 🎙️ Wake Word Support
- 🧠 Local LLM Integration
- 💬 Conversation Memory
- 🌦️ Weather Integration
- 🎵 Music Controls
- 📅 Calendar & Reminder Support
- 🔍 Better Natural Language Understanding

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you have ideas to improve the project, feel free to fork the repository and open a Pull Request.

---

## 👨‍💻 Author

**Saurav**

Built as a personal project to learn and practice:

- Python
- MySQL
- APIs
- AI Development
- Software Engineering
- Git & GitHub