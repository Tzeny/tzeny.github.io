from pathlib import PosixPath
import glob
import html
import re
import textdistance
import numpy as np

input_folder = '../mediawiki-to-markdown/export'
output_folder = r"/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/_posts/wiki"

files = [f for f in glob.glob(input_folder + "/*.md", recursive=True)]
count = 0

print(f'Found {len(files)} .md file for import in {input_folder}')

def HTMLEntitiesToUnicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    return html.unescape(text)

def modify_file_content(file_content):
    global count 

    file_content = HTMLEntitiesToUnicode(file_content)
    img_src_regex = r'((\W|^)\[([^\[\]]*)(\[\d*\])?\]\(([^\ \[\]#]*)[^\)\[\]]*\))'
    
    new_file_lines = []
    for line in file_content.split('\n'):
        new_line = line

        if 'permalink' in line or '#drawio' in line:
            continue

        if 'date: ' in line:
            print(f'Appending layout line')
            new_file_lines.append('layout: post\n')
            new_file_lines.append('base: Wiki\n')
            new_file_lines.append('base_url: /wiki\n')
            continue

        img_src_regex_matches = re.findall(img_src_regex, new_line, flags=re.IGNORECASE|re.MULTILINE)
        for img_src_regex_match in img_src_regex_matches:
            src = str(img_src_regex_match[4])
            src = src.replace('/File:', '/assets/img/wiki/')

            # make sure we only do this to images
            if src.split('.')[-1] in ['jpeg','jpg','png','gif','svg']:
                caption = str(img_src_regex_match[2])
                caption = caption.replace('thumb|','')

                # new_line = new_line.replace(img_src_regex_match.group(0), f"![{caption}]({src})")
                new_image_s = '{%% include figure_caption.html url="%s" description="%s" %%}' % (src, caption)
                new_line = new_line.replace(img_src_regex_match[0], new_image_s)
                print(f'Found image tag with src {img_src_regex_match[2]}, replacing with {new_line}')
            elif 'wikilink' in str(img_src_regex_match[0]).lower() and 'file:' not in str(img_src_regex_match[0]).lower():
                title = img_src_regex_match[4]
                title = title.replace('/','').lower()

                found_files = []
                for f in files:
                    if title in f:
                        found_files.append(f)

                if len(found_files) > 0:
                    distances = np.zeros(len(found_files))
                    for i in range(len(distances)):
                        distances[i] = textdistance.hamming(title, found_files[i])

                    closest_file = found_files[np.argmin(distances)]

                    post_link = "{% post_url /wiki/" + closest_file.split('/')[-1].replace('.md','') + "%}"
                    new_link_s = f'[{img_src_regex_match[2]}]({post_link})'
                    if 'file:' not in new_link_s:
                        new_line = new_line.replace(img_src_regex_match[0], new_link_s)
                        print(f'Found link tag with src {img_src_regex_match[3]}, replacing "{img_src_regex_match[0]}" -> {new_link_s}')
                else:                
                    print(f'welpy {title} not found in {files} files')

        reference_regex = r'(\[(\d*)\]\W?<([^>]*)>)'
        reference_regex_matches = re.findall(reference_regex, new_line)
        for reference_regex_match in reference_regex_matches:
            reference = reference_regex_match[1] + f'. [{reference_regex_match[2]}]({reference_regex_match[2]})'
            new_line = new_line.replace(reference_regex_match[0], reference)
            print(f'Replaced reference {reference_regex_match[0]} with {reference}')

        reference_number_regex = r'(\[(\d*)\])'
        reference_number_matches = re.findall(reference_number_regex, new_line)
        for reference_number_match in reference_number_matches:
            # scroll_to_bottom = f'<a href="javascript: document.body.scrollIntoView(false);">{reference_number_match[1]}</a>'
            reference_nr = f'<sup>{reference_number_match[1]}</sup>'
            new_line = new_line.replace(reference_number_match[0], reference_nr)
            
            

        # remove all html tags
        new_line = re.sub(r'<\/?[^>]*>', '', new_line)

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
print(f'Count {count}')