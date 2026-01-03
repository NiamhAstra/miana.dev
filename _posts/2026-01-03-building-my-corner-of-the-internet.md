---
layout: post
title: "Building My Corner of the Internet"
date: 2026-01-03
tags: [career, tech, devops]
description: "Why I built this site, the technical decisions behind it, and what I learned about creativity along the way."
thumbnail: /assets/images/blog/my-corner.png
---

I've had a LinkedIn profile for years. It works. Recruiters find me, I can list my experience, it does the job. But it never felt like *mine*. The algorithm decides what gets seen, the format is rigid, and I'm just renting space on someone else's platform.

So between jobs, with a free weekend ahead of me, I finally built the thing I'd been thinking about for years.

## The Problem

Anyone who's job hunted knows this pain. You update your resume PDF, then remember your LinkedIn is out of date, then realise your personal site still mentions a role from two years ago. Inconsistencies creep in. You forget which version has the better wording for that one achievement.

I wanted a single source of truth. One file that defines who I am professionally, which then generates everything else. Change one place, everything updates. That's it.

## Why Jekyll and LaTeX

I landed on Jekyll for the site and LaTeX for PDF generation. Both pull from the same YAML data file.

Jekyll had been on my radar for a while and it pairs nicely with GitHub Pages. No database, no server to maintain, just static files. Markdown for content, Liquid for templating. It makes sense.

LaTeX I've always loved. There's something about the output that just looks *right*... the typography, the spacing. And as an engineer, writing documents in a markup language feels natural. It's code. I understand code.

The architecture is simple:

<pre class="mermaid">
flowchart TD
    A[resume.yml] --> B[Jekyll]
    A --> C[Python + Jinja2]
    B --> D[Website]
    C --> E[LaTeX]
    E --> F[PDF Resume]
</pre>

A Python script reads the YAML, renders a Jinja2 template to LaTeX, compiles it with XeLaTeX. The Jekyll site reads the same YAML directly. One data file, two outputs.

## The Design

Purple is my favourite colour. That's the whole story there. I wanted something that felt like me, and violet makes an impact without being overwhelming. The rest follows from that... clean typography, plenty of whitespace, content first.

## The AI Thing

I built this with AI assistance and it changed how I think about these tools.

Going in, I figured AI would make things faster but maybe more generic. Trade creativity for efficiency. The opposite happened.

Having an AI pair programmer meant I could iterate on design decisions quickly. "Make the section headings purple with a subtle underline." "Actually, less padding." "What if the buttons had icons?" Each tweak took seconds instead of minutes. I could try more things, explore more directions, discover what I actually wanted through experimentation.

The AI helped flesh out the initial plan by asking questions about my goals. It handled the tedious parts... the CSS tweaks, the LaTeX syntax, the Sass migration... while I focused on decisions. What should this feel like? What's the right hierarchy? Does this represent me?

I didn't expect this, but AI made me *more* creative, not less. When iteration is cheap, you try things you wouldn't otherwise attempt.

## What I'm Hoping For

I don't have grand ambitions here. I don't need this to go viral or generate leads.

I just want keeping it updated to become a habit I enjoy rather than a chore. The single source of truth architecture should help. When I change jobs or pick up a new skill, I update one YAML file and everything follows.

It's mine. That's the point.

## Build Your Own Thing

If you've been thinking about building a personal site, or a blog, or any creative project... do it. Don't wait for the perfect weekend or the right tools or a complete vision. Start with what you have.

There's something satisfying about typing your own domain into a browser and seeing something you made. The tools are accessible. Hosting is practically free. The only thing stopping you is starting.
