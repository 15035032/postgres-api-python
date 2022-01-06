from typing import Optional
from fastapi import FastAPI

BD_HOST = "localhost"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "sqyrd@123"

# pip install psycopg2
import psycopg2
import psycopg2.extras


app = FastAPI()

conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host = BD_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/land_record/{id}")

def land_records_navimumbai(id: int):
    print(type(id))
    cur.execute("select * from land_records_landrecordnavimumbai where id={}".format(id))


    t=cur.fetchall()
    t1=t[0]

    y={"id":t1[0],"record_id":t1[1],"layer_path":t1[2],"source":t1[3],
    "city":t1[4],"owner_name":t1[5],"area":t1[6],"cts_plot":t1[7],"date_of_allotment":t1[8],
    "node":t1[9],"asset_type":t1[10],"date_of_agreement":t1[11],"industry":t1[12],
    "plot_status":t1[13],"created_date":t1[14],"updated_date":t1[15]}

    return y








  