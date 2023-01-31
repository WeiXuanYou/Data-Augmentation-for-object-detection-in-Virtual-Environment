# VR-RL
## Introduction

we proposed a method to expand the data and real-time training architecture through VR to improve the accuracy of the model and reduce labor costs and time consumed.

In addition, it can also complete labeling tasks rapidly, and even 3D object detection can be quickly obtained.
![](https://i.imgur.com/Jz7AbXF.jpg)

## Installation
### Development environment
 ![](https://img.shields.io/badge/windows-11-orange) 
 ![](https://img.shields.io/badge/Python-3.10-green)
 ![](https://img.shields.io/badge/airsim-1.6-yellow)
 ![](https://img.shields.io/badge/unreal-4.27.x-purple)
### Device
- GPU : RTX 3090
- CPU : i9-12900
- RAM : 32 GB
### Docker image
If you would rather not have to install anything, you can pull the docker image.
```
docker pull ...
docker run ...
```
### Install from source
1. computer request first: [Unreal](https://www.unrealengine.com/en-US/download) ```4.27.X```, [Airsim](https://github.com/Microsoft/AirSim) ```1.6```
2. clone and submodule

We use YOLOv7 to train real time , so we include YOLOv7 as a submodule.
```
git clone ...
cd ...
git submodule init
git submodule update
```
3. Download a pretrained model from YOLOv7
```
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7.pt
```

## Traing
```
python train.py
```

## Demo
Demo for image:
```

```
Demo for video:
```

```
## Result Video
[![Watch the video](https://img.youtube.com/vi/E8Nj7RwXf0s/sddefault.jpg)](https://youtu.be/E8Nj7RwXf0s)

## Citation
## License
## Reference
