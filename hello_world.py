from naoqi import ALProxy


# Once the Nao is up, press its power button in his chest and Nao will
# announce his IP. put that below.

NAO_IP="192.168.1.7" # <YOUR_NAO_IP> or nao.local

tts = ALProxy("ALTextToSpeech", NAO_IP, 9559)
tts.say("Hello, world!")
