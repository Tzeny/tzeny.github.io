import glob
import shutil

from PIL import Image

input_folder = '/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/_posts/blog'
assets_folder = '/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/assets/img/posts'

md_files = glob.glob(input_folder + '/*.md')

if __name__ == '__main__':
    for md_file_path in md_files:
        with open(md_file_path, 'r',  encoding="utf8") as content_file:
            content = content_file.readlines()

        for line in content:
            if 'thumbnail:' in line:
                thumbnail_path = line.split(' ')[-1].strip()
                print(f'Found thumbnail {thumbnail_path}')
                break
        else:
            raise Exception(f'No thumbnail found for post {md_file_path}')
        
        thumbnail_path = 'assets/img/posts/' + thumbnail_path

        # save a backup
        shutil.copy(thumbnail_path, thumbnail_path+'.bk')

        img = Image.open(thumbnail_path)
        width, height = img.size

        if width < height:
            left = 0 
            right = width
            top = (height - width) / 2
            bottom = height - top
        elif width > height:
            top = 0
            bottom = height
            left = (width - height) / 2
            right = width - left
        else:
            continue # it's already a square

        img = img.crop((left, top, right, bottom))
        img.save(thumbnail_path)


        
