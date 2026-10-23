from fastapi import FastAPI
import psycopg


conn = psycopg.connect(
        "postgresql://app:test@localhost:5432/data_db"
    )

cursor = conn.cursor()

cursor.execute("SELECT * FROM humidity")
result = cursor.fetchall()

#cursor.execute("SELECT * FROM temp_dry")

#cursor.close()
#conn.close()

app = FastAPI()

#@app.lifespan("startup")

#def on_startup():
    #create_db_and_tables()

@app.get("/humidity")
def read_user_me():
    return result
    #cursor = conn.cursor()

#cursor.execute("SELECT * FROM humidity")
#result = cursor.fetchall()


#@app.get("/temp_dry")
#def read_user(user_id: str):
    #return {"user_id": user_id}

#@app.get("/pressure")
#def read_user_me():
    #return result

