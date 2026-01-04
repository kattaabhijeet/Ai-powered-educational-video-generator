from manim import *

class PerfectScene(Scene):
    def construct(self):
        # Wide camera
        self.camera.frame_width = 18
        self.camera.background_color = "#0a0a0a"
        
        # Colorful rectangle
        rect_0 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.3,
            color="#00E5FF",
            fill_opacity=0.6,
            stroke_width=6
        )
        rect_0.move_to([-4.0, 0.0, 0])
        
        # Vibrant shadow
        shadow_0 = rect_0.copy()
        shadow_0.set_fill("#00E5FF", opacity=0.2)
        shadow_0.set_stroke(opacity=0)
        shadow_0.shift(DOWN*0.12 + RIGHT*0.12)
        
        # Label INSIDE (no overlap)
        label_0 = Text(
            "Your Computer", 
            font_size=16,
            weight=BOLD,
            color=WHITE
        )
        label_0.scale_to_fit_width(rect_0.width * 0.85)  # FIT inside
        label_0.move_to(rect_0)  # Centered
        
        elem_0 = VGroup(shadow_0, rect_0, label_0)

        # Vibrant arrow
        arrow_1 = Arrow(
            start=[-2.0, 0.0, 0],
            end=[0.0, 0.0, 0],
            color="#00E5FF",
            stroke_width=8,
            buff=0.4,
            max_tip_length_to_length_ratio=0.3
        )
        
        # Label ABOVE arrow (no overlap)
        label_1 = Text("Request to Resolver", font_size=16, weight=BOLD, color=WHITE)
        label_1.next_to(arrow_1, UP, buff=0.8)  # FAR above
        
        # Dark background for visibility
        label_bg_1 = BackgroundRectangle(
            label_1,
            color="#000000",
            fill_opacity=0.85,
            buff=0.25,
            corner_radius=0.2
        )
        
        elem_1 = VGroup(arrow_1, label_bg_1, label_1)

        # Colorful rectangle
        rect_2 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.3,
            color="#00E5FF",
            fill_opacity=0.6,
            stroke_width=6
        )
        rect_2.move_to([0.0, 0.0, 0])
        
        # Vibrant shadow
        shadow_2 = rect_2.copy()
        shadow_2.set_fill("#00E5FF", opacity=0.2)
        shadow_2.set_stroke(opacity=0)
        shadow_2.shift(DOWN*0.12 + RIGHT*0.12)
        
        # Label INSIDE (no overlap)
        label_2 = Text(
            "Local Resolver", 
            font_size=16,
            weight=BOLD,
            color=WHITE
        )
        label_2.scale_to_fit_width(rect_2.width * 0.85)  # FIT inside
        label_2.move_to(rect_2)  # Centered
        
        elem_2 = VGroup(shadow_2, rect_2, label_2)

        # Colorful text
        text_3 = Text(
            "Cache Miss",
            font_size=36,
            weight=BOLD,
            color="#FF6B35"
        )
        text_3.move_to([0.0, 0.8, 0])
        
        text_bg_3 = BackgroundRectangle(
            text_3,
            color="#000000",
            fill_opacity=0.7,
            buff=0.3,
            corner_radius=0.25
        )
        
        elem_3 = VGroup(text_bg_3, text_3)

        # Vibrant arrow
        arrow_4 = Arrow(
            start=[1.0, 0.0, 0],
            end=[3.0, 0.0, 0],
            color="#FF6B35",
            stroke_width=8,
            buff=0.4,
            max_tip_length_to_length_ratio=0.3
        )
        
        # Label ABOVE arrow (no overlap)
        label_4 = Text("Forward to Root", font_size=16, weight=BOLD, color=WHITE)
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

        # Colorful rectangle
        rect_5 = RoundedRectangle(
            width=2.0, height=1.5,
            corner_radius=0.3,
            color="#FF6B35",
            fill_opacity=0.6,
            stroke_width=6
        )
        rect_5.move_to([4.0, 0.0, 0])
        
        # Vibrant shadow
        shadow_5 = rect_5.copy()
        shadow_5.set_fill("#FF6B35", opacity=0.2)
        shadow_5.set_stroke(opacity=0)
        shadow_5.shift(DOWN*0.12 + RIGHT*0.12)
        
        # Label INSIDE (no overlap)
        label_5 = Text(
            "Root Server", 
            font_size=16,
            weight=BOLD,
            color=WHITE
        )
        label_5.scale_to_fit_width(rect_5.width * 0.85)  # FIT inside
        label_5.move_to(rect_5)  # Centered
        
        elem_5 = VGroup(shadow_5, rect_5, label_5)


        # Dynamic animations
        animations = [
            (elem_0, "GrowFromCenter", 0.0),
            (elem_1, "Write", 0.5),
            (elem_2, "GrowFromCenter", 1.0),
            (elem_3, "GrowFromCenter", 1.5),
            (elem_4, "Write", 2.0),
            (elem_5, "GrowFromCenter", 2.5),
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
        
        remaining = 10.0 - current_time
        if remaining > 0:
            self.wait(remaining)
