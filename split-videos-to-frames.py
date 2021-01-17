import cv2
import os

vidcap = cv2.VideoCapture('video/uav.mp4')
path_to_save = 'dataset'



def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
          name = 'frame' + str(count) + '.jpg'
          cv2.imwrite(os.path.join(path_to_save, name), image)
        
    return hasFrames


sec = 5
frameRate = 0.75 
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
