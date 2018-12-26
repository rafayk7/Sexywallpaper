import os
from PIL import Image
from appscript import *
import argparse
import time
import datetime


def extractFrames(gif, outFolder):
    frame = Image.open(gif)
    nframes = 0
    while frame:
        frame.save( '%s/%s-%s.gif' % (outFolder, os.path.basename(gif), nframes ) , 'GIF')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True
    
def setWallpaper(image):

    se = app('System Events')
    desktops = se.desktops.display_name.get()

    for d in desktops:
        desk = se.desktops[its.display_name == d]
        desk.picture.set(mactypes.File(image))



#extractFrames('good.gif', 'frames')

t1 = datetime.datetime.now()
t2 = datetime.datetime(t1.year, t1.month, t1.day, t1.hour, t1.minute+1, t1.second, t1.microsecond)
t3 = t2-t1

while t3 !=0 and 0<=t3.days:
        t1 = datetime.datetime.now()
        t3 = t2-t1

count = 1
while count<=215:
    path = 'frames/good.gif-' + str(count) + '.gif'
    setWallpaper(path)
    time.sleep(2)
    count+=1
