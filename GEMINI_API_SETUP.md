# Gemini API Key Setup Guide

## What is the Gemini API Key?

The Gemini API key allows your application to use Google's Gemini AI model for tone analysis. Your app needs this key to communicate with Google's AI services.

## Current Status

Your `.env` file already has a Gemini API key configured:
```
GEMINI_API_KEY=AIzaSyDv9GNogJAt0eEdAhHyjtY25B4GNPcpEW4
```

---

## Option 1: Getting a New Gemini API Key

If you need a fresh API key or the current one isn't working, follow these steps:

### Step 1: Visit Google AI Studio
1. Go to: https://aistudio.google.com/app/apikey
2. Sign in with your Google account

### Step 2: Create an API Key
1. Click the **"Create API Key"** button
2. Select **"Create API key in new project"** (or use an existing project)
3. Copy the generated API key (it will look like: `AIzaSy...`)

### Step 3: Update Your .env File
1. Open `Tone_translator_backend1/.env` in your editor
2. Replace the existing key with your new key:
   ```
   GEMINI_API_KEY=YOUR_NEW_API_KEY_HERE
   SECRET_KEY=super_secret_flask_key
   ENCRYPTION_KEY=your_32byte_encryption_key_here
   ```

---

## Option 2: Test Your Current API Key

Let's verify if your current API key is working:

### Quick Test
Run this command in your terminal from the `Tone_translator_backend1` directory:

```bash
python test_api.py
```

If it works, you'll see tone analysis results. If not, you'll need to get a new key.

---

## Option 3: Configure for Render Deployment

If you're deploying to Render, you need to add the API key as an environment variable on Render's platform:

### Step 1: Go to Render Dashboard
1. Visit: https://dashboard.render.com
2. Click on your deployed service

### Step 2: Add Environment Variable
1. Click **"Environment"** in the left sidebar
2. Click **"Add Environment Variable"**
3. Enter:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your API key (e.g., `AIzaSyDv9GNogJAt0eEdAhHyjtY25B4GNPcpEW4`)
4. Click **"Save Changes"**
5. Your service will automatically redeploy

---

## Running Your App Locally

Once your API key is configured in `.env`:

### Step 1: Install Dependencies
```bash
cd Tone_translator_backend1
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: http://localhost:5000

---

## Troubleshooting

### Error: "GEMINI_API_KEY not found"
- Make sure your `.env` file is in the `Tone_translator_backend1` directory
- Ensure there are no extra spaces around the `=` sign
- Restart your application after updating `.env`

### Error: "API key not valid"
- Your API key might be expired or revoked
- Get a new API key from https://aistudio.google.com/app/apikey
- Make sure you copied the entire key (they're usually 39 characters long)

### Error: "Quota exceeded"
- Free tier has usage limits
- Wait 24 hours or upgrade your Google Cloud project

---

## Important Notes

⚠️ **Never commit your API key to Git!**
- The `.gitignore` file should already include `.env`
- Your API key should only be in `.env` for local development
- For production (Render), add it as an environment variable on the platform

✅ **Your API key is working if:**
- The test script runs successfully
- The app analyzes text and returns emojis
- No error messages about API keys appear in logs

---

## Need Help?

If you're still having issues:
1. Check if the API key is active at https://aistudio.google.com/app/apikey
2. Review the logs when running `python app.py`
3. Make sure your `.env` file has the correct format (no quotes around values)
