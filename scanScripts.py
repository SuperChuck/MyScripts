#!utf-8
import os,sys

def main(contain):
    filenames = os.listdir(folder)
    for filename in filenames:
        f=open(os.path.join(folder,filename))
        for line in f:
            if keyword in line:
                contain.append(filename)            
        f.close()

if '__main__'==__name__:
    if len(sys.argv)!=3:
        print('format: scan.py folder keyword')
        exit(1)
    folder=sys.argv[1]
    keyword=sys.argv[2]
    allContain=[]
    main(allContain)
    print(allContain)
