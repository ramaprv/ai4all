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
    image_prefix = current_directory + "/data/f"
    image_suffix = ".jpg"

    # Proxy for ALVideoDevice
    name = "nao_opencv"
    video = ALProxy("ALVideoDevice", NAO_IP, 9559)
    motionProxy = ALProxy("ALMotion", NAO_IP, 9559)
    motionProxy.setStiffnesses("Head", 1.0)

    # names            = "HeadYaw"
    # angles           = 30.0*almath.TO_RAD
    # fractionMaxSpeed = 0.1
    # motionProxy.setAngles(names,angles,fractionMaxSpeed)
    # time.sleep(3.0)
    # motionProxy.setStiffnesses("Head", 0.0)

    # Subscribe to video device on a specific camera
    # BGR for OpenCV
    name = video.subscribeCamera(name,camera_index,kQVGA,kBGRColorSpace,30)
    print "Subscribed to ", name

    useSensors  = True
    # names = ["HeadYaw", "HeadPitch"]

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
                image_path = image_prefix + str(image_count) + image_suffix
                cv2.imwrite(image_path,frame)
                image_count = image_count+1

    finally: # As fallback we'll make sure to unsubscribe
        print "Unsubscribing ",name
        # Reset the stiffness
        motionProxy.setStiffnesses("Head", 0.0)

video.unsubscribe(name)
