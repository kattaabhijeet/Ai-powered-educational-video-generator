@echo off
echo ========================================
echo Render ALL Enhanced Scenes
echo ========================================
echo.
echo Enhancements:
echo  - Rounded corners
echo  - Shadows for depth
echo  - Text inside boxes (no overlap)
echo  - Label backgrounds
echo  - Thicker arrows
echo.

echo [1/4] Rendering Scene 1...
manim -ql --disable_caching output\manim_scene_1_enhanced.py EnhancedScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 1) else (echo [ERROR] Scene 1)

echo [2/4] Rendering Scene 2...
manim -ql --disable_caching output\manim_scene_2_enhanced.py EnhancedScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 2) else (echo [ERROR] Scene 2)

echo [3/4] Rendering Scene 3...
manim -ql --disable_caching output\manim_scene_3_enhanced.py EnhancedScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 3) else (echo [ERROR] Scene 3)

echo [4/4] Rendering Scene 4...
manim -ql --disable_caching output\manim_scene_4_enhanced.py EnhancedScene
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 4) else (echo [ERROR] Scene 4)

echo.
echo ========================================
echo Copying enhanced scenes...
echo ========================================

copy "media\videos\manim_scene_1_enhanced\480p15\EnhancedScene.mp4" "output\scene_1_enhanced.mp4"
copy "media\videos\manim_scene_2_enhanced\480p15\EnhancedScene.mp4" "output\scene_2_enhanced.mp4"
copy "media\videos\manim_scene_3_enhanced\480p15\EnhancedScene.mp4" "output\scene_3_enhanced.mp4"
copy "media\videos\manim_scene_4_enhanced\480p15\EnhancedScene.mp4" "output\scene_4_enhanced.mp4"

echo.
echo ========================================
echo All enhanced scenes rendered!
echo ========================================
echo.
pause
