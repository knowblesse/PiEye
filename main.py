import cv2 as cv
import numpy as np
import time
import picamera
import picamera.array

# Setup Camera
camera = picamera.PiCamera()
camera.resolution = [640,480]
camera.iso = 640
camera.framerate = 30

rawCapture = picamera.array.PiRGBArray(camera)

# Preview
camera.start_preview()
time.sleep(5)
camera.stop_preview()

# open opencv window and show the current view
# when the user press some button, prompt area selection screen
vc = cv.VideoCapture(r"C:\VCF\butter\Lobster_Recording-210330-101307_21AUG3-211205-180108_Vid1.avi")
ret, img = vc.read()
cv.imshow('Test', img)
data = {'img':img, 'lastLoc':None, 'firstLoc':None}

def onclick(event, x, y, flags, data):
    if event == cv.EVENT_LBUTTONDOWN:
        if data['lastLoc'] is not None:
            cv.line(data['img'], data['lastLoc'], tuple([x,y]), [0,255,255], 2)
            cv.imshow('Test', data['img'])
            data['lastLoc'] = tuple([x,y])
        else:
            data['lastLoc'] = tuple([x, y])
            data['firstLoc'] = tuple([x,y])
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.line(data['img'], data['firstLoc'], tuple([x, y]), [0, 255, 255], 2)
        cv.imshow('Test', data['img'])

cv.setMouseCallback('Test', onclick, data)
cv.waitKey()

# 
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    fr = frame.array
    bgimage = cv.cvtColor(fr, cv.COLOR_BGR2GRAY)
            diff_value = np.sum(cv.subtract(image, bgimage) > 50)
            print(diff_value)
            if(diff_value > 2000):
                signal.on()
                print("on")
            else:
                signal.off()
                print("off")
            time.sleep(0.5)            
            if (live_button.is_pressed):
                cv.imshow('live',image)
                time.sleep(1)
    rawCapture.truncate(0)

