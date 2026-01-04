@echo off
echo ========================================
echo Rendering All Scenes with Manim
echo ========================================
echo.

echo [1/4] Rendering Scene 1...
manim -ql --disable_caching output\manim_scene_1.py DynamicScene
if %ERRORLEVEL% EQU 0 (
    echo [OK] Scene 1 rendered
) else (
    echo [ERROR] Scene 1 failed
)
echo.

echo [2/4] Rendering Scene 2...
manim -ql --disable_caching output\manim_scene_2.py DynamicScene
if %ERRORLEVEL% EQU 0 (
    echo [OK] Scene 2 rendered
) else (
    echo [ERROR] Scene 2 failed
)
echo.

echo [3/4] Rendering Scene 3...
manim -ql --disable_caching output\manim_scene_3.py DynamicScene
if %ERRORLEVEL% EQU 0 (
    echo [OK] Scene 3 rendered
) else (
    echo [ERROR] Scene 3 failed
)
echo.

echo [4/4] Rendering Scene 4...
manim -ql --disable_caching output\manim_scene_4.py DynamicScene
if %ERRORLEVEL% EQU 0 (
    echo [OK] Scene 4 rendered
) else (
    echo [ERROR] Scene 4 failed
)
echo.

echo ========================================
echo Copying rendered scenes to output folder...
echo ========================================

copy "media\videos\manim_scene_1\480p15\DynamicScene.mp4" "output\scene_1_video.mp4"
copy "media\videos\manim_scene_2\480p15\DynamicScene.mp4" "output\scene_2_video.mp4"
copy "media\videos\manim_scene_3\480p15\DynamicScene.mp4" "output\scene_3_video.mp4"
copy "media\videos\manim_scene_4\480p15\DynamicScene.mp4" "output\scene_4_video.mp4"

echo.
echo ========================================
echo All scenes rendered!
echo ========================================
echo.
echo Now run: python add_audio_to_scenes.py
echo.
pause
