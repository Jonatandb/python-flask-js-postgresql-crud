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


@app.get("/")
def Home():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 1 + 1")
    result = cur.fetchone()
    print("result: " + str(result))
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
