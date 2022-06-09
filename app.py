from flask import Flask, request, jsonify
from psycopg2 import connect, extras
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()

host = "localhost"
port = 5432
dbname = "fazt-postgres-flask-crud"
user = "postgres"
password = ""


def get_connection():
    conn = connect(host=host, port=port, dbname=dbname,
                   user=user, password=password)
    return conn


@app.get("/api/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(users)


@app.get("/api/users/<id>")
def get_user(id):
    return "getting user " + str(id)


@app.post("/api/users")
def create_user():
    newUser = request.get_json()
    userName = newUser["username"]
    email = newUser["email"]
    password = Fernet(key).encrypt(bytes(newUser["password"], "utf-8"))

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING *", (
            userName, email, password),
    )
    newCreatedUser = cur.fetchone()

    conn.commit()
    cur.close()
    conn.close()
    return jsonify(newCreatedUser)


@app.delete("/api/users/<id>")
def delete_user(id):
    return "deleting user " + str(id)


@app.put("/api/users/<id>")
def update_user(id):
    return "updating user " + str(id)


if __name__ == "__main__":
    app.run(debug=True)
