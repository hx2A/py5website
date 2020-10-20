"""
Simple script for adjusting a notebook's image links and copying the images to
the appropriate image folder.

To use, add this to the notebook's metadata:

    "filters": "python scripts/adjust_notebook_img_link.py '%s'"
"""

import re
from pathlib import Path
import argparse
import shutil


IMG_REGEX = re.compile(r'<img src=\"(images/[^\"]*)\"[^>]*>')


parser = argparse.ArgumentParser(
    description='nikola filter for adjusting notebook image links')

parser.add_argument('filename', action='store',
                    help='path to html file of converted notebook')


def copy_img(src, dst):
    if not dst.parent.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(src, dst)


def adjust_file(filename):
    filename = Path(filename)
    with open(filename, 'r') as f:
        html = f.read()

    adj_html = html

    for m in IMG_REGEX.finditer(html):
        # first, adjust the image tag in the html
        full_tag = m.group(0)
        img_path = m.group(1)
        new_img_path = img_path.replace('images', f'/images/{filename.parts[1]}')
        new_full_tag = full_tag.replace(img_path, new_img_path)
        adj_html = adj_html.replace(full_tag, new_full_tag)

        # second, locate the actual image and copy it to the image and output directories
        act_img_path = Path(filename.parts[1], img_path)
        copy_img(act_img_path, Path(new_img_path[1:]))
        copy_img(act_img_path, Path('output', new_img_path[1:]))

    with open(filename, 'w') as f:
        f.write(adj_html)


def main():
    args = parser.parse_args()
    adjust_file(args.filename)


if __name__ == '__main__':
    main()
