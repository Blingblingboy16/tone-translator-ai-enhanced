# 🧠 Tone Translator AI

**Tone Translator AI** is an accessibility-focused web app that helps users — especially those in the **neurodivergent community** — better understand the *tone* and *emotional intent* behind written text.  

It analyzes messages for tone cues like **sarcasm, excitement, appreciation, humor**, and more, then displays an appropriate **emoji** to visually represent that tone.  

It can also **read the message aloud** (text-to-speech) and includes **light/dark green themes** and a **high-contrast mode** for comfortable readability.

---

## 🌟 Features

- 🗣️ **AI-Powered Tone Detection** – Uses Google Gemini to analyze tone and emotion.  
- 💚 **Tone Visualization** – Displays matching emojis for tones like sarcasm, excitement, appreciation, sadness, etc.  
- 🔊 **Text-to-Speech** – Optionally read text aloud for better accessibility.  
- 🌞 **Light/Dark Mode** – Switch between soothing light and dark green themes.  
- ⚡ **High-Contrast Mode** – Enhances visual clarity for better accessibility.  
- 🎨 **Emoji Style Selector** – Choose from *default*, *fun*, or *minimal* emoji sets.  
- 💾 **Persistent Settings** – Preferences (TTS, emoji style, theme) are saved locally.

---

## 🧩 Project Structure

```
tone-translator-ai/
│
├── app.py               # Flask backend – routes, AI tone analysis, TTS
├── templates/
│   └── index.html       # Frontend HTML interface
├── static/
│   └── style.css        # Custom green-themed stylesheet
├── .env                 # Contains your Gemini API key
├── requirements.txt     # (optional) Python dependencies
└── README.md            # You're reading this
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/tone-translator-ai.git
cd tone-translator-ai
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install flask flask-cors python-dotenv pyttsx3 google-generativeai
```

### 4️⃣ Create a `.env` file
In the root folder, create a file named `.env` containing your Google Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run the app
```bash
python app.py
```

Then open your browser and go to:  
👉 http://127.0.0.1:5000/

---

## 🧠 How It Works

1. User types a message (e.g., “I love you” or “Oh great, another Monday 🙄”).  
2. The app sends the text to the **Gemini API** for tone interpretation.  
3. The model classifies the tone into categories such as:  
   - SARCASM 🙃  
   - EXCITED 😃  
   - APPRECIATION 😍  
   - HUMOR 😆  
   - ANGER 😡  
   - SADNESS 😢  
   - NEUTRAL 😐  
4. The appropriate emoji is appended to the text and displayed on-screen.  
5. If Text-to-Speech is enabled, the app will also read the text aloud.

---

## 🎨 Accessibility Design

- **Color-friendly** light and dark green modes.  
- **High-contrast toggle** for users with vision sensitivity.  
- **Centered, minimal UI** for reduced cognitive load.  
- **Bold, legible Arial font** across the interface.  

---

## 🧰 Technologies Used

- **Python** (Flask backend)  
- **HTML, CSS, JavaScript** (Frontend)  
- **Google Gemini API** (Tone and emotion analysis)  
- **pyttsx3** (Text-to-speech)  
- **Flask-CORS** (Cross-origin support)  

---

## 🧑‍🤝‍🧑 About

Tone Translator AI was created to **bridge the communication gap** for people who find it difficult to interpret emotional tone in text — such as members of the **autistic and neurodivergent communities** — helping online communication feel more clear, comfortable, and human.

---

## 💡 Example Inputs

| Input Text                     | Detected Tone     | Emoji |
|-------------------------------|------------------|-------|
| I love you ❤️                 | Appreciation     | 😍    |
| Oh great, another Monday...   | Sarcasm          | 🙃    |
| LET’S GOOOOO!!!               | Excited          | 😃    |
| Thanks so much for your help! | Appreciation     | 🥰    |
| Ugh, not again…               | Sadness          | 😢    |

---

## 🛡️ License

This project is open-source under the **MIT License**.  
Feel free to fork, improve, and share responsibly.
