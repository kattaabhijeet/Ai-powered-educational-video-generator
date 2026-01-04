"""
Updated pipeline using enhanced audio generator with natural voices.
"""
import os
import json
from pathlib import Path
from script_generator import ScriptGenerator
from blueprint_generator import BlueprintGenerator
from simple_video_generator import SimpleVideoGenerator
from enhanced_audio_generator import EnhancedAudioGenerator  # NEW!
from config import Config


class EnhancedVideoPipeline:
    """Pipeline with natural voice audio."""
    
    def __init__(self, voice="en-US-GuyNeural"):
        """
        Initialize pipeline.
        
        Args:
            voice: Edge TTS voice. Options:
                - en-US-GuyNeural (male, professional) - DEFAULT
                - en-US-JennyNeural (female, friendly)
                - en-US-AriaNeural (female, news anchor)
                - en-US-DavisNeural (male, deep, authoritative)
        """
        self.script_gen = ScriptGenerator()
        self.blueprint_gen = BlueprintGenerator()
        self.video_gen = SimpleVideoGenerator()
        self.audio_gen = EnhancedAudioGenerator(voice=voice)  # Natural voice!
        
        Path(Config.OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    
    def generate_video(self, topic: str, output_filename: str = None) -> dict:
        """Generate complete video with natural voice."""
        print("="*70)
        print(f"[>>] VIDEO GENERATION WITH NATURAL VOICE")
        print(f"[NOTE] Topic: {topic}")
        print("="*70)
        
        safe_topic = topic.lower().replace(" ", "_").replace("/", "_")
        if not output_filename:
            output_filename = f"{safe_topic}_video"
        
        # Step 1: Generate Script
        print("\n" + "-"*70)
        print("STEP 1: SCRIPT GENERATION")
        print("-"*70)
        script = self.script_gen.generate(topic)
        script_path = os.path.join(Config.OUTPUT_DIR, f"{output_filename}_script.json")
        self.script_gen.save_script(script, script_path)
        
        # Step 2: Generate Blueprint
        print("\n" + "-"*70)
        print("STEP 2: ANIMATION BLUEPRINT GENERATION")
        print("-"*70)
        blueprint = self.blueprint_gen.generate(script)
        blueprint_path = os.path.join(Config.OUTPUT_DIR, f"{output_filename}_blueprint.json")
        self.blueprint_gen.save_blueprint(blueprint, blueprint_path)
        
        # Step 3: Generate Audio with NATURAL VOICE
        print("\n" + "-"*70)
        print("STEP 3: NATURAL VOICE NARRATION")
        print("-"*70)
        audio_dir = os.path.join(Config.OUTPUT_DIR, f"{output_filename}_audio_natural")
        audio_files = self.audio_gen.generate_narration(script, audio_dir)
        
        # Step 4: Generate Video
        print("\n" + "-"*70)
        print("STEP 4: VIDEO ANIMATION GENERATION")
        print("-"*70)
        video_path = os.path.join(Config.OUTPUT_DIR, f"{output_filename}.mp4")
        scene_files = self.video_gen.generate(blueprint, video_path)
        
        # Summary
        print("\n" + "="*70)
        print("[DONE] VIDEO GENERATION COMPLETE!")
        print("="*70)
        
        results = {
            "topic": topic,
            "script": script_path,
            "blueprint": blueprint_path,
            "audio_files": audio_files,
            "video": video_path,
            "scene_files": scene_files,
            "voice_used": self.audio_gen.voice
        }
        
        results_path = os.path.join(Config.OUTPUT_DIR, f"{output_filename}_results.json")
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n[STATS] Results Summary:")
        print(f"  Script: {script_path}")
        print(f"  Blueprint: {blueprint_path}")
        print(f"  Audio files: {len(audio_files)} (Natural voice: {self.audio_gen.voice})")
        print(f"  Video: {video_path}")
        print(f"  Full results: {results_path}")
        
        return results


if __name__ == "__main__":
    # Test with natural voice
    pipeline = EnhancedVideoPipeline(voice="en-US-GuyNeural")
    results = pipeline.generate_video("How DNS works")
    
    print("\n[DONE] Check the audio - much more natural!")
