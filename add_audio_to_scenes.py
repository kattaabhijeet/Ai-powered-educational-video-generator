"""
Add audio to rendered Manim scenes using moviepy.
Fixed import for moviepy 2.x
"""
import os

print("="*70)
print("Adding Audio to Scenes and Creating Final Video")
print("="*70)

try:
    # Try moviepy 2.x import
    from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips
except ImportError:
    try:
        # Try moviepy 1.x import
        from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
    except ImportError:
        print("\n[ERROR] moviepy not properly installed")
        print("Try: pip uninstall moviepy && pip install moviepy==1.0.3")
        exit(1)

output_dir = "output"
audio_dir = os.path.join(output_dir, "how_dns_works_video_audio")

# Scene information
scenes = [
    {"video": "scene_1_video.mp4", "audio": "scene_1_narration.mp3"},
    {"video": "scene_2_video.mp4", "audio": "scene_2_narration.mp3"},
    {"video": "scene_3_video.mp4", "audio": "scene_3_narration.mp3"},
    {"video": "scene_4_video.mp4", "audio": "scene_4_narration.mp3"},
]

clips_with_audio = []

print("\nProcessing scenes...")
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
        # Load video and audio
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        # Set audio to video
        video_with_audio = video.with_audio(audio)
        
        clips_with_audio.append(video_with_audio)
        print(f"[OK] Scene {i}: Video + Audio combined")
        
    except Exception as e:
        print(f"[ERROR] Scene {i} failed: {e}")

if clips_with_audio:
    print(f"\nCombining {len(clips_with_audio)} scenes into final video...")
    
    # Concatenate all clips
    final_video = concatenate_videoclips(clips_with_audio, method="compose")
    
    # Write final video
    output_path = os.path.join(output_dir, "how_dns_works_FINAL.mp4")
    print(f"Writing final video (this may take a minute)...")
    
    final_video.write_videofile(
        output_path,
        fps=30,
        codec='libx264',
        audio_codec='aac'
    )
    
    print("\n" + "="*70)
    print("[DONE] Final video created!")
    print("="*70)
    print(f"\nOutput: {output_path}")
    print(f"Duration: {final_video.duration:.1f} seconds")
    print(f"Scenes: {len(clips_with_audio)}")
    
    # Clean up
    final_video.close()
    for clip in clips_with_audio:
        clip.close()
    
    print("\nPlaying video...")
    os.system(f'start {output_path}')
    
else:
    print("\n[ERROR] No scenes were successfully processed")
    print("Make sure to run render_all_scenes.bat first!")
