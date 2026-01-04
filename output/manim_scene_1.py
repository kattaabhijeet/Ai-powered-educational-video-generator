from manim import *

class DynamicScene(Scene):
    def construct(self):
        # Fix cropping by widening camera frame
        self.camera.frame_width = 18
        self.camera.background_color = "#1a1a1a"

        elem_0 = Text("Title", font_size=36, color="#ffffff")
        elem_0.move_to([0.0, 2.5, 0])

        rect_1 = Rectangle(width=2.0, height=1.5, color="#00d4ff", fill_opacity=0.2, stroke_width=3)
        rect_1.move_to([-3.0, 0.0, 0])
        label_1 = Text("Your Computer", font_size=24, color=WHITE)
        label_1.move_to(rect_1)
        elem_1 = VGroup(rect_1, label_1)

        elem_2 = Text("Computer Query", font_size=36, color="#ffffff")
        elem_2.move_to([-3.0, 0.8, 0])

        rect_3 = Rectangle(width=2.0, height=1.5, color="#ff6b35", fill_opacity=0.2, stroke_width=3)
        rect_3.move_to([3.0, 0.0, 0])
        label_3 = Text("DNS", font_size=24, color=WHITE)
        label_3.move_to(rect_3)
        elem_3 = VGroup(rect_3, label_3)

        arrow_4 = Arrow(start=[-1.0, 0.0, 0], end=[1.0, 0.0, 0], color="#00d4ff", stroke_width=4, buff=0.1)
        label_4 = Text("Request", font_size=20, color=WHITE)
        label_4.next_to(arrow_4, UP, buff=0.2)
        elem_4 = VGroup(arrow_4, label_4)


        # Animate elements by timing
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

            # Wait if needed
            if timing > current_time:
                self.wait(timing - current_time)
                current_time = timing

            # Apply animation
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
                elif anim_type == "GrowFromCenter":
                    self.play(GrowFromCenter(mob), run_time=0.5)
                    current_time += 0.5
                else:
                    self.play(FadeIn(mob), run_time=0.5)
                    current_time += 0.5
            except Exception as e:
                print(f"Animation error: {e}")

        # Hold final frame
        remaining = 8.0 - current_time
        if remaining > 0:
            self.wait(remaining)
