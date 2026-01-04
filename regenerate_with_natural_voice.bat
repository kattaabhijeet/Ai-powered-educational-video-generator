@echo off
echo ========================================
echo Regenerate Video with Natural Voice
echo ========================================
echo.
echo This will create a new video with:
echo  - Natural human-like voice (Edge TTS)
echo  - Same animations
echo  - Better audio quality
echo.

echo Step 1: Generate script and blueprint...
python -c "from enhanced_pipeline import EnhancedVideoPipeline; p = EnhancedVideoPipeline(voice='en-US-GuyNeural'); import json; from pathlib import Path; script_path = Path('output/how_dns_works_video_script.json'); bp_path = Path('output/how_dns_works_video_blueprint.json'); from models_schemas import Script, VideoBlueprint; script = Script(**json.load(open(script_path))); blueprint = VideoBlueprint(**json.load(open(bp_path))); audio_files = p.audio_gen.generate_narration(script, 'output/how_dns_works_video_audio_natural'); print(f'Generated {len(audio_files)} natural voice audio files')"

echo.
echo Step 2: Rendering scenes with Manim...
call render_all_scenes.bat

echo.
echo Step 3: Combining with natural voice audio...
python create_natural_voice_video.py

pause
