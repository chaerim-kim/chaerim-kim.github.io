---
title: "User Management System"
tags: [Projects]
permalink: /projects/user-management-sys/
categories:
  - Projects
header:
  overlay_image: /assets/images/empty-header.jpg/
  overlay_filter: rgba(0,0,0,0.2)
  actions:
    - label: "Project Github"
      url: "https://github.com/chaerim-kim/Springboot-ReactJS"
---

> 🌱 A full-stack Springboot-React web application that implements a User control system

A Full-Stack user control system focusing on basic functionalities implemented with Springboot for backend, React for frontend and PostgreSQL for the database engine.


## 🎨 Features / 주요 기능
- The application performs the following CRUD RESTful APIs:
  - [x] Create user
  - [x] List user
  - [x] Update user
  - [x] Delete user
- Uses docker for containerisation.



## ➰ Project Duration
October 2020 - November 2020


## 🐾 Examples / 사용 예제
1. Create User  
![create](https://user-images.githubusercontent.com/33334078/100756706-d87bd200-3430-11eb-83fb-07c77475fb25.gif)

2. List User  
![view](https://user-images.githubusercontent.com/33334078/100756811-f47f7380-3430-11eb-872a-51ea46bf1b70.gif)

3. Update User  
![update](https://user-images.githubusercontent.com/33334078/100756806-f34e4680-3430-11eb-865b-414338a54c77.gif)

4. Delete User  
![delete](https://user-images.githubusercontent.com/33334078/100756787-ee899280-3430-11eb-80d0-3b0bf67f4c64.gif)


## 📚 Stack / 개발 환경
- Java
- [Springboot](#https://spring.io) - A Java-based framework used to create a micro Service - used to build stand-alone and production ready spring applications.
- [PostgreSQL](#https://www.postgresql.org) - A relational database management system emphasizing extensibility and SQL compliance.
- [ReactJS](#http://reactjs.org) - A JavaScript library for building user interfaces or UI components.
- [Docker](#www.docker.com) - The container for the application


## Installation / 실행 방법


#### 1. Docker Setup
```sh
git clone https://github.com/chaerim-kim/Springboot-ReactJS.git

cd Springboot-ReactJS

docker-compose up -d workspace postgres frontend

docker-compose exec workspace bash

```

#### 2. Build and Run the Springboot App with Maven
```sh
./mvnw spring-boot:run
```

#### 3. Build and Run the React Frontend App
```sh
cd frontend

npm start
```
Then access: http://localhost:3000/user





## 📜 License
This project is licensed under the terms of the MIT license.
> You can check out the full license [here](#https://opensource.org/licenses/mit-license.php)
