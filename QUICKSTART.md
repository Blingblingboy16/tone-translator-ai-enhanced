# Quick Start Guide 🚀

Get your Tone Translator AI website live in 3 simple steps!

## 🎯 Fastest Way to Deploy (Render - FREE)

### Step 1: Get Your Gemini API Key
1. Go to https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy your key (starts with "AIza...")

### Step 2: Push to GitHub
```bash
cd Tone_translator_backend1
git init
git add .
git commit -m "Initial commit"
```

Create a new repo at https://github.com/new then:
```bash
git remote add origin https://github.com/YOUR_USERNAME/tone-translator-ai.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render
1. Go to https://render.com (sign up with GitHub)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Add Environment Variable:
   - **Key**: `GEMINI_API_KEY`
   - **Value**: Your API key from Step 1
6. Click "Create Web Service"

⏰ Wait 5-10 minutes... Done! Your site is live! 🎉

## 🔗 Your Website URL

After deployment, Render gives you a URL like:
```
https://tone-translator-ai.onrender.com
```

Share it with anyone! 🌐

## ✅ Test It

1. Visit your URL
2. Type: "This is the best day ever!"
3. Should detect: EXCITED 😃

## 🆘 Troubleshooting

**Site won't load?**
- Check Render logs: Dashboard → Your Service → Logs
- Verify API key is set correctly

**"GEMINI_API_KEY not found"?**
- Go to Render Dashboard → Environment
- Make sure `GEMINI_API_KEY` is there

**Need help?**
See full guide: [DEPLOYMENT.md](DEPLOYMENT.md)

## 🎨 Features to Try

- Toggle Dark/Light mode
- Try different emoji styles (Default, Fun, Minimal)
- Enable text-to-speech
- Test on your phone (it's responsive!)

## 📊 Free Tier Limits

- **Render**: 750 hours/month (always on for 31 days)
- **Gemini API**: 60 requests/minute (plenty for personal use)

---

**Need more details?** Check [DEPLOYMENT.md](DEPLOYMENT.md) for advanced options!
