import glob
import os
import shutil

from datetime import datetime
from pathlib import Path

# Used for parsing YAML frontmatter
import frontmatter

# Used for rendering final HTML from template
import jinja2

# Used for parsing Markdown content
import markdown

def render_markdown(text):
    return markdown.markdown(text, extensions=['footnotes', 'smarty'])

# Ensure the output directory exists for summary pages.
Path('site/summaries').mkdir(parents=True, exist_ok=True)

# Ensure the output directory exists for 'thoughts'.
Path('site/thoughts').mkdir(parents=True, exist_ok=True)

# Ensure the output directory exists for images.
Path('site/images').mkdir(parents=True, exist_ok=True)

# Produce a rendered HTML file for each summary.
with open('templates/summary.html') as f:
    template_content = f.read()

summaries = []
for p in glob.glob('summaries/*/*'):
    filename = os.path.basename(p)
    slug, ext = os.path.splitext(filename)

    if ext == '.md':
        summary = frontmatter.load(p)
        title_date = datetime.strftime(summary['date'], '%b %-d, %Y')
        template = jinja2.Template(template_content)
        output = template.render({
            'slug': slug,
            'title': summary['summary'],
            # The frontmatter library strips out the trailing newline character;
            # add it back in to ensure links are rendered properly.
            'content': render_markdown(summary.content + '\n'),
            'url': summary['url'],
            'title_date': title_date,
            'date': summary['date']
        })
        with open(f'site/summaries/{slug}.html', 'w+') as f:
            f.write(output)

        summaries.append({
            'slug': slug,
            'title': summary['summary'],
            'url': summary['url'],
            'title_date': title_date,
            'date': summary['date']
        })

    # Copy images to the 'images' directory.
    elif ext in ('.gif', '.jpg', '.jpeg', '.png'):
        shutil.copyfile(p, f'site/images/{filename}')

# Produce a rendered HTML file for each 'thought'.
with open('templates/thought.html') as f:
    template_content = f.read()

thoughts = []
for p in glob.glob('thoughts/*'):
    filename = os.path.basename(p)
    slug, ext = os.path.splitext(filename)

    if ext == '.md':
        thought = frontmatter.load(p)
        title_date = datetime.strftime(thought['date'], '%b %-d, %Y')
        template = jinja2.Template(template_content)
        output = template.render({
            'slug': slug,
            'title': thought['summary'],
            # The frontmatter library strips out the trailing newline character;
            # add it back in to ensure links are rendered properly.
            'content': render_markdown(thought.content + '\n'),
            'title_date': title_date,
            'date': thought['date']
        })
        with open(f'site/thoughts/{slug}.html', 'w+') as f:
            f.write(output)

        thoughts.append({
            'slug': slug,
            'title': thought['summary'],
            'title_date': title_date,
            'date': thought['date']
        })

# Produce the rendered index page.
with open('templates/index.html') as f:
    template_content = f.read()

with open('README.md') as f:
    readme = f.read()

with open('site/index.html', 'w+') as f:
    template = jinja2.Template(template_content)
    output = template.render({
        'readme': render_markdown(readme),
        'summaries': sorted(summaries, key=lambda s: s['date'], reverse=True),
        'thoughts': sorted(thoughts, key=lambda t: t['date'], reverse=True)
    })
    with open(f'site/index.html', 'w+') as f:
        f.write(output)
