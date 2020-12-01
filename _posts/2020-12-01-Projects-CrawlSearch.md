---
title: "Crawl and Search"
tags: [Projects]
categories:
  - Projects
header:
  overlay_image: /assets/images/empty-header.jpg/
  overlay_filter: rgba(0,0,0,0.2)
  actions:
    - label: "Project Github"
      url: "https://github.com/chaerim-kim/Crawl-and-Search"
---


> 🔎 A Search tool that crawls the 'webscraping' website to provide you with country search functionality!

A Python search tool that crawls, creates an inverted index of all word occurrences in this [example scraping website](http://example.webscraping.com) using BeautifulSoup library, which then allows the user to find pages containing the search term.


## ➰ Project Duration
April, 2020 - May 2020



## 🎨 Features / 주요 기능
- **Crawls** all the pages of the website
- **Tokenizes** the parsed objects and removes styling elements and strips punctuation and whitespaces.
- Creates the **inverted index** for the whole website
- **Prints the inverted list** for a certain word
- **Find** pages containing search terms
- **Compute the scores** of pages when processing a search query


## 🐾 Examples / 사용 예제

Commands | Explanation | Syntax
-- | -- | --
Build | It crawls the website, build the inverted index, and save the resulting index into the file system | `build`
Load | It loads the existing index from the file system | `load`
Print | It prints the inverted index for a particular word | `print <word>`
Find | It finds a certain query phrase in the inverted index and returns a list of all pages containing this phrase | `find <word1> <word2> <word n>`

#### - Command Line menu  
![Screenshot 2020-12-01 at 5 21 41 pm](https://user-images.githubusercontent.com/33334078/100715714-f3335400-33fa-11eb-8a25-02df701e9969.png)


#### 1. Built inverted index  
![Screenshot 2020-12-01 at 5 11 46 pm](https://user-images.githubusercontent.com/33334078/100713866-4ce64f00-33f8-11eb-8231-39d60a4c5806.png)


#### 2. Print <word>   
![Screenshot 2020-12-01 at 5 21 48 pm](https://user-images.githubusercontent.com/33334078/100715789-10682280-33fb-11eb-8ebd-a350a649a45f.png)


#### 3. Find  
- No match (when the search term doesn't exist):  
![Screenshot 2020-12-01 at 5 22 11 pm](https://user-images.githubusercontent.com/33334078/100715838-237af280-33fb-11eb-8bb1-b3b6d7484853.png)

- Successful search:  
![Screenshot 2020-12-01 at 5 27 39 pm](https://user-images.githubusercontent.com/33334078/100715878-37265900-33fb-11eb-81fc-a0c00d0bb296.png)

  ![Screenshot 2020-12-01 at 5 25 29 pm](https://user-images.githubusercontent.com/33334078/100715899-3ee5fd80-33fb-11eb-8038-f482cb1135fb.png)




## 📚 Stack / 개발 환경
- Python
- [Requests Library]((http://docs.python-requests.org/en/master/) - A simple python library to compose HTTP requests.
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/doc) - A Python library for navigating, searching, and modifying a parse tree out of HTML and XML files.


## ⚒ Installation / 실행 방법

#### Pip-install the following libraries:
```
pip install requests
pip install beautifulsoup4
pip install urllib
```

#### Running the client:
- python3 Crawl and Search.py


## 📜 License
This project is licensed under the terms of the MIT license.
> You can check out the full license [here](#https://opensource.org/licenses/mit-license.php)
