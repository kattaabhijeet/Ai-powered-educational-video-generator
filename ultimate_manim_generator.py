"""
ULTIMATE professional Manim generator with the user's preferred style.
- Dark gradient background
- Subtle fills (opacity 0.18)
- Inter font
- Professional shadows
- Female AI voice compatible
"""
import os
import subprocess
from models_schemas import VideoBlueprint, SceneBlueprint, AnimationElement
from config import Config


class UltimateManimGenerator:
    """Ultimate professional Manim generator."""
    
    def __init__(self):
        self.output_dir = Config.OUTPUT_DIR
    
    def generate(self, blueprint: VideoBlueprint, output_path: str):
        """Generate ultimate professional video."""
        print(f"[VIDEO] Generating ULTIMATE professional video")
        print(f"  Style: Dark gradient + Inter font + Subtle fills")
        
        scene_files = []
        
        for scene_bp in blueprint.scene_blueprints:
            print(f"\n  Scene {scene_bp.scene_number}...")
            try:
                scene_file = self.render_scene(scene_bp, blueprint.topic)
                if scene_file and os.path.exists(scene_file):
                    scene_files.append(scene_file)
                    print(f"    [OK]")
            except Exception as e:
                print(f"    [X] {e}")
        
        return scene_files
    
    def render_scene(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Render professional scene."""
        scene_code = self._generate_pro_code(scene_bp, topic)
        
        temp_file = os.path.join(self.output_dir, f"manim_scene_{scene_bp.scene_number}_ultimate.py")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(scene_code)
        
        try:
            cmd = ["manim", "-ql", "--disable_caching", "--format=mp4", temp_file, "UltimateScene"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.output_dir, timeout=120)
            
            if result.returncode != 0:
                return None
            
            media_base = os.path.join(self.output_dir, "media", "videos", f"manim_scene_{scene_bp.scene_number}_ultimate", "480p15")
            
            if os.path.exists(media_base):
                for file in os.listdir(media_base):
                    if file.endswith(".mp4"):
                        src = os.path.join(media_base, file)
                        dst = os.path.join(self.output_dir, f"scene_{scene_bp.scene_number}_ultimate.mp4")
                        import shutil
                        shutil.copy(src, dst)
                        return dst
            return None
        except Exception as e:
            print(f"    Error: {e}")
            return None
    
    def _generate_pro_code(self, scene_bp: SceneBlueprint, topic: str) -> str:
        """Generate professional Manim code with user's style."""
        code = '''from manim import *

config.background_color = "#0F172A"

class UltimateScene(Scene):
    def construct(self):
        # Dark gradient background
        bg = Rectangle(20, 12).set_fill(
            color=["#0F172A", "#020617"], opacity=1
        ).set_stroke(width=0)
        self.add(bg)
        
        # Wide camera
        self.camera.frame_width = 18
        
'''
        
        # Generate professional elements
        for i, elem in enumerate(scene_bp.elements):
            elem_code = self._generate_pro_element(elem, i)
            if elem_code:
                code += elem_code
        
        # Professional animations
        code += '''
        # Smooth animations
        animations = [
'''
        
        for i, elem in enumerate(scene_bp.elements):
            anim = "Write" if elem.animation == "Write" else "FadeIn"
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
                if anim_type == "FadeIn":
                    self.play(FadeIn(mob, shift=UP*0.3), run_time=0.6)
                    current_time += 0.6
                elif anim_type == "Write":
                    self.play(Write(mob), run_time=0.8)
                    current_time += 0.8
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
    
    def _generate_pro_element(self, elem: AnimationElement, index: int) -> str:
        """Generate professional element with user's style."""
        code = ""
        
        if elem.element_type == "rectangle":
            w = elem.size.get("width", 2)
            h = elem.size.get("height", 1.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            # Use vibrant color for stroke
            color = elem.color.upper()
            
            code += f'''        # Professional rectangle
        rect_{index} = RoundedRectangle(
            width={w}, height={h},
            corner_radius=0.25,
            stroke_color="{color}",
            stroke_width=1.2
        ).set_fill("{color}", opacity=0.18)
        rect_{index}.move_to([{x}, {y}, 0])
        
        # Subtle shadow
        shadow_{index} = rect_{index}.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_{index}.shift(DOWN*0.08 + RIGHT*0.08)
        
'''
            
            if elem.label:
                # Clean text
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                # Scale to fit
                font_size = min(22, int(w * 9))
                
                code += f'''        # Inter font label
        label_{index} = Text(
            "{label_text}", 
            font="Calibri",
            font_size={font_size},
            color=WHITE
        )
        label_{index}.scale_to_fit_width(rect_{index}.width * 0.85)
        label_{index}.move_to(rect_{index}).shift(UP*2.5)
        
        elem_{index} = VGroup(shadow_{index}, rect_{index}, label_{index})

'''
            else:
                code += f'        elem_{index} = VGroup(shadow_{index}, rect_{index})\n\n'
        
        elif elem.element_type == "circle":
            r = elem.size.get("radius", 0.5)
            x = elem.position.get("x", 0)
            y = elem.position.get("y", 0)
            
            color = elem.color.upper()
            
            code += f'''        # Professional circle
        circle_{index} = Circle(
            radius={r},
            stroke_color="{color}",
            stroke_width=1.2
        ).set_fill("{color}", opacity=0.18)
        circle_{index}.move_to([{x}, {y}, 0])
        
        shadow_{index} = circle_{index}.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_{index}.shift(DOWN*0.08 + RIGHT*0.08)
        
'''
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                code += f'''        label_{index} = Text("{label_text}", font="Inter", font_size=18, color=WHITE)
        label_{index}.scale_to_fit_width(circle_{index}.width * 0.7)
        label_{index}.move_to(circle_{index})
        elem_{index} = VGroup(shadow_{index}, circle_{index}, label_{index})

'''
            else:
                code += f'        elem_{index} = VGroup(shadow_{index}, circle_{index})\n\n'
        
        elif elem.element_type == "arrow":
            x_start = elem.position.get("x_start", -2)
            y_start = elem.position.get("y_start", 0)
            x_end = elem.position.get("x_end", 2)
            y_end = elem.position.get("y_end", 0)
            
            color = elem.color.upper()
            
            code += f'''        # Professional arrow
        arrow_{index} = Arrow(
            start=[{x_start}, {y_start}, 0],
            end=[{x_end}, {y_end}, 0],
            color="{color}",
            stroke_width=2.5,
            buff=0.3,
            max_tip_length_to_length_ratio=0.25
        )
        
'''
            
            if elem.label:
                label_text = elem.label.replace('"', '\\"').replace("'", "\\'")
                label_text = label_text.replace("→", "to").replace("â†'", "to")
                
                code += f'''        # Label with subtle background
        label_{index} = Text("{label_text}", font="Calibri", font_size=18, color=WHITE)
        label_{index}.next_to(arrow_{index}, UP, buff=2.0)
        
        label_bg_{index} = BackgroundRectangle(
            label_{index},
            color="#020617",
            fill_opacity=0.9,
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
            
            color = elem.color.upper()
            
            code += f'''        # Professional text
        text_{index} = Text(
            "{label_text}",
            font="Calibri",
            font_size={font_size},
            color="{color}",
            weight=BOLD
        )
        text_{index}.move_to([{x}, {y}, 0])
        
        text_bg_{index} = BackgroundRectangle(
            text_{index},
            color="#020617",
            fill_opacity=0.85,
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
    
    gen = UltimateManimGenerator()
    gen.generate(blueprint, "output/ultimate.mp4")
