## Data Preparation

##### TILDA dataset 
download from [ https://lmb.informatik.uni-freiburg.de/resources/datasets/tilda.en.html](https://lmb.informatik.uni-freiburg.de/resources/datasets/tilda.en.html)
##### Hong Kong dataset
download from [ https://ytngan.wordpress.com/codes/]( https://ytngan.wordpress.com/codes/)
##### DAGM2007 dataset
download from [ https://hci.iwr.uni-heidelberg.de/content/weakly-supervised-learningindustrial-optical-inspection]( https://hci.iwr.uni-heidelberg.de/content/weakly-supervised-learningindustrial-optical-inspection)

## Installation
- Install [PyTorch](http://pytorch.org/) by selecting your environment on the website and running the appropriate command.
  * Note: You should use at least PyTorch 0.4.0
- Clone this repository.
  * Note: Only support Python 3+.
- Annotate defective data set data and Generate VOC format (/data/XXXXdatasets/VOCdevkit/VOC2007/JPEGImages and /data/XXXXdatasets/VOCdevkit/VOC2007/Annotations)
  * Note: Install [labelImg](https://github.com/tzutalin/labelImg) to label data
- Divide training set and data set (/data/XXXXdatasets/VOCdevkit/VOC2007/ImageSets/Main/test.txt and /data/XXXXdatasets/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt)
  * Note: The ratio of training set to test set can be from 6:4 to 8:2

## Training
- Download the VGG-16 pretrained weight file from [ https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth]( https://s3.amazonaws.com/amdegroot-models/vgg16_reducedfc.pth)
- Edit the key ##num_class and ##max_iter in data/config.py
- Edit the path of dataset and all name of defect class  in data/voc0712.py
- Run train.py 

## Evaluation
- Edit the file path of trained weight model in test.py
- Run test.py

## Test result
See file "test results" of my experiments for detail

