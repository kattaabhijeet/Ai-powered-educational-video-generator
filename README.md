# AI-Powered Educational Video Generator

Generate professional YouTube explainer-style educational videos automatically using AI.

## 🎥 Features

- **Professional Design**: ByteByteGo/Fireship-style animations
- **Zero Overlap**: Smart label positioning prevents text overlap
- **Natural Voice**: AI-generated female narration with perfect sync
- **Concept-First**: Visual metaphors over technical diagrams
- **Automatic Generation**: Script → Blueprint → Audio → Video in minutes

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys
Create a `.env` file:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your-api-key-here
OPENAI_MODEL=gpt-4o
OPENAI_BASE_URL=https://openrouter.ai/api/v1
```

### 3. Generate Your First Video
```bash
python main.py --topic "How DNS works"
```

**Output:** `output/how_dns_works_video.mp4` (30-60 seconds)

## 📊 System Architecture

```
User Input (Topic)
    ↓
Script Generation (GPT-4) → JSON
    ↓
Blueprint Generation (GPT-4) → Animation Layout
    ↓
Audio Generation (Edge TTS) → MP3 Files
    ↓
Video Rendering (PIL/MoviePy) → Final MP4
```

## 🎨 Design Principles

### Professional YouTube Explainer Style
- **Dark Background**: #0F172A (slate)
- **Grid-Based Layout**: Clean, symmetric positioning
- **Limited Colors**: Orange (#FF6B35), Cyan (#00D4FF), White
- **Smooth Animations**: 1.0-1.5s timing
- **Visual Metaphors**: Icons and cards, not complex diagrams

### Anti-Overlap Rules
- Labels positioned ABOVE containers (not inside)
- Text scaled to 70-80% of container width
- Arrow labels 60px above arrow lines
- Generous spacing (minimum 1.5 units)

## 📁 Project Structure

```
d:/atg/atg assn 2/
├── main.py                      # Entry point
├── pipeline.py                  # Orchestrates generation
├── script_generator.py          # Generates narration scripts
├── blueprint_generator.py       # Generates animation layouts
├── audio_generator.py           # Generates voice narration
├── simple_video_generator.py    # Renders final video
├── prompts.py                   # AI prompts with design rules
├── models_schemas.py            # Data models
├── config.py                    # Configuration
├── requirements.txt             # Dependencies
├── .env.example                 # API key template
└── output/                      # Generated videos
```

## 🛠️ Configuration

Edit `config.py` or `.env`:

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI/OpenRouter API key | Required |
| `OPENAI_MODEL` | LLM model for generation | gpt-4o |
| `OPENAI_BASE_URL` | API endpoint (OpenRouter) | Optional |
| `OPENAI_TTS_MODEL` | Text-to-speech model | gpt-4o-mini-tts |
| `OPENAI_TTS_VOICE` | Voice style | alloy |

## 📝 Example Usage

### Basic Video Generation
```bash
python main.py --topic "What is API"
```

### Custom Output Path
```bash
python main.py --topic "Microservices" --output "custom_video.mp4"
```

## 🐛 Troubleshooting

### "moviepy not installed"
```bash
pip install moviepy
```

### "OPENAI_API_KEY not found"
Make sure `.env` file exists with your API key.

### JSON Parsing Errors
The system auto-retries 3 times with progressive temperature reduction. If issues persist, check `output/failed_blueprint_response.txt` for debugging.

### Voice Overlap
Fixed! Audio duration now controls video timing.

### Text Overlap
Fixed! Renderer implements anti-overlap rules automatically.

## 🎯 Coming Soon

- [ ] Manim-based rendering for smoother animations
- [ ] Multiple voice options
- [ ] Custom color themes
- [ ] Video length customization
- [ ] Batch video generation

## 📄 License

MIT License - Feel free to use and modify!

## 🙏 Credits

- **Design Inspiration**: ByteByteGo, Fireship
- **AI Models**: OpenAI/OpenRouter
- **Text-to-Speech**: Edge TTS
- **Animation**: Manim Community Edition
- **Video Processing**: MoviePy

## 📧 Support

For issues or questions, please open a GitHub issue.

---

**Made with ❤️ for educational content creators**
