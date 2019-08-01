
import Queue
from timeit import default_timer as timer

import almath
import vision_definitions as vd
from naoqi import ALProxy, motion

import Image
from constants import *


class NAO:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.motion = ALProxy("ALMotion", ip, port)
        self.posture = ALProxy("ALRobotPosture", ip, port)
        self.video = ALProxy("ALVideoDevice", ip, port)
        self.tts = ALProxy("ALTextToSpeech", ip, port)
        self.subscriber = None
        self.frame = None

        self.grasped_it = False
        self.cnt_grasp = 0
        self.score_vals = np.zeros(1)
        self.predictions = np.zeros(5)
        # self.history = Queue.Queue(maxsize=5)

        # head and hand position/orientation for visual servo
        # and end-effector adaptation
        self.head_pose = None
        self.head_pos0 = None
        self.head_rot = None
        self.head_transform0 = None
        self.head_transform1 = None

        self.hand_pos0 = None
        self.hand_rot = None
        self.hand_transform0 = None

        self.arm_pose = None

    def init_camera(self):
        """
        Activates camera and checks if it has been already activated
        """
        cam_bottom = 0
        fps = 5
        try:
            self.video.unsubscribe("demo")
            print("Robot: Camera unsubscribed")
        except:
            print("Robot: Camera cannot be unsubsribed")

        try:
            self.subscriber = self.video.subscribeCamera("demo",
                                                               cam_bottom, vd.kVGA, vd.kRGBColorSpace, fps)
            print("Robot: Camera activated!")
        except:
            print("Robot: Camera not available")

    def crouch(self):
        """
        Makes the robot crouch (kneel)
        """
        self.posture.goToPosture("Crouch", 0.5)

    def open_hand(self, close=False):
        """
        Opens/closes the robot's hand
        """
        action = HAND_OPEN
        if close:
            action = HAND_CLOSE
        self.motion.setAngles(R_HAND, action, 0.2)

    def cam2numpy(self):
        """
        Converts robot's camera image to a numpy array
        """
        nao_image = self.video.getImageRemote(self.subscriber)
        image_width = nao_image[0]
        image_height = nao_image[1]
        array = nao_image[6]
        frame = Image.frombytes("RGB", (image_width, image_height), array)
        frame = np.array(frame)
        return frame

    def speak(self, msg):
        self.tts.say(msg)
