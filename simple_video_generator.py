"""
Simple video generator using PIL for images and moviepy for video composition.
This creates actual MP4 files without requiring Manim.
"""
import os
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from models_schemas import VideoBlueprint, SceneBlueprint, AnimationElement
from config import Config


class SimpleVideoGenerator:
    """Generates MP4 videos using PIL and moviepy."""
    
    def __init__(self):
        """Initialize the simple video generator."""
        self.output_dir = Config.OUTPUT_DIR
        self.width = 1920
        self.height = 1080
        self.fps = 30
    
    def generate(self, blueprint: VideoBlueprint, output_path: str):
        """
        Generate a video from a blueprint.
        
        Args:
            blueprint: The animation blueprint
            output_path: Path to save the final video
        """
        print(f"[VIDEO] Generating video for: {blueprint.topic}")
        print(f"  Total scenes: {len(blueprint.scene_blueprints)}")
        print(f"  Using simple image-based renderer")
        
        scene_files = []
        
        # Generate each scene as an image
        for scene_bp in blueprint.scene_blueprints:
            print(f"  Creating scene {scene_bp.scene_number}...")
            try:
                scene_file = self.render_scene_image(scene_bp)
                if scene_file and os.path.exists(scene_file):
                    scene_files.append(scene_file)
                    print(f"    [OK] Scene {scene_bp.scene_number} image created")
            except Exception as e:
                print(f"    [X] Error creating scene {scene_bp.scene_number}: {e}")
        
        # Combine scenes with audio using moviepy
        if scene_files:
            print(f"\n  Composing final video...")
            try:
                self.compose_video(blueprint, scene_files, output_path)
                print(f"[OK] Video generation complete")
                print(f"  Output: {output_path}")
            except Exception as e:
                print(f"[X] Error composing video: {e}")
                print(f"  Scene images saved in: {self.output_dir}")
        
        return scene_files
    
    def render_scene_image(self, scene_bp: SceneBlueprint) -> str:
        """Render a single scene as a static image."""
        # Create image with dark background
        bg_color = self._hex_to_rgb(scene_bp.background_color)
        img = Image.new('RGB', (self.width, self.height), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to load a font, fallback to default
        try:
            font_large = ImageFont.truetype("arial.ttf", 48)
            font_medium = ImageFont.truetype("arial.ttf", 32)
            font_small = ImageFont.truetype("arial.ttf", 24)
        except:
            font_large = ImageFont.load_default()
            font_medium = ImageFont.load_default()
            font_small = ImageFont.load_default()
        
        # Center point
        cx, cy = self.width // 2, self.height // 2
        
        # Draw elements
        for elem in scene_bp.elements:
            self._draw_element(draw, elem, cx, cy, font_medium, font_small)
        
        # Save image
        output_file = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}.png")
        img.save(output_file)
        
        return output_file
    
    def _draw_element(self, draw, elem: AnimationElement, cx, cy, font_medium, font_small):
        """Draw a single element on the image."""
        color = self._hex_to_rgb(elem.color)
        
        # Convert coordinates (Manim uses center origin, PIL uses top-left)
        # Manim: x in [-7, 7], y in [-4, 4]
        # Scale to pixels
        scale_x = self.width / 14
        scale_y = self.height / 8
        
        if elem.element_type == "rectangle":
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            w = elem.size.get("width", 2)
            h = elem.size.get("height", 1.5)
            
            # Convert to pixel coordinates
            px = cx + (x * scale_x)
            py = cy - (y * scale_y)  # Flip Y
            pw = w * scale_x
            ph = h * scale_y
            
            # Draw rectangle
            left = px - pw/2
            top = py - ph/2
            right = px + pw/2
            bottom = py + ph/2
            
            draw.rectangle([left, top, right, bottom], outline=color, width=5)
            
            # Draw label ABOVE the rectangle (anti-overlap rule)
            if elem.label:
                bbox = draw.textbbox((0, 0), elem.label, font=font_medium)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
                
                # Scale text to 70% of rectangle width if too wide
                max_width = pw * 0.7
                if text_w > max_width:
                    scale_factor = max_width / text_w
                    # Use smaller font
                    font_label = font_small
                    bbox = draw.textbbox((0, 0), elem.label, font=font_label)
                    text_w = bbox[2] - bbox[0]
                    text_h = bbox[3] - bbox[1]
                else:
                    font_label = font_medium
                
                # Position label ABOVE the rectangle (y - height/2 - spacing)
                label_x = px - text_w/2
                label_y = top - text_h - 15  # 15px spacing above rectangle
                draw.text((label_x, label_y), elem.label, fill=(255, 255, 255), font=font_label)
        
        elif elem.element_type == "circle":
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            r = elem.size.get("radius", 0.5)
            
            px = cx + (x * scale_x)
            py = cy - (y * scale_y)
            pr = r * scale_x
            
            # Draw circle
            draw.ellipse([px-pr, py-pr, px+pr, py+pr], outline=color, width=5)
            
            # Draw label
            if elem.label:
                bbox = draw.textbbox((0, 0), elem.label, font=font_small)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
                draw.text((px - text_w/2, py - text_h/2), elem.label, fill=(255, 255, 255), font=font_small)
        
        elif elem.element_type == "arrow":
            x_start = elem.position.get("x_start", -2)
            y_start = elem.position.get("y_start", 0)
            x_end = elem.position.get("x_end", 2)
            y_end = elem.position.get("y_end", 0)
            
            px1 = cx + (x_start * scale_x)
            py1 = cy - (y_start * scale_y)
            px2 = cx + (x_end * scale_x)
            py2 = cy - (y_end * scale_y)
            
            # Draw line
            draw.line([px1, py1, px2, py2], fill=color, width=5)
            
            # Draw arrowhead (simple triangle)
            import math
            angle = math.atan2(py2 - py1, px2 - px1)
            arrow_size = 20
            
            p1 = (px2, py2)
            p2 = (px2 - arrow_size * math.cos(angle - math.pi/6),
                  py2 - arrow_size * math.sin(angle - math.pi/6))
            p3 = (px2 - arrow_size * math.cos(angle + math.pi/6),
                  py2 - arrow_size * math.sin(angle + math.pi/6))
            
            draw.polygon([p1, p2, p3], fill=color)
            
            # Draw label FAR ABOVE the arrow (anti-overlap rule)
            if elem.label:
                mid_x = (px1 + px2) / 2
                mid_y = (py1 + py2) / 2 - 60  # Increased from 30 to 60 for better spacing
                bbox = draw.textbbox((0, 0), elem.label, font=font_small)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
                
                # Add background for better visibility
                padding = 5
                bg_left = mid_x - text_w/2 - padding
                bg_top = mid_y - padding
                bg_right = mid_x + text_w/2 + padding
                bg_bottom = mid_y + text_h + padding
                draw.rectangle([bg_left, bg_top, bg_right, bg_bottom], 
                             fill=(15, 23, 42),  # Dark background matching #0F172A
                             outline=(255, 255, 255), 
                             width=1)
                
                draw.text((mid_x - text_w/2, mid_y), elem.label, fill=(255, 255, 255), font=font_small)
        
        elif elem.element_type == "text":
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            px = cx + (x * scale_x)
            py = cy - (y * scale_y)
            
            if elem.label:
                bbox = draw.textbbox((0, 0), elem.label, font=font_medium)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]
                draw.text((px - text_w/2, py - text_h/2), elem.label, fill=color, font=font_medium)
    
    def compose_video(self, blueprint: VideoBlueprint, scene_images: list, output_path: str):
        """Compose final video from scene images and audio."""
        try:
            try:
                from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
            except ImportError:
                from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip
                
            clips = []
            audio_dir = os.path.join(self.output_dir, f"{blueprint.topic.lower().replace(' ', '_')}_video_audio")
            
            for i, (scene_bp, img_path) in enumerate(zip(blueprint.scene_blueprints, scene_images)):
                # Add audio if available and set duration based on audio length
                audio_path = os.path.join(audio_dir, f"scene_{scene_bp.scene_number}_narration.mp3")
                
                if os.path.exists(audio_path):
                    # Load audio first to get its duration
                    audio = AudioFileClip(audio_path)
                    audio_duration = audio.duration
                    
                    # Create image clip with audio duration to prevent overlap
                    img_clip = ImageClip(img_path, duration=audio_duration)
                    
                    # Support both MoviePy v1 (set_audio) and v2 (with_audio)
                    try:
                        img_clip = img_clip.with_audio(audio)
                    except AttributeError:
                        img_clip = img_clip.set_audio(audio)
                else:
                    # No audio, use blueprint duration
                    img_clip = ImageClip(img_path, duration=scene_bp.duration)
                
                clips.append(img_clip)
            
            # Concatenate all clips
            final_clip = concatenate_videoclips(clips, method="compose")
            
            # Write video file
            final_clip.write_videofile(
                output_path,
                fps=self.fps,
                codec='libx264',
                audio_codec='aac',
                temp_audiofile='temp-audio.m4a',
                remove_temp=True,
                logger=None  # Suppress moviepy output
            )
            
            # Clean up
            final_clip.close()
            for clip in clips:
                clip.close()
            
        except ImportError:
            print("[ERROR] moviepy not installed. Install with: pip install moviepy")
            print("  Scene images have been saved and can be used manually.")
        except Exception as e:
            print(f"[ERROR] Video composition failed: {e}")
            print("  Scene images have been saved in the output directory.")
    
    def _hex_to_rgb(self, hex_color: str) -> tuple:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


if __name__ == "__main__":
    # Test the simple video generator
    from script_generator import ScriptGenerator
    from blueprint_generator import BlueprintGenerator
    
    # Generate script and blueprint
    script_gen = ScriptGenerator()
    script = script_gen.generate("How DNS works")
    
    blueprint_gen = BlueprintGenerator()
    blueprint = blueprint_gen.generate(script)
    
    # Generate video
    video_gen = SimpleVideoGenerator()
    video_gen.generate(blueprint, "output/dns_video_simple.mp4")
