import os
import re

path = 'assets/icons'
for f in os.listdir(path):
    if f.endswith('.svg'):
        p = os.path.join(path, f)
        with open(p, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove width/height attributes
        content = re.sub(r'\s(width|height)="[^"]*"', '', content)
        
        # Replace specific hex fills with currentColor to allow Tailwind styling
        content = re.sub(r'fill="#[0-9a-fA-F]{3,6}"', 'fill="currentColor"', content)
        
        # If no fill was present on the svg tag, add it as currentColor
        if '<svg' in content and 'fill=' not in content:
            content = content.replace('<svg', '<svg fill="currentColor"')

        with open(p, 'w', encoding='utf-8') as file:
            file.write(content)

print("Icons optimized.")
