---
title: "Convolutional-Neural-Network"
tags: [Projects]
permalink: /projects/Convolutional-Neural-Network/
categories:
  - Projects
header:
  overlay_image: /assets/images/empty-header.jpg/
  overlay_filter: rgba(0,0,0,0.2)
  actions:
    - label: "Project Github"
      url: "https://github.com/chaerim-kim/Convolutional-Neural-Network"
---

> 🧠 Correctly classify the fashion images from Zalando's Fashion-MNIST dataset.

Performs image recognition to classify Zalando's Fashion-MNIST dataset with 92% accuracy. The Convolutional Neural Network is powered by tensorflow and keras libraries.



## ➰ Project Duration
November 2019 - December 2019



## 🎨 Features / 주요 기능
- [x] **Design a Convolutional Neural Network** - combination of convolutional, polling, dropout, and dense layers to design a small and deep neural network.
  - It contains 128 filters of size 3 * 3, and has 128 dense layers.
  - In addition, it has the learning rate of 0.001 with 20 epoches, and each layer is followed by pooling and dropout layers.  


## 💡 Result

### 1. Effect of a Learning Rate
**Learning rate**, a hyper-parameter, controls how much we are adjusting the weights of our network.
- **High learning rate** may fail to converge as gradient descent can overshoot the minimum
- On the other hand, **small learning rate** can take too long to converge, but is more resistant to noise and inaccuracies. Hence, finding a moderate learning rate is desirable.

**Most appropriate learning rate= 0.001**
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100751818-2988c780-342b-11eb-85fc-6df79fbf4028.png"/>
</p>

- The learning rate that is considered the most appropriate was found to be **0.001**. Both the training and validation loss is low, hence is stable and resistant to errors and inaccuracies.
- It satisfies to be small enough to not diverge, but big enough classify correctly without overfitting.


### 2. The Neural Network Architecture
<p align="center"><img src="https://user-images.githubusercontent.com/33334078/73648658-eed0ca00-4675-11ea-9cf3-69b6f8fa4f84.png" height="50%" width="50%"/></p>

In the first part of the model, it **extracts the features using convolutional filters**. This is done in the **Conv2D, MaxPooling2D and Dropout layers**, as it can be seen in the figure above.

The second part of the model **performs the classification**, where it maps the identifies features to a specific class, which in this architecture, is done in **two dense layers.**

In between these layers are the **Flatten layer**, which has no effect on the input size, but **makes it a one single layer.**



#### Training & Validation graph
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100752187-a0be5b80-342b-11eb-92ad-23d3148ae806.png"/>
</p>

The final model generally achieves a good fit, with both accuracy and loss curves converging (figure above). The graph suggests that the model has the ability to generalize and classify unseen data correctly.



## 📚 Stack / 개발 환경
- [Keras](https://keras.io) - An open-source library that provides a Python interface for artificial neural networks - an interface for tensorflow library
- [TensorFlow](www.tensorflow.org) - An open-source software library for machine learning, with a particular focus on training and inference of deep neural networks


## ⚒ Installation / 실행 방법
```
pip install numpy==1.15.2
pip install sklearn
pip install matplotlib==2.2.3
pip install tensorflow==1.5
pip install keras==2.2.4

python3 ConvolutionalNN.py
```



## 📜 License
This project is licensed under the terms of the MIT license.
> You can check out the full license [here](#https://opensource.org/licenses/mit-license.php)
