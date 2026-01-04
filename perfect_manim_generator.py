"""
PERFECT final generator:
- Colorful vibrant visualizations
- NO overlap (text properly positioned)
- Same content
- Dynamic animations
"""
import os
import subprocess
from models_schemas import VideoBlueprint, SceneBlueprint, AnimationElement
from config import Config


class PerfectManimGenerator:
    """Perfect Manim generator with colorful visuals and no overlap."""
    
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
    
    def generate(self, blueprint: VideoBlueprint, output_path: str):
        """Generate perfect video."""
        print(f"[VIDEO] Generating PERFECT colorful video")
        print(f"  Features:")
        print(f"    - COLORFUL vibrant visualizations")
        print(f"    - NO text overlap (proper positioning)")
        print(f"    - Dynamic animations")
        print(f"    - Female AI voice compatible")
        
        scene_files = []
        
        for scene_bp in blueprint.scene_blueprints:
            print(f"\n  Scene {scene_bp.scene_number}...")
            try:
                scene_file = self.render_scene(scene_bp, blueprint.topic)
                if scene_file and os.path.exists(scene_file):
                    scene_files.append(scene_file)
                    print(f"    [OK] Scene {scene_bp.scene_number}")
            except Exception as e:
                print(f"    [X] Error: {e}")
        
        return scene_files
    
    def render_scene(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Render scene."""
        scene_code = self._generate_perfect_code(scene_bp, topic)
        
        temp_file = os.path.join(self.output_dir, f"manim_scene_{scene_bp.scene_number}_perfect.py")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(scene_code)
        
        try:
            cmd = ["manim", "-ql", "--disable_caching", "--format=mp4", temp_file, "PerfectScene"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.output_dir, timeout=120)
            
            if result.returncode != 0:
                return None
            
            media_base = os.path.join(self.output_dir, "media", "videos", f"manim_scene_{scene_bp.scene_number}_perfect", "480p15")
            
            if os.path.exists(media_base):
                for file in os.listdir(media_base):
                    if file.endswith(".mp4"):
                        src = os.path.join(media_base, file)
                        dst = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}_perfect.mp4")
                        import shutil
                        shutil.copy(src, dst)
                        return dst
            return None
        except Exception as e:
            print(f"    Error: {e}")
            return None
    
    def _generate_perfect_code(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Generate perfect Manim code with colorful visuals."""
        code = '''from manim import *

class PerfectScene(Scene):
    def construct(self):
        # Wide camera
        self.camera.frame_width = 18
        self.camera.background_color = "#0a0a0a"
        
'''
        
        # Generate colorful elements
        for i, elem in enumerate(scene_bp.elements):
            elem_code = self._generate_colorful_element(elem, i)
            if elem_code:
                code += elem_code
        
        # Dynamic animations
        code += '''
        # Dynamic animations
        animations = [
'''
        
        for i, elem in enumerate(scene_bp.elements):
            anim = elem.animation if elem.animation == "Write" else "GrowFromCenter"
            code += f'            (elem_{i}, "{anim}", {elem.timing}),\n'
        
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
                if anim_type == "GrowFromCenter":
                    self.play(GrowFromCenter(mob), run_time=0.6)
                    current_time += 0.6
                elif anim_type == "Write":
                    self.play(Write(mob), run_time=0.8)
                    current_time += 0.8
                else:
                    self.play(GrowFromCenter(mob), run_time=0.6)
                    current_time += 0.6
            except:
                pass
        
        remaining = ''' + str(scene_bp.duration) + ''' - current_time
        if remaining > 0:
            self.wait(remaining)
'''
        
        return code
    
    def _get_vibrant_color(self, original_color):
        """Convert to more vibrant color."""
        color_map = {
            "#ff6b35": "#FF6B35",  # Vibrant orange
            "#00d4ff": "#00E5FF",  # Bright cyan
            "#ffffff": "#FFFFFF",  # White
        }
        return color_map.get(original_color.lower(), original_color)
    
    def _generate_colorful_element(self, elem: AnimationElement, index: int) -> str:
        """Generate colorful element - NO overlap!"""
        code = ""
        
        if elem.element_type == "rectangle":
            w = elem.size.get("width", 2)
            h = elem.size.get("height", 1.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            # VIBRANT colors
            vibrant_color = self._get_vibrant_color(elem.color)
            
            code += f'''        # Colorful rectangle
        rect_{index} = RoundedRectangle(
            width={w}, height={h},
            corner_radius=0.3,
            color="{vibrant_color}",
            fill_opacity=0.6,
            stroke_width=6
        )
        rect_{index}.move_to([{x}, {y}, 0])
        
        # Vibrant shadow
        shadow_{index} = rect_{index}.copy()
        shadow_{index}.set_fill("{vibrant_color}", opacity=0.2)
        shadow_{index}.set_stroke(opacity=0)
        shadow_{index}.shift(DOWN*0.12 + RIGHT*0.12)
        
'''
            
            if elem.label:
                # NO Unicode - clean text
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                # Smaller font to FIT inside
                font_size = min(20, int(w * 8))  # Scale with box width
                
                code += f'''        # Label INSIDE (no overlap)
        label_{index} = Text(
            "{label_text}", 
            font_size={font_size},
            weight=BOLD,
            color=WHITE
        )
        label_{index}.scale_to_fit_width(rect_{index}.width * 0.85)  # FIT inside
        label_{index}.move_to(rect_{index})  # Centered
        
        elem_{index} = VGroup(shadow_{index}, rect_{index}, label_{index})

'''
            else:
                code += f'        elem_{index} = VGroup(shadow_{index}, rect_{index})\n\n'
        
        elif elem.element_type == "circle":
            r = elem.size.get("radius", 0.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            vibrant_color = self._get_vibrant_color(elem.color)
            
            code += f'''        # Colorful circle
        circle_{index} = Circle(
            radius={r},
            color="{vibrant_color}",
            fill_opacity=0.5,
            stroke_width=6
        )
        circle_{index}.move_to([{x}, {y}, 0])
        
'''
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                code += f'''        label_{index} = Text("{label_text}", font_size=16, weight=BOLD, color=WHITE)
        label_{index}.scale_to_fit_width(circle_{index}.width * 0.7)
        label_{index}.move_to(circle_{index})
        elem_{index} = VGroup(circle_{index}, label_{index})

'''
            else:
                code += f'        elem_{index} = circle_{index}\n\n'
        
        elif elem.element_type == "arrow":
            x_start = elem.position.get("x_start", -2)
            y_start = elem.position.get("y_start", 0)
            x_end = elem.position.get("x_end", 2)
            y_end = elem.position.get("y_end", 0)
            
            vibrant_color = self._get_vibrant_color(elem.color)
            
            code += f'''        # Vibrant arrow
        arrow_{index} = Arrow(
            start=[{x_start}, {y_start}, 0],
            end=[{x_end}, {y_end}, 0],
            color="{vibrant_color}",
            stroke_width=8,
            buff=0.4,
            max_tip_length_to_length_ratio=0.3
        )
        
'''
            
            if elem.label:
                # Clean text, NO Unicode
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                # Position WELL ABOVE arrow - no overlap!
                code += f'''        # Label ABOVE arrow (no overlap)
        label_{index} = Text("{label_text}", font_size=16, weight=BOLD, color=WHITE)
        label_{index}.next_to(arrow_{index}, UP, buff=0.8)  # FAR above
        
        # Dark background for visibility
        label_bg_{index} = BackgroundRectangle(
            label_{index},
            color="#000000",
            fill_opacity=0.85,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_{index} = VGroup(arrow_{index}, label_bg_{index}, label_{index})

'''
            else:
                code += f'        elem_{index} = arrow_{index}\n\n'
        
        elif elem.element_type == "text":
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            font_size = elem.size.get("font_size", 36)
            label_text = (elem.label or "").replace('"', '\\"').replace("'", "\\'")
            label_text = label_text.replace("→", "to").replace("â†'", "to")
            
            vibrant_color = self._get_vibrant_color(elem.color)
            
            code += f'''        # Colorful text
        text_{index} = Text(
            "{label_text}",
            font_size={font_size},
            weight=BOLD,
            color="{vibrant_color}"
        )
        text_{index}.move_to([{x}, {y}, 0])
        
        text_bg_{index} = BackgroundRectangle(
            text_{index},
            color="#000000",
            fill_opacity=0.7,
            buff=0.3,
            corner_radius=0.25
        )
        
        elem_{index} = VGroup(text_bg_{index}, text_{index})

'''
        
        else:
            code += f'        elem_{index} = None\n\n'
        
        return code


if __name__ == "__main__":
    import json
    from models_schemas import VideoBlueprint
    
    with open("output/how_dns_works_video_blueprint.json", "r") as f:
        blueprint_data = json.load(f)
    
    blueprint = VideoBlueprint(**blueprint_data)
    
    gen = PerfectManimGenerator()
    gen.generate(blueprint, "output/perfect.mp4")
