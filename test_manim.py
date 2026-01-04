"""
Test Manim video generator with existing blueprint.
"""
import json
from manim_video_generator import ManimVideoGenerator
from models_schemas import VideoBlueprint

print("Loading blueprint...")
with open("output/how_dns_works_video_blueprint.json", "r") as f:
    blueprint_data = json.load(f)

blueprint = VideoBlueprint(**blueprint_data)

print(f"\nGenerating animated video with Manim...")
print(f"This will take a few minutes - Manim renders high-quality animations\n")

gen = ManimVideoGenerator()
gen.generate(blueprint, "output/how_dns_works_manim.mp4")

print("\n" + "="*70)
print("[DONE] Manim video generation complete!")
print("="*70)
print("\nCheck output/ directory for:")
print("  - scene_1.mp4, scene_2.mp4, etc. (individual scenes)")
print("  - how_dns_works_manim.mp4 (combined video)")
