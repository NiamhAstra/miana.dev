#!/usr/bin/env python3
"""
Build PDF resume from YAML data using LaTeX.

Requirements:
  - Python: pyyaml, jinja2
  - System: texlive with xelatex, inter-font, texlive-fontsextra (for colorful version)
  
Install on Arch Linux:
  sudo pacman -S texlive-xetex texlive-latexextra texlive-fontsrecommended texlive-fontsextra inter-font
"""
import yaml
from jinja2 import Environment, FileSystemLoader
import subprocess
import os
import shutil
import sys

def latex_escape(text):
    if not isinstance(text, str):
        return text
    replacements = [
        ('\\', r'\textbackslash{}'),
        ('&', r'\&'),
        ('%', r'\%'),
        ('$', r'\$'),
        ('#', r'\#'),
        ('_', r'\_'),
        ('{', r'\{'),
        ('}', r'\}'),
        ('~', r'\textasciitilde{}'),
        ('^', r'\textasciicircum{}'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def build_template(template_name, output_name, data, env):
    template = env.get_template(template_name)
    rendered = template.render(resume=data)
    
    tex_file = f'latex/{output_name}.tex'
    with open(tex_file, 'w') as f:
        f.write(rendered)
    
    subprocess.run([
        'xelatex',
        '-interaction=nonstopmode',
        '-output-directory=latex',
        tex_file
    ], capture_output=True, text=True)
    
    pdf_file = f'latex/{output_name}.pdf'
    if not os.path.exists(pdf_file):
        print(f"  Failed: {template_name} - check latex/{output_name}.log")
        return False
    
    return True

def build_resume():
    if shutil.which('xelatex') is None:
        print("Error: xelatex not found. Please install texlive-xetex.")
        sys.exit(1)
    
    with open('_data/resume.yml', 'r') as f:
        data = yaml.safe_load(f)
    
    env = Environment(loader=FileSystemLoader('latex/'))
    env.filters['latex'] = latex_escape
    
    os.makedirs('assets/files', exist_ok=True)
    
    print("Building resumes...")
    
    if build_template('resume-template.tex.j2', 'resume', data, env):
        shutil.copy('latex/resume.pdf', 'assets/files/miana-winter-resume.pdf')
        print("  OK: assets/files/miana-winter-resume.pdf (colorful)")
    
    if build_template('resume-template-minimal.tex.j2', 'resume-minimal', data, env):
        shutil.copy('latex/resume-minimal.pdf', 'assets/files/miana-winter-resume-minimal.pdf')
        print("  OK: assets/files/miana-winter-resume-minimal.pdf (minimal)")
    
    print("Done.")

if __name__ == '__main__':
    build_resume()
