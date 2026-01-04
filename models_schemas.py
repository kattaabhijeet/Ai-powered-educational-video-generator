"""
Data models for the video generation pipeline.
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class Scene(BaseModel):
    """Represents a single scene in the video."""
    scene_number: int
    duration: float = Field(description="Duration in seconds")
    narration: str = Field(description="Voice-over text for this scene")
    visual_description: str = Field(description="What should be shown visually")
    key_concepts: List[str] = Field(default_factory=list, description="Main concepts to highlight")
    
    
class Script(BaseModel):
    """Complete script for the video."""
    topic: str
    total_duration: float = Field(description="Total video duration in seconds")
    scenes: List[Scene]
    style_notes: Optional[str] = None


class AnimationElement(BaseModel):
    """A single visual element in a scene."""
    element_type: str = Field(description="Type: rectangle, circle, arrow, text, etc.")
    label: Optional[str] = None
    color: str = Field(default="#00d4ff")
    position: Dict[str, float] = Field(default_factory=dict, description="x, y coordinates")
    size: Dict[str, float] = Field(default_factory=dict, description="width, height or radius")
    animation: str = Field(default="FadeIn", description="Entry animation type")
    timing: float = Field(default=0.0, description="When to appear in scene (seconds)")


class SceneBlueprint(BaseModel):
    """Animation blueprint for a single scene."""
    scene_number: int
    duration: float
    background_color: str = "#1a1a1a"
    elements: List[AnimationElement]
    transitions: List[str] = Field(default_factory=list)
    narration_text: str
    

class VideoBlueprint(BaseModel):
    """Complete animation blueprint for the video."""
    topic: str
    total_duration: float
    scene_blueprints: List[SceneBlueprint]
    style_profile: Dict[str, Any] = Field(default_factory=dict)
