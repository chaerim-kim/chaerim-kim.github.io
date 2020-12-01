---
title: "OpenGL-Leeds Scene"
tags: [Projects]
permalink: /projects/OpenGL-leeds/
categories:
  - Projects
header:
  overlay_image: /assets/images/empty-header.jpg/
  overlay_filter: rgba(0,0,0,0.2)
  actions:
    - label: "Project Github"
      url: "https://github.com/chaerim-kim/OpenGL-Leeds-Scene"
---

> 🏰 Renders the landmarks of Leeds! - Millennium square, a carousel and Leeds University’s Bacon statue

The Leeds application renders a visual scene of Leeds by creating an interactive animated scene using OpenGL and C++. It provides a certain level of user interaction through two sliders which manipulates the camera angle and the horse speed.


## ➰ Project Duration
November, 2019 - December 2019


## 🎨 Objects & OpenGL techniques / 사용된 OpenGL 기술
- [x] A user interactive application - change the view angle, change the speed of the moving horse.
1. **Leeds city council** - texture mapping, light and material, made up of convex objects
2. **Bacon statue** - rotating, material
3. **Christmas trees** - instancing, material
4. **Carousel** - spinning, material, motion, complex rotation
5. **Moving horse** - user interaction with horse leg, rotating, hierarchical modelling


## 🐾 Examples / 사용 예제
- **Overall**  
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100721385-9b005000-3402-11eb-823c-74ceb0afdce4.png" width="70%"/>
</p>


1. **Leeds city council**  
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100721475-b79c8800-3402-11eb-95c0-11fd7fe02863.png"/>
</p>

2. **Bacon statue**   
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100721511-c2efb380-3402-11eb-964a-04474cff2438.png"/>
</p>

3. **Christmas trees**   
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100721544-cdaa4880-3402-11eb-8ddf-b864876d6f7a.png"/>
</p>

4. **Carousel**  
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100721570-d4d15680-3402-11eb-84ea-cab50f242635.png"/>
</p>


5. **Moving horse**   
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100721592-dc90fb00-3402-11eb-862f-1c5bc0468d98.png"/>
</p>


- **Different view angles**  
<p align="center">
  <img src="https://user-images.githubusercontent.com/33334078/100721786-22e65a00-3403-11eb-99b3-57dc018067d5.png" width="80%"/>
</p>


## 📚 Stack / 개발 환경
- C++
- [OpenGL](www.opengl.org) - An application programming interface (API) for rendering 2D and 3D vector graphics


## 💡 What I learned
- A hands-on learning of OpenGL, Graphical rendering of a scene and modular file structure.
- Designing of various objects using convex objects and/ or GLUT objects.
- Various OpenGL methods including texture mapping, light and material setup, rotation, scaling and transitions;
- Hierarchical placing of objects to create a movement and a hierarchical rotation.
- Matrix calculation and instancing of convex coordinates and vertex-normal calculation.


## ⚒ Installation / 실행 방법
```
module add qt  
qmake  
make.
./Leeds  
```


## 📜 License
This project is licensed under the terms of the MIT license.
> You can check out the full license [here](#https://opensource.org/licenses/mit-license.php)
