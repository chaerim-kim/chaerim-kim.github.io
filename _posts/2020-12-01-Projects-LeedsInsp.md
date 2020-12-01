---
title: "Leeds Inspired Web Search"
tags: [Projects]
categories:
  - Projects
header:
  overlay_image: /assets/images/1.Unicycle-header.jpg
  overlay_filter: rgba(0,0,0,0.2)
  actions:
    - label: "Project Github"
      url: "https://github.com/chaerim-kim/Leeds-Inspired"
---


> 💃 Search the kind of event you want to attend, and scroll through **Yelp's recommendations** of places to go, eat, and drink nearby!

A website for Leeds-based users to search a type of event, get recommendations of local events and venues; powered by Leeds Inspired and Yelp API using Python Flask.


## 🎨 Features / 주요 기능

- [x]  Use of REST APIs - [Leeds Inspired API](http://api.leedsinspired.co.uk/) and [Yelp Fusion API](https://www.yelp.com/fusion)
- [x]  User to select the **category of the event**
- [x]  Fetch **local Leeds events** of user’s choice, via **LeedsInspired’s** API.
- [x]  User to **select one event** from the recommendations
- [x]  Lists the **venue information** alongside the **restaurants nearby,** via **Yelp’s** API.
- [x]  Server and Client communication, which passes session information.



## ➰ Project Duration
November, 2019



## 🐾 Examples / 사용 예제

![https://user-images.githubusercontent.com/33334078/100367537-b4417f00-3045-11eb-8007-17c8b51410be.gif](https://user-images.githubusercontent.com/33334078/100367537-b4417f00-3045-11eb-8007-17c8b51410be.gif)


## 📚 Stack / 개발 환경

- Python
- [Flask](https://flask.palletsprojects.com/) - Micro web framework for Python
- HTML, CSS - Templating and styling of the web service


## ⚒ Installation / 실행 방법

### Installation

1. Create a virtual environment
`virtualenv flask`
2. Activate the flask virtual environment
`source flask/bin/activate`
3. Install dependencies. (-U: update if already installed)
`pip install -U -r requirements.txt`
4. Setting development environment
`export FLASK_ENV=development`

### Running Server and Client

1. Run the server
`python server.py`
2. Run the client
```
cd client
python client.py
```

## 📜 License

This project is licensed under the terms of the [MIT license.](https://opensource.org/licenses/mit-license.php)
- [Leeds Inspired API](http://api.leedsinspired.co.uk/)
- [Yelp Fusion API](https://www.yelp.com/fusion)
