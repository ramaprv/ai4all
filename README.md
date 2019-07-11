# AI4ALL Summer Project by PRG at UMD
AI4ALL Summer project repository by [Perception & Robotics Group](http://prg.cs.umd.edu/) at [UMD](https://umd.edu/)

This project involves using the NAO robot to detect gestures and imitate them
on real time.


## [Course Material](./notebooks/README.md)


## Requirements
* Python 3
* OpenCV
* numpy
* almath
* imutils
* naoqi
* pytorch - torch, torchvision


## NAO Network Setup
* Connect NAO to same network as your PC.
* Press power button on NAO and NAO will announce IP
* You can input this IP in your browser to verify if you are able to connect to NAO.
* Change the IP in hello_world.py and run
    `python hello_world.py`
* Run `python train.py` which opens up the NAO camera frame.
* Press key `c` to capture training data and `q` to quit.
