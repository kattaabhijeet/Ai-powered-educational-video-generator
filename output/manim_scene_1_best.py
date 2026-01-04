from manim import *

class BestScene(Scene):
    def construct(self):
        # Wide camera frame
        self.camera.frame_width = 18
        self.camera.background_color = "#1a1a1a"
        
        text_0 = Text(
            "Title",
            font_size=36,
            weight=BOLD,
            color="#ffffff"
        )
        text_0.move_to([0.0, 2.5, 0])
        
        text_bg_0 = BackgroundRectangle(
            text_0,
            color=BLACK,
            fill_opacity=0.6,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_0 = VGroup(text_bg_0, text_0)

        # Rectangle with shadow
        rect_1 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.3,
            color="#00d4ff",
            fill_opacity=0.5,
            stroke_width=5
        )
        rect_1.move_to([-3.0, 0.0, 0])
        
        shadow_1 = rect_1.copy()
        shadow_1.set_fill(BLACK, opacity=0.4)
        shadow_1.set_stroke(opacity=0)
        shadow_1.shift(DOWN*0.1 + RIGHT*0.1)
        
        label_1 = Text(
            "Your Computer", 
            font_size=20,
            weight=BOLD,
            color=WHITE
        )
        label_1.move_to(rect_1)
        
        elem_1 = VGroup(shadow_1, rect_1, label_1)

        text_2 = Text(
            "Computer Query",
            font_size=36,
            weight=BOLD,
            color="#ffffff"
        )
        text_2.move_to([-3.0, 0.8, 0])
        
        text_bg_2 = BackgroundRectangle(
            text_2,
            color=BLACK,
            fill_opacity=0.6,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_2 = VGroup(text_bg_2, text_2)

        # Rectangle with shadow
        rect_3 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.3,
            color="#ff6b35",
            fill_opacity=0.5,
            stroke_width=5
        )
        rect_3.move_to([3.0, 0.0, 0])
        
        shadow_3 = rect_3.copy()
        shadow_3.set_fill(BLACK, opacity=0.4)
        shadow_3.set_stroke(opacity=0)
        shadow_3.shift(DOWN*0.1 + RIGHT*0.1)
        
        label_3 = Text(
            "DNS", 
            font_size=20,
            weight=BOLD,
            color=WHITE
        )
        label_3.move_to(rect_3)
        
        elem_3 = VGroup(shadow_3, rect_3, label_3)

        arrow_4 = Arrow(
            start=[-1.0, 0.0, 0],
            end=[1.0, 0.0, 0],
            color="#00d4ff",
            stroke_width=7,
            buff=0.3,
            max_tip_length_to_length_ratio=0.25
        )
        
        label_4 = Text("Request", font_size=18, weight=BOLD, color=WHITE)
        label_4.next_to(arrow_4, UP, buff=0.6)
        
        label_bg_4 = BackgroundRectangle(
            label_4,
            color=BLACK,
            fill_opacity=0.8,
            buff=0.2,
            corner_radius=0.15
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
        
        remaining = 8.0 - current_time
        if remaining > 0:
            self.wait(remaining)
