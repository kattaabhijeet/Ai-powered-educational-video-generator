"""
Configuration and environment management.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Configuration settings for the video generation system."""
    
    # OpenAI API (works with OpenRouter too)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", None)  # For OpenRouter
    OPENAI_TTS_MODEL = os.getenv("OPENAI_TTS_MODEL", "tts-1")
    OPENAI_TTS_VOICE = os.getenv("OPENAI_TTS_VOICE", "alloy")
    
    # Style Profile Colors (from WebSockets video analysis)
    DARK_BG = "#1a1a1a"
    CLIENT_COLOR = "#00d4ff"
    SERVER_COLOR = "#ff6b35"
    TEXT_COLOR = "#ffffff"
    SECONDARY_TEXT = "#a0a0a0"
    
    # Video Settings
    VIDEO_WIDTH = 1920
    VIDEO_HEIGHT = 1080
    VIDEO_FPS = 30
    DEFAULT_SCENE_DURATION = 8.0
    
    # Output Paths
    OUTPUT_DIR = "output"
    TEMP_DIR = "output/temp"
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present."""
        if not cls.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found. Please create a .env file with your API key."
            )
        return True


# Validate configuration on import
try:
    Config.validate()
    print("[OK] Configuration loaded successfully")
except ValueError as e:
    print(f"[WARNING] Configuration warning: {e}")
