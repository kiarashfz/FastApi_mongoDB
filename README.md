# FastApi MongoDB Authentication

This is a FastApi project that uses MongoDB as a database & motor as a database driver & Redis for caching blocked JWT tokens.
## Pre requirements
| MongoDB | Redis |
|---------|-------|
## Installation
#### 1. The first step is cloning the project
```bash
$ git clone https://github.com/kiarashfz/FastApi_mongoDB.git
```
#### 2. The next step is changing the .env-sample file name to .env
> **_NOTE:_**  You should put your own data in .env file for DB & other configurations.
#### 3. The next step is running FastApi project using command below
```bash
$ uvicorn api.main:app --reload
```
#### 4. Now you can go to http://127.0.0.1:8000/docs URL to see the beautiful swagger UI and using the APIs :wink:
