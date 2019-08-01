from naoqi import ALProxy


def speak(NAO_IP, NAO_PORT, msg):
    tts = ALProxy("ALTextToSpeech", NAO_IP, 9559)
    tts.say(msg)
