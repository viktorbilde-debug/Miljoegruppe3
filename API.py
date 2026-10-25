from fastapi import FastAPI
import psycopg
from etl import return_humidity_local_DB

app = FastAPI()

@app.get("/humidity")
def read_user_me():
    return return_humidity_local_DB("humidity",2)

#cursor.execute("SELECT * FROM humidity")
#result = cursor.fetchall()


#@app.get("/temp_dry")
#def read_user(user_id: str):
    #return {"user_id": user_id}

#@app.get("/pressure")
#def read_user_me():
    #return result

