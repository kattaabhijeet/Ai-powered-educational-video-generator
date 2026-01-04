from manim import *

class DynamicScene(Scene):
    def construct(self):
        # Fix cropping by widening camera frame
        self.camera.frame_width = 18
        self.camera.background_color = "#1a1a1a"

        rect_0 = Rectangle(width=2.0, height=1.5, color="#ff6b35", fill_opacity=0.2, stroke_width=3)
        rect_0.move_to([-2.0, 1.0, 0])
        label_0 = Text("Root Server", font_size=24, color=WHITE)
        label_0.move_to(rect_0)
        elem_0 = VGroup(rect_0, label_0)

        arrow_1 = Arrow(start=[-1.0, 1.0, 0], end=[1.0, 1.0, 0], color="#ff6b35", stroke_width=4, buff=0.1)
        label_1 = Text("Root â†’ TLD", font_size=20, color=WHITE)
        label_1.next_to(arrow_1, UP, buff=0.2)
        elem_1 = VGroup(arrow_1, label_1)

        rect_2 = Rectangle(width=2.5, height=1.5, color="#ff6b35", fill_opacity=0.2, stroke_width=3)
        rect_2.move_to([2.0, 1.0, 0])
        label_2 = Text("TLD (.com) Server", font_size=24, color=WHITE)
        label_2.move_to(rect_2)
        elem_2 = VGroup(rect_2, label_2)

        arrow_3 = Arrow(start=[3.5, 1.0, 0], end=[5.5, 1.0, 0], color="#ff6b35", stroke_width=4, buff=0.1)
        label_3 = Text("TLD â†’ Auth", font_size=20, color=WHITE)
        label_3.next_to(arrow_3, UP, buff=0.2)
        elem_3 = VGroup(arrow_3, label_3)

        rect_4 = Rectangle(width=3.0, height=1.5, color="#ff6b35", fill_opacity=0.2, stroke_width=3)
        rect_4.move_to([6.5, 1.0, 0])
        label_4 = Text("Authoritative Server", font_size=24, color=WHITE)
        label_4.move_to(rect_4)
        elem_4 = VGroup(rect_4, label_4)

        arrow_5 = Arrow(start=[5.5, 1.0, 0], end=[-1.0, -0.5, 0], color="#00d4ff", stroke_width=4, buff=0.1)
        label_5 = Text("Response (IP)", font_size=20, color=WHITE)
        label_5.next_to(arrow_5, UP, buff=0.2)
        elem_5 = VGroup(arrow_5, label_5)

        elem_6 = Text("IP Address", font_size=36, color="#ffffff")
        elem_6.move_to([-1.0, -0.5, 0])

        rect_7 = Rectangle(width=2.0, height=1.5, color="#00d4ff", fill_opacity=0.2, stroke_width=3)
        rect_7.move_to([-4.0, -0.5, 0])
        label_7 = Text("Your Computer", font_size=24, color=WHITE)
        label_7.move_to(rect_7)
        elem_7 = VGroup(rect_7, label_7)


        # Animate elements by timing
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
        remaining = 15.0 - current_time
        if remaining > 0:
            self.wait(remaining)
