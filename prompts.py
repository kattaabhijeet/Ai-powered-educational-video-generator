"""
Prompt templates for GPT-4 script and blueprint generation.
"""

SCRIPT_GENERATION_PROMPT = """You are an expert educational content creator specializing in technical explainer videos.

Topic: {topic}

Create a detailed script for a 30-60 second educational video about this topic. The video should:
- Explain the concept clearly and concisely
- Break down into 3-5 scenes
- Use simple language accessible to beginners
- Focus on visual explanations

Visual Style Reference:
- Dark minimalist design
- Flowchart/diagram-based explanations
- Client-server architecture visualizations
- Geometric shapes (rectangles, circles, arrows)
- Color coding: Cyan for client-side, Orange for server-side

Return a JSON object with this structure:
{{
  "topic": "{topic}",
  "total_duration": 45.0,
  "scenes": [
    {{
      "scene_number": 1,
      "duration": 8.0,
      "narration": "Voice-over text for this scene",
      "visual_description": "What should be shown on screen",
      "key_concepts": ["concept1", "concept2"]
    }}
  ]
}}

Make it engaging, clear, and visually descriptive!"""


BLUEPRINT_GENERATION_PROMPT = """You are a SENIOR EDUCATIONAL MOTION DESIGNER and MANIM ENGINEER.
Your task is to generate PROFESSIONAL, CONCEPT-FIRST educational animations,
similar in style to ByteByteGo, Fireship (calm scenes), and modern explainer videos.

Script to Visualize:
{script_json}

STRICT DESIGN PRINCIPLES (DO NOT VIOLATE):

1. TEACH IDEAS, NOT RAW DATA
   - Never dump full technical structures at once.
   - Reveal complexity progressively.
   - Prefer abstraction before precision.

2. ONE SCENE = ONE IDEA
   - Each scene must communicate a single concept clearly.
   - Avoid overcrowding.
   - Use pauses between ideas.

3. VISUAL METAPHORS FIRST
   - Use icons, symbols, and cards instead of literal diagrams.
   - Examples:
     * Chat → chat bubble icon
     * Streaming → play or Twitch-like icon
     * Internet → globe icon
     * Realtime data → graph icon

4. CONSISTENT VISUAL SYSTEM
   - Background: #0F172A (dark slate)
   - Cards: white or light-gray rounded rectangles
   - Icons: monochrome, flat, centered
   - Text: minimal labels only (never paragraphs)

5. GRID-BASED LAYOUT
   - Align all elements to an invisible grid.
   - Symmetry and spacing are mandatory.
   - Avoid arbitrary coordinates.
   - Use clean spacing: x positions like -4, -2, 0, 2, 4
   - Use clean spacing: y positions like -2, -1, 0, 1, 2

6. TYPOGRAPHY RULES
   - Use modern sans-serif style
   - Titles: larger (font_size: 48), bold
   - Labels: small (font_size: 24), medium weight
   - Never mix font styles

7. COLOR RULES (MAX 3 COLORS)
   - Accent color: #FF6B35 (orange) for emphasis
   - Neutral: #FFFFFF (white) for text
   - Secondary: #00D4FF (cyan) for highlights
   - Background: #0F172A (dark) stays quiet
   - Never use random colors

8. ANIMATION STYLE
   - Use slow, smooth animations only
   - Preferred: FadeIn, FadeOut, gentle animations
   - animation timing (run_time): between 1.0 – 1.5 seconds
   - Use smooth easing
   - Avoid flashy effects

9. NEGATIVE SPACE IS IMPORTANT
   - Leave empty space intentionally
   - Bigger spacing looks more professional
   - Don't fill every corner

10. ELEMENT SPECIFICATIONS
    - Rectangles: rounded corners, width 2-3, height 1.5-2
    - Text: centered, concise labels (max 2-3 words)
    - Arrows: simple, labeled with action verbs
    - Icons: represented as small circles or simple shapes

CRITICAL ANTI-OVERLAP RULES (MANDATORY):

1. NO OVERLAPPING — EVER
   - Text must NEVER overlap with other text, shapes, arrows, or borders
   - If space is insufficient, increase container size automatically
   - This is the #1 rule - violating it is unacceptable

2. SEPARATE LABELS AND CONTENT
   - Container labels (e.g., "Server", "Client", "DB") must be placed OUTSIDE or TOP-aligned
   - Internal content must be centered and minimal
   - Never place label text inside small containers

3. INTERNAL PADDING RULE
   - All text inside shapes must use 70-80% of container width
   - Never allow text to touch edges
   - If text is too long, make the container bigger

4. STACK MULTIPLE TEXTS
   - If a container has more than one text element, use vertical stacking
   - Never manually position multiple texts in the same space
   - Use generous vertical spacing between stacked items

5. GENEROUS SPACING
   - Prefer larger containers and more empty space
   - Minimum spacing between elements: 1.5 units
   - If the layout feels slightly too spaced, it is correct

6. ARROWS MUST AVOID TEXT
   - Arrows must attach to container edges, never cross text
   - Always use sufficient buffer (buff ≥ 0.3)
   - Arrow labels must be positioned FAR above/below the arrow line

7. GRID-ALIGNED LAYOUT
   - Align elements symmetrically using the grid system
   - Avoid random offsets that cause elements to crowd
   - Use positions: x = -4, -2, 0, 2, 4 (with spacing)
   - Use positions: y = -2, -1, 0, 1, 2 (with spacing)

8. FONT HIERARCHY FOR CLARITY
   - Scene titles: font_size 48, positioned well above content
   - Container labels: font_size 24, positioned outside containers
   - Internal text: font_size 18, scaled to fit inside containers

9. FAIL-SAFE RULE
   - If overlap risk is detected, take action:
     * Increase container size (width/height)
     * Reduce text size (font_size)
     * Or move text outside the container
   - Never accept overlap as a solution

10. POSITIONING STRATEGY
    - For text inside rectangles: center it, scale to 70% width
    - For text labels: position ABOVE container (y + height/2 + 0.5)
    - For arrow labels: position FAR above arrow (y + 1.0 minimum)
    - For scene titles: position at top (y = 3.0 or higher)

Return a JSON object with this structure:
{{
  "topic": "{topic}",
  "total_duration": 45.0,
  "scene_blueprints": [
    {{
      "scene_number": 1,
      "duration": 8.0,
      "background_color": "#0F172A",
      "narration_text": "Voice-over text",
      "elements": [
        {{
          "element_type": "rectangle",
          "label": "Concept Card",
          "color": "#FF6B35",
          "position": {{"x": 0, "y": 0}},
          "size": {{"width": 3, "height": 2}},
          "animation": "FadeIn",
          "timing": 0.0
        }},
        {{
          "element_type": "text",
          "label": "Main Title",
          "color": "#FFFFFF",
          "position": {{"x": 0, "y": 2}},
          "size": {{"font_size": 48}},
          "animation": "FadeIn",
          "timing": 0.5
        }},
        {{
          "element_type": "circle",
          "label": "Icon",
          "color": "#00D4FF",
          "position": {{"x": -3, "y": 0}},
          "size": {{"radius": 0.5}},
          "animation": "FadeIn",
          "timing": 1.0
        }},
        {{
          "element_type": "arrow",
          "label": "Flow",
          "color": "#FFFFFF",
          "position": {{"x_start": -2, "y_start": 0, "x_end": 2, "y_end": 0}},
          "size": {{}},
          "animation": "FadeIn",
          "timing": 2.0
        }}
      ],
      "transitions": ["FadeOut"]
    }}
  ]
}}

KEY REQUIREMENTS (IN ORDER OF PRIORITY):

1. ZERO OVERLAP (HIGHEST PRIORITY)
   - Text must NEVER overlap with shapes, arrows, or other text
   - Use generous spacing (minimum 1.5 units between elements)
   - Scale text to 70-80% of container width
   - Position labels OUTSIDE containers when possible
   - Arrow labels positioned FAR above/below arrows (y ± 1.0 minimum)

2. PROFESSIONAL LAYOUT
   - Grid-aligned positions (clean numbers only: -4, -2, 0, 2, 4)
   - Symmetric, balanced composition
   - Intentional negative space

3. VISUAL CLARITY
   - Interpret the script semantically (concept-level), not literally
   - Use visual metaphors (icons, cards) instead of technical diagrams
   - Max 3-5 elements per scene

4. SMOOTH ANIMATIONS
   - Smooth, slow animations (timing: 1.0-1.5s apart)
   - FadeIn/FadeOut preferred

5. COLOR DISCIPLINE
   - Dark background (#0F172A) always
   - Limited color palette (orange #FF6B35, cyan #00D4FF, white #FFFFFF)

The result must look like a PROFESSIONAL YOUTUBE EXPLAINER FRAME with ZERO OVERLAP,
not a classroom chalkboard!"""


