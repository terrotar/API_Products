
# API_Products


## About

That project was created due to a test of my Analisys and Development of Systems and i've decided to use the framework
FastAPI because has been a while since I didn't use it and I really would like it to be my main framework, so I'm kind of
adapting and remembering about it.

Basically it's an API with integration of a database(SQLite3) and has only 1 table(Product). It's more an exercise then a big and functional project, to understand better the basics of that INCREDIBLE framework.

---
## How to Run

After install all the requirements found inside Pipfile, just run the following command inside your terminal inside the main project's directory, NOT INSIDE the api folders:

<code>uvicorn api.main:api</code>

Or that one if you gonna make some changes:

<code>uvicorn api.main:api --reload</code>


Obs: Must be outside the api directory because of imports... I changed it to fit the deploy on heroku, where you can check it out in the link: https://fastproducts.herokuapp.com/
---
