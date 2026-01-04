"""
Simple demonstration scene showing the visual style.
This can be rendered directly with Manim to test the setup.
"""
from manim import *


class WebSocketStyleDemo(Scene):
    """Demonstrates the WebSocket video visual style."""
    
    def construct(self):
        # Set dark background
        self.camera.background_color = "#1a1a1a"
        
        # Title
        title = Text("WebSocket Communication", font_size=48, color=WHITE)
        title.to_edge(UP)
        self.play(FadeIn(title))
        self.wait(0.5)
        
        # Client (left side, cyan)
        client = Rectangle(
            width=2.5,
            height=1.8,
            color="#00d4ff",
            fill_opacity=0.2,
            stroke_width=3
        )
        client.shift(LEFT * 4)
        client_label = Text("Client", font_size=32, color=WHITE)
        client_label.move_to(client.get_center())
        client_group = VGroup(client, client_label)
        
        # Server (right side, orange)
        server = Rectangle(
            width=2.5,
            height=1.8,
            color="#ff6b35",
            fill_opacity=0.2,
            stroke_width=3
        )
        server.shift(RIGHT * 4)
        server_label = Text("Server", font_size=32, color=WHITE)
        server_label.move_to(server.get_center())
        server_group = VGroup(server, server_label)
        
        # Animate client and server appearing
        self.play(
            FadeIn(client_group),
            FadeIn(server_group)
        )
        self.wait(0.5)
        
        # Connection arrow (cyan)
        connection = Arrow(
            start=client.get_right(),
            end=server.get_left(),
            color="#00d4ff",
            stroke_width=4,
            buff=0.1
        )
        connection_label = Text("Handshake", font_size=24, color=WHITE)
        connection_label.next_to(connection, UP, buff=0.2)
        
        self.play(Write(connection))
        self.play(FadeIn(connection_label))
        self.wait(0.5)
        
        # Data packet (small circle moving)
        packet = Circle(radius=0.15, color="#00d4ff", fill_opacity=0.8)
        packet.move_to(client.get_right())
        
        self.play(GrowFromCenter(packet))
        self.play(
            packet.animate.move_to(server.get_left()),
            run_time=1.5,
            rate_func=linear
        )
        self.play(FadeOut(packet))
        
        # Response packet (orange, going back)
        response = Circle(radius=0.15, color="#ff6b35", fill_opacity=0.8)
        response.move_to(server.get_left())
        
        self.play(GrowFromCenter(response))
        self.play(
            response.animate.move_to(client.get_right()),
            run_time=1.5,
            rate_func=linear
        )
        self.play(FadeOut(response))
        
        self.wait(1)
        
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


# To render this scene, run:
# manim -pql demo_scene.py WebSocketStyleDemo
# 
# Options:
#   -p: preview after rendering
#   -q: quality (l=low, m=medium, h=high, k=4k)
#   -l: low quality (faster rendering)
