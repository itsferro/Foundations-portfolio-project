#!/usr/bin/python3
"""
"""
import mysql.connector
import time


# database credentials dictionary
"""
db_creds = {
        "host": "127.0.0.1",
        "user": "feras",
        "password": "",
        "time_zone": "+02:00"
        }
"""


def get_new_connection(db_creds):
    while True:
        try:
            conn = mysql.connector.connect(**db_creds)
            print("database connected")
            return conn
            break
        except Exception as error:
            print("connection to database attempt **Failed**")
            print(f"Error: {error}")
            time.sleep(2)

"""
# the initialization of the database connection
old_conn = get_new_connection(db_creds)
"""


def get_cursor(conn):
    """
    """
    try:
        cursor = conn.cursor(dictionary=True)
        print("cursor created")
        return cursor
    except Exception as error:
        print("cursor couldn't be created **Failed**")
        print(error)


def get_new_cursor(conn):
    cursor = get_cursor(old_conn)
    try:
        yield cursor
    finally:
        cursor.close()
        print("cursor closed")


if __name__ == "__main__":
    """
    """
    print("Hi!")
    # database credentials dictionary
    db_creds = {
            "host": "127.0.0.1",
            "user": "feras",
            "password": "",
            "time_zone": "+02:00"
            }

    # the initialization of the database connection
    old_conn = get_new_connection(db_creds)

    x = get_new_cursor(old_conn)
    for i in x:
        print(f"this is the cursor: {i}")

    old_conn.close()
    print("database disconnected")