STYLE_ANALYSIS_SUMMARY = """
Visual Style: Professional YouTube Explainer (ByteByteGo/Fireship Style)

Design Philosophy:
- Concept-first, not data-first
- Visual metaphors over literal diagrams
- Grid-based, symmetric layouts
- Generous negative space

Key Characteristics:
1. Background: Dark slate (#0F172A) - quiet and professional
2. Color Palette (MAX 3):
   - Accent: Orange (#FF6B35) for emphasis
   - Highlight: Cyan (#00D4FF) for secondary elements
   - Text: White (#FFFFFF) for clarity
3. Geometric Elements:
   - Rounded rectangles (width 2-3, height 1.5-2)
   - Simple circles for icons (radius 0.5-1.0)
   - Clean arrows for flow
4. Grid-Aligned Positioning:
   - X-axis: -4, -2, 0, 2, 4 (clean increments)
   - Y-axis: -2, -1, 0, 1, 2 (clean increments)
5. Typography:
   - Modern sans-serif style
   - Titles: 48px, bold
   - Labels: 24px, medium weight
6. Animation Style:
   - Slow and smooth (1.0-1.5s timing)
   - FadeIn/FadeOut preferred
   - Progressive revelation
7. Scene Structure:
   - ONE concept per scene
   - 3-5 elements maximum
   - Intentional negative space
8. Visual Metaphors:
   - Icons instead of detailed diagrams
   - Cards for concepts
   - Simple symbols for actions

Perfect for professional educational explainer videos.
"""
