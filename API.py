from fastapi import FastAPI
from etl import return_local_DB

app = FastAPI()

@app.get("/humidity")
def read_user_me():
    return return_local_DB("humidity",4)

@app.get("/temp_dry")
def read_user_me():
    return return_local_DB("temp_dry",4)

@app.get("/pressure")
def read_user_me():
    return return_local_DB("pressure",4)


#cursor.execute("SELECT * FROM humidity")
#result = cursor.fetchall()


#@app.get("/temp_dry")
#def read_user(user_id: str):
    #return {"user_id": user_id}

#@app.get("/pressure")
#def read_user_me():
    #return result

