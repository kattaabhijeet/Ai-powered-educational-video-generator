"""
Blueprint generator - converts scripts into animation blueprints.
"""
import json
from openai import OpenAI
from config import Config
from prompts import BLUEPRINT_GENERATION_PROMPT
from models_schemas import Script, VideoBlueprint


class BlueprintGenerator:
    """Converts video scripts into detailed animation blueprints."""
    
    def __init__(self):
        """Initialize the blueprint generator with OpenAI client."""
        client_kwargs = {"api_key": Config.OPENAI_API_KEY}
        if Config.OPENAI_BASE_URL:
            client_kwargs["base_url"] = Config.OPENAI_BASE_URL
        self.client = OpenAI(**client_kwargs)
        self.model = Config.OPENAI_MODEL
    
    def generate(self, script: Script) -> VideoBlueprint:
        """
        Generate an animation blueprint from a script.
        
        Args:
            script: The video script to convert
            
        Returns:
            VideoBlueprint with detailed animation instructions
        """
        print(f"[ART] Generating animation blueprint for: {script.topic}")
        
        # Convert script to JSON string
        script_json = json.dumps(script.model_dump(), indent=2)
        
        # Create the prompt
        prompt = BLUEPRINT_GENERATION_PROMPT.format(
            script_json=script_json,
            topic=script.topic
        )
        
        # Call GPT-4 with retry logic
        max_retries = 3  # Increased from 2
        for attempt in range(max_retries):
            try:
                # Lower temperature on retries for more consistent JSON
                temperature = 0.3 if attempt == 0 else 0.2 if attempt == 1 else 0.1
                
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an animation director. Always respond with valid JSON following the exact schema provided. Keep responses concise."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    temperature=temperature,
                    max_tokens=4000,  # Ensure complete response
                    response_format={"type": "json_object"}
                )
                
                # Parse the response
                content = response.choices[0].message.content
                
                # Robust JSON cleaning
                content = content.strip()
                
                # Remove markdown code blocks if present
                if content.startswith("```json"):
                    content = content[7:]  # Remove ```json
                if content.startswith("```"):
                    content = content[3:]  # Remove ```
                if content.endswith("```"):
                    content = content[:-3]  # Remove trailing ```
                
                content = content.strip()
                
                # Decode HTML entities (&amp; -> &, &quot; -> ", etc.)
                import html
                content = html.unescape(content)
                
                # Find JSON object boundaries
                if not content.startswith("{"):
                    start = content.find("{")
                    if start != -1:
                        content = content[start:]
                    else:
                        raise json.JSONDecodeError("No JSON object found", content, 0)
                
                if not content.endswith("}"):
                    end = content.rfind("}")
                    if end != -1:
                        content = content[:end + 1]
                    else:
                        raise json.JSONDecodeError("No closing brace found", content, len(content))
                
                # Remove any trailing commas before closing braces/brackets
                import re
                content = re.sub(r',(\s*[}\]])', r'\1', content)
                
                # Auto-complete truncated JSON if needed
                content = self._auto_complete_json(content)
                
                # Parse JSON
                blueprint_data = json.loads(content)
                
                # Validate and create VideoBlueprint object
                blueprint = VideoBlueprint(**blueprint_data)
                
                print(f"[OK] Generated blueprint with {len(blueprint.scene_blueprints)} scenes")
                total_elements = sum(len(scene.elements) for scene in blueprint.scene_blueprints)
                print(f"  Total animation elements: {total_elements}")
                
                return blueprint
                
            except json.JSONDecodeError as e:
                print(f"[WARN] JSON parse error (attempt {attempt + 1}/{max_retries}): {e}")
                if attempt == max_retries - 1:
                    # Save failed response for debugging
                    try:
                        with open("output/failed_blueprint_response.txt", "w", encoding="utf-8") as f:
                            f.write(content if 'content' in locals() else "No content available")
                        print(f"[DEBUG] Failed response saved to: output/failed_blueprint_response.txt")
                    except:
                        pass
                    print(f"[X] Error generating blueprint: {e}")
                    raise
                print("  Retrying...")
                continue
            except Exception as e:
                print(f"[X] Error generating blueprint: {e}")
                raise
    
    def _auto_complete_json(self, content: str) -> str:
        """Auto-complete truncated JSON by adding missing brackets."""
        # Count opening and closing brackets
        open_braces = content.count('{')
        close_braces = content.count('}')
        open_brackets = content.count('[')
        close_brackets = content.count(']')
        
        # Add missing closing brackets
        if open_brackets > close_brackets:
            content += ']' * (open_brackets - close_brackets)
        
        # Add missing closing braces
        if open_braces > close_braces:
            content += '}' * (open_braces - close_braces)
        
        return content
    
    def save_blueprint(self, blueprint: VideoBlueprint, output_path: str):
        """Save blueprint to JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(blueprint.model_dump(), f, indent=2, ensure_ascii=False)
        print(f"[OK] Blueprint saved to: {output_path}")


if __name__ == "__main__":
    # Test the blueprint generator
    from script_generator import ScriptGenerator
    
    # Generate a script first
    script_gen = ScriptGenerator()
    script = script_gen.generate("How HTTPS works")
    
    # Generate blueprint
    blueprint_gen = BlueprintGenerator()
    blueprint = blueprint_gen.generate(script)
    blueprint_gen.save_blueprint(blueprint, "output/test_blueprint.json")
    
    # Print summary
    print("\n" + "="*60)
    print("GENERATED BLUEPRINT")
    print("="*60)
    for scene in blueprint.scene_blueprints:
        print(f"\nScene {scene.scene_number}:")
        print(f"  Elements: {len(scene.elements)}")
        for elem in scene.elements[:3]:  # Show first 3 elements
            print(f"    - {elem.element_type}: {elem.label or 'unlabeled'}")
