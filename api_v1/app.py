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

# closing connection with database
conn.close()
