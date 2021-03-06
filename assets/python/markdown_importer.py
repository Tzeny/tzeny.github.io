import glob
import re

import html
import cgi

def HTMLEntitiesToUnicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    return html.unescape(text)

def modify_src_to_jekyll(src):
    if 'tzeny.com' in src:
        src = src.split('/')
        src = ('/'+'/'.join(src[src.index('uploads'):])).replace('/uploads','/assets/img/posts')
    return src

def modify_file_content(file_content):
    # img_src_regex = r'.*(<img.*src="([^\ ]*)".*\/>).*'
    img_src_regex = r'((<figure class="[^"]*">(\W|\n)*)?(<img.*src="([^\ ]*)".*\/>)\W?(<figcaption>(.*?)<\/figcaption>)?(<\/figure>)?)'
    img_src_regex_2 = r'((<figure class="[^"]*">(\W|\n)*)?(!\[[^\]]*\])\(([^\ ]*)\)\W?(<figcaption>(.*?)<\/figcaption>)?(<\/figure>)?)'
    category_regex = r'.*- (Miscellaneous|Hardware|Software|Engineering|Sports|Art|3D Design|Travelling|3D Design|Artificial Intelligence)$'
    gallery_item_regex = r'(<div class=".*?gallery-item.*?">(.|\n)*?<a href="(.*?)" title="(.*?)".*?<img src="(.*?)"(.|\n)*?<\/div>)'

    file_content = HTMLEntitiesToUnicode(file_content)

    gallery_item_regex_matches = re.findall(gallery_item_regex, file_content, flags=re.IGNORECASE|re.MULTILINE)
    for gallery_item_regex_match in gallery_item_regex_matches:
        # ('<div class="rl-gallery-item"><a href="https://tzeny.com/wp-content/uploads/2019/11/rusty_sideways.jpg" title="a" data-rl_title="" class="rl-gallery-link" data-rl_caption="" data-rel="lightbox-gallery-24"><img src="https://tzeny.com/wp-content/uploads/2019/11/rusty_sideways-300x225.jpg"width="300" height="225" /></a></div>',
        # '',
        # 'https://tzeny.com/wp-content/uploads/2019/11/rusty_sideways.jpg',
        # 'a',
        # 'https://tzeny.com/wp-content/uploads/2019/11/rusty_sideways-300x225.jpg',
        # '>')
        # print(gallery_item_regex_match)
        original_src = modify_src_to_jekyll(gallery_item_regex_match[2])
        thumbnail_src = modify_src_to_jekyll(gallery_item_regex_match[4])
        caption = gallery_item_regex_match[3]

        new_img = '\n\n{% include lightbox2_image.html original_image="'+original_src+'" thumbnail_image="'+thumbnail_src+'" caption="'+caption+'" set_name="set_1" %}'

        file_content = file_content.replace(gallery_item_regex_match[0], new_img)
        print(f'Replacing {gallery_item_regex_match[0]} with {new_img}')
        # a = 1/0
        # print(f'Found image tag with src {src}, replacing with {new_img}')

    # img_src_regex_match = re.match(img_src_regex, new_line)
    img_src_regex_matches = re.findall(img_src_regex, file_content, flags=re.IGNORECASE|re.MULTILINE)
    img_src_regex_matches_2 = re.findall(img_src_regex_2, file_content, flags=re.IGNORECASE|re.MULTILINE)
    for img_src_regex_match in img_src_regex_matches + img_src_regex_matches_2:
        print(img_src_regex_match)
        src = modify_src_to_jekyll(img_src_regex_match[4])

        caption = img_src_regex_match[6]
        print('---'+caption)

        # a = 1/0

        # new_line = new_line.replace(img_src_regex_match[0], f"![My helpful screenshot]({src})")
        new_img = '\n\n{% include figure_caption.html url="'+src+'" description="'+caption+'" %}'

        file_content = file_content.replace(img_src_regex_match[0], new_img)
        print(f'Found image tag with src {src}, replacing with {new_img}')

    new_file_lines = []
    for line in file_content.split('\n'):
        if 'permalink' in line:
            continue

        if 'layout: post' in line:
            new_file_lines.append('layout: blog_post\n')
            continue

        if 'date: ' in line:
            print(f'Appending base line')
            new_file_lines.append('base: Blog\n')
            new_file_lines.append('base_url: /blog\n')
            continue

        new_line = line

        # # img_src_regex_match = re.match(img_src_regex, new_line)
        # img_src_regex_matches = re.findall(img_src_regex, new_line, flags=re.IGNORECASE|re.MULTILINE)
        # for img_src_regex_match in img_src_regex_matches:
        #     # print(img_src_regex_match)
        #     src = img_src_regex_match[1]
        #     src = src.split('/')
        #     src = ('/'+'/'.join(src[src.index('uploads'):])).replace('/uploads','/assets/img/posts')

        #     caption = img_src_regex_match[3]
        #     print('---'+caption)

        #     # new_line = new_line.replace(img_src_regex_match[0], f"![My helpful screenshot]({src})")
        #     new_img = '{% include figure_caption.html url="'+src+'" description="'+caption+'" %}'

        #     new_line = new_line.replace(img_src_regex_match[0], new_img)
        #     print(f'Found image tag with src {img_src_regex_match[1]}, replacing with {new_line}')

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
output_folder = r"/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/_posts/blog"

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


