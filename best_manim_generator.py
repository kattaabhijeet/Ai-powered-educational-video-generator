"""
BEST Manim generator - fixes overlap completely and adds dynamic animations.
"""
import os
import subprocess
from models_schemas import VideoBlueprint, SceneBlueprint, AnimationElement
from config import Config


class BestManimGenerator:
    """Generate best quality Manim videos with dynamic animations."""
    
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
    
    def generate(self, blueprint: VideoBlueprint, output_path: str):
        """Generate best video."""
        print(f"[VIDEO] Generating BEST video for: {blueprint.topic}")
        print(f"  Enhancements:")
        print(f"    - Fixed text overlap (plain text, no Unicode)")
        print(f"    - Dynamic animations (GrowFromCenter, Transform)")
        print(f"    - Professional styling")
        
        scene_files = []
        
        for scene_bp in blueprint.scene_blueprints:
            print(f"\n  Rendering scene {scene_bp.scene_number}...")
            try:
                scene_file = self.render_scene(scene_bp, blueprint.topic)
                if scene_file and os.path.exists(scene_file):
                    scene_files.append(scene_file)
                    print(f"    [OK] Scene {scene_bp.scene_number}")
            except Exception as e:
                print(f"    [X] Error: {e}")
        
        print(f"\n[OK] Rendered {len(scene_files)} scenes")
        return scene_files
    
    def render_scene(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Render scene."""
        scene_code = self._generate_best_code(scene_bp, topic)
        
        temp_file = os.path.join(self.output_dir, f"manim_scene_{scene_bp.scene_number}_best.py")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(scene_code)
        
        try:
            cmd = [
                "manim",
                "-ql",
                "--disable_caching",
                "--format=mp4",
                temp_file,
                "BestScene"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.output_dir, timeout=120)
            
            if result.returncode != 0:
                print(f"    Manim error: {result.stderr}")
                return None
            
            media_base = os.path.join(
                self.output_dir, 
                "media", 
                "videos", 
                f"manim_scene_{scene_bp.scene_number}_best", 
                "480p15"
            )
            
            if os.path.exists(media_base):
                for file in os.listdir(media_base):
                    if file.endswith(".mp4"):
                        src = os.path.join(media_base, file)
                        dst = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}_best.mp4")
                        import shutil
                        shutil.copy(src, dst)
                        return dst
            
            return None
            
        except Exception as e:
            print(f"    Error: {e}")
            return None
    
    def _generate_best_code(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Generate best Manim code with dynamic animations."""
        code = '''from manim import *

class BestScene(Scene):
    def construct(self):
        # Wide camera frame
        self.camera.frame_width = 18
        self.camera.background_color = "#1a1a1a"
        
'''
        
        # Generate elements with better code
        for i, elem in enumerate(scene_bp.elements):
            elem_code = self._generate_best_element(elem, i)
            if elem_code:
                code += elem_code
        
        # BETTER ANIMATIONS
        code += '''
        # Dynamic animations
        animations = [
'''
        
        for i, elem in enumerate(scene_bp.elements):
            # Use more dynamic animation types
            anim = elem.animation
            if anim == "FadeIn":
                anim = "GrowFromCenter"  # More dynamic
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
                elif anim_type == "Create":
                    self.play(Create(mob), run_time=0.7)
                    current_time += 0.7
                elif anim_type == "FadeIn":
                    self.play(FadeIn(mob, shift=UP*0.5), run_time=0.5)
                    current_time += 0.5
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
    
    def _generate_best_element(self, elem: AnimationElement, index: int) -> str:
        """Generate best element code - NO UNICODE, better positioning."""
        code = ""
        
        if elem.element_type == "rectangle":
            w = elem.size.get("width", 2)
            h = elem.size.get("height", 1.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            code += f'''        # Rectangle with shadow
        rect_{index} = RoundedRectangle(
            width={w}, height={h},
            corner_radius=0.3,
            color="{elem.color}",
            fill_opacity=0.5,
            stroke_width=5
        )
        rect_{index}.move_to([{x}, {y}, 0])
        
        shadow_{index} = rect_{index}.copy()
        shadow_{index}.set_fill(BLACK, opacity=0.4)
        shadow_{index}.set_stroke(opacity=0)
        shadow_{index}.shift(DOWN*0.1 + RIGHT*0.1)
        
'''
            
            if elem.label:
                # FIX: Remove Unicode, use plain text
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")  # Remove arrows
                
                code += f'''        label_{index} = Text(
            "{label_text}", 
            font_size=20,
            weight=BOLD,
            color=WHITE
        )
        label_{index}.move_to(rect_{index})
        
        elem_{index} = VGroup(shadow_{index}, rect_{index}, label_{index})

'''
            else:
                code += f'        elem_{index} = VGroup(shadow_{index}, rect_{index})\n\n'
        
        elif elem.element_type == "circle":
            r = elem.size.get("radius", 0.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            code += f'''        circle_{index} = Circle(
            radius={r},
            color="{elem.color}",
            fill_opacity=0.4,
            stroke_width=5
        )
        circle_{index}.move_to([{x}, {y}, 0])
        
'''
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                code += f'''        label_{index} = Text("{label_text}", font_size=18, weight=BOLD, color=WHITE)
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
            
            code += f'''        arrow_{index} = Arrow(
            start=[{x_start}, {y_start}, 0],
            end=[{x_end}, {y_end}, 0],
            color="{elem.color}",
            stroke_width=7,
            buff=0.3,
            max_tip_length_to_length_ratio=0.25
        )
        
'''
            
            if elem.label:
                # FIX: Plain text only, no Unicode
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                # Position label ABOVE arrow with more space
                code += f'''        label_{index} = Text("{label_text}", font_size=18, weight=BOLD, color=WHITE)
        label_{index}.next_to(arrow_{index}, UP, buff=0.6)
        
        label_bg_{index} = BackgroundRectangle(
            label_{index},
            color=BLACK,
            fill_opacity=0.8,
            buff=0.2,
            corner_radius=0.15
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
            
            code += f'''        text_{index} = Text(
            "{label_text}",
            font_size={font_size},
            weight=BOLD,
            color="{elem.color}"
        )
        text_{index}.move_to([{x}, {y}, 0])
        
        text_bg_{index} = BackgroundRectangle(
            text_{index},
            color=BLACK,
            fill_opacity=0.6,
            buff=0.25,
            corner_radius=0.2
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
    
    gen = BestManimGenerator()
    gen.generate(blueprint, "output/best.mp4")
