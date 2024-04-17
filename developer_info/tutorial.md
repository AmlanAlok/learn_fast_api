
How to Begin

Source = https://www.youtube.com/watch?v=0sOvCWFmrtA&t=1s


Default Port = 8000

In Production:
uvicorn main:app

In development:
uvicorn main:app --reload
uvicorn app.main:app --reload




Dependencies
1. FastAPI - Python API development framework
2. Autopep8 - Provides formatting to python code
3. Uvicorn - Web server library. Sub dependency of FastAPI library, when installed with the [all] flag


FastAPI has built-in Swagger API support
http://127.0.0.1:8000/docs

It also supports Redoc
http://localhost:8000/redoc


Postgres Driver = Psycopg
