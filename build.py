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
import marko

markdown = marko.Markdown(extensions=['gfm'])

# Get the base template that we'll use for every post.
with open('templates/summary.html') as f:
    template_content = f.read()

# Ensure the output directory exists for summary pages.
Path('site/summaries').mkdir(parents=True, exist_ok=True)

# Ensure the output directory exists for images.
Path('site/images').mkdir(parents=True, exist_ok=True)

# Produce a rendered HTML file for each summary.
summaries = []
for p in glob.glob('summaries/*/*'):
    filename = os.path.basename(p)
    slug, ext = os.path.splitext(filename)

    if ext == '.md':
        summary = frontmatter.load(p)
        date = datetime.strftime(summary['date'], '%b %-d, %Y')
        template = jinja2.Template(template_content)
        output = template.render({
            'slug': slug,
            'title': summary['summary'],
            # The frontmatter library strips out the trailing newline character;
            # add it back in to ensure links are rendered properly.
            'content': markdown.convert(summary.content + '\n'),
            'url': summary['url'],
            'date': date
        })
        with open(f'site/summaries/{slug}.html', 'w+') as f:
            f.write(output)

        summaries.append({
            'slug': slug,
            'title': summary['summary'],
            'url': summary['url'],
            'date': date
        })

    # Copy images to the 'images' directory.
    elif ext in ('.gif', '.jpg', '.jpeg', '.png'):
        shutil.copyfile(p, f'site/images/{filename}')

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
