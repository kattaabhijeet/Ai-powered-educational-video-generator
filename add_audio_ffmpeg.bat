@echo off
echo ========================================
echo Adding Audio to Scenes with FFmpeg
echo ========================================
echo.

echo [1/4] Adding audio to Scene 1...
ffmpeg -i output\scene_1_video.mp4 -i output\how_dns_works_video_audio\scene_1_narration.mp3 -c:v copy -c:a aac -shortest -y output\scene_1_with_audio.mp4
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 1) else (echo [ERROR] Scene 1)

echo [2/4] Adding audio to Scene 2...
ffmpeg -i output\scene_2_video.mp4 -i output\how_dns_works_video_audio\scene_2_narration.mp3 -c:v copy -c:a aac -shortest -y output\scene_2_with_audio.mp4
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 2) else (echo [ERROR] Scene 2)

echo [3/4] Adding audio to Scene 3...
ffmpeg -i output\scene_3_video.mp4 -i output\how_dns_works_video_audio\scene_3_narration.mp3 -c:v copy -c:a aac -shortest -y output\scene_3_with_audio.mp4
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 3) else (echo [ERROR] Scene 3)

echo [4/4] Adding audio to Scene 4...
ffmpeg -i output\scene_4_video.mp4 -i output\how_dns_works_video_audio\scene_4_narration.mp3 -c:v copy -c:a aac -shortest -y output\scene_4_with_audio.mp4
if %ERRORLEVEL% EQU 0 (echo [OK] Scene 4) else (echo [ERROR] Scene 4)

echo.
echo ========================================
echo Creating concat file...
echo ========================================

(
echo file 'scene_1_with_audio.mp4'
echo file 'scene_2_with_audio.mp4'
echo file 'scene_3_with_audio.mp4'
echo file 'scene_4_with_audio.mp4'
) > output\concat_list.txt

echo.
echo ========================================
echo Combining all scenes into final video...
echo ========================================

cd output
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy -y how_dns_works_FINAL.mp4
cd ..

if exist "output\how_dns_works_FINAL.mp4" (
    echo.
    echo ========================================
    echo [DONE] Final video created!
    echo ========================================
    echo.
    echo Output: output\how_dns_works_FINAL.mp4
    echo.
    echo Playing video...
    start output\how_dns_works_FINAL.mp4
) else (
    echo.
    echo [ERROR] Final video not created
)

pause
