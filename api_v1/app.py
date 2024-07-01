#!/user/bin/python3

from fastapi import FastAPI, Response, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import sqlite3
from helper_functions.get_queries_from_file import get_queries
from helper_functions.create import delivery_service
import random

# app creation statement
app = FastAPI()

# defining the static files path
app.mount(
        "/static",
        StaticFiles(directory="static"),
        name="static",
)

# making a database connection
conn = sqlite3.connect("compactecom.db")


def create_schema(conn):
    queries = get_queries("create_tables.sql")
    cur = conn.cursor()
    for query in queries.split(';'):
        cur.execute(query)
    conn.commit()

def add_data(conn):
    # add data
    # generate data to insert
    all_data = []
    for i in range(1,10):
        data = []
        n = random.randint(0,999)
        data.append(i + n)
        data.append(f"{n} status")
        data.append(f"{n} descreption")
        data.append(None)
        all_data.append(data)
    # get query
    query = get_queries("insert_into_statuses.sql")
    # execute query
    cur = conn.cursor()
    cur.executemany(query, tuple(all_data))
    conn.commit()


def get_data(conn):
    # select data
    query = get_queries("select_all_from.sql")
    #print(query)
    try:
        cur = conn.cursor()
        cur.execute(query)
    except Exception as e:
        print(e)

    rows = cur.fetchone()
    for row in rows:
        print(row)

def test_helper_fuctions(conn):
    """
    """
    delivery_service(conn, None)


# calling the functions
#create_schema(conn)
#add_data(conn)
#get_data(conn)
test_helper_fuctions(conn)

# closing connection with database
conn.close()
