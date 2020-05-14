from pathlib import PosixPath
import pathlib
import glob
import os
import sys
import tempfile
import shutil
from tqdm import tqdm

from PIL import Image, ExifTags

THUMBNAIL_SIZE = (500, 500) 
MAX_IMAGE_SIZE = (2000, 2000)

def yes_or_no(question):
    reply = str(input(question+' (y/n)[Y]: ')).lower().strip()
    if reply == '':
        return True
    elif reply[0] == 'y':
        return True
    elif reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

def rotate_inplace(img_path):
    try:
        image=Image.open(img_path)

        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break

        exif=dict(image._getexif().items())

        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
            print(f'Rotated {img_path} 180 degress')
        elif exif[orientation] == 6:
            image=image.rotate(270, expand=True)
            print(f'Rotated {img_path} 270 degress')
        elif exif[orientation] == 8:
            image=image.rotate(90, expand=True)
            print(f'Rotated {img_path} 90 degress')

        image.save(img_path)
        image.close()
    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass

def crop_to_square_inplace(img_path):
    img = Image.open(img_path)
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
        return
    
    img = img.crop((left, top, right, bottom))
    img.save(img_path)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'Usage: {sys.argv[0]} input_folder output_folder')
        exit(1)

    input_folder = sys.argv[1]
    if input_folder[-1] == '\\' or  input_folder[-1] == '/':
        input_folder = input_folder[:-1]

    output_folder = PosixPath(sys.argv[2])

    files = glob.glob(input_folder + '//*')
    files = [f for f in files if os.path.isfile(f)]
    files = sorted(files)

    print('Found files: ')
    for f in files:
        print(f'\t{os.path.basename(f)} - {os.path.getsize(f)/1024/1024} MB')

    if not yes_or_no('Proceed?'):
        exit(0)

    try:
        temp_output_dir = PosixPath(tempfile.mkdtemp())
        print(f'Temp output directory: {temp_output_dir}')

        print('Rename files: ')
        for index, f in enumerate(files):
            print(f'\t{os.path.basename(f)} -> {os.path.basename(input_folder)}_{index}{pathlib.Path(f).suffix}')

        if yes_or_no('Rename?'):
            for index, f in enumerate(files):
                shutil.copy(f, temp_output_dir/f'{os.path.basename(input_folder)}_{index}{pathlib.Path(f).suffix}')
        else:
            for f in files:
                shutil.copy(f, temp_output_dir/os.path.basename(f))

        files = glob.glob(str(temp_output_dir) + '//*')
        files = sorted(files)
        files_extensions = [pathlib.Path(f).suffix for f in files]
        thumbnails = [f.replace(ext, '_thumb.jpg') for f,ext in zip(files, files_extensions)]

        square_thumbs = yes_or_no('Crop thumbnails to generate square thumbnails')

        pbar = tqdm(total=len(files))
        for f, t in zip(files, thumbnails):
            rotate_inplace(f)

            image = Image.open(f).convert('RGB') # we can't save transparent thumbnails
            image.thumbnail(THUMBNAIL_SIZE) 
            
            image.save(t) 

            if square_thumbs:
                crop_to_square_inplace(t)

            if image.width < THUMBNAIL_SIZE[0] or image.height < THUMBNAIL_SIZE[1]:
                image = Image.open(t).resize(THUMBNAIL_SIZE)
                
                image.save(t) 

            # resize images down
            image = Image.open(f).convert('RGB') # we can't save transparent thumbnails
            image.thumbnail(MAX_IMAGE_SIZE) 
            
            image.save(f) 
            pbar.update(1)

        print(f'Move files to {output_folder}?')
        for f, t in zip(files, thumbnails):
            print(f'{os.path.basename(f)} ({os.path.getsize(f)/1024/1024:.2f} MB) -> {output_folder}/{os.path.basename(f)}')
            print(f'{os.path.basename(t)} ({os.path.getsize(t)/1024:.2f} kB) -> {output_folder}/{os.path.basename(t)}')
        if not yes_or_no('Proceed?'):
            exit(0)

        print('\n\nGallery code:\n\n')
        for f, t in zip(files, thumbnails):
            shutil.move(f, output_folder/os.path.basename(f))
            shutil.move(t, output_folder/os.path.basename(t))

            s = '\n{% include lightbox2_image.html original_image="/' + f'{output_folder}/{os.path.basename(f)}' + '" thumbnail_image="/' + f'{output_folder}/{os.path.basename(t)}' + '" caption="" set_name="set_1" %}'
            print(s)
    finally:
        shutil.rmtree(temp_output_dir)