# miana.io

Personal portfolio and resume site for Miana Ella Winter.

## What This Is

A Jekyll-based static site with a twist... the resume data lives in a single YAML file that generates both the website and a PDF resume via LaTeX. Update one file, everything stays in sync.

## Architecture

```
_data/resume.yml      ← Single source of truth
       │
       ├──→ Jekyll        → Website (GitHub Pages)
       │
       └──→ Python/Jinja2 → LaTeX → PDF Resume
```

## Quick Start

```bash
# Install dependencies
bundle install

# Run locally
bundle exec jekyll serve --livereload

# Build for production
JEKYLL_ENV=production bundle exec jekyll build
```

The site will be at `http://localhost:4000`.

## Building the PDF Resume

Requires LaTeX (texlive) and Python with PyYAML and Jinja2.

```bash
# Arch Linux
sudo pacman -S texlive-xetex texlive-latexextra texlive-fontsextra inter-font

# Build both PDF versions
python scripts/build-resume.py
```

This generates:
- `assets/files/miana-winter-resume.pdf` (colourful version)
- `assets/files/miana-winter-resume-minimal.pdf` (minimal version)

## Project Structure

```
├── _config.yml           # Jekyll config
├── _data/resume.yml      # Resume data (the single source of truth)
├── _layouts/             # Page templates
├── _includes/            # Reusable components
├── _sass/                # SCSS stylesheets
├── _posts/               # Blog posts
├── assets/
│   ├── css/              # Compiled styles
│   ├── js/               # JavaScript
│   ├── fonts/            # Self-hosted fonts
│   └── files/            # Generated PDFs
├── latex/
│   ├── resume-template.tex.j2          # Colourful template
│   └── resume-template-minimal.tex.j2  # Minimal template
├── scripts/
│   └── build-resume.py   # PDF generation script
└── pages/                # Additional pages
```

## Tech Stack

- **Site:** Jekyll 4.3, vanilla SCSS, vanilla JS
- **PDF:** XeLaTeX with Jinja2 templating
- **Hosting:** GitHub Pages
- **Fonts:** Inter, JetBrains Mono
- **Icons:** Devicon (skills), Lucide (UI)
- **Diagrams:** Mermaid.js

## Updating Resume Content

Edit `_data/resume.yml`. The structure is self-documenting... personal info, summary, skills, experience, education. Changes automatically reflect on the website. Run the build script to regenerate the PDFs.

## Writing Blog Posts

Drop a markdown file in `_posts/` with the standard Jekyll naming convention:

```
_posts/2026-01-15-your-post-title.md
```

Front matter:

```yaml
---
layout: post
title: "Your Post Title"
date: 2026-01-15
tags: [tech, career]
description: "A brief description for SEO and previews."
---
```

Mermaid diagrams work out of the box:

```html
<pre class="mermaid">
flowchart TD
    A[Start] --> B[End]
</pre>
```

## Deployment

Push to `main`. GitHub Actions builds and deploys to GitHub Pages automatically.

## Licence

Content is copyrighted. Code structure is CC0 if you want to use it as a starting point for your own site.
