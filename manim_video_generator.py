"""
Manim-based video generator that creates actual animated videos.
This uses Manim Community Edition to render professional animations.
"""
import os
import json
import subprocess
from pathlib import Path
from models_schemas import VideoBlueprint, SceneBlueprint, AnimationElement
from config import Config


class ManimVideoGenerator:
    """Generates animated MP4 videos using Manim."""
    
    def __init__(self):
        """Initialize the Manim video generator."""
        self.output_dir = Config.OUTPUT_DIR
    
    def generate(self, blueprint: VideoBlueprint, output_path: str):
        """
        Generate an animated video from a blueprint.
        
        Args:
            blueprint: The animation blueprint
            output_path: Path to save the final video
        """
        print(f"[VIDEO] Generating animated video for: {blueprint.topic}")
        print(f"  Total scenes: {len(blueprint.scene_blueprints)}")
        print(f"  Using Manim for professional animations")
        
        scene_files = []
        
        # Generate each scene with Manim
        for scene_bp in blueprint.scene_blueprints:
            print(f"\n  Rendering scene {scene_bp.scene_number} with Manim...")
            try:
                scene_file = self.render_manim_scene(scene_bp, blueprint.topic)
                if scene_file and os.path.exists(scene_file):
                    scene_files.append(scene_file)
                    print(f"    [OK] Scene {scene_bp.scene_number} rendered: {scene_file}")
                else:
                    print(f"    [WARN] Scene {scene_bp.scene_number} file not found")
            except Exception as e:
                print(f"    [X] Error rendering scene {scene_bp.scene_number}: {e}")
        
        if scene_files:
            print(f"\n[OK] Manim rendering complete")
            print(f"  Rendered {len(scene_files)} scenes")
            
            # Combine scenes if we have multiple
            if len(scene_files) > 1:
                print(f"\n  Combining scenes into final video...")
                self.combine_scenes(scene_files, output_path)
            elif len(scene_files) == 1:
                # Just copy the single scene
                import shutil
                shutil.copy(scene_files[0], output_path)
                print(f"  Output: {output_path}")
        
        return scene_files
    
    def render_manim_scene(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Render a single scene using Manim CLI."""
        # Generate Manim Python code
        scene_code = self._generate_manim_code(scene_bp, topic)
        
        # Write to temporary file
        temp_file = os.path.join(self.output_dir, f"manim_scene_{scene_bp.scene_number}.py")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(scene_code)
        
        print(f"    Generated Manim code: {temp_file}")
        
        # Run Manim command
        try:
            cmd = [
                "manim",
                "-ql",  # Low quality for faster rendering (use -qh for high quality)
                "--disable_caching",
                "--format=mp4",
                temp_file,
                "DynamicScene"
            ]
            
            print(f"    Running Manim (this may take 30-60 seconds)...")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.output_dir,
                timeout=120  # 2 minute timeout
            )
            
            if result.returncode != 0:
                print(f"    Manim error: {result.stderr}")
                return None
            
            # Find the rendered video file
            # Manim outputs to media/videos/<filename>/480p15/DynamicScene.mp4
            media_base = os.path.join(self.output_dir, "media", "videos", f"manim_scene_{scene_bp.scene_number}", "480p15")
            
            if os.path.exists(media_base):
                for file in os.listdir(media_base):
                    if file.endswith(".mp4"):
                        src = os.path.join(media_base, file)
                        dst = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}.mp4")
                        import shutil
                        shutil.copy(src, dst)
                        return dst
            
            print(f"    Could not find rendered file in {media_base}")
            return None
            
        except subprocess.TimeoutExpired:
            print(f"    Manim rendering timed out")
            return None
        except FileNotFoundError:
            print(f"    Manim not found. Install with: pip install manim")
            return None
        except Exception as e:
            print(f"    Manim error: {e}")
            return None
    
    def _generate_manim_code(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Generate Manim Python code for a scene."""
        code = '''from manim import *

class DynamicScene(Scene):
    def construct(self):
'''
        
        # Set background
        code += f'        self.camera.background_color = "{scene_bp.background_color}"\n\n'
        
        # Create all elements first
        for i, elem in enumerate(scene_bp.elements):
            elem_code = self._generate_element_code(elem, i)
            if elem_code:
                code += elem_code
        
        # Sort elements by timing and animate
        code += '\n        # Animate elements by timing\n'
        code += '        animations = [\n'
        
        for i, elem in enumerate(scene_bp.elements):
            anim_type = elem.animation or "FadeIn"
            timing = elem.timing
            code += f'            (elem_{i}, "{anim_type}", {timing}),\n'
        
        code += '        ]\n\n'
        code += '        animations.sort(key=lambda x: x[2])\n\n'
        code += '        current_time = 0\n'
        code += '        for mob, anim_type, timing in animations:\n'
        code += '            if mob is None:\n'
        code += '                continue\n\n'
        code += '            # Wait if needed\n'
        code += '            if timing > current_time:\n'
        code += '                self.wait(timing - current_time)\n'
        code += '                current_time = timing\n\n'
        code += '            # Apply animation\n'
        code += '            try:\n'
        code += '                if anim_type == "FadeIn":\n'
        code += '                    self.play(FadeIn(mob), run_time=0.5)\n'
        code += '                    current_time += 0.5\n'
        code += '                elif anim_type == "Write":\n'
        code += '                    self.play(Write(mob), run_time=0.8)\n'
        code += '                    current_time += 0.8\n'
        code += '                elif anim_type == "Create":\n'
        code += '                    self.play(Create(mob), run_time=0.6)\n'
        code += '                    current_time += 0.6\n'
        code += '                elif anim_type == "GrowFromCenter":\n'
        code += '                    self.play(GrowFromCenter(mob), run_time=0.5)\n'
        code += '                    current_time += 0.5\n'
        code += '                else:\n'
        code += '                    self.play(FadeIn(mob), run_time=0.5)\n'
        code += '                    current_time += 0.5\n'
        code += '            except Exception as e:\n'
        code += '                print(f"Animation error: {e}")\n\n'
        
        # Hold final frame
        code += f'        # Hold final frame\n'
        code += f'        remaining = {scene_bp.duration} - current_time\n'
        code += f'        if remaining > 0:\n'
        code += f'            self.wait(remaining)\n'
        
        return code
    
    def _generate_element_code(self, elem: AnimationElement, index: int) -> str:
        """Generate Manim code for a single element."""
        code = ""
        
        if elem.element_type == "rectangle":
            w = elem.size.get("width", 2)
            h = elem.size.get("height", 1.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            code += f'        rect_{index} = Rectangle(width={w}, height={h}, color="{elem.color}", fill_opacity=0.2, stroke_width=3)\n'
            code += f'        rect_{index}.move_to([{x}, {y}, 0])\n'
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                code += f'        label_{index} = Text("{label_text}", font_size=24, color=WHITE)\n'
                code += f'        label_{index}.move_to(rect_{index})\n'
                code += f'        elem_{index} = VGroup(rect_{index}, label_{index})\n\n'
            else:
                code += f'        elem_{index} = rect_{index}\n\n'
        
        elif elem.element_type == "circle":
            r = elem.size.get("radius", 0.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            code += f'        circle_{index} = Circle(radius={r}, color="{elem.color}", fill_opacity=0.3, stroke_width=3)\n'
            code += f'        circle_{index}.move_to([{x}, {y}, 0])\n'
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                code += f'        label_{index} = Text("{label_text}", font_size=18, color=WHITE)\n'
                code += f'        label_{index}.move_to(circle_{index})\n'
                code += f'        elem_{index} = VGroup(circle_{index}, label_{index})\n\n'
            else:
                code += f'        elem_{index} = circle_{index}\n\n'
        
        elif elem.element_type == "arrow":
            x_start = elem.position.get("x_start", -2)
            y_start = elem.position.get("y_start", 0)
            x_end = elem.position.get("x_end", 2)
            y_end = elem.position.get("y_end", 0)
            
            code += f'        arrow_{index} = Arrow(start=[{x_start}, {y_start}, 0], end=[{x_end}, {y_end}, 0], color="{elem.color}", stroke_width=4, buff=0.1)\n'
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                code += f'        label_{index} = Text("{label_text}", font_size=20, color=WHITE)\n'
                code += f'        label_{index}.next_to(arrow_{index}, UP, buff=0.2)\n'
                code += f'        elem_{index} = VGroup(arrow_{index}, label_{index})\n\n'
            else:
                code += f'        elem_{index} = arrow_{index}\n\n'
        
        elif elem.element_type == "text":
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            font_size = elem.size.get("font_size", 36)
            label_text = (elem.label or "").replace('"', '\\"').replace("'", "\\'")
            
            code += f'        elem_{index} = Text("{label_text}", font_size={font_size}, color="{elem.color}")\n'
            code += f'        elem_{index}.move_to([{x}, {y}, 0])\n\n'
        
        else:
            code += f'        elem_{index} = None  # Unknown type: {elem.element_type}\n\n'
        
        return code
    
    def combine_scenes(self, scene_files: list, output_path: str):
        """Combine multiple scene videos into one."""
        try:
            # Use ffmpeg to concatenate
            concat_file = os.path.join(self.output_dir, "concat_list.txt")
            with open(concat_file, 'w') as f:
                for scene_file in scene_files:
                    f.write(f"file '{os.path.basename(scene_file)}'\n")
            
            cmd = [
                "ffmpeg",
                "-f", "concat",
                "-safe", "0",
                "-i", concat_file,
                "-c", "copy",
                "-y",  # Overwrite
                output_path
            ]
            
            result = subprocess.run(cmd, capture_output=True, cwd=self.output_dir)
            
            if result.returncode == 0:
                print(f"  [OK] Combined video: {output_path}")
            else:
                print(f"  [WARN] Could not combine scenes. Individual scenes available.")
            
            # Clean up
            if os.path.exists(concat_file):
                os.remove(concat_file)
                
        except Exception as e:
            print(f"  [WARN] Scene combination failed: {e}")
            print(f"  Individual scene files are available")


if __name__ == "__main__":
    # Test
    import json
    from models_schemas import VideoBlueprint
    
    with open("output/how_dns_works_video_blueprint.json", "r") as f:
        blueprint_data = json.load(f)
    
    blueprint = VideoBlueprint(**blueprint_data)
    
    gen = ManimVideoGenerator()
    gen.generate(blueprint, "output/how_dns_works_manim.mp4")
