# Site Structure

This is a Jekyll 4.3 site. Static HTML, no database, no server-side logic. GitHub Pages builds and hosts it.

## The Stack

Jekyll handles templating and builds. SCSS compiles to a single CSS file. One vanilla JS file handles interactivity. Fonts are self-hosted. That's pretty much it.

No frameworks, no build tools beyond what Jekyll provides. I wanted something I could understand completely and maintain years from now.

## Directory Layout

```
├── _config.yml           # Jekyll config
├── _data/
│   └── resume.yml        # Single source of truth for resume content
├── _includes/            # Reusable HTML partials
├── _layouts/             # Page templates
├── _posts/               # Blog posts (markdown)
├── _sass/                # SCSS source files
├── assets/
│   ├── css/main.scss     # SCSS entry point
│   ├── js/main.js        # All client-side JS
│   ├── fonts/            # Self-hosted Inter and JetBrains Mono
│   ├── images/           # Site images
│   └── files/            # Generated PDFs
├── docs/                 # Internal documentation (you're here)
├── latex/                # LaTeX templates for PDF generation
├── pages/                # Static pages (about, blog index, etc.)
└── scripts/              # Build scripts
```

## SCSS Architecture

The styles follow a loose ITCSS-inspired structure. Everything compiles through `assets/css/main.scss`.

```
_sass/
├── _variables.scss       # Colours, spacing, breakpoints, fonts
├── _reset.scss           # CSS reset / normalisation
├── _typography.scss      # Font faces, base type styles
├── _base.scss            # HTML element defaults
├── _layout.scss          # Container, grid utilities
├── _utilities.scss       # Helper classes
├── _animations.scss      # Scroll animations, transitions
├── _syntax.scss          # Code syntax highlighting (Dracula theme)
├── _print.scss           # Print stylesheet
├── components/           # Reusable UI components
│   ├── _buttons.scss
│   ├── _cards.scss
│   ├── _badges.scss
│   ├── _terminal.scss    # Terminal-style code blocks
│   ├── _timeline.scss    # Experience timeline
│   ├── _forms.scss
│   ├── _anchor-links.scss
│   ├── _toast.scss
│   └── _skip-link.scss
└── sections/             # Page-specific sections
    ├── _navigation.scss
    ├── _hero.scss
    ├── _skills.scss
    ├── _experience.scss
    ├── _education.scss
    ├── _speaking.scss
    ├── _blog.scss
    ├── _contact.scss
    ├── _footer.scss
    └── _error.scss
```

Each partial uses `@use '../variables' as *` to access shared variables. No global imports... everything is explicit.

## Variables

The colour palette lives in `_variables.scss`. The primary violet runs through everything.

```scss
$color-primary: #7C3AED;
$color-primary-dark: #5B21B6;
$color-primary-light: #EDE9FE;

$color-text: #1F2937;
$color-text-secondary: #6B7280;

$color-bg: #FFFFFF;
$color-surface: #F9FAFB;
$color-border: #E5E7EB;
```

Spacing uses a consistent scale. Typography has two font families: Inter for body text and JetBrains Mono for code.

## Layouts

Four layouts handle all pages:

**default.html** is the base. Includes the header, footer, SEO tags, font preloads and the Mermaid script. Everything else extends this.

**home.html** is the index page. Pulls sections from includes based on resume.yml data.

**post.html** wraps blog posts. Adds breadcrumbs, reading time, tags and a back link.

**page.html** is for static pages like the blog index or error pages.

## Includes

The `_includes/` folder has reusable partials. Most pull data from `_data/resume.yml` so the homepage builds itself from the YAML.

The main ones:
- `header.html` and `footer.html` for site chrome
- `hero.html`, `skills.html`, `experience.html`, etc. for homepage sections
- `schema-person.html` and `schema-blogpost.html` for structured data
- `reading-time.html` calculates post reading time

## JavaScript

One file: `assets/js/main.js`. About 200 lines. Handles:
- Scroll-triggered animations via IntersectionObserver
- Mobile navigation toggle
- Header shrink on scroll
- Contact form submission (Formspree)
- Blog tag filtering
- Anchor link copying with toast notification

No jQuery, no frameworks. Just vanilla JS with modern browser APIs.

## External Dependencies

Kept to a minimum:
- **Devicon** (CDN) for technology icons on the skills section
- **Mermaid** (CDN, ES module) for diagrams in blog posts
- **Formspree** for the contact form backend

Everything else is self-hosted.

## Building Locally

```bash
bundle install
bundle exec jekyll serve --livereload
```

The site runs at `http://localhost:4000`. Changes to SCSS, markdown and templates trigger a rebuild automatically.

For production builds:

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

This outputs to `_site/`. GitHub Actions handles this on push to main.
