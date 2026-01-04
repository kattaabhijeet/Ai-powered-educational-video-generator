"""
Test the simple video generator with existing blueprint.
"""
import json
from simple_video_generator import SimpleVideoGenerator
from models_schemas import VideoBlueprint

# Load existing blueprint
with open("output/how_dns_works_video_blueprint.json", "r") as f:
    blueprint_data = json.load(f)

blueprint = VideoBlueprint(**blueprint_data)

# Generate video
video_gen = SimpleVideoGenerator()
video_gen.generate(blueprint, "output/how_dns_works_video.mp4")

print("\n[DONE] Video generation complete!")
print("Check output/how_dns_works_video.mp4")
