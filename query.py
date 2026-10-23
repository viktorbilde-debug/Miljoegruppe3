from fastapi import FastAPI
import psycopg


conn = psycopg.connect(
        "postgresql://app:test@localhost:5432/data_db"
    )

cursor = conn.cursor()

cursor.execute("SELECT * FROM humidity")
result = cursor.fetchall()


app = FastAPI()


@app.get("/humidity/")
def read_user_me(q: str | None = None):
    if q:
        result.append("hejfraMinna")
    return result

#Check at det virker på fx http://127.0.0.1:8000/humidity/?q=4