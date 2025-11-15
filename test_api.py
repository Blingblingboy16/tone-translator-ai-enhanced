import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv('GEMINI_API_KEY')
if not api_key:
    print("❌ GEMINI_API_KEY not found in .env")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash')

try:
    print("🔄 Testing Gemini API...")
    response = model.generate_content("Hello, how are you?")
    print("✅ API call successful!")
    print("Response:", response.text)
except Exception as e:
    print("❌ API call failed:", str(e))
