from PIL import Image
import os, sys

im = Image.open(sys.argv[1])
print(im.format, im.size, im.mode)

times = int(im.size[1]/(im.size[0]*2))

for i in range(times):
    outfile = sys.argv[1][:-4] + '_' + str(i+1) + '.jpg'
    box = (0, i*2*im.size[0], im.size[0], (i+1)*2*im.size[0] + 30 )
    region  = im.crop(box)
    region.save(outfile, 'JPEG')
