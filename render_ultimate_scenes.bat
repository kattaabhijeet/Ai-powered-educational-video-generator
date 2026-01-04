@echo off
echo ========================================
echo Render ULTIMATE Professional Scenes
echo ========================================
echo.
echo Style:
echo  - Dark gradient background
echo  - Subtle fills (opacity 0.18)
echo  - Inter font
echo  - Professional shadows
echo.

echo [1/4] Scene 1...
manim -ql --disable_caching output\manim_scene_1_ultimate.py UltimateScene
if %ERRORLEVEL% EQU 0 (echo [OK]) else (echo [SKIP])

echo [2/4] Scene 2...
manim -ql --disable_caching output\manim_scene_2_ultimate.py UltimateScene
if %ERRORLEVEL% EQU 0 (echo [OK]) else (echo [SKIP])

echo [3/4] Scene 3...
manim -ql --disable_caching output\manim_scene_3_ultimate.py UltimateScene
if %ERRORLEVEL% EQU 0 (echo [OK]) else (echo [SKIP])

echo [4/4] Scene 4...
manim -ql --disable_caching output\manim_scene_4_ultimate.py UltimateScene
if %ERRORLEVEL% EQU 0 (echo [OK]) else (echo [SKIP])

echo.
echo Copying...
copy "media\videos\manim_scene_1_ultimate\480p15\UltimateScene.mp4" "output\scene_1_ultimate.mp4"
copy "media\videos\manim_scene_2_ultimate\480p15\UltimateScene.mp4" "output\scene_2_ultimate.mp4"
copy "media\videos\manim_scene_3_ultimate\480p15\UltimateScene.mp4" "output\scene_3_ultimate.mp4"
copy "media\videos\manim_scene_4_ultimate\480p15\UltimateScene.mp4" "output\scene_4_ultimate.mp4"

echo.
echo ========================================
echo ULTIMATE scenes rendered!
echo ========================================
pause
