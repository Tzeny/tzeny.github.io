import glob
import re

import html
import cgi

def HTMLEntitiesToUnicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    return html.unescape(text)

def modify_file_content(file_content):
    img_src_regex = r'.*(<img.*src="([^\ ]*)".*\/>).*'
    category_regex = r'.*- (Miscellaneous|Hardware|Software|Engineering|Sports|Art|3D Design|Travelling|3D Design|Artificial Intelligence)$'

    file_content = HTMLEntitiesToUnicode(file_content)

    new_file_lines = []
    for line in file_content.split('\n'):
        new_line = line
        img_src_regex_match = re.match(img_src_regex, new_line)
        if img_src_regex_match:
            src = img_src_regex_match.group(2)
            src = src.split('/')
            src = ('/'+'/'.join(src[src.index('uploads'):])).replace('/uploads','/assets/img/posts')

            new_line = new_line.replace(img_src_regex_match.group(1), f"![My helpful screenshot]({src})")
            print(f'Found image tag with src {img_src_regex_match.group(2)}, replacing with {new_line}')

        category_regex_match = re.match(category_regex, new_line)
        if category_regex_match:
            new_line = line.lower()
            new_line = new_line.replace('artificial intelligence', 'artificialintelligence').replace('3d design','3ddesign')
            print(f'Found Category, lowering case to {new_line}')

        if 'image: /wp-content/uploads/' in new_line:
            new_line = f'thumbnail: {new_line.replace("image: /wp-content/uploads/", "")}'

        new_line += '\n'
        new_file_lines.append(new_line)

    return new_file_lines

input_folder = r"/home/tzeny/Other/Projects/Websites/static_blog/_posts"
output_folder = r"/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/_posts"

files = [f for f in glob.glob(input_folder + "**/*.md", recursive=True)]

for f in files:
    print(f'Processing {f}')
    with open(f, 'r',  encoding="utf8") as content_file:
        content = content_file.read()
        new_content = modify_file_content(content)

        output_path = output_folder + '/' + f.split('/')[-1]
        with open(output_path, 'w', encoding="utf8") as output_file:
            print(f"Writing to {output_path}")
            output_file.writelines(new_content)


