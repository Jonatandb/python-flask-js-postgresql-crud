# Python, PostgreSQL & Javascript - Aplicación Web CRUD (Flask y Vanilla JS)

https://www.youtube.com/watch?v=Qqgry8mezC8

---

<img src="Flask-JS-CRUD.gif" />

---

## Running project with VSCode

- Create .env file by copying the .env.example file
- Open new integrated terminal and run:
  - python -m virtualenv venv
- Select Python interpreter from VSCode:
  - F1 -> Python: Select Interpreter -> Enter interpreter path -> Select: venv\Scripts\python.exe
- Open new integrated terminal and run:

  - pip install -r requirements.txt
  - python app.py

- Visit: http://localhost:5000 (\* PostgreSQL must be installed, must contain db with users table and must be running)

---

### Push to Heroku

- git push heroku master
- Then visit: https://flask-js-postgresql-crud.herokuapp.com/

### Push to GitHub

- git push origin master

---
