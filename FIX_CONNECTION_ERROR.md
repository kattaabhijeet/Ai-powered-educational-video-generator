# Quick fix guide for the connection error

## Problem
Your `.env` file has the wrong base URL for OpenRouter.

## Solution

Open your `.env` file and make sure line 6 looks EXACTLY like this:

```bash
OPENAI_BASE_URL=https://openrouter.ai/api/v1
```

**NOT** `https://api.openrouter.ai` (this is wrong!)

## Complete .env File Should Look Like:

```bash
# OpenRouter API Key
OPENAI_API_KEY=sk-or-v1-your-actual-key-here

# Model configuration
OPENAI_MODEL=openai/gpt-oss-120b:free
OPENAI_BASE_URL=https://openrouter.ai/api/v1

# TTS settings (optional)
OPENAI_TTS_MODEL=tts-1
OPENAI_TTS_VOICE=alloy
```

## After Fixing

Save the file and run again:
```bash
python main.py --topic "How DNS works"
```

---

**Note**: Also ignore the ffmpeg warning - it's optional and won't affect the script/blueprint generation. We'll address it later if needed.
