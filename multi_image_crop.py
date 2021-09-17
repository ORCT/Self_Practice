#lu = 1371,156 ld = 1371,2031 ru:2745,157
import os
from PIL import Image

#print('\n',os.getcwd())

for root, dirs, files in os.walk('./'):
    for idx, file in enumerate(files):
        fname, ext = os.path.splitext(file)
        if ext in ['.jpg','.png','.gif']:
            im = Image.open(file)
            width, heignt = im.size

            crop_image = im.crop((1361, 126, 2765, 2051))
            crop_image.save('img'+str(idx)+'.png')
            #crop = ((left, top, right, bottom))