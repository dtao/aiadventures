import glob
import os

from pathlib import Path

# Used for parsing YAML frontmatter
import frontmatter

# Used for rendering final HTML from template
import jinja2

# Used for parsing Markdown content
import marko

markdown = marko.Markdown(extensions=['gfm'])

# Get the base template that we'll use for every post.
with open('templates/summary.html') as f:
    template_content = f.read()

# Ensure the output directory exists.
Path('site/summaries').mkdir(parents=True, exist_ok=True)

# Produce a rendered HTML file for each summary.
summaries = []
for p in glob.glob('summaries/*/*.md'):
    filename = os.path.basename(p)
    slug, _ = os.path.splitext(filename)
    summary = frontmatter.load(p)
    template = jinja2.Template(template_content)
    output = template.render({
        'slug': slug,
        'title': summary['summary'],
        'content': markdown.convert(summary.content)
    })
    with open(f'site/summaries/{slug}.html', 'w+') as f:
        f.write(output)

    summaries.append({
        'slug': slug,
        'title': summary['summary']
    })

# Produce the rendered index page.
with open('templates/index.html') as f:
    template_content = f.read()

with open('README.md') as f:
    readme = f.read()

with open('site/index.html', 'w+') as f:
    template = jinja2.Template(template_content)
    output = template.render({
        'readme': markdown.convert(readme),
        'summaries': summaries
    })
    with open(f'site/index.html', 'w+') as f:
        f.write(output)
