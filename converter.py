from PIL import Image
import os, sys
import re

supported_formats = {'bmp': True, 'gif': True, 'jpg': True, 'png': True}

try:
    path = sys.argv[1]
    path_to_save = sys.argv[2]
    convert_to_type = sys.argv[3]
    pattern = re.compile(r"[^.]*")

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if '.jpg' in filename:
                fullpath = path + filename
                image_to_convert = Image.open(fullpath)
                file_no_suffix = pattern.match(filename).group()
                image_to_convert.save(path_to_save + file_no_suffix + '.' + convert_to_type, convert_to_type)

except:
    print('something went wrong')
    print('check that your folder directories and type you wish to convert to are correctly spelled')

    if convert_to_type not in supported_formats:
        raise ValueError('the format you wish to convert to is not supported. Maybe it\'s spelled incorrectly?')
