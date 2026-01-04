from manim import *

class EnhancedScene(Scene):
    def construct(self):
        # Enhanced camera frame (wider to prevent cropping)
        self.camera.frame_width = 18
        self.camera.background_color = "#1a1a1a"
        
        # Enhanced rectangle with rounded corners and gradient
        rect_0 = RoundedRectangle(
            width=2.0, 
            height=1.5,
            corner_radius=0.25,
            color="#ff6b35",
            fill_opacity=0.4,
            stroke_width=4
        )
        rect_0.move_to([-2.0, 1.0, 0])
        
        # Add subtle shadow
        shadow_0 = rect_0.copy()
        shadow_0.set_fill(BLACK, opacity=0.3)
        shadow_0.set_stroke(opacity=0)
        shadow_0.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Label positioned INSIDE rectangle (no overlap)
        label_0 = Text(
            "Root Server", 
            font_size=22,
            weight=BOLD,
            color=WHITE
        )
        label_0.move_to(rect_0)  # Centered in box
        
        elem_0 = VGroup(shadow_0, rect_0, label_0)

        # Enhanced arrow with better visibility
        arrow_1 = Arrow(
            start=[-1.0, 1.0, 0],
            end=[1.0, 1.0, 0],
            color="#ff6b35",
            stroke_width=6,
            buff=0.2,
            max_tip_length_to_length_ratio=0.2
        )
        
        # Arrow label with background (better visibility)
        label_1 = Text("Root â†’ TLD", font_size=20, weight=BOLD, color=WHITE)
        label_1.next_to(arrow_1, UP, buff=0.4)  # More space
        
        # Add background to label
        label_bg_1 = BackgroundRectangle(
            label_1,
            color=BLACK,
            fill_opacity=0.7,
            buff=0.15,
            corner_radius=0.1
        )
        
        elem_1 = VGroup(arrow_1, label_bg_1, label_1)

        # Enhanced rectangle with rounded corners and gradient
        rect_2 = RoundedRectangle(
            width=2.5, 
            height=1.5,
            corner_radius=0.25,
            color="#ff6b35",
            fill_opacity=0.4,
            stroke_width=4
        )
        rect_2.move_to([2.0, 1.0, 0])
        
        # Add subtle shadow
        shadow_2 = rect_2.copy()
        shadow_2.set_fill(BLACK, opacity=0.3)
        shadow_2.set_stroke(opacity=0)
        shadow_2.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Label positioned INSIDE rectangle (no overlap)
        label_2 = Text(
            "TLD (.com) Server", 
            font_size=22,
            weight=BOLD,
            color=WHITE
        )
        label_2.move_to(rect_2)  # Centered in box
        
        elem_2 = VGroup(shadow_2, rect_2, label_2)

        # Enhanced arrow with better visibility
        arrow_3 = Arrow(
            start=[3.5, 1.0, 0],
            end=[5.5, 1.0, 0],
            color="#ff6b35",
            stroke_width=6,
            buff=0.2,
            max_tip_length_to_length_ratio=0.2
        )
        
        # Arrow label with background (better visibility)
        label_3 = Text("TLD â†’ Auth", font_size=20, weight=BOLD, color=WHITE)
        label_3.next_to(arrow_3, UP, buff=0.4)  # More space
        
        # Add background to label
        label_bg_3 = BackgroundRectangle(
            label_3,
            color=BLACK,
            fill_opacity=0.7,
            buff=0.15,
            corner_radius=0.1
        )
        
        elem_3 = VGroup(arrow_3, label_bg_3, label_3)

        # Enhanced rectangle with rounded corners and gradient
        rect_4 = RoundedRectangle(
            width=3.0, 
            height=1.5,
            corner_radius=0.25,
            color="#ff6b35",
            fill_opacity=0.4,
            stroke_width=4
        )
        rect_4.move_to([6.5, 1.0, 0])
        
        # Add subtle shadow
        shadow_4 = rect_4.copy()
        shadow_4.set_fill(BLACK, opacity=0.3)
        shadow_4.set_stroke(opacity=0)
        shadow_4.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Label positioned INSIDE rectangle (no overlap)
        label_4 = Text(
            "Authoritative Server", 
            font_size=22,
            weight=BOLD,
            color=WHITE
        )
        label_4.move_to(rect_4)  # Centered in box
        
        elem_4 = VGroup(shadow_4, rect_4, label_4)

        # Enhanced arrow with better visibility
        arrow_5 = Arrow(
            start=[5.5, 1.0, 0],
            end=[-1.0, -0.5, 0],
            color="#00d4ff",
            stroke_width=6,
            buff=0.2,
            max_tip_length_to_length_ratio=0.2
        )
        
        # Arrow label with background (better visibility)
        label_5 = Text("Response (IP)", font_size=20, weight=BOLD, color=WHITE)
        label_5.next_to(arrow_5, UP, buff=0.4)  # More space
        
        # Add background to label
        label_bg_5 = BackgroundRectangle(
            label_5,
            color=BLACK,
            fill_opacity=0.7,
            buff=0.15,
            corner_radius=0.1
        )
        
        elem_5 = VGroup(arrow_5, label_bg_5, label_5)

        # Enhanced text with background
        text_6 = Text(
            "IP Address",
            font_size=36,
            weight=BOLD,
            color="#ffffff"
        )
        text_6.move_to([-1.0, -0.5, 0])
        
        text_bg_6 = BackgroundRectangle(
            text_6,
            color=BLACK,
            fill_opacity=0.5,
            buff=0.2,
            corner_radius=0.15
        )
        
        elem_6 = VGroup(text_bg_6, text_6)

        # Enhanced rectangle with rounded corners and gradient
        rect_7 = RoundedRectangle(
            width=2.0, 
            height=1.5,
            corner_radius=0.25,
            color="#00d4ff",
            fill_opacity=0.4,
            stroke_width=4
        )
        rect_7.move_to([-4.0, -0.5, 0])
        
        # Add subtle shadow
        shadow_7 = rect_7.copy()
        shadow_7.set_fill(BLACK, opacity=0.3)
        shadow_7.set_stroke(opacity=0)
        shadow_7.shift(DOWN*0.08 + RIGHT*0.08)
        
        # Label positioned INSIDE rectangle (no overlap)
        label_7 = Text(
            "Your Computer", 
            font_size=22,
            weight=BOLD,
            color=WHITE
        )
        label_7.move_to(rect_7)  # Centered in box
        
        elem_7 = VGroup(shadow_7, rect_7, label_7)


        # Animate elements
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
        
        remaining = 15.0 - current_time
        if remaining > 0:
            self.wait(remaining)
