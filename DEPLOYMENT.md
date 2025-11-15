# Deployment Guide - Tone Translator AI

This guide will help you deploy your Tone Translator AI application as a public website.

## Important Security Changes Made

1. **API Key Security**: Removed hardcoded Gemini API key from code - now uses environment variables
2. **Text-to-Speech**: Removed server-side pyttsx3 dependency (replaced with browser-based speech synthesis)
3. **Production Configuration**: Updated app to run with proper security settings

## Prerequisites

- A Gemini API key from Google (https://makersuite.google.com/app/apikey)
- Git installed on your computer
- A GitHub account (for Render) or hosting platform account

---

## Option 1: Deploy to Render (Recommended - Free Tier Available)

Render is a modern cloud platform with a generous free tier.

### Step 1: Prepare Your Repository

1. **Initialize Git (if not already done):**
   ```bash
   cd Tone_translator_backend1
   git init
   git add .
   git commit -m "Initial commit - ready for deployment"
   ```

2. **Create a GitHub repository:**
   - Go to https://github.com/new
   - Create a new repository (e.g., "tone-translator-ai")
   - Don't initialize with README (we already have files)

3. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/tone-translator-ai.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Sign up/Login to Render:**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select "tone-translator-ai" repository

3. **Configure the Service:**
   - **Name**: tone-translator-ai (or your preferred name)
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

4. **Add Environment Variable:**
   - Click "Environment" tab
   - Add environment variable:
     - **Key**: `GEMINI_API_KEY`
     - **Value**: Your Gemini API key (e.g., AIzaSyDv9GNogJAt0eEdAhHyjtY25B4GNPcpEW4)

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your site will be live at: `https://tone-translator-ai.onrender.com`

### Step 3: Test Your Website

1. Visit your Render URL
2. Type some text in the textarea
3. Watch as it analyzes the tone and adds emojis!

---

## Option 2: Deploy to Heroku

Heroku is another popular platform (requires credit card for verification, but has free tier).

### Step 1: Install Heroku CLI

Download from: https://devcenter.heroku.com/articles/heroku-cli

### Step 2: Deploy

1. **Login to Heroku:**
   ```bash
   heroku login
   ```

2. **Create Heroku app:**
   ```bash
   cd Tone_translator_backend1
   heroku create your-tone-translator-app
   ```

3. **Set environment variable:**
   ```bash
   heroku config:set GEMINI_API_KEY=AIzaSyDv9GNogJAt0eEdAhHyjtY25B4GNPcpEW4
   ```

4. **Deploy:**
   ```bash
   git init
   git add .
   git commit -m "Deploy to Heroku"
   heroku git:remote -a your-tone-translator-app
   git push heroku main
   ```

5. **Open your app:**
   ```bash
   heroku open
   ```

---

## Option 3: Deploy to PythonAnywhere

PythonAnywhere offers a simple free tier perfect for Flask apps.

### Steps:

1. **Sign up:** https://www.pythonanywhere.com/registration/register/beginner/
2. **Upload files:** Use their file upload feature or Git
3. **Create virtual environment:**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```
4. **Configure Web App:**
   - Go to Web tab → Add a new web app
   - Choose Flask
   - Set WSGI file to point to your app.py
5. **Set environment variables:**
   - In Web tab, scroll to "Environment variables"
   - Add GEMINI_API_KEY

---

## Option 4: Deploy to Railway

Railway offers an easy deployment with generous free tier.

### Steps:

1. **Sign up:** https://railway.app
2. **Create new project:** New Project → Deploy from GitHub
3. **Select repository:** Choose your GitHub repo
4. **Add environment variable:**
   - Settings → Variables
   - Add `GEMINI_API_KEY` with your API key
5. **Deploy:** Railway auto-deploys
6. **Get URL:** Click "Generate Domain"

---

## Troubleshooting

### Common Issues:

1. **"GEMINI_API_KEY not found" error:**
   - Make sure you've set the environment variable in your hosting platform
   - Check for typos in the variable name

2. **Application crashes on startup:**
   - Check the logs in your hosting platform
   - Ensure all requirements are installed
   - Verify Python version compatibility

3. **Website loads but doesn't translate text:**
   - Check browser console for errors
   - Verify API key is valid and has quota
   - Check platform logs for backend errors

### Checking Logs:

- **Render:** Dashboard → Your Service → Logs tab
- **Heroku:** `heroku logs --tail`
- **PythonAnywhere:** Web tab → Log files
- **Railway:** Dashboard → Your Project → Logs

---

## Post-Deployment Checklist

- [ ] Website loads successfully
- [ ] Can enter text in the textarea
- [ ] Text analysis works (tone detected, emoji added)
- [ ] Dark/Light mode toggle works
- [ ] Text-to-speech works in browser
- [ ] Different emoji styles work
- [ ] Mobile responsive design works

---

## Updating Your Deployed Site

After making changes locally:

### For Render/Railway (GitHub-based):
```bash
git add .
git commit -m "Your update message"
git push origin main
```
The platform will auto-deploy.

### For Heroku:
```bash
git add .
git commit -m "Your update message"
git push heroku main
```

---

## Cost Considerations

### Free Tiers:
- **Render**: 750 hours/month, sleeps after 15 min inactivity
- **Heroku**: 1000 hours/month (with credit card verification)
- **PythonAnywhere**: Limited CPU time, basic features
- **Railway**: $5 credit/month

### Gemini API:
- Free tier: 60 requests per minute
- Check current limits at: https://ai.google.dev/pricing

---

## Security Best Practices

1. **Never commit .env file** to Git (already in .gitignore)
2. **Use environment variables** for all secrets
3. **Rotate API keys** periodically
4. **Monitor API usage** to detect abuse
5. **Enable HTTPS** (most platforms do this automatically)

---

## Custom Domain (Optional)

Most platforms support custom domains:

1. **Purchase domain** (e.g., from Namecheap, Google Domains)
2. **Configure DNS** in your hosting platform
3. **Update DNS records** at your domain registrar
4. **Enable SSL** (automatic on most platforms)

---

## Need Help?

- **Render Docs**: https://render.com/docs
- **Heroku Docs**: https://devcenter.heroku.com
- **Flask Docs**: https://flask.palletsprojects.com
- **Gemini API Docs**: https://ai.google.dev/docs

---

## What Was Changed for Deployment

1. **app.py:**
   - API key now loaded from environment variable
   - Server-side TTS removed (using browser API)
   - Production-ready settings (host, port, debug=False)

2. **requirements.txt:**
   - Removed pyttsx3 (not compatible with cloud hosting)
   - Removed unused dependencies (flask_bcrypt, flask_sqlalchemy, cryptography)
   - Added gunicorn (production WSGI server)

3. **New files created:**
   - `.gitignore` - Prevents sensitive files from being committed
   - `Procfile` - Tells platforms how to run the app
   - `runtime.txt` - Specifies Python version
   - `render.yaml` - Configuration for Render deployment
   - `DEPLOYMENT.md` - This guide!

Your app is now ready to be deployed to the world! 🚀
