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
        
        # Professional rectangle
        rect_0 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.25,
            stroke_color="#FF6B35",
            stroke_width=1.2
        ).set_fill("#FF6B35", opacity=0.18)
        rect_0.move_to([-2.0, 1.0, 0])
        
        # Subtle shadow
        shadow_0 = rect_0.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_0.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Inter font label
        label_0 = Text(
            "Root Server", 
            font="Calibri",
            font_size=18,
            color=WHITE
        )
        label_0.scale_to_fit_width(rect_0.width * 0.85)
        label_0.move_to(rect_0)
        
        elem_0 = VGroup(shadow_0, rect_0, label_0)

        # Professional arrow
        arrow_1 = Arrow(
            start=[-1.0, 1.0, 0],
            end=[1.0, 1.0, 0],
            color="#FF6B35",
            stroke_width=2.5,
            buff=0.3,
            max_tip_length_to_length_ratio=0.25
        )
        
        # Label with subtle background
        label_1 = Text("Root â†’ TLD", font="Inter", font_size=18, color=WHITE)
        label_1.next_to(arrow_1, UP, buff=0.5)
        
        label_bg_1 = BackgroundRectangle(
            label_1,
            color="#020617",
            fill_opacity=0.9,
            buff=0.2,
            corner_radius=0.15
        )
        
        elem_1 = VGroup(arrow_1, label_bg_1, label_1)

        # Professional rectangle
        rect_2 = RoundedRectangle(
            width=2.5, height=1.5,
            corner_radius=0.25,
            stroke_color="#FF6B35",
            stroke_width=1.2
        ).set_fill("#FF6B35", opacity=0.18)
        rect_2.move_to([2.0, 1.0, 0])
        
        # Subtle shadow
        shadow_2 = rect_2.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_2.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Inter font label
        label_2 = Text(
            "TLD (.com) Server", 
            font="Calibri",
            font_size=22,
            color=WHITE
        )
        label_2.scale_to_fit_width(rect_2.width * 0.85)
        label_2.move_to(rect_2)
        
        elem_2 = VGroup(shadow_2, rect_2, label_2)

        # Professional arrow
        arrow_3 = Arrow(
            start=[3.5, 1.0, 0],
            end=[5.5, 1.0, 0],
            color="#FF6B35",
            stroke_width=2.5,
            buff=0.3,
            max_tip_length_to_length_ratio=0.25
        )
        
        # Label with subtle background
        label_3 = Text("TLD â†’ Auth", font="Inter", font_size=18, color=WHITE)
        label_3.next_to(arrow_3, UP, buff=0.5)
        
        label_bg_3 = BackgroundRectangle(
            label_3,
            color="#020617",
            fill_opacity=0.9,
            buff=0.2,
            corner_radius=0.15
        )
        
        elem_3 = VGroup(arrow_3, label_bg_3, label_3)

        # Professional rectangle
        rect_4 = RoundedRectangle(
            width=3.0, height=1.5,
            corner_radius=0.25,
            stroke_color="#FF6B35",
            stroke_width=1.2
        ).set_fill("#FF6B35", opacity=0.18)
        rect_4.move_to([6.5, 1.0, 0])
        
        # Subtle shadow
        shadow_4 = rect_4.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_4.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Inter font label
        label_4 = Text(
            "Authoritative Server", 
            font="Calibri",
            font_size=22,
            color=WHITE
        )
        label_4.scale_to_fit_width(rect_4.width * 0.85)
        label_4.move_to(rect_4)
        
        elem_4 = VGroup(shadow_4, rect_4, label_4)

        # Professional arrow
        arrow_5 = Arrow(
            start=[5.5, 1.0, 0],
            end=[-1.0, -0.5, 0],
            color="#00D4FF",
            stroke_width=2.5,
            buff=0.3,
            max_tip_length_to_length_ratio=0.25
        )
        
        # Label with subtle background
        label_5 = Text("Response (IP)", font="Inter", font_size=18, color=WHITE)
        label_5.next_to(arrow_5, UP, buff=0.5)
        
        label_bg_5 = BackgroundRectangle(
            label_5,
            color="#020617",
            fill_opacity=0.9,
            buff=0.2,
            corner_radius=0.15
        )
        
        elem_5 = VGroup(arrow_5, label_bg_5, label_5)

        # Professional text
        text_6 = Text(
            "IP Address",
            font="Calibri",
            font_size=36,
            color="#FFFFFF",
            weight=BOLD
        )
        text_6.move_to([-1.0, -0.5, 0])
        
        text_bg_6 = BackgroundRectangle(
            text_6,
            color="#020617",
            fill_opacity=0.85,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_6 = VGroup(text_bg_6, text_6)

        # Professional rectangle
        rect_7 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.25,
            stroke_color="#00D4FF",
            stroke_width=1.2
        ).set_fill("#00D4FF", opacity=0.18)
        rect_7.move_to([-4.0, -0.5, 0])
        
        # Subtle shadow
        shadow_7 = rect_7.copy().set_fill(BLACK, 0.25).set_stroke(0)
        shadow_7.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Inter font label
        label_7 = Text(
            "Your Computer", 
            font="Calibri",
            font_size=18,
            color=WHITE
        )
        label_7.scale_to_fit_width(rect_7.width * 0.85)
        label_7.move_to(rect_7)
        
        elem_7 = VGroup(shadow_7, rect_7, label_7)


        # Smooth animations
        animations = [
            (elem_0, "FadeIn", 0.0),
            (elem_1, "Write", 0.5),
            (elem_2, "FadeIn", 1.0),
            (elem_3, "Write", 1.5),
            (elem_4, "FadeIn", 2.0),
            (elem_5, "Write", 2.5),
            (elem_6, "FadeIn", 3.0),
            (elem_7, "FadeIn", 3.5),
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
        
        remaining = 15.0 - current_time
        if remaining > 0:
            self.wait(remaining)
