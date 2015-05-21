#!C:\Python34\python.exe
from PIL import Image
import os, sys
import shutil

def main():
    filenames = os.listdir('.')

    for filename in filenames:
        filenameL = filename.lower()
        if filenameL.endswith(".jpg") or filenameL.endswith(".png"):
            im = Image.open(filename)
        
            if im.size[1] / im.size[0] < 5:
                print(im.format, im.size, im.mode, end=". ")
                print("This pic does not need split...")
                continue
            print(im.format, im.size, im.mode)
            if not os.path.exists(filename[:-4]):
                os.makedirs(filename[:-4])
        
            times = int(im.size[1]/(im.size[0]*2))

            for i in range(times):
                outfile = os.path.join(filename[:-4] , str(i+1) + '.jpg')
                box = (0, i*2*im.size[0], im.size[0], (i+1)*2*im.size[0] + 30 )
                region  = im.crop(box)
                region.save(outfile, 'JPEG')
            shutil.move(filename, os.path.join(filename[:-4], filename))


if '__main__' == __name__:
    main()