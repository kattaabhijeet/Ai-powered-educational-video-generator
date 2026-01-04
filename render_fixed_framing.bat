@echo off
echo ========================================
echo Rendering Scenes with FIXED Framing
echo ========================================
echo.
echo This will prevent cropped/cut-off elements
echo.

python -c "from fixed_manim_generator import FixedManimVideoGenerator; from models_schemas import VideoBlueprint; import json; bp = VideoBlueprint(**json.load(open('output/how_dns_works_video_blueprint.json'))); FixedManimVideoGenerator().generate(bp, 'output/fixed.mp4')"

echo.
echo ========================================
echo Scenes rendered with proper framing!
echo ========================================
echo.
echo Now combining with audio...
python create_improved_video_fixed.py

pause
