from fastapi import FastAPI
import psycopg


conn = psycopg.connect(
        "postgresql://app:test@localhost:5432/data_db"
    )

cursor = conn.cursor()

cursor.execute("SELECT * FROM humidity")
result = cursor.fetchall()


app = FastAPI()


@app.get("/humidity")
def read_user_me():
    return result

print(result)