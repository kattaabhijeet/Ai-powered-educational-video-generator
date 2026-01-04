"""
Fix audio sync by adjusting video duration to match audio length.
"""
import os
from moviepy import VideoFileClip, AudioFileClip, concatenate_videoclips

print("="*70)
print("Fixing Audio Sync - Adjusting Video Duration")
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

print("\nProcessing scenes with duration adjustment...")
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
        
        # If audio is longer, loop the video to match audio duration
        if audio.duration > video.duration:
            # Calculate how many times to loop
            loops_needed = int(audio.duration / video.duration) + 1
            
            # Create looped video
            video_looped = concatenate_videoclips([video] * loops_needed)
            
            # Trim to exact audio duration
            video_adjusted = video_looped.subclipped(0, audio.duration)
            
            print(f"    Adjusted to: {video_adjusted.duration:.2f}s (looped)")
        else:
            # If video is longer or equal, just trim to audio duration
            video_adjusted = video.subclipped(0, audio.duration)
            print(f"    Adjusted to: {video_adjusted.duration:.2f}s (trimmed)")
        
        # Set audio to adjusted video
        video_with_audio = video_adjusted.with_audio(audio)
        
        clips_with_audio.append(video_with_audio)
        print(f"    [OK] Scene {i} synced")
        
    except Exception as e:
        print(f"    [ERROR] Scene {i} failed: {e}")
        import traceback
        traceback.print_exc()

if clips_with_audio:
    print(f"\nCombining {len(clips_with_audio)} scenes into final video...")
    
    # Concatenate all clips
    final_video = concatenate_videoclips(clips_with_audio, method="compose")
    
    # Write final video
    output_path = os.path.join(output_dir, "how_dns_works_FINAL_SYNCED.mp4")
    print(f"Writing final video...")
    
    final_video.write_videofile(
        output_path,
        fps=30,
        codec='libx264',
        audio_codec='aac'
    )
    
    print("\n" + "="*70)
    print("[DONE] Synced video created!")
    print("="*70)
    print(f"\nOutput: {output_path}")
    print(f"Duration: {final_video.duration:.1f} seconds")
    print(f"Scenes: {len(clips_with_audio)}")
    
    # Clean up
    final_video.close()
    for clip in clips_with_audio:
        clip.close()
    
    print("\nPlaying synced video...")
    os.system(f'start {output_path}')
    
else:
    print("\n[ERROR] No scenes were successfully processed")
