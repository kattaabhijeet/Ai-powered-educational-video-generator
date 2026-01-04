# Fix Unicode emoji characters for Windows console
import os
import re

files_to_fix = [
    "audio_generator.py",
    "blueprint_generator.py",
    "main.py",
    "pipeline.py",
    "script_generator.py",
    "video_generator.py",
    "setup.py"
]

emoji_replacements = {
    "🚀": "[>>]",
    "🤖": "[AI]",
    "✓": "[OK]",
    "✗": "[X]",
    "🎨": "[ART]",
    "🎙️": "[MIC]",
    "🎬": "[VIDEO]",
    "✅": "[DONE]",
    "📊": "[STATS]",
    "📁": "[FOLDER]",
    "❌": "[ERROR]",
    "⚠": "[WARN]",
    "📝": "[NOTE]",
}

for filename in files_to_fix:
    filepath = f"d:/atg/atg assn 2/{filename}"
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for emoji, replacement in emoji_replacements.items():
        content = content.replace(emoji, replacement)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {filename}")

print("All files fixed!")
