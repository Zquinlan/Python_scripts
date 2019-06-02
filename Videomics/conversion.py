import numpy as np
import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('infile', help = 'movie file which will be converted to file of tiffs')
parser.add_argument('outfile_name', help ='name of folder')
args = parser.parse_args()

cap = cv2.VideoCapture(args.infile)

try:
    if not os.path.exists(args.outfile_name):
        os.makedirs(args.outfile_name)
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in tiff file
    name = './' + args.outfile_name + '/' + 'frame' + str(currentFrame) + '.tif'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()