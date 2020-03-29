from pathlib import PosixPath
import glob
import html
import mimetypes
import shutil

mimetypes.init()

input_folder = '/home/tzeny/Other/Projects/Websites/static_blog/wiki/wikimediacomposer_wikimedia-data/html/images'
output_folder = r"/home/tzeny/Other/Projects/Websites/static_blog/tzeny.github.io/assets/img/wiki"


def get_extensions_for_type(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext

VIDEO = tuple(get_extensions_for_type('video'))
AUDIO = tuple(get_extensions_for_type('audio'))
IMAGE = tuple(get_extensions_for_type('image'))

for extension in IMAGE:
    search_regex = input_folder + f"/**/*{extension}"

    files = [f for f in glob.glob(search_regex, recursive=True)]
    print(f'Found {len(files)} files for import in ' + search_regex)

    for f in files:
        try:
            shutil.copy(f, output_folder + '/' + f.split('/')[-1])
        except:
            print(f'Error copying {f}')

