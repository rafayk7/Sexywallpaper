from PIL import Image, ImageSequence
from datetime import datetime

class GenFrames:
    def __init__(self, outFolder,gifPath):
        self.frames = 0
        self.outFolder = outFolder
        self.gifPath = gifPath
        self.timeBetweenChange = 0  # Minutes
        self.SECONDSINDAY = 86400
        self.times = []
        self.currentImg = ''

    def extractFrames(self):
        gifPIL = Image.open(self.gifPath)

        self.frames = gifPIL.n_frames
        index = 1
        for frame in ImageSequence.Iterator(gifPIL):
            frame.save("%s/frame%d.png" % (self.outFolder, index))
            index += 1

        self.timeBetweenChange = self.SECONDSINDAY / self.frames

    def getTimes(self):
        #Need to run it every 6.67 minutes. Get current time, current minute of the day. modulu by self.timeBetweenChange. Change it to that image. Get remainder. Schedule it for now+that minutes
        now = datetime.now()
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)

        secondsElapsedInDay = (now - midnight).seconds
        imgNumber = secondsElapsedInDay % self.timeBetweenChange

        self.currentImg = "%s/frame%d.png" % (self.outFolder, imgNumber)
        print(imgNumber)
        print(self.currentImg)




x = GenFrames('frames', 'good.gif')
x.extractFrames()
x.getTimes()
