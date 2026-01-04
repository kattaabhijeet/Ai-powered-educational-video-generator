# Using OpenRouter (Free Model)

This project is configured to use **OpenRouter's free model** `openai/gpt-oss-120b:free` instead of paid OpenAI GPT-4.

## Setup with OpenRouter

### 1. Get Your OpenRouter API Key

1. Go to [OpenRouter.ai](https://openrouter.ai/)
2. Sign up for a free account
3. Navigate to **Keys** section
4. Create a new API key
5. Copy your API key

### 2. Configure the Project

Edit your `.env` file:

```bash
# OpenRouter API Key
OPENAI_API_KEY=sk-or-v1-your-openrouter-key-here

# Free model configuration
OPENAI_MODEL=openai/gpt-oss-120b:free
OPENAI_BASE_URL=https://openrouter.ai/api/v1
```

### 3. Run the System

```bash
# Generate a video (uses free model for script/blueprint)
python main.py --topic "How DNS works"

# Note: Use free gTTS for audio (OpenRouter doesn't support TTS)
# The --openai-tts flag won't work with OpenRouter
```

## What's Free vs Paid

| Component | Free Option | Paid Option |
|-----------|-------------|-------------|
| **Script Generation** | ✅ OpenRouter free model | OpenAI GPT-4 |
| **Blueprint Generation** | ✅ OpenRouter free model | OpenAI GPT-4 |
| **Audio (TTS)** | ✅ gTTS (Google TTS) | OpenAI TTS |
| **Video Rendering** | ✅ Manim (open source) | Same |

## Current Configuration

✅ **Script & Blueprint**: OpenRouter free model (`openai/gpt-oss-120b:free`)  
✅ **Audio**: Free gTTS (Google Text-to-Speech)  
✅ **Video**: Free Manim (open source)  

**Total Cost**: $0 🎉

## OpenRouter Benefits

- **Free tier available** with generous limits
- **Compatible with OpenAI SDK** (drop-in replacement)
- **Multiple models** to choose from
- **No credit card required** for free tier

## Limitations

- OpenRouter doesn't support TTS endpoints (use gTTS instead)
- Free model may have rate limits
- Quality may differ from GPT-4 (but still very good!)

## Alternative: Use OpenAI GPT-4

If you prefer to use OpenAI's GPT-4:

```bash
# In .env file:
OPENAI_API_KEY=sk-your-openai-key
OPENAI_MODEL=gpt-4
# Remove or comment out OPENAI_BASE_URL
```

Then you can use OpenAI TTS:
```bash
python main.py --topic "Your Topic" --openai-tts
```

---

**Recommended**: Stick with the free configuration (OpenRouter + gTTS) for unlimited video generation at zero cost!
