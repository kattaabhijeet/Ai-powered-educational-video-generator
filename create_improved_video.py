"""
IMPROVED: Fix audio sync by freezing last frame instead of looping.
This prevents the same animation from playing twice.
"""
import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips, ImageClip

print("="*70)
print("IMPROVED Audio Sync - Freeze Last Frame")
print("="*70)

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

print("\nProcessing scenes with freeze-frame extension...")
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
        
        print(f"  Scene {i}:")
        print(f"    Video duration: {video.duration:.2f}s")
        print(f"    Audio duration: {audio.duration:.2f}s")
        
        # If audio is longer, freeze the last frame
        if audio.duration > video.duration:
            # Get the last frame as an image
            last_frame = video.get_frame(video.duration - 0.1)
            
            # Create an image clip from the last frame
            freeze_duration = audio.duration - video.duration
            freeze_clip = ImageClip(last_frame, duration=freeze_duration)
            
            # Concatenate original video with frozen frame
            video_extended = concatenate_videoclips([video, freeze_clip])
            
            print(f"    Extended with frozen frame: +{freeze_duration:.2f}s")
            print(f"    Final duration: {video_extended.duration:.2f}s")
        else:
            # If video is longer or equal, just trim
            video_extended = video.subclipped(0, audio.duration)
            print(f"    Trimmed to: {video_extended.duration:.2f}s")
        
        # Set audio to extended video
        video_with_audio = video_extended.with_audio(audio)
        
        clips_with_audio.append(video_with_audio)
        print(f"    [OK] Scene {i} synced (no loop)")
        
    except Exception as e:
        print(f"    [ERROR] Scene {i} failed: {e}")
        import traceback
        traceback.print_exc()

if clips_with_audio:
    print(f"\nCombining {len(clips_with_audio)} scenes into final video...")
    
    # Concatenate all clips
    final_video = concatenate_videoclips(clips_with_audio, method="compose")
    
    # Write final video
    output_path = os.path.join(output_dir, "how_dns_works_IMPROVED.mp4")
    print(f"Writing improved video...")
    
    final_video.write_videofile(
        output_path,
        fps=30,
        codec='libx264',
        audio_codec='aac'
    )
    
    print("\n" + "="*70)
    print("[DONE] Improved video created!")
    print("="*70)
    print(f"\nOutput: {output_path}")
    print(f"Duration: {final_video.duration:.1f} seconds")
    print(f"Scenes: {len(clips_with_audio)}")
    print("\nIMPROVEMENTS:")
    print("  - No looping (last frame frozen instead)")
    print("  - Smooth transitions between scenes")
    print("  - Audio perfectly synced")
    
    # Clean up
    final_video.close()
    for clip in clips_with_audio:
        clip.close()
    
    print("\nPlaying improved video...")
    os.system(f'start {output_path}')
    
else:
    print("\n[ERROR] No scenes were successfully processed")
