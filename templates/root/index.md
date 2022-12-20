---
title: /me
layout: home
permalink: /
---

# {{ name[0] }} {{ name[1] }} {{ name[2] }}
## {{ pronoun[0] }}/{{ pronoun[1] }}/{{ pronoun[2] }}
{{ contact.email }}
{{ contact.phone }}

# RELEVANT EXPERIENCE:

{% for job in work -%}
# {{ job.company }}
{{ job.role }}
{{ job.team }}
{{ job.time }}
{{ job.description.short }}

{% endfor %}
# SKILLS:
{% for skill in skills -%}
  - {{ skill }}
{% endfor %}

# EDUCATION:

{% for study in studies -%}
# {{ study.institute }}
{{ study.topic }}
{{ study.time }}

{% endfor %}
# PUBLICATIONS:

{% for publication in publications -%}
# {{ publication.title }}
## {{ publication.description }}
{{ publication.link }}

{% endfor %}
# ALGORITHMIC WORD SOUP:
{% for keyword in keywords -%}
  - {{ keyword }}
{% endfor %}