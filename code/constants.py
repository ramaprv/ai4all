import numpy as np

IP = "192.168.1.7"
PORT = 9559

# joint names
HEAD_YAW = "HeadYaw"
HEAD_PITCH = "HeadPitch"
R_SHOULDER_ROLL = "RShoulderRoll"
R_SHOULDER_PITCH = "RShoulderPitch"
R_ELBOW_ROLL = "RElbowRoll"
R_ELBOW_YAW = "RElbowYaw"
R_WRIST_YAW = "RWristYaw"
R_HAND = "RHand"

# chain names
HEAD = "Head"
R_ARM = "RArm"

# axis masks
AXIS_MASK_X = 1
AXIS_MASK_Y = 2
AXIS_MASK_Z = 4
AXIS_MASK_WX = 8
AXIS_MASK_WY = 16
AXIS_MASK_WZ = 32

AXIS_MASK_ALL = AXIS_MASK_X + AXIS_MASK_Y + AXIS_MASK_Z + \
                AXIS_MASK_WX + AXIS_MASK_WY + AXIS_MASK_WZ

# last row of transformation matrix
R0001 = np.array([[0, 0, 0, 1]])

# initial position of right arm
INIT_HAND_POS = np.array([[0.18109862506389618], [-0.053951337933540344], [0.12278126180171967]])
INIT_HAND_ROT = np.array([1.0500797033309937, -0.433413565158844, 0.31683531403541565])

INIT_END_EFFECTOR_POSE = INIT_HAND_POS.flatten()
INIT_END_EFFECTOR_POSE = np.concatenate((INIT_END_EFFECTOR_POSE, INIT_HAND_ROT))
INIT_END_EFFECTOR_POSE = list(INIT_END_EFFECTOR_POSE)
INIT_END_EFFECTOR_POSE = np.array(INIT_END_EFFECTOR_POSE)

# joint values
HAND_OPEN = 1.0
HAND_CLOSE = 0.0

# image dimensions
IMG_W = 640
IMG_H = 480
