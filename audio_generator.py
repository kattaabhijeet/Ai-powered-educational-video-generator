"""
Audio generation using OpenAI TTS or gTTS.
"""
import os
from pathlib import Path
from openai import OpenAI
from gtts import gTTS
from config import Config
from models_schemas import Script


class AudioGenerator:
    """Generates narration audio from scripts."""
    
    def __init__(self, use_openai_tts: bool = True):
        """
        Initialize the audio generator.
        
        Args:
            use_openai_tts: If True, use OpenAI TTS. If False, use free gTTS.
        """
        self.use_openai_tts = use_openai_tts
        if use_openai_tts:
            client_kwargs = {"api_key": Config.OPENAI_API_KEY}
            # Note: OpenRouter may not support TTS, so this might fail
            # In that case, fall back to gTTS
            if Config.OPENAI_BASE_URL:
                client_kwargs["base_url"] = Config.OPENAI_BASE_URL
            self.client = OpenAI(**client_kwargs)
            self.model = Config.OPENAI_TTS_MODEL
            self.voice = Config.OPENAI_TTS_VOICE
    
    def generate_narration(self, script: Script, output_dir: str = "output/audio"):
        """
        Generate audio narration for all scenes in a script.
        
        Args:
            script: The video script
            output_dir: Directory to save audio files
            
        Returns:
            List of audio file paths
        """
        print(f"[MIC] Generating narration audio...")
        
        # Create output directory
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        audio_files = []
        
        for scene in script.scenes:
            audio_path = os.path.join(
                output_dir,
                f"scene_{scene.scene_number}_narration.mp3"
            )
            
            if self.use_openai_tts:
                self._generate_openai_tts(scene.narration, audio_path)
            else:
                self._generate_gtts(scene.narration, audio_path)
            
            audio_files.append(audio_path)
            print(f"  [OK] Scene {scene.scene_number} audio saved")
        
        print(f"[OK] Generated {len(audio_files)} audio files")
        return audio_files
    
    def _generate_openai_tts(self, text: str, output_path: str):
        """Generate audio using OpenAI TTS."""
        response = self.client.audio.speech.create(
            model=self.model,
            voice=self.voice,
            input=text
        )
        response.stream_to_file(output_path)
    
    def _generate_gtts(self, text: str, output_path: str):
        """Generate audio using Google TTS (free)."""
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_path)


if __name__ == "__main__":
    # Test audio generation
    from script_generator import ScriptGenerator
    
    script_gen = ScriptGenerator()
    script = script_gen.generate("How DNS works")
    
    # Test with gTTS (free)
    audio_gen = AudioGenerator(use_openai_tts=False)
    audio_files = audio_gen.generate_narration(script)
    
    print("\nGenerated audio files:")
    for f in audio_files:
        print(f"  - {f}")
