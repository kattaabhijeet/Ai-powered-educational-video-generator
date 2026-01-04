"""
Command-line interface for the video generation system.
"""
import argparse
import sys
from pipeline import VideoPipeline
from config import Config


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="AI Video Generation System - Create educational explainer videos from any topic",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --topic "How DNS works"
  python main.py --topic "How HTTPS works" --output my_video
  python main.py --topic "How WebSockets work" --openai-tts
        """
    )
    
    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="The topic to create a video about"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output filename (without extension). Default: auto-generated from topic"
    )
    
    parser.add_argument(
        "--openai-tts",
        action="store_true",
        help="Use OpenAI TTS for narration (requires API key). Default: use free gTTS"
    )
    
    args = parser.parse_args()
    
    # Validate configuration
    try:
        Config.validate()
    except ValueError as e:
        print(f"[ERROR] Configuration Error: {e}")
        print("\nPlease create a .env file with your OpenAI API key:")
        print("  OPENAI_API_KEY=your_key_here")
        sys.exit(1)
    
    # Create pipeline
    pipeline = VideoPipeline(use_openai_tts=args.openai_tts)
    
    # Generate video
    try:
        results = pipeline.generate_video(args.topic, args.output)
        print("\n[DONE] Success! Your video has been generated.")
        print(f"\n[FOLDER] Output location: {results['video']}")
    except Exception as e:
        print(f"\n[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
