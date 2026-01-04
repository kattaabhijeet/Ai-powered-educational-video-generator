@echo off
echo ========================================
echo Render BEST Scenes - Fixed Overlap + Better Animations
echo ========================================
echo.
echo Fixes:
echo  - NO Unicode arrows (plain text)
echo  - More spacing (buff=0.6)
echo  - Dynamic animations (GrowFromCenter)
echo  - Original content
echo.

echo [1/4] Rendering Scene 1...
manim -ql --disable_caching output\manim_scene_1_best.py BestScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 1) else (echo [ERROR] Scene 1)

echo [2/4] Rendering Scene 2...
manim -ql --disable_caching output\manim_scene_2_best.py BestScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 2) else (echo [ERROR] Scene 2)

echo [3/4] Rendering Scene 3...
manim -ql --disable_caching output\manim_scene_3_best.py BestScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 3) else (echo [ERROR] Scene 3)

echo [4/4] Rendering Scene 4...
manim -ql --disable_caching output\manim_scene_4_best.py BestScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 4) else (echo [ERROR] Scene 4)

echo.
echo ========================================
echo Copying scenes...
echo ========================================

copy "media\videos\manim_scene_1_best\480p15\BestScene.mp4" "output\scene_1_best.mp4"
copy "media\videos\manim_scene_2_best\480p15\BestScene.mp4" "output\scene_2_best.mp4"
copy "media\videos\manim_scene_3_best\480p15\BestScene.mp4" "output\scene_3_best.mp4"
copy "media\videos\manim_scene_4_best\480p15\BestScene.mp4" "output\scene_4_best.mp4"

echo.
echo ========================================
echo All BEST scenes rendered!
echo ========================================
echo.
pause
