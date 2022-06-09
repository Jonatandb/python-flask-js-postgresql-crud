from flask import Flask
from psycopg2 import connect

app = Flask(__name__)

host = "localhost"
port = 5432
dbname = "fazt-postgres-flask-crud"
user = "postgres"
password = ""


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname, user=user, password=password)
    return conn


@app.get("/api/users")
def get_users():
    return "getting users"


@app.get("/api/users/<id>")
def get_user(id):
    return "getting user " + str(id)


@app.post("/api/users")
def create_user():
    return "creating user"


@app.delete("/api/users/<id>")
def delete_user(id):
    return "deleting user " + str(id)


@app.put("/api/users/<id>")
def update_user(id):
    return "updating user " + str(id)


if __name__ == "__main__":
    app.run(debug=True)
