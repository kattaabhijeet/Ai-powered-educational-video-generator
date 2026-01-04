from manim import *

class FixedScene(Scene):
    def construct(self):
        # FIX: Adjust camera to show more area
        self.camera.frame_width = 16  # Wider frame (default is 14.22)
        self.camera.frame_height = 9   # Taller frame (default is 8)
        
        self.camera.background_color = "#1a1a1a"

        rect_0 = Rectangle(width=2.0999999999999996, height=1.0499999999999998, color="#ff6b35", fill_opacity=0.2, stroke_width=3)
        rect_0.move_to([2.8, 0.0, 0])
        label_0 = Text("Authoritative Server", font_size=20, color=WHITE)
        label_0.move_to(rect_0)
        elem_0 = VGroup(rect_0, label_0)

        arrow_1 = Arrow(start=[1.75, 0.0, 0], end=[0.0, 0.0, 0], color="#ff6b35", stroke_width=4, buff=0.1)
        label_1 = Text("IP to Resolver", font_size=18, color=WHITE)
        label_1.next_to(arrow_1, UP, buff=0.2)
        elem_1 = VGroup(arrow_1, label_1)

        rect_2 = Rectangle(width=1.4, height=1.0499999999999998, color="#00d4ff", fill_opacity=0.2, stroke_width=3)
        rect_2.move_to([-1.4, 0.0, 0])
        label_2 = Text("Local Resolver", font_size=20, color=WHITE)
        label_2.move_to(rect_2)
        elem_2 = VGroup(rect_2, label_2)

        circle_3 = Circle(radius=0.13999999999999999, color="#00d4ff", fill_opacity=0.3, stroke_width=3)
        circle_3.move_to([-1.4, -0.5599999999999999, 0])
        label_3 = Text("Cache Icon", font_size=16, color=WHITE)
        label_3.move_to(circle_3)
        elem_3 = VGroup(circle_3, label_3)

        arrow_4 = Arrow(start=[-0.7, 0.0, 0], end=[-2.8, 0.0, 0], color="#00d4ff", stroke_width=4, buff=0.1)
        label_4 = Text("IP to Computer", font_size=18, color=WHITE)
        label_4.next_to(arrow_4, UP, buff=0.2)
        elem_4 = VGroup(arrow_4, label_4)

        rect_5 = Rectangle(width=1.4, height=1.0499999999999998, color="#00d4ff", fill_opacity=0.2, stroke_width=3)
        rect_5.move_to([-4.199999999999999, 0.0, 0])
        label_5 = Text("Your Computer", font_size=20, color=WHITE)
        label_5.move_to(rect_5)
        elem_5 = VGroup(rect_5, label_5)

        circle_6 = Circle(radius=0.21, color="#ffffff", fill_opacity=0.3, stroke_width=3)
        circle_6.move_to([-4.199999999999999, 0.5599999999999999, 0])
        label_6 = Text("Globe Icon", font_size=16, color=WHITE)
        label_6.move_to(circle_6)
        elem_6 = VGroup(circle_6, label_6)


        # Animate elements
        animations = [
            (elem_0, "FadeIn", 0.0),
            (elem_1, "Write", 0.5),
            (elem_2, "FadeIn", 1.0),
            (elem_3, "FadeIn", 1.5),
            (elem_4, "Write", 2.0),
            (elem_5, "FadeIn", 2.5),
            (elem_6, "FadeIn", 3.0),
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
        
        remaining = 12.0 - current_time
        if remaining > 0:
            self.wait(remaining)
