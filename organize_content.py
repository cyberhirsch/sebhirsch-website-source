import os
import re
import shutil
from pathlib import Path

content_dir = Path(r"d:\Google Drive\Backup\Code\sebhirsch_com\content")
projects_dir = content_dir / "projects"
photography_dir = content_dir / "photography"
images_root = Path(r"d:\Google Drive\Backup\Code\sebhirsch_com\Images")

def humanize(s):
    return s.replace('-', ' ').replace('_', ' ').title()

def update_frontmatter(fm, key, value):
    # If key exists, replace it
    pattern = rf'^({key}:\s*).*'
    if re.search(pattern, fm, re.MULTILINE):
        return re.sub(pattern, rf'\1"{value}"', fm, flags=re.MULTILINE)
    else:
        # Add it
        return fm.strip() + f'\n{key}: "{value}"'

def process_projects():
    print("Processing projects...")
    if not projects_dir.exists():
        return
    for md_file in projects_dir.glob("*.md"):
        if md_file.name == "_index.md":
            continue
        
        name = md_file.stem
        project_folder = projects_dir / name
        project_folder.mkdir(exist_ok=True)
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n?(.*)', content, re.DOTALL | re.MULTILINE)
        if not match:
            continue
            
        frontmatter = match.group(1)
        body = match.group(2)
        
        # Extract featured_image using regex
        img_match = re.search(r'^featured_image:\s*"(.*)"', frontmatter, re.MULTILINE)
        if not img_match:
            img_match = re.search(r'^featured_image:\s*(.*)', frontmatter, re.MULTILINE)
            
        if img_match:
            featured_image = img_match.group(1).strip().strip('"').strip("'")
            if featured_image.startswith('/images/portfolio/'):
                img_name = Path(featured_image).name
                src_img = images_root / img_name
                if src_img.exists():
                    dest_img = project_folder / img_name
                    shutil.copy2(src_img, dest_img)
                    frontmatter = update_frontmatter(frontmatter, 'featured_image', img_name)
                    print(f"  Moved thumbnail for {name}")
                else:
                    print(f"  Warning: Source image {src_img} not found for {name}")
        
        new_content = f"---\n{frontmatter.strip()}\n---\n{body}"
        
        with open(project_folder / "index.md", 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        md_file.unlink()
        print(f"  Organized {name} into folder")

def process_photography():
    print("Processing photography...")
    if not photography_dir.exists():
        return
    for folder in photography_dir.iterdir():
        if not folder.is_dir():
            continue
        
        images = sorted([f for f in folder.iterdir() if f.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp', '.gif') and f.name != "featured_image.jpg"])
        
        index_file = folder / "index.md"
        frontmatter = ""
        body = ""
        
        if index_file.exists():
            with open(index_file, 'r', encoding='utf-8') as f:
                content = f.read()
            match = re.search(r'^---\s*\n(.*?)\n---\s*\n?(.*)', content, re.DOTALL | re.MULTILINE)
            if match:
                frontmatter = match.group(1)
                body = match.group(2)
        else:
            frontmatter = f'title: "{humanize(folder.name)}"\ndate: 2026-01-09T14:45:00+01:00'
            
        if not images:
            frontmatter = update_frontmatter(frontmatter, 'draft', 'true')
            print(f"  Gallery {folder.name} is empty, setting draft: true")
        else:
            frontmatter = update_frontmatter(frontmatter, 'draft', 'false')
            first_img = images[0]
            dest_img = folder / "featured_image.jpg"
            shutil.copy2(first_img, dest_img)
            frontmatter = update_frontmatter(frontmatter, 'featured_image', 'featured_image.jpg')
            print(f"  Set thumbnail for {folder.name} using {first_img.name}")
            
        new_content = f"---\n{frontmatter.strip()}\n---\n{body}"
        
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == "__main__":
    process_projects()
    process_photography()
