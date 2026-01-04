# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Configure API key
cp .env.example .env
# Edit .env and add your OpenRouter API key (free!)
# See OPENROUTER_GUIDE.md for details
```

**Using OpenRouter (Free)**: The system is pre-configured to use OpenRouter's free model `openai/gpt-oss-120b:free`. Just get a free API key from [OpenRouter.ai](https://openrouter.ai/) and add it to `.env`.

### Step 2: Generate Your First Video
```bash
python main.py --topic "How DNS works"
```

### Step 3: Check Output
```bash
# Your video is ready!
output/how_dns_works.mp4
```

---

## 📋 Command Reference

### Basic Usage
```bash
python main.py --topic "Your Topic Here"
```

### With OpenAI TTS (Better Voice Quality)
```bash
python main.py --topic "Your Topic" --openai-tts
```

### Custom Output Name
```bash
python main.py --topic "Your Topic" --output my_custom_name
```

---

## 🎨 Test the Visual Style

Render the demo scene to see the visual style:

```bash
manim -pql demo_scene.py WebSocketStyleDemo
```

Options:
- `-p` = preview after rendering
- `-q` = quality level
- `-l` = low quality (fast)
- `-h` = high quality (slow)

---

## 📂 Output Files

After generation, you'll find:

```
output/
├── [topic]_script.json        # AI-generated script
├── [topic]_blueprint.json     # Animation instructions
├── [topic]_audio/             # Narration files
│   └── scene_*.mp3
├── [topic].mp4                # Final video
└── [topic]_results.json       # Summary
```

---

## 🔧 Troubleshooting

### "OPENAI_API_KEY not found"
- Create `.env` file from `.env.example`
- Add your API key: `OPENAI_API_KEY=sk-...`

### "Module not found"
```bash
pip install -r requirements.txt
```

### Manim Installation Issues
Visit: https://docs.manim.community/en/stable/installation.html

---

## 💡 Example Topics

Try these topics:
- "How DNS works"
- "How HTTPS works"
- "How WebSockets work"
- "How JWT authentication works"
- "How REST APIs work"
- "How Docker containers work"

---

## 📖 Full Documentation

- [README.md](README.md) - Complete documentation
- [analysis/websockets_video_analysis.md](analysis/websockets_video_analysis.md) - Visual style guide
- Demo scene: `demo_scene.py`

---

## 🎯 What Each File Does

| File | Purpose |
|------|---------|
| `main.py` | Command-line interface |
| `pipeline.py` | Orchestrates the workflow |
| `script_generator.py` | Creates video scripts |
| `blueprint_generator.py` | Generates animation plans |
| `video_generator.py` | Renders with Manim |
| `audio_generator.py` | Creates narration |
| `config.py` | Configuration settings |
| `models_schemas.py` | Data structures |

---

**Need help?** Check the full [README.md](README.md) or review the [walkthrough](../brain/8037423d-2a5a-41c1-b4dc-05faf3d0e531/walkthrough.md).
