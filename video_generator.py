"""
Video generator using Manim for animation.
"""
import os
import json
import subprocess
from pathlib import Path
from manim import *
from models_schemas import VideoBlueprint, SceneBlueprint, AnimationElement
from config import Config


class VideoGenerator:
    """Generates MP4 videos from animation blueprints using Manim."""
    
    def __init__(self):
        """Initialize the video generator."""
        self.output_dir = Config.OUTPUT_DIR
    
    def generate(self, blueprint: VideoBlueprint, output_path: str):
        """
        Generate a video from a blueprint.
        
        Args:
            blueprint: The animation blueprint
            output_path: Path to save the final video
        """
        print(f"[VIDEO] Generating video for: {blueprint.topic}")
        print(f"  Total scenes: {len(blueprint.scene_blueprints)}")
        
        scene_files = []
        
        # Generate each scene
        for scene_bp in blueprint.scene_blueprints:
            print(f"  Rendering scene {scene_bp.scene_number}...")
            try:
                scene_file = self.render_scene(scene_bp, blueprint.topic)
                if scene_file and os.path.exists(scene_file):
                    scene_files.append(scene_file)
                    print(f"    [OK] Scene {scene_bp.scene_number} rendered")
            except Exception as e:
                print(f"    [X] Error rendering scene {scene_bp.scene_number}: {e}")
        
        print(f"[OK] Video generation complete")
        print(f"  Rendered {len(scene_files)} scenes")
        
        return scene_files
    
    def render_scene(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Render a single scene using Manim."""
        # Create a temporary Python file with the scene
        scene_code = self._generate_scene_code(scene_bp, topic)
        
        # Write to temporary file
        temp_file = os.path.join(self.output_dir, f"temp_scene_{scene_bp.scene_number}.py")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(scene_code)
        
        # Render with Manim CLI
        output_file = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}.mp4")
        
        try:
            # Run manim command
            cmd = [
                "manim",
                "-ql",  # Low quality for speed
                "--format=mp4",
                f"--output_file={output_file}",
                "--disable_caching",
                temp_file,
                "DynamicScene"
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.output_dir
            )
            
            # Clean up temp file
            if os.path.exists(temp_file):
                os.remove(temp_file)
            
            # Find the rendered file (Manim puts it in media folder)
            media_dir = os.path.join(self.output_dir, "media", "videos", f"temp_scene_{scene_bp.scene_number}", "480p15")
            if os.path.exists(media_dir):
                for file in os.listdir(media_dir):
                    if file.endswith(".mp4"):
                        src = os.path.join(media_dir, file)
                        dst = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}.mp4")
                        if os.path.exists(src):
                            import shutil
                            shutil.copy(src, dst)
                            return dst
            
            return output_file
            
        except Exception as e:
            print(f"Error running Manim: {e}")
            return None
    
    def _generate_scene_code(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Generate Python code for a Manim scene."""
        code = f'''from manim import *

class DynamicScene(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "{scene_bp.background_color}"
        
        # Create elements
        elements = []
        
'''
        
        # Generate code for each element
        for i, elem in enumerate(scene_bp.elements):
            elem_code = self._generate_element_code(elem, i)
            if elem_code:
                code += elem_code + "\n"
        
        # Generate animation code
        code += '''
        # Animate elements by timing
        elements_with_timing = [
'''
        
        for i, elem in enumerate(scene_bp.elements):
            code += f'            (elem_{i}, "{elem.animation}", {elem.timing}),\n'
        
        code += '''        ]
        
        elements_with_timing.sort(key=lambda x: x[2])
        
        current_time = 0
        for mob, anim_type, timing in elements_with_timing:
            if mob is None:
                continue
                
            # Wait if needed
            if timing > current_time:
                self.wait(timing - current_time)
                current_time = timing
            
            # Apply animation
            try:
                if anim_type == "FadeIn":
                    self.play(FadeIn(mob), run_time=0.5)
                elif anim_type == "Write":
                    self.play(Write(mob), run_time=0.8)
                elif anim_type == "Create":
                    self.play(Create(mob), run_time=0.6)
                elif anim_type == "GrowFromCenter":
                    self.play(GrowFromCenter(mob), run_time=0.5)
                else:
                    self.play(FadeIn(mob), run_time=0.5)
                current_time += 0.5
            except:
                pass
        
        # Hold final frame
        remaining = ''' + str(scene_bp.duration) + ''' - current_time
        if remaining > 0:
            self.wait(remaining)
'''
        
        return code
    
    def _generate_element_code(self, elem: AnimationElement, index: int) -> str:
        """Generate code for a single element."""
        code = ""
        
        if elem.element_type == "rectangle":
            w = elem.size.get("width", 2)
            h = elem.size.get("height", 1.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            code += f'''        rect_{index} = Rectangle(width={w}, height={h}, color="{elem.color}", fill_opacity=0.2, stroke_width=3)
        rect_{index}.move_to([{x}, {y}, 0])
'''
            if elem.label:
                code += f'''        label_{index} = Text("{elem.label}", font_size=24, color=WHITE)
        label_{index}.move_to(rect_{index})
        elem_{index} = VGroup(rect_{index}, label_{index})
'''
            else:
                code += f'''        elem_{index} = rect_{index}
'''
        
        elif elem.element_type == "circle":
            r = elem.size.get("radius", 0.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            code += f'''        circle_{index} = Circle(radius={r}, color="{elem.color}", fill_opacity=0.3, stroke_width=3)
        circle_{index}.move_to([{x}, {y}, 0])
'''
            if elem.label:
                label_text = elem.label.replace('"', '\\"')
                code += f'''        label_{index} = Text("{label_text}", font_size=18, color=WHITE)
        label_{index}.move_to(circle_{index})
        elem_{index} = VGroup(circle_{index}, label_{index})
'''
            else:
                code += f'''        elem_{index} = circle_{index}
'''
        
        elif elem.element_type == "arrow":
            x_start = elem.position.get("x_start", -2)
            y_start = elem.position.get("y_start", 0)
            x_end = elem.position.get("x_end", 2)
            y_end = elem.position.get("y_end", 0)
            
            code += f'''        arrow_{index} = Arrow(start=[{x_start}, {y_start}, 0], end=[{x_end}, {y_end}, 0], color="{elem.color}", stroke_width=4, buff=0.1)
'''
            if elem.label:
                code += f'''        label_{index} = Text("{elem.label}", font_size=20, color=WHITE)
        label_{index}.next_to(arrow_{index}, UP, buff=0.2)
        elem_{index} = VGroup(arrow_{index}, label_{index})
'''
            else:
                code += f'''        elem_{index} = arrow_{index}
'''
        
        elif elem.element_type == "text":
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            font_size = elem.size.get("font_size", 36)
            label_text = (elem.label or "").replace('"', '\\"')
            
            code += f'''        elem_{index} = Text("{label_text}", font_size={font_size}, color="{elem.color}")
        elem_{index}.move_to([{x}, {y}, 0])
'''
        
        else:
            # Unknown element type, create placeholder
            code += f'''        elem_{index} = None
'''
        
        return code


if __name__ == "__main__":
    # Test the video generator
    from script_generator import ScriptGenerator
    from blueprint_generator import BlueprintGenerator
    
    # Generate script and blueprint
    script_gen = ScriptGenerator()
    script = script_gen.generate("How DNS works")
    
    blueprint_gen = BlueprintGenerator()
    blueprint = blueprint_gen.generate(script)
    
    # Generate video
    video_gen = VideoGenerator()
    video_gen.generate(blueprint, "output/dns_video.mp4")
