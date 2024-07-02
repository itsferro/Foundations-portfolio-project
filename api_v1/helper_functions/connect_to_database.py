#!/usr/bin/python3
"""
contains the fuctions for dealing with the batabase session.
"""
import mysql.connector
import time


def get_session():
    """
    starts a new session by initiates a connection to the database
    and yields the cursor,
    then commits changes and closes everything.
    """
    db_creds = {
            "host": "127.0.0.1",
            "user": "feras",
            "password": "",
            "database": "compactecom_MVP_dev",
            "time_zone": "+02:00"
            }

    while True:
        try:
            session = mysql.connector.connect(**db_creds)
            print("______________________________________________")
            print("_____database connected : session started_____\n")
            break
        except Exception as error:
            print("connection to database attempt **Failed**")
            print(f"Error: {error}")
            time.sleep(2)

    try:
        cursor = session.cursor(dictionary=True, buffered=True)
        print("cursor created")
    except Exception as error:
        print("cursor couldn't be created **Failed**")
        print(error)

    try:
        yield cursor
    finally:
        session.commit()
        print("session commited")
        cursor.close()
        print("cursor closed")
        session.close()
        print("\n______database connected : session ended______")
        print("______________________________________________")


if __name__ == "__main__":
    """
    """
    print("Hi!")

    cursor = get_session()
    for i in cursor:
        pass
