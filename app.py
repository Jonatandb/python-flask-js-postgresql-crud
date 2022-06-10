from flask import Flask, request, jsonify, send_file
from psycopg2 import connect, extras
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()

host = "localhost"
port = 5432
dbname = "fazt-postgres-flask-crud"
user = "postgres"
password = "root"


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

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cur.fetchone()

    cur.close()
    conn.close()

    if(user is None):
        return jsonify({"message": "User not found"}), 404

    return jsonify(user)


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

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute("DELETE FROM users WHERE id = %s RETURNING *", (id,))
    user = cur.fetchone()
    conn.commit()

    conn.close()
    cur.close()

    if(user is None):
        return jsonify({"message": "User not found"}), 404

    return jsonify(user)


@app.put("/api/users/<id>")
def update_user(id):

    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    newUser = request.get_json()
    userName = newUser["username"]
    email = newUser["email"]
    password = Fernet(key).encrypt(bytes(newUser["password"], "utf-8"))

    cur.execute("UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s RETURNING *",
                (userName, email, password, id))
    updatedUser = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()

    if(updatedUser is None):
        return jsonify({"message": "User not found"}), 404

    return jsonify(updatedUser)


@app.get('/')
def home():
    return send_file('static/index.html')


if __name__ == "__main__":
    app.run(debug=True)
