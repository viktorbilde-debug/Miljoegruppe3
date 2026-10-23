from fastapi import FastAPI
import psycopg
conn = psycopg.connect(
        "postgresql://app:test@localhost:5432/data_db"
    )

cursor = conn.cursor()

cursor.execute("SELECT * FROM humidity")
#conn.commit()
#cursor.close()
#conn.close()
#print(data)
#app = FastAPI()

#@app.get("/users/me")
#def read_user_me():
    #return {"user_id": "the current user"}


#@app.get("/users/{user_id}")
#def read_user(user_id: str):
    #return {"user_id": user_id}