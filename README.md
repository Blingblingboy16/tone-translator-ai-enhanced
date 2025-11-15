# Tone Translator AI 🎭

An AI-powered web application that analyzes the emotional tone of text and adds contextual emojis using Google's Gemini AI.

## Features

- 🤖 **AI Tone Analysis** - Detects emotions like sarcasm, excitement, appreciation, anger, and more
- 😊 **Multiple Emoji Styles** - Choose from default, fun, or minimal emoji sets
- 🎨 **Dark/Light Mode** - Toggle between themes for comfortable viewing
- 🔊 **Text-to-Speech** - Browser-based speech synthesis (works on all platforms)
- ♿ **High Contrast Mode** - Accessibility feature for better readability
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile

## Technology Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Gemini 2.5 Flash
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Ready for Render, Heroku, Railway, or PythonAnywhere

## Quick Start (Local Development)

1. **Install dependencies:**
   ```bash
   cd Tone_translator_backend1
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file with:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://localhost:5000`

## Deploy as Public Website

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for detailed deployment instructions to:
- ✅ Render (Recommended)
- ✅ Heroku
- ✅ PythonAnywhere
- ✅ Railway

## How It Works

1. User types text in the textarea
2. AI analyzes the emotional tone using Gemini API
3. Appropriate emoji is selected based on detected tone
4. Result is displayed with tone label and emoji
5. Optional text-to-speech reads the result

## Tone Categories

- **SARCASM** 🙃 - Sarcastic or ironic messages
- **EXCITED** 😃 - Enthusiastic or happy messages
- **NEUTRAL** 😐 - Factual or emotionally neutral messages
- **APPRECIATION** 😍 - Grateful or appreciative messages
- **ANGER** 😡 - Frustrated or angry messages
- **SADNESS** 😢 - Sad or disappointed messages
- **HUMOR** 😆 - Funny or comedic messages
- **OTHER** 🤔 - Unclear or mixed emotions

## Project Structure

```
Tone_translator_backend1/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
├── runtime.txt            # Python version specification
├── render.yaml            # Render deployment config
├── .gitignore             # Git ignore file
├── .env                   # Environment variables (not committed)
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   └── style.css          # Styling
└── DEPLOYMENT.md          # Deployment guide
```

## Security

- ✅ API keys stored in environment variables (not hardcoded)
- ✅ `.env` file excluded from version control
- ✅ Production-ready configuration
- ✅ HTTPS enforced on deployment platforms

## License

This project is open source and available for personal and commercial use.

## Contributing

Contributions, issues, and feature requests are welcome!

## Support

For deployment issues, see [DEPLOYMENT.md](DEPLOYMENT.md) troubleshooting section.

---

**Ready to deploy?** Follow the step-by-step guide in [DEPLOYMENT.md](DEPLOYMENT.md)! 🚀
