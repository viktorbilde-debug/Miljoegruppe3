from fastapi import FastAPI
import psycopg
from etl import open_connection_local_DB, close_connection, return_local_DB

app = FastAPI()

# @app.get("/humidity/")
# def read_user_me(q: str | None = None):   
#     result = return_humidity_local_DB("temp_dry", 4) 
#     if q:
#         result.append("hejfraMinna")
#     return result

@app.get("/")
def read_user_me(table_name: str | None = None, num_obs: int | None = None, source: str | None = None):

    if table_name not in ("temp_dry", "humidity", "pressure"):
        return "Choose tablename and number of observations. Example: http://127.0.0.1:8000/?table_name=humidity&num_obs=1"

    if num_obs is None or num_obs < 1:
        return "Choose tablename and number of observations. Example: http://127.0.0.1:8000/?table_name=humidity&num_obs=1"

    if source not in ("DMI", "Specialisterne"):
        return "Choose tablename and number of observations. Example: http://127.0.0.1:8000/?table_name=humidity&num_obs=1"

    result = return_local_DB(table_name, num_obs, source) #sæt source på

    return result


#Check at det virker på fx http://127.0.0.1:8000/humidity/?q=4