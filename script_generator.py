"""
AI-powered script generator using OpenAI GPT-4.
"""
import json
from openai import OpenAI
from config import Config
from prompts import SCRIPT_GENERATION_PROMPT
from models_schemas import Script


class ScriptGenerator:
    """Generates video scripts from topics using GPT-4."""
    
    def __init__(self):
        """Initialize the script generator with OpenAI client."""
        client_kwargs = {"api_key": Config.OPENAI_API_KEY}
        if Config.OPENAI_BASE_URL:
            client_kwargs["base_url"] = Config.OPENAI_BASE_URL
        self.client = OpenAI(**client_kwargs)
        self.model = Config.OPENAI_MODEL
    
    def generate(self, topic: str) -> Script:
        """
        Generate a video script for the given topic.
        
        Args:
            topic: The topic to create a video about
            
        Returns:
            Script object containing scenes and narration
        """
        print(f"[AI] Generating script for topic: {topic}")
        
        # Create the prompt
        prompt = SCRIPT_GENERATION_PROMPT.format(topic=topic)
        
        # Call GPT-4
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert educational content creator. Always respond with valid JSON."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                response_format={"type": "json_object"}
            )
            
            # Parse the response
            script_data = json.loads(response.choices[0].message.content)
            
            # Validate and create Script object
            script = Script(**script_data)
            
            print(f"[OK] Generated script with {len(script.scenes)} scenes")
            print(f"  Total duration: {script.total_duration}s")
            
            return script
            
        except Exception as e:
            print(f"[X] Error generating script: {e}")
            raise
    
    def save_script(self, script: Script, output_path: str):
        """Save script to JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(script.model_dump(), f, indent=2, ensure_ascii=False)
        print(f"[OK] Script saved to: {output_path}")


if __name__ == "__main__":
    # Test the script generator
    generator = ScriptGenerator()
    script = generator.generate("How DNS works")
    generator.save_script(script, "output/test_script.json")
    
    # Print the script
    print("\n" + "="*60)
    print("GENERATED SCRIPT")
    print("="*60)
    for scene in script.scenes:
        print(f"\nScene {scene.scene_number} ({scene.duration}s):")
        print(f"  Narration: {scene.narration}")
        print(f"  Visual: {scene.visual_description}")
