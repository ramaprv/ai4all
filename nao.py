
import Queue
from timeit import default_timer as timer

import almath
import Image
import utils
import vision_definitions as vd
from constants import *
from naoqi import ALProxy, motion


class NAO:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.motion_proxy = ALProxy("ALMotion", ip, port)
        self.posture_proxy = ALProxy("ALRobotPosture", ip, port)
        self.video_proxy = ALProxy("ALVideoDevice", ip, port)
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
            self.video_proxy.unsubscribe("demo")
            print("Robot: Camera unsubscribed")
        except:
            print("Robot: Camera cannot be unsubsribed")

        try:
            self.subscriber = self.video_proxy.subscribeCamera("demo",
                                                               cam_bottom, vd.kVGA, vd.kRGBColorSpace, fps)
            print("Robot: Camera activated!")
        except:
            print("Robot: Camera not available")

    def crouch(self):
        """
        Makes the robot crouch (kneel)
        """
        self.posture_proxy.goToPosture("Crouch", 0.5)

    def init_head(self):
        """
        Fixes head orientation to see from the bottom camera
        """
        self.motion_proxy.setStiffnesses(["Head"], 1)
        self.motion_proxy.setPosition(HEAD,
                                      motion.FRAME_TORSO,
                                      [0, 0, 0, 0, 20 * almath.TO_RAD, 0],
                                      0.5, AXIS_MASK_ALL)

        # for interactive handover
        self.head_pose = self.motion_proxy.getPosition(HEAD, motion.FRAME_TORSO, True)
        self.head_pos0 = np.array([[self.head_pose[0]], [self.head_pose[1]], [self.head_pose[2]]])
        self.head_rot = np.array([0, 20, 0]) * almath.TO_RAD
        self.head_transform0 = utils.posor2tf(self.head_pos0, self.head_rot)
        self.head_transform1 = self.head_transform0

    def init_arm(self):
        """
        Moves arm to initial position for the handover
        """
        self.motion_proxy.setPosition(R_ARM,
                                      motion.FRAME_TORSO,
                                      list(np.concatenate((INIT_HAND_POS.flatten(), INIT_HAND_ROT))),
                                      0.5, AXIS_MASK_ALL)
        self.open_hand()

        # for interactive handover
        self.hand_pos0 = INIT_HAND_POS
        self.hand_rot = INIT_HAND_ROT
        self.hand_transform0 = utils.posor2tf(self.hand_pos0, self.hand_rot)

    def open_hand(self, close=False):
        """
        Opens/closes the robot's hand
        """
        action = HAND_OPEN
        if close:
            action = HAND_CLOSE
        self.motion_proxy.setAngles(R_HAND, action, 0.2)

    def cam2numpy(self):
        """
        Converts robot's camera image to a numpy array
        """
        nao_image = self.video_proxy.getImageRemote(self.subscriber)
        image_width = nao_image[0]
        image_height = nao_image[1]
        array = nao_image[6]
        frame = Image.frombytes("RGB", (image_width, image_height), array)
        frame = np.array(frame)
        return frame
