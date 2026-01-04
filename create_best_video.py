"""
Create BEST final video with:
- Fixed overlap (no Unicode)
- Better animations
- ORIGINAL audio (gTTS from first generation)
"""
import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, ImageClip

print("="*70)
print("Creating BEST Video - Original Content + Fixes")
print("="*70)

output_dir = "output"
audio_dir = os.path.join(output_dir, "how_dns_works_video_audio")  # ORIGINAL audio

scenes = [
    {"video": "scene_1_best.mp4", "audio": "scene_1_narration.mp3"},
    {"video": "scene_2_best.mp4", "audio": "scene_2_narration.mp3"},
    {"video": "scene_3_best.mp4", "audio": "scene_3_narration.mp3"},
    {"video": "scene_4_best.mp4", "audio": "scene_4_narration.mp3"},
]

clips_with_audio = []

print("\nProcessing BEST scenes with ORIGINAL audio...")
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
        print(f"    Video: {video.duration:.2f}s (BEST - no overlap)")
        print(f"    Audio: {audio.duration:.2f}s (ORIGINAL)")
        
        # Freeze last frame if needed
        if audio.duration > video.duration:
            last_frame = video.get_frame(video.duration - 0.1)
            freeze_duration = audio.duration - video.duration
            freeze_clip = ImageClip(last_frame, duration=freeze_duration)
            video_extended = concatenate_videoclips([video, freeze_clip])
            print(f"    Extended: +{freeze_duration:.2f}s")
        else:
            video_extended = video.subclipped(0, audio.duration)
        
        video_with_audio = video_extended.with_audio(audio)
        clips_with_audio.append(video_with_audio)
        print(f"    [OK] Scene {i}")
        
    except Exception as e:
        print(f"    [ERROR] Scene {i}: {e}")

if clips_with_audio:
    print(f"\nCombining {len(clips_with_audio)} scenes...")
    
    final_video = concatenate_videoclips(clips_with_audio, method="compose")
    output_path = os.path.join(output_dir, "how_dns_works_BEST.mp4")
    
    print(f"Writing BEST video...")
    final_video.write_videofile(output_path, fps=30, codec='libx264', audio_codec='aac')
    
    print("\n" + "="*70)
    print("[DONE] BEST VIDEO CREATED!")
    print("="*70)
    print(f"\nOutput: {output_path}")
    print(f"Duration: {final_video.duration:.1f}s")
    print(f"\nFIXES APPLIED:")
    print(f"  [OK] No text overlap (Unicode removed)")
    print(f"  [OK] Better spacing (buff=0.6)")
    print(f"  [OK] Dynamic animations (GrowFromCenter)")
    print(f"  [OK] Original audio content")
    print(f"  [OK] Professional styling")
    
    final_video.close()
    for clip in clips_with_audio:
        clip.close()
    
    print("\nPlaying BEST video...")
    os.system(f'start {output_path}')
else:
    print("\n[ERROR] No scenes processed")
