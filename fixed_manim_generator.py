"""
Fix cropped images by adjusting Manim camera frame and element positioning.
"""
import os
import json
from models_schemas import VideoBlueprint, SceneBlueprint, AnimationElement
from config import Config


class FixedManimVideoGenerator:
    """Manim generator with fixed camera frame to prevent cropping."""
    
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
    
    def generate(self, blueprint: VideoBlueprint, output_path: str):
        """Generate video with fixed framing."""
        print(f"[VIDEO] Generating video with FIXED framing")
        print(f"  Total scenes: {len(blueprint.scene_blueprints)}")
        
        scene_files = []
        
        for scene_bp in blueprint.scene_blueprints:
            print(f"\n  Rendering scene {scene_bp.scene_number}...")
            try:
                scene_file = self.render_scene(scene_bp, blueprint.topic)
                if scene_file and os.path.exists(scene_file):
                    scene_files.append(scene_file)
                    print(f"    [OK] Scene {scene_bp.scene_number} rendered")
            except Exception as e:
                print(f"    [X] Error: {e}")
        
        print(f"\n[OK] Rendered {len(scene_files)} scenes")
        return scene_files
    
    def render_scene(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Render scene with fixed camera frame."""
        import subprocess
        
        # Generate Manim code with camera fix
        scene_code = self._generate_fixed_manim_code(scene_bp, topic)
        
        # Write to file
        temp_file = os.path.join(self.output_dir, f"manim_scene_{scene_bp.scene_number}_fixed.py")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(scene_code)
        
        # Render with Manim
        try:
            cmd = [
                "manim",
                "-ql",
                "--disable_caching",
                "--format=mp4",
                temp_file,
                "FixedScene"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.output_dir, timeout=120)
            
            if result.returncode != 0:
                print(f"    Manim error: {result.stderr}")
                return None
            
            # Find rendered file
            media_base = os.path.join(
                self.output_dir, 
                "media", 
                "videos", 
                f"manim_scene_{scene_bp.scene_number}_fixed", 
                "480p15"
            )
            
            if os.path.exists(media_base):
                for file in os.listdir(media_base):
                    if file.endswith(".mp4"):
                        src = os.path.join(media_base, file)
                        dst = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}_fixed.mp4")
                        import shutil
                        shutil.copy(src, dst)
                        return dst
            
            return None
            
        except Exception as e:
            print(f"    Error: {e}")
            return None
    
    def _generate_fixed_manim_code(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Generate Manim code with proper camera framing."""
        code = '''from manim import *

class FixedScene(Scene):
    def construct(self):
        # FIX: Adjust camera to show more area
        self.camera.frame_width = 16  # Wider frame (default is 14.22)
        self.camera.frame_height = 9   # Taller frame (default is 8)
        
'''
        
        # Set background
        code += f'        self.camera.background_color = "{scene_bp.background_color}"\n\n'
        
        # Scale factor to fit elements better
        scale_factor = 0.7  # Make elements smaller to fit in frame
        
        # Generate elements with scaling
        for i, elem in enumerate(scene_bp.elements):
            elem_code = self._generate_element_code(elem, i, scale_factor)
            if elem_code:
                code += elem_code
        
        # Animation code
        code += '''
        # Animate elements
        animations = [
'''
        
        for i, elem in enumerate(scene_bp.elements):
            code += f'            (elem_{i}, "{elem.animation}", {elem.timing}),\n'
        
        code += '''        ]
        
        animations.sort(key=lambda x: x[2])
        
        current_time = 0
        for mob, anim_type, timing in animations:
            if mob is None:
                continue
            
            if timing > current_time:
                self.wait(timing - current_time)
                current_time = timing
            
            try:
                if anim_type == "FadeIn":
                    self.play(FadeIn(mob), run_time=0.5)
                    current_time += 0.5
                elif anim_type == "Write":
                    self.play(Write(mob), run_time=0.8)
                    current_time += 0.8
                elif anim_type == "Create":
                    self.play(Create(mob), run_time=0.6)
                    current_time += 0.6
                else:
                    self.play(FadeIn(mob), run_time=0.5)
                    current_time += 0.5
            except:
                pass
        
        remaining = ''' + str(scene_bp.duration) + ''' - current_time
        if remaining > 0:
            self.wait(remaining)
'''
        
        return code
    
    def _generate_element_code(self, elem: AnimationElement, index: int, scale: float) -> str:
        """Generate element code with scaling."""
        code = ""
        
        if elem.element_type == "rectangle":
            w = elem.size.get("width", 2) * scale
            h = elem.size.get("height", 1.5) * scale
            x = elem.position.get("x", 0) * scale
            y = elem.position.get("y", 0) * scale
            
            code += f'        rect_{index} = Rectangle(width={w}, height={h}, color="{elem.color}", fill_opacity=0.2, stroke_width=3)\n'
            code += f'        rect_{index}.move_to([{x}, {y}, 0])\n'
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                code += f'        label_{index} = Text("{label_text}", font_size=20, color=WHITE)\n'
                code += f'        label_{index}.move_to(rect_{index})\n'
                code += f'        elem_{index} = VGroup(rect_{index}, label_{index})\n\n'
            else:
                code += f'        elem_{index} = rect_{index}\n\n'
        
        elif elem.element_type == "circle":
            r = elem.size.get("radius", 0.5) * scale
            x = elem.position.get("x", 0) * scale
            y = elem.position.get("y", 0) * scale
            
            code += f'        circle_{index} = Circle(radius={r}, color="{elem.color}", fill_opacity=0.3, stroke_width=3)\n'
            code += f'        circle_{index}.move_to([{x}, {y}, 0])\n'
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                code += f'        label_{index} = Text("{label_text}", font_size=16, color=WHITE)\n'
                code += f'        label_{index}.move_to(circle_{index})\n'
                code += f'        elem_{index} = VGroup(circle_{index}, label_{index})\n\n'
            else:
                code += f'        elem_{index} = circle_{index}\n\n'
        
        elif elem.element_type == "arrow":
            x_start = elem.position.get("x_start", -2) * scale
            y_start = elem.position.get("y_start", 0) * scale
            x_end = elem.position.get("x_end", 2) * scale
            y_end = elem.position.get("y_end", 0) * scale
            
            code += f'        arrow_{index} = Arrow(start=[{x_start}, {y_start}, 0], end=[{x_end}, {y_end}, 0], color="{elem.color}", stroke_width=4, buff=0.1)\n'
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                code += f'        label_{index} = Text("{label_text}", font_size=18, color=WHITE)\n'
                code += f'        label_{index}.next_to(arrow_{index}, UP, buff=0.2)\n'
                code += f'        elem_{index} = VGroup(arrow_{index}, label_{index})\n\n'
            else:
                code += f'        elem_{index} = arrow_{index}\n\n'
        
        elif elem.element_type == "text":
            x = elem.position.get("x", 0) * scale
            y = elem.position.get("y", 0) * scale
            font_size = elem.size.get("font_size", 36) * scale
            label_text = (elem.label or "").replace('"', '\\"').replace("'", "\\'")
            
            code += f'        elem_{index} = Text("{label_text}", font_size={font_size}, color="{elem.color}")\n'
            code += f'        elem_{index}.move_to([{x}, {y}, 0])\n\n'
        
        else:
            code += f'        elem_{index} = None\n\n'
        
        return code


if __name__ == "__main__":
    import json
    from models_schemas import VideoBlueprint
    
    with open("output/how_dns_works_video_blueprint.json", "r") as f:
        blueprint_data = json.load(f)
    
    blueprint = VideoBlueprint(**blueprint_data)
    
    gen = FixedManimVideoGenerator()
    gen.generate(blueprint, "output/dns_fixed.mp4")
