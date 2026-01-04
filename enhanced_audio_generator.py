"""
Enhanced audio generator with natural human-like voices using Edge TTS.
Falls back to gTTS if Edge TTS is unavailable.
"""
import os
from pathlib import Path
from models_schemas import Script, Scene
from config import Config


class EnhancedAudioGenerator:
    """Generate natural-sounding narration audio using Edge TTS."""
    
    def __init__(self, voice="en-US-GuyNeural"):
        """
        Initialize audio generator.
        
        Args:
            voice: Edge TTS voice to use. Options:
                - en-US-GuyNeural (male, professional)
                - en-US-JennyNeural (female, friendly)
                - en-US-AriaNeural (female, news anchor)
                - en-US-DavisNeural (male, deep)
        """
        self.voice = voice
        
        # Try to import edge-tts
        try:
            import edge_tts
            self.use_edge_tts = True
            print(f"[OK] Using Edge TTS with voice: {voice}")
        except ImportError:
            self.use_edge_tts = False
            print("[WARN] Edge TTS not installed, falling back to gTTS")
            print("  Install with: pip install edge-tts")
    
    def generate_narration(self, script: Script, output_dir: str) -> list:
        """
        Generate narration audio for all scenes.
        
        Args:
            script: The video script
            output_dir: Directory to save audio files
            
        Returns:
            List of paths to generated audio files
        """
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        print(f"[MIC] Generating narration audio with {self.voice}...")
        
        audio_files = []
        
        for scene in script.scenes:
            output_file = os.path.join(output_dir, f"scene_{scene.scene_number}_narration.mp3")
            
            if self.use_edge_tts:
                self._generate_edge_tts(scene.narration, output_file)
            else:
                self._generate_gtts(scene.narration, output_file)
            
            audio_files.append(output_file)
            print(f"  [OK] Scene {scene.scene_number} audio saved")
        
        print(f"[OK] Generated {len(audio_files)} audio files")
        return audio_files
    
    def _generate_edge_tts(self, text: str, output_path: str):
        """Generate audio using Edge TTS (natural voice)."""
        import edge_tts
        import asyncio
        
        async def generate():
            communicate = edge_tts.Communicate(text, self.voice)
            await communicate.save(output_path)
        
        # Run async function
        try:
            asyncio.run(generate())
        except RuntimeError:
            # If event loop already running, create new one
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(generate())
            loop.close()
    
    def _generate_gtts(self, text: str, output_path: str):
        """Fallback to gTTS if Edge TTS unavailable."""
        from gtts import gTTS
        
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(output_path)


if __name__ == "__main__":
    # Test the enhanced audio generator
    from script_generator import ScriptGenerator
    
    print("Testing Enhanced Audio Generator...")
    print("="*70)
    
    # Generate a test script
    script_gen = ScriptGenerator()
    script = script_gen.generate("How DNS works")
    
    # Generate audio with Edge TTS
    audio_gen = EnhancedAudioGenerator(voice="en-US-GuyNeural")
    audio_files = audio_gen.generate_narration(script, "output/test_audio_edge")
    
    print("\n" + "="*70)
    print("[DONE] Test complete!")
    print(f"Audio files: {len(audio_files)}")
    print("\nListen to compare:")
    print(f"  Edge TTS: {audio_files[0]}")
    print("\nMuch more natural than gTTS!")
