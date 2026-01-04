from manim import *

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
        
        # Professional text
        text_0 = Text(
            "Title",
            font="Calibri",
            font_size=36,
            color="#FFFFFF",
            weight=BOLD
        )
        text_0.move_to([0.0, 2.5, 0])
        
        text_bg_0 = BackgroundRectangle(
            text_0,
            color="#020617",
            fill_opacity=0.85,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_0 = VGroup(text_bg_0, text_0)

        # Professional rectangle
        rect_1 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.25,
            stroke_color="#00D4FF",
            stroke_width=1.2
        ).set_fill("#00D4FF", opacity=0.18)
        rect_1.move_to([-3.0, 0.0, 0])
        
        # Subtle shadow
        shadow_1 = rect_1.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_1.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Inter font label
        label_1 = Text(
            "Your Computer", 
            font="Calibri",
            font_size=18,
            color=WHITE
        )
        label_1.scale_to_fit_width(rect_1.width * 0.85)
        label_1.move_to(rect_1)
        
        elem_1 = VGroup(shadow_1, rect_1, label_1)

        # Professional text
        text_2 = Text(
            "Computer Query",
            font="Calibri",
            font_size=36,
            color="#FFFFFF",
            weight=BOLD
        )
        text_2.move_to([-3.0, 0.8, 0])
        
        text_bg_2 = BackgroundRectangle(
            text_2,
            color="#020617",
            fill_opacity=0.85,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_2 = VGroup(text_bg_2, text_2)

        # Professional rectangle
        rect_3 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.25,
            stroke_color="#FF6B35",
            stroke_width=1.2
        ).set_fill("#FF6B35", opacity=0.18)
        rect_3.move_to([3.0, 0.0, 0])
        
        # Subtle shadow
        shadow_3 = rect_3.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_3.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Inter font label
        label_3 = Text(
            "DNS", 
            font="Calibri",
            font_size=18,
            color=WHITE
        )
        label_3.scale_to_fit_width(rect_3.width * 0.85)
        label_3.move_to(rect_3)
        
        elem_3 = VGroup(shadow_3, rect_3, label_3)

        # Professional arrow
        arrow_4 = Arrow(
            start=[-1.0, 0.0, 0],
            end=[1.0, 0.0, 0],
            color="#00D4FF",
            stroke_width=2.5,
            buff=0.3,
            max_tip_length_to_length_ratio=0.25
        )
        
        # Label with subtle background
        label_4 = Text("Request", font="Inter", font_size=18, color=WHITE)
        label_4.next_to(arrow_4, UP, buff=0.5)
        
        label_bg_4 = BackgroundRectangle(
            label_4,
            color="#020617",
            fill_opacity=0.9,
            buff=0.2,
            corner_radius=0.15
        )
        
        elem_4 = VGroup(arrow_4, label_bg_4, label_4)


        # Smooth animations
        animations = [
            (elem_0, "FadeIn", 0.0),
            (elem_1, "FadeIn", 0.5),
            (elem_2, "FadeIn", 0.7),
            (elem_3, "FadeIn", 1.0),
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
        
        remaining = 8.0 - current_time
        if remaining > 0:
            self.wait(remaining)
