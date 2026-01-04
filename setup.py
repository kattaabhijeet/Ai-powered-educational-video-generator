"""
Setup and installation verification script.
"""
import sys
import subprocess


def check_python_version():
    """Check if Python version is 3.8+"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"[OK] Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"[X] Python {version.major}.{version.minor} (requires 3.8+)")
        return False


def install_dependencies():
    """Install required packages."""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("[OK] Dependencies installed")
        return True
    except subprocess.CalledProcessError:
        print("[X] Failed to install dependencies")
        return False


def check_env_file():
    """Check if .env file exists."""
    import os
    if os.path.exists(".env"):
        print("[OK] .env file found")
        return True
    else:
        print("[WARN] .env file not found")
        print("  Creating from template...")
        try:
            with open(".env.example", "r") as src:
                with open(".env", "w") as dst:
                    dst.write(src.read())
            print("[OK] Created .env file - please add your OpenAI API key")
            return False
        except Exception as e:
            print(f"[X] Failed to create .env: {e}")
            return False


def verify_imports():
    """Verify all required modules can be imported."""
    print("\n🔍 Verifying imports...")
    modules = [
        "openai",
        "manim",
        "ffmpeg",
        "gtts",
        "dotenv",
        "pydantic"
    ]
    
    all_ok = True
    for module in modules:
        try:
            __import__(module)
            print(f"  [OK] {module}")
        except ImportError:
            print(f"  [X] {module} (not installed)")
            all_ok = False
    
    return all_ok


def main():
    """Run setup verification."""
    print("="*60)
    print("[>>] VIDEO GENERATION SYSTEM - SETUP VERIFICATION")
    print("="*60)
    
    # Check Python version
    if not check_python_version():
        print("\n[ERROR] Please upgrade to Python 3.8 or higher")
        return
    
    # Check/create .env file
    env_ok = check_env_file()
    
    # Install dependencies
    if not install_dependencies():
        print("\n[ERROR] Setup failed - could not install dependencies")
        return
    
    # Verify imports
    if not verify_imports():
        print("\n[ERROR] Some modules failed to import")
        print("Try running: pip install -r requirements.txt")
        return
    
    print("\n" + "="*60)
    if env_ok:
        print("[DONE] SETUP COMPLETE - Ready to generate videos!")
        print("\nTry running:")
        print('  python main.py --topic "How DNS works"')
    else:
        print("[WARN] SETUP ALMOST COMPLETE")
        print("\nNext steps:")
        print("  1. Edit .env file and add your OpenAI API key")
        print("  2. Run: python main.py --topic \"How DNS works\"")
    print("="*60)


if __name__ == "__main__":
    main()
