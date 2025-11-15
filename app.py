from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Add file handler
file_handler = logging.FileHandler('debug.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    logging.error("GEMINI_API_KEY not found in environment variables")
    raise ValueError("GEMINI_API_KEY environment variable is required")
    
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

def analyze_tone(text):
    """Use Gemini to analyze the tone of the text with enhanced sarcasm detection."""
    try:
        prompt = f"""
        You are an advanced tone and emotion classifier with expertise in detecting sarcasm and subtle emotional cues.
        
        Analyze the following text carefully, paying special attention to:
        - Contextual clues that might indicate sarcasm (exaggeration, contradiction, irony)
        - Punctuation patterns (excessive punctuation, ellipsis, etc.)
        - Common sarcastic phrases or patterns
        - The contrast between literal meaning and implied meaning
        
        Identify the emotional tone of the message as ONE of these categories:
        SARCASM, EXCITED, NEUTRAL, APPRECIATION, ANGER, SADNESS, HUMOR, OTHER
        
        If you detect any hint of sarcasm, irony, or mockery, classify it as SARCASM.
        Respond with ONLY the tone word in uppercase.

        Text: {text}

        Output format: <tone>
        """

        response = model.generate_content(prompt)
        raw_output = response.text.strip().upper()

        valid_tones = [
            "SARCASM",
            "EXCITED",
            "NEUTRAL",
            "APPRECIATION",
            "ANGER",
            "SADNESS",
            "HUMOR",
            "OTHER"
        ]

        # Try direct match first
        for tone in valid_tones:
            if tone in raw_output:
                return tone

        # Fallback if no valid tone found
        logging.warning("Unexpected model output: %s", raw_output)
        return "OTHER"

    except Exception as e:
        logging.error("Error analyzing tone: %s", e)
        return "NEUTRAL"

# Expanded emoji sets
emoji_sets = {
    "default": {
        "SARCASM": "🙃",
        "EXCITED": "😃",
        "NEUTRAL": "😐",
        "APPRECIATION": "😍",
        "ANGER": "😡",
        "SADNESS": "😢",
        "HUMOR": "😆",
        "OTHER": "🤔"
    },
    "fun": {
        "SARCASM": "😜",
        "EXCITED": "🤩",
        "NEUTRAL": "😶",
        "APPRECIATION": "🥰",
        "ANGER": "🤬",
        "SADNESS": "😭",
        "HUMOR": "🤣",
        "OTHER": "🧐"
    },
    "minimal": {
        "SARCASM": "😏",
        "EXCITED": "😄",
        "NEUTRAL": "😐",
        "APPRECIATION": "❤️",
        "ANGER": "😠",
        "SADNESS": "☹️",
        "HUMOR": "🙂",
        "OTHER": "❓"
    }
}

@app.route("/")
def index():
    """Render the web UI."""
    return render_template("index.html")

# Translations
translations = {
    "en": {
        "SARCASM": "Sarcasm",
        "EXCITED": "Excited",
        "NEUTRAL": "Neutral",
        "APPRECIATION": "Appreciation",
        "ANGER": "Anger",
        "SADNESS": "Sadness",
        "HUMOR": "Humor",
        "OTHER": "Other"
    },
    "es": {
        "SARCASM": "Sarcasmo",
        "EXCITED": "Emocionado",
        "NEUTRAL": "Neutral",
        "APPRECIATION": "Apreciación",
        "ANGER": "Enojo",
        "SADNESS": "Tristeza",
        "HUMOR": "Humor",
        "OTHER": "Otro"
    }
}

@app.route("/translate-tone", methods=["POST"])
def translate_tone():
    """Analyze text tone and return emoji + tone label."""
    logging.info("translate_tone endpoint called")
    data = request.json
    text = data.get("text", "")
    emoji_style = data.get("emoji_style", "default")
    language = data.get("language", "en")
    logging.info("Received text: %s, emoji_style: %s, language: %s", text, emoji_style, language)

    if not text:
        logging.warning("No text provided in request")
        error_msg = "No se proporcionó texto" if language == "es" else "No text provided"
        return jsonify({"error": error_msg}), 400

    tone = analyze_tone(text)
    emoji = emoji_sets.get(emoji_style, emoji_sets["default"]).get(tone, "🤔")
    tone_label = translations.get(language, translations["en"]).get(tone, tone)

    logging.info("Analyzed tone: %s, emoji: %s", tone, emoji)
    return jsonify({
        "tone": tone,
        "tone_label": tone_label,
        "emoji": emoji,
        "translated_text": f"{text} {emoji}"
    })

@app.route("/speak", methods=["POST"])
def speak():
    """Text-to-speech endpoint - now handled client-side via browser API."""
    # This endpoint is kept for backward compatibility but does nothing server-side
    # The frontend now uses the browser's SpeechSynthesis API
    return jsonify({"success": True, "message": "TTS handled client-side"})

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
