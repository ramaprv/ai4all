import os
import sys
import cv2
import numpy as np
import imutils
import almath
import time

from vision_definitions import kQVGA,kBGRColorSpace
from naoqi import ALProxy


NAO_IP="192.168.1.7" # <YOUR_NAO_IP> or nao.local


if __name__=="__main__":  # Should not run when imported

    camera_index = 0 # Top camera
    image_count = 0
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_prefix = current_directory + "/data/"
    image_suffix = ".jpg"

    # Proxy for ALVideoDevice
    name = "nao_opencv"
    video = ALProxy("ALVideoDevice", NAO_IP, 9559)
    motionProxy = ALProxy("ALMotion", NAO_IP, 9559)
    motionProxy.setStiffnesses("Head", 0.8)

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
                motionProxy.setStiffnesses("Head", 0.0)
                break
            elif key == 99:
                # 'c' pressed | Capture image
                upper_left = (80, 40)
                bottom_right = (230, 190)
                # Display crop center for the frame 320x240
                # cv2.rectangle(frame, upper_left, bottom_right, (0, 255, 0), 2)
                # cv2.imshow('Area to be cropped in Frame', frame)
                cropped_frame = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
                gray_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)
                resized_frame = cv2.resize(gray_frame, dsize=(28, 28), interpolation=cv2.INTER_CUBIC)
                # cv2.imshow("Resized Frame", resized_frame)
                image_path = image_prefix + str(image_count) + image_suffix
                cv2.imwrite(image_path, resized_frame)
                image_count = image_count+1

    finally: # As fallback we'll make sure to unsubscribe
        print "Unsubscribing ",name
        # Reset the stiffness
        motionProxy.setStiffnesses("Head", 0.0)

video.unsubscribe(name)
