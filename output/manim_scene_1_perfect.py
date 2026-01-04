from manim import *

class PerfectScene(Scene):
    def construct(self):
        # Wide camera
        self.camera.frame_width = 18
        self.camera.background_color = "#0a0a0a"
        
        # Colorful text
        text_0 = Text(
            "Title",
            font_size=36,
            weight=BOLD,
            color="#FFFFFF"
        )
        text_0.move_to([0.0, 2.5, 0])
        
        text_bg_0 = BackgroundRectangle(
            text_0,
            color="#000000",
            fill_opacity=0.7,
            buff=0.3,
            corner_radius=0.25
        )
        
        elem_0 = VGroup(text_bg_0, text_0)

        # Colorful rectangle
        rect_1 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.3,
            color="#00E5FF",
            fill_opacity=0.6,
            stroke_width=6
        )
        rect_1.move_to([-3.0, 0.0, 0])
        
        # Vibrant shadow
        shadow_1 = rect_1.copy()
        shadow_1.set_fill("#00E5FF", opacity=0.2)
        shadow_1.set_stroke(opacity=0)
        shadow_1.shift(DOWN*0.12 + RIGHT*0.12)
        
        # Label INSIDE (no overlap)
        label_1 = Text(
            "Your Computer", 
            font_size=16,
            weight=BOLD,
            color=WHITE
        )
        label_1.scale_to_fit_width(rect_1.width * 0.85)  # FIT inside
        label_1.move_to(rect_1)  # Centered
        
        elem_1 = VGroup(shadow_1, rect_1, label_1)

        # Colorful text
        text_2 = Text(
            "Computer Query",
            font_size=36,
            weight=BOLD,
            color="#FFFFFF"
        )
        text_2.move_to([-3.0, 0.8, 0])
        
        text_bg_2 = BackgroundRectangle(
            text_2,
            color="#000000",
            fill_opacity=0.7,
            buff=0.3,
            corner_radius=0.25
        )
        
        elem_2 = VGroup(text_bg_2, text_2)

        # Colorful rectangle
        rect_3 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.3,
            color="#FF6B35",
            fill_opacity=0.6,
            stroke_width=6
        )
        rect_3.move_to([3.0, 0.0, 0])
        
        # Vibrant shadow
        shadow_3 = rect_3.copy()
        shadow_3.set_fill("#FF6B35", opacity=0.2)
        shadow_3.set_stroke(opacity=0)
        shadow_3.shift(DOWN*0.12 + RIGHT*0.12)
        
        # Label INSIDE (no overlap)
        label_3 = Text(
            "DNS", 
            font_size=16,
            weight=BOLD,
            color=WHITE
        )
        label_3.scale_to_fit_width(rect_3.width * 0.85)  # FIT inside
        label_3.move_to(rect_3)  # Centered
        
        elem_3 = VGroup(shadow_3, rect_3, label_3)

        # Vibrant arrow
        arrow_4 = Arrow(
            start=[-1.0, 0.0, 0],
            end=[1.0, 0.0, 0],
            color="#00E5FF",
            stroke_width=8,
            buff=0.4,
            max_tip_length_to_length_ratio=0.3
        )
        
        # Label ABOVE arrow (no overlap)
        label_4 = Text("Request", font_size=16, weight=BOLD, color=WHITE)
        label_4.next_to(arrow_4, UP, buff=0.8)  # FAR above
        
        # Dark background for visibility
        label_bg_4 = BackgroundRectangle(
            label_4,
            color="#000000",
            fill_opacity=0.85,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_4 = VGroup(arrow_4, label_bg_4, label_4)


        # Dynamic animations
        animations = [
            (elem_0, "GrowFromCenter", 0.0),
            (elem_1, "GrowFromCenter", 0.5),
            (elem_2, "GrowFromCenter", 0.7),
            (elem_3, "GrowFromCenter", 1.0),
            (elem_4, "Write", 1.5),
        ]
        
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
        
        remaining = 8.0 - current_time
        if remaining > 0:
            self.wait(remaining)
