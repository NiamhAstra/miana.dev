# Blog Post Formatting

Everything in `_posts/` is markdown with YAML frontmatter. Jekyll compiles it to HTML using the `post` layout.

## File Naming

Posts follow the standard Jekyll convention:

```
_posts/YYYY-MM-DD-slug-goes-here.md
```

The date in the filename matters... it sets the post date and affects ordering. The slug becomes the URL path.

## Frontmatter

Every post needs YAML frontmatter at the top:

```yaml
---
layout: post
title: "Your Post Title"
date: 2026-01-15
tags: [tech, career]
description: "A brief description for SEO and social previews."
---
```

**Required fields:**
- `title` — displayed as the h1 and in meta tags
- `date` — publication date (overrides the filename date if different)

**Optional but recommended:**
- `tags` — array of tags for filtering on the blog index
- `description` — used for SEO meta description and social cards
- `excerpt` — alternative to description, same purpose

The layout defaults to `post` via `_config.yml` so you can omit it, but being explicit doesn't hurt.

## Standard Markdown

All the usual markdown works. Headers, bold, italic, links, lists. Jekyll uses Kramdown as the parser.

```markdown
## Section Heading

Regular paragraph text. **Bold** and *italic* work as expected.

- Bullet points
- Work fine

1. So do
2. Numbered lists

[Links work too](https://example.com)
```

## Code Blocks

Fenced code blocks with language hints get syntax highlighting via Rouge. The theme is Dracula-inspired.

````markdown
```kotlin
fun main() {
    println("Hello, world!")
}
```
````

Renders with proper highlighting:

```kotlin
fun main() {
    println("Hello, world!")
}
```

Inline code uses single backticks: `like this`.

## Terminal Blocks

For command-line examples, there's a custom terminal component that looks like a macOS terminal window.

```html
<div class="terminal">
  <div class="terminal-header">
    <span class="dot dot--red"></span>
    <span class="dot dot--yellow"></span>
    <span class="dot dot--green"></span>
  </div>
  <pre><code>$ echo "Hello from the terminal"
Hello from the terminal

$ ls -la
total 42
drwxr-xr-x  5 user user 4096 Jan  3 10:00 .</code></pre>
</div>
```

The dots are purely decorative. Put your commands and output inside the `<pre><code>` block. The styling handles the rest.

## Mermaid Diagrams

Mermaid.js is loaded site-wide, so diagrams just work. Use a `<pre class="mermaid">` block:

```html
<pre class="mermaid">
flowchart TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Do something]
    B -->|No| D[Do something else]
    C --> E[End]
    D --> E
</pre>
```

The theme is customised to match the site's violet colour scheme. Mermaid supports flowcharts, sequence diagrams, class diagrams and more... check their docs for the full syntax.

## Images

Drop images in `assets/images/` and reference them with markdown or HTML:

```markdown
![Alt text](/assets/images/your-image.jpg)
```

For more control over sizing or styling:

```html
<img src="/assets/images/your-image.jpg" alt="Description" class="your-class">
```

## Links

Internal links should use relative paths from root:

```markdown
[See my experience](/experience/)
[Another post](/blog/post-slug/)
```

External links work normally:

```markdown
[GitHub](https://github.com/NiamhAstra)
```

## Tags

Tags in the frontmatter show up on the post page and enable filtering on the blog index. Keep them lowercase and consistent. Common ones I use:

- `tech` — general technology topics
- `career` — career and professional development
- `backend` — backend engineering
- `devops` — CI/CD, infrastructure, automation
- `tutorial` — step-by-step guides
- `kotlin` — Kotlin-specific content

The blog index page has filter buttons that show/hide posts by tag. The JavaScript handles this client-side.

## Reading Time

Calculated automatically based on word count. Shows up in the post metadata. The include is at `_includes/reading-time.html` if you want to tweak the words-per-minute assumption.

## Things to Avoid

Don't use HTML comments for TODOs or notes... they'll end up in the compiled output. Use actual comments in your editor or just delete unfinished sections.

Don't put sensitive content in drafts and expect it to stay hidden. If it's in the repo, assume it's public.

Avoid massive inline images. Compress them first. The build doesn't optimise images automatically.
