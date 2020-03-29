from pathlib import PosixPath
import glob
import html
import re

input_folder = '../mediawiki-to-markdown/export'
output_folder = r"/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/_posts/wiki"

files = [f for f in glob.glob(input_folder + "**/*.md", recursive=True)]

print(f'Found {len(files)} .md file for import in {input_folder}')

def HTMLEntitiesToUnicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    return html.unescape(text)

def modify_file_content(file_content):
    file_content = HTMLEntitiesToUnicode(file_content)
    img_src_regex = r'(\W|^)\[([^\[\]]*)\]\(([^\ \[\]]*)[^\)\[\]]*\)'

    new_file_lines = []
    for line in file_content.split('\n'):
        new_line = line

        if 'permalink' in line:
            continue

        if 'date: ' in line:
            print(f'Appending layout line')
            new_file_lines.append('layout: post\n')
            new_file_lines.append('base: Wiki\n')
            new_file_lines.append('base_url: /wiki\n')
            continue

        img_src_regex_match = re.match(img_src_regex, new_line)
        if img_src_regex_match:
            src = str(img_src_regex_match.group(3))
            src = src.replace('/File:', '/assets/img/wiki/')

            # make sure we only do this to images
            if src.split('.')[-1] not in ['jpeg','jpg','png','gif','svg']:
                continue

            caption = str(img_src_regex_match.group(2))
            caption = caption.replace('thumb|','')

            # new_line = new_line.replace(img_src_regex_match.group(0), f"![{caption}]({src})")
            new_image_s = '{%% include figure_caption.html url="%s" description="%s" %%}' % (src, caption)
            new_line = new_line.replace(img_src_regex_match.group(0), new_image_s)
            print(f'Found image tag with src {img_src_regex_match.group(2)}, replacing with {new_line}')

        new_line += '\n'
        new_file_lines.append(new_line)

    return new_file_lines

for f in files:
    print(f'Processing {f}')
    with open(f, 'r',  encoding="utf8") as content_file:
        if 'file:' in f.lower():
            print(f'Skipping {f} as it appears to be a file description page')
            continue
        content = content_file.read()
        new_content = modify_file_content(content)

        output_path = output_folder + '/' + f.split('/')[-1]
        with open(output_path, 'w', encoding="utf8") as output_file:
            print(f"Writing to {output_path}")
            output_file.writelines(new_content)