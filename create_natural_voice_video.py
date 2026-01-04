"""
Create final video with natural voice audio.
"""
import os
import json
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, ImageClip
from models_schemas import Script

print("="*70)
print("Creating Video with NATURAL VOICE")
print("="*70)

output_dir = "output"

# Load script to get scene info
with open(os.path.join(output_dir, "how_dns_works_video_script.json"), "r") as f:
    script_data = json.load(f)

script = Script(**script_data)

# Audio directory with natural voices
audio_dir = os.path.join(output_dir, "how_dns_works_video_audio_natural")

# Check if natural voice audio exists
if not os.path.exists(audio_dir):
    print(f"\n[ERROR] Natural voice audio not found!")
    print(f"  Expected: {audio_dir}")
    print(f"\n  Run this first:")
    print(f"  python enhanced_audio_generator.py")
    exit(1)

scenes = [
    {"video": "scene_1_video.mp4", "audio": "scene_1_narration.mp3"},
    {"video": "scene_2_video.mp4", "audio": "scene_2_narration.mp3"},
    {"video": "scene_3_video.mp4", "audio": "scene_3_narration.mp3"},
    {"video": "scene_4_video.mp4", "audio": "scene_4_narration.mp3"},
]

clips_with_audio = []

print("\nProcessing scenes with natural voice...")
for i, scene in enumerate(scenes, 1):
    video_path = os.path.join(output_dir, scene["video"])
    audio_path = os.path.join(audio_dir, scene["audio"])
    
    if not os.path.exists(video_path):
        print(f"[WARN] Scene {i} video not found: {video_path}")
        continue
    
    if not os.path.exists(audio_path):
        print(f"[WARN] Scene {i} audio not found: {audio_path}")
        continue
    
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        print(f"  Scene {i}:")
        print(f"    Video: {video.duration:.2f}s")
        print(f"    Audio: {audio.duration:.2f}s (Natural voice)")
        
        # Freeze last frame if needed
        if audio.duration > video.duration:
            last_frame = video.get_frame(video.duration - 0.1)
            freeze_duration = audio.duration - video.duration
            freeze_clip = ImageClip(last_frame, duration=freeze_duration)
            video_extended = concatenate_videoclips([video, freeze_clip])
            print(f"    Extended: +{freeze_duration:.2f}s (freeze frame)")
        else:
            video_extended = video.subclipped(0, audio.duration)
        
        video_with_audio = video_extended.with_audio(audio)
        clips_with_audio.append(video_with_audio)
        print(f"    [OK] Scene {i} synced")
        
    except Exception as e:
        print(f"    [ERROR] Scene {i}: {e}")

if clips_with_audio:
    print(f"\nCombining {len(clips_with_audio)} scenes...")
    
    final_video = concatenate_videoclips(clips_with_audio, method="compose")
    output_path = os.path.join(output_dir, "how_dns_works_NATURAL_VOICE.mp4")
    
    print(f"Writing final video...")
    final_video.write_videofile(output_path, fps=30, codec='libx264', audio_codec='aac')
    
    print("\n" + "="*70)
    print("[DONE] Natural Voice Video Created!")
    print("="*70)
    print(f"\nOutput: {output_path}")
    print(f"Duration: {final_video.duration:.1f}s")
    print(f"\nIMPROVEMENTS:")
    print(f"  - Natural human-like voice (Edge TTS)")
    print(f"  - Professional narration quality")
    print(f"  - No robotic sound")
    
    final_video.close()
    for clip in clips_with_audio:
        clip.close()
    
    print("\nPlaying video...")
    os.system(f'start {output_path}')
else:
    print("\n[ERROR] No scenes processed")
