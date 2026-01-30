# Website Design Structure & Notes

This document describes the visual layout and structural organization of the Seb Hirsch portfolio website for future reference and maintenance.

## Visual Hierarchy: The "Six Bars" Layout
The website layout is organized into six distinct horizontal "bars" or strips from top to bottom. This creates a structured, cinematic rhythm to the page.

### 1. Navigation Header (Top Bar)
- **Background**: Black / Very Dark Grey (`#0a0a0a`)
- **Content**: Site Logo (Left), Main Navigation Menu (Right).
- **Behavior**: Sticky on desktop (remains at the top while scrolling).

### 2. Section Banner (Title Bar)
- **Background**: Medium Grey (`#8e8e8e`)
- **Content**: Large Page Title (e.g., "Projects", "Research & Development").
- **Purpose**: Immediate context for the user.

### 3. Content Body (Main Bar)
- **Background**: Dark Grey (`#1b1b1b`)
- **Content**: Intro text, Project/Photography tiles, and main page copy.
- **Note**: This is the primary interactive zone.

### 4. Footer Layer 1 (Imprint Bar)
- **Background**: Black (`#121212`)
- **Content**: "Imprint" link.
- **Design**: Separated from the content above by padding to mark the start of the footer.

### 5. Footer Layer 2 (Social Media Bar)
- **Background**: Black (`#121212`)
- **Content**: Six white social media icons (LinkedIn, Vimeo, GitHub, ArtStation, Sketchfab, IMDb).
- **Design**: Icons are white with centered alignment and generous vertical spacing.

### 6. Footer Layer 3 (Copyright Bar)
- **Background**: Black (`#121212`)
- **Content**: Copyright notice and current year.
- **Design**: Sits at the absolute bottom of the page.

---

## Content Organization
The content is split into two primary categories to distinguish between commercial output and technical craftsmanship.

### Projects Section (`/projects/`)
- **Focus**: Professional production work, client projects, and major film/TV titles.
- **Examples**: *The Avengers*, *Game of Thrones*, *Armenien*.

### R&D Section (`/rnd/`)
- **Focus**: Technical studies, experiments, research, and personal craft mastery.
- **Examples**: *Octopus Character Study* (ZBrush/Rigging), *Posca* (Anatomy), *Sky Lanterns* (Dynamics).
- **Concept**: Acts as a "Lab" to showcase your evolution as a Technical Director and Professor.

---

## Technical Maintenance Notes
- **Favicon**: The site uses a custom `favicon.png` located in `/static/favicon/`.
- **CSS**: Custom styles including the social icon scaling are defined in `/assets/css/main.css`.
- **Social Icons**: Managed via `layouts/partials/footer.html` using Tailwind utility classes for sizing (`w-6 h-6`) and Hugo parameters for enabled/disabled status.
