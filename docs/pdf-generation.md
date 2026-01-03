# PDF Resume Generation

The PDF resumes are generated from the same YAML that powers the website. A Python script reads `_data/resume.yml`, renders it through Jinja2 templates, and compiles the result with XeLaTeX.

## How It Works

```
_data/resume.yml → Python/Jinja2 → .tex file → XeLaTeX → .pdf
```

Two versions get built. The colourful one (`miana-winter-resume.pdf`) has violet accents, icons and styled headings. The minimal one (`miana-winter-resume-minimal.pdf`) is clean black and white with no icons... better for ATS systems that choke on fancy formatting.

## Requirements

**Python packages:**
```bash
pip install pyyaml jinja2
```

**System packages (Arch Linux):**
```bash
sudo pacman -S texlive-xetex texlive-latexextra texlive-fontsextra inter-font
```

**System packages (Ubuntu/Debian):**
```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra fonts-inter
```

## Building

From the project root:

```bash
python scripts/build-resume.py
```

Output looks like:
```
Building resumes...
  OK: assets/files/miana-winter-resume.pdf (colorful)
  OK: assets/files/miana-winter-resume-minimal.pdf (minimal)
Done.
```

## Templates

Both templates live in `latex/`:

| File | What it is |
|------|------------|
| `resume-template.tex.j2` | Colourful version with FontAwesome icons |
| `resume-template-minimal.tex.j2` | Minimal black and white version |

### Template Syntax

The templates use Jinja2 with a custom `latex` filter that escapes special characters. LaTeX doesn't like raw `&`, `%`, `$`, `#`, or `_` in text... the filter handles that.

```latex
\section*{Experience}
{% for job in resume.experience %}
\textbf{ {{- job.title | latex -}} } \hfill {{ job.start_date }} -- {{ job.end_date }}\\
{% endfor %}
```

### Page Break Control

Each entry is wrapped in a `minipage` to prevent awkward page breaks mid-entry:

```latex
\noindent\begin{minipage}{\textwidth}
% Entry content here
\end{minipage}
```

### Colours

The colourful template defines colours matching the website:

```latex
\definecolor{primary}{HTML}{7C3AED}
\definecolor{primarydark}{HTML}{5B21B6}
\definecolor{primarylight}{HTML}{EDE9FE}
\definecolor{textmain}{HTML}{1F2937}
\definecolor{textsecondary}{HTML}{6B7280}
```

## What the Script Does

`scripts/build-resume.py` runs through this process:

1. Checks for `xelatex` in PATH
2. Loads `_data/resume.yml`
3. Sets up Jinja2 with the `latex` escape filter
4. Renders each template to a `.tex` file
5. Runs `xelatex` to compile the PDF
6. Copies the PDFs to `assets/files/`

### LaTeX Escaping

The `latex_escape` function handles characters with special meaning in LaTeX:

```python
def latex_escape(text):
    replacements = [
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        # ... etc
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text
```

## Troubleshooting

**"xelatex not found"** — Install texlive-xetex. On Arch that's `sudo pacman -S texlive-xetex`.

**Font not found errors** — Make sure Inter is installed system-wide. The template falls back to Latin Modern Roman if Inter isn't available, but it won't look right.

**Missing fontawesome5** — Install texlive-fontsextra (Arch) or texlive-fonts-extra (Ubuntu).

**Build succeeds but PDF looks wrong** — Check `latex/resume.log` for warnings. Common culprit is unescaped special characters in the YAML data.
