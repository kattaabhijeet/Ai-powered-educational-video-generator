@echo off
echo ========================================
echo Render PERFECT Scenes - Colorful + Female AI Voice
echo ========================================
echo.
echo Features:
echo  - COLORFUL vibrant visuals
echo  - NO overlap (text scales to fit)
echo  - Dynamic animations
echo  - Female AI voice ready
echo.

echo [1/4] Scene 1...
manim -ql --disable_caching output\manim_scene_1_perfect.py PerfectScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 1) else (echo [SKIP] Scene 1)

echo [2/4] Scene 2...
manim -ql --disable_caching output\manim_scene_2_perfect.py PerfectScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 2) else (echo [SKIP] Scene 2)

echo [3/4] Scene 3...
manim -ql --disable_caching output\manim_scene_3_perfect.py PerfectScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 3) else (echo [SKIP] Scene 3)

echo [4/4] Scene 4...
manim -ql --disable_caching output\manim_scene_4_perfect.py PerfectScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 4) else (echo [SKIP] Scene 4)

echo.
echo Copying scenes...
copy "media\videos\manim_scene_1_perfect\480p15\PerfectScene.mp4" "output\scene_1_perfect.mp4"
copy "media\videos\manim_scene_2_perfect\480p15\PerfectScene.mp4" "output\scene_2_perfect.mp4"
copy "media\videos\manim_scene_3_perfect\480p15\PerfectScene.mp4" "output\scene_3_perfect.mp4"
copy "media\videos\manim_scene_4_perfect\480p15\PerfectScene.mp4" "output\scene_4_perfect.mp4"

echo.
echo ========================================
echo PERFECT scenes rendered!
echo ========================================
pause
