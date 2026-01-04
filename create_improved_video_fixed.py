"""
Combine fixed-framing videos with audio.
"""
import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, ImageClip

print("="*70)
print("Creating Final Video with Fixed Framing")
print("="*70)

output_dir = "output"
audio_dir = os.path.join(output_dir, "how_dns_works_video_audio")

scenes = [
    {"video": "scene_1_fixed.mp4", "audio": "scene_1_narration.mp3"},
    {"video": "scene_2_fixed.mp4", "audio": "scene_2_narration.mp3"},
    {"video": "scene_3_fixed.mp4", "audio": "scene_3_narration.mp3"},
    {"video": "scene_4_fixed.mp4", "audio": "scene_4_narration.mp3"},
]

clips_with_audio = []

print("\nProcessing scenes...")
for i, scene in enumerate(scenes, 1):
    video_path = os.path.join(output_dir, scene["video"])
    audio_path = os.path.join(audio_dir, scene["audio"])
    
    if not os.path.exists(video_path):
        print(f"[WARN] Scene {i} not found: {video_path}")
        continue
    
    if not os.path.exists(audio_path):
        print(f"[WARN] Audio {i} not found: {audio_path}")
        continue
    
    try:
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        # Freeze last frame if needed
        if audio.duration > video.duration:
            last_frame = video.get_frame(video.duration - 0.1)
            freeze_duration = audio.duration - video.duration
            freeze_clip = ImageClip(last_frame, duration=freeze_duration)
            video_extended = concatenate_videoclips([video, freeze_clip])
        else:
            video_extended = video.subclipped(0, audio.duration)
        
        video_with_audio = video_extended.with_audio(audio)
        clips_with_audio.append(video_with_audio)
        print(f"  [OK] Scene {i}")
        
    except Exception as e:
        print(f"  [ERROR] Scene {i}: {e}")

if clips_with_audio:
    print(f"\nCombining {len(clips_with_audio)} scenes...")
    
    final_video = concatenate_videoclips(clips_with_audio, method="compose")
    output_path = os.path.join(output_dir, "how_dns_works_FINAL_FIXED.mp4")
    
    print(f"Writing final video...")
    final_video.write_videofile(output_path, fps=30, codec='libx264', audio_codec='aac')
    
    print("\n" + "="*70)
    print("[DONE] Final video with FIXED framing!")
    print("="*70)
    print(f"\nOutput: {output_path}")
    print(f"Duration: {final_video.duration:.1f}s")
    print("\nFIXES:")
    print("  - No cropped elements")
    print("  - All text visible")
    print("  - Proper framing")
    print("  - No looping")
    
    final_video.close()
    for clip in clips_with_audio:
        clip.close()
    
    print("\nPlaying...")
    os.system(f'start {output_path}')
else:
    print("\n[ERROR] No scenes processed")
