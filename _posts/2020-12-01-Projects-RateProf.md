---
title: "Rate and View Professors"
tags: [Projects]
permalink: /projects/rate-and-view/
categories:
  - Projects
header:
  overlay_image: /assets/images/empty-header.jpg/
  overlay_filter: rgba(0,0,0,0.2)
  actions:
    - label: "Project Github"
      url: "https://github.com/chaerim-kim/Rating-Professors"
---

> 👩🏻‍💻 Rate and view your professors from various modules, semesters and years!

A Django based RESTful API project that allows students to rate the teaching of professors in various modules - it makes SQL queries to the database to add, update and view ratings.



## ➰ Project Duration
March, 2020 - April 2020


## 🎨 Features / 주요 기능
- These REST API endpoints provide the following functionalities:

Commands | API | Explanation | Syntax
-- | -- | -- | --
Register | /api/register/ | register to the website | `register`
Login | /api/login/ | login | `login http://localhost:8000/`
Logout | /api/logout/ | logout | `logout`
List | /api/list/ | List all module instances and the professors teaching each of them | `list`
View | /api/view/ | View the rating of all professors | `view`
Average | /api/average/ | View the average rating of a certain professor in a certain module | `average professor_id module_code **e.g.**` **e.g.** average JE1 CD1
Rate | /api/rate/ | Rate the teaching of the professor in a certain module instance | `rate professor_id module_code year semester rating` **e.g.** rate JE1 CD1 2017 1 4




## 🐾 Examples / 사용 예제
- Main Command Line Interface  
![Screenshot 2020-12-01 at 3 37 52 pm](https://user-images.githubusercontent.com/33334078/100707710-6da9a700-33ee-11eb-824d-dc303a4f7416.png)

1. Register  
![Screenshot 2020-12-01 at 4 02 22 pm](https://user-images.githubusercontent.com/33334078/100707805-9af65500-33ee-11eb-9e24-09ed4e526054.png)

2. Login / logout  
![Screenshot 2020-12-01 at 3 43 42 pm](https://user-images.githubusercontent.com/33334078/100707179-98473000-33ed-11eb-8c2c-b89796c5318c.png)

3. List  
![Screenshot 2020-12-01 at 3 42 08 pm](https://user-images.githubusercontent.com/33334078/100707157-8ebdc800-33ed-11eb-9956-80212643baec.png)

4. View  
![Screenshot 2020-12-01 at 3 42 02 pm](https://user-images.githubusercontent.com/33334078/100707129-836a9c80-33ed-11eb-9b6b-766732b9f690.png)

5. Average  
![Screenshot 2020-12-01 at 3 44 09 pm](https://user-images.githubusercontent.com/33334078/100707197-a006d480-33ed-11eb-874f-cd8be77178c0.png)

6. Rate  
![Screenshot 2020-12-01 at 3 45 29 pm](https://user-images.githubusercontent.com/33334078/100707203-a1380180-33ed-11eb-880e-9423f1a4f4ed.png)




## 📚 Stack / 개발 환경
- Python
- [Django](https://www.djangoproject.com) - A high-level Python Web framework that allows for rapid development and clean, pragmatic design
- [SQLite3](https://www.sqlite.org) - A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.


## ⚒ Installation / 실행 방법

#### Installing dependencies
`pip install requests`  
`pip install pandas`

#### Running the server:  
`python3 manage.py runserver 8000`

#### Running the client:
`python3 client.py`



## 📜 License
This project is licensed under the terms of the MIT license.
> You can check out the full license [here](#https://opensource.org/licenses/mit-license.php)
