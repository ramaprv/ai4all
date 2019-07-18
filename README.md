# AI4ALL Summer Project by PRG at UMD

AI4ALL Summer project repository by [Perception & Robotics Group](http://prg.cs.umd.edu/) at [UMD](https://umd.edu/)

This project involves using the NAO robot to detect gestures / hand signals and perform actions correspondingly.


##  Project

### [1. Introduction](./notebooks/project/1.Introduction.ipynb)
### [2. Connecting to NAO](./notebooks/project/2.Connecting%20to%20NAO.ipynb)
### [3. Getting Images](./notebooks/project/3.Getting%20Images.ipynb)
### [4. Recognizing Gestures](./notebooks/project/4.Recognizing%20Gestures.ipynb)
### [5. Putting Things Together](./notebooks/project/5.Putting%20Things%20Together.ipynb)


## Further Reading

## Python Basics

### Introduction
#### [Using Jupyter Notebook](./notebooks/python/Using%20Jupyter%20Notebook.ipynb)
#### [Data Constructs](./notebooks/python/Data%20Constructs.ipynb)
#### [Math](./notebooks/python/Math.ipynb)
#### [To Do: Math in Jupyter Notebook](./notebooks/python/Math%20in%20Jupyter%20Notebook.ipynb)

### Data Structures
#### [Data Structures](./notebooks/python/Data%20Structures.ipynb)
#### [Strings](./notebooks/python/Strings.ipynb)
#### [Lists](./notebooks/python/Lists.ipynb)
#### [Dictionaries](./notebooks/python/Dictionaries.ipynb)
#### [To Do: Indexing and Slicing](./notebooks/python/Indexing%20and%20Slicing.ipynb)

### Advanced Operations
#### [Flow Control](./notebooks/python/Flow%20Control.ipynb)
#### [Functions](./notebooks/python/Functions.ipynb)
#### [Loops](./notebooks/python/Loops.ipynb)
#### [Working With Objects](./notebooks/python/Working%20With%20Objects.ipynb)

### Hands On
#### [File Handling](./notebooks/python/File%20Handling.ipynb)
#### [To Do: Creating your first script](./notebooks/python/Creating%20your%20first%20script.ipynb)
#### [To Do: Answer Key](./notebooks/python/Answer%20Key.ipynb)
#### [To Do: Fizz Buzz](./notebooks/python/Fizz%20Buzz.ipynb)


### Computer Vision Basics

#### [Linear Algebra](./notebooks/computer%20vision/Linear%20Algebra.ipynb)
#### [Image Processing](./notebooks/computer%20vision/Image%20Processing.ipynb)


### Machine Learning Basics

#### [PyTorch](./notebooks/machine%20learning/PyTorch.ipynb)


### NAO Programming Basics

#### [Network Setup](http://doc.aldebaran.com/2-1/nao/nao-connecting.html)
#### [Hello World](http://www.bx.psu.edu/~thanh/naoqi/getting_started/helloworld_python.html)
#### [Making NAO Speak](http://www.bx.psu.edu/~thanh/naoqi/dev/python/making_nao_speak.html)
#### [Making NAO Move](http://www.bx.psu.edu/~thanh/naoqi/dev/python/making_nao_move.html)
#### [Face Detection and Tracking](http://www.bx.psu.edu/~thanh/naoqi/dev/python/examples/vision/face_detection.html#python-example-vision-facedetection)


## Requirements
* Ubuntu 16.04
* Python 2.7
* OpenCV
* numpy
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
