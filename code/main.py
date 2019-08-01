import os
import sys
import time

import almath
import cv2
import numpy as np
from naoqi import ALProxy
from vision_definitions import kBGRColorSpace, kQVGA

import imutils

sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')



NAO_IP="192.168.1.3" # <YOUR_NAO_IP> or nao.local


if __name__=="__main__":  # Should not run when imported

    camera_index = 0 # Top camera
    image_count = 0

    # Proxy for ALVideoDevice
    name = "nao_opencv"
    video = ALProxy("ALVideoDevice", NAO_IP, 9559)
    motion = ALProxy("ALMotion", NAO_IP, 9559)

    # Subscribe to video device on a specific camera
    # BGR for OpenCV
    name = video.subscribeCamera(name,camera_index,kQVGA,kBGRColorSpace,30)
    print "Subscribed to ", name

    try:
        frame = None
        # Keep Looping
        while True:
            # Get image
            img = video.getImageRemote(name)

            # Get image attributes
            width = img[0]
            height = img[1]
            nchannels = img[2]
            imgbuffer = img[6]
            center_frame = (width, height)

            # Get OpenCV image (allocate on first pass)
            if frame is None:
                print 'Grabbed image: ',width,'x',height,' nchannels=',nchannels
                frame=np.asarray(bytearray(imgbuffer), dtype=np.uint8)
                frame=frame.reshape((height,width,3))
            else:
                frame.data=bytearray(imgbuffer)

            # Display the frame to our screen
            # NONTE : Do not run this code if your run your python in the robot
            # as NAO has no screen to show
            cv2.imshow("Frame", frame)

            # Get the key pressed in the image window
            key = cv2.waitKey(33)&0xFF
            if  key == ord('q') or key == 27:
                # Exit loop when 'q' or 'Esc' is pressed on the image window
                break

    finally: # As fallback we'll make sure to unsubscribe
        print "Unsubscribing ",name
        # Reset the stiffness
video.unsubscribe(name)
cv2.destroyAllWindows()
