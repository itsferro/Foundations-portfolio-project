#!/usr/bin/python3
"""
delivery services table CRUD functions.
"""


from fastapi import Response, APIRouter, Depends, HTTPException
from helper_functions.get_queries_from_file import get_queries
from helper_functions.connect_to_database import get_session
import mysql.connector


router = APIRouter(
        prefix='/delivery_services',
        tags=['delivery_services']
        )

# delivery services file path
path = "delivery_services/"


@router.post("/")
def create(data, db = Depends(get_session)):
    """
    creates deleviry service row in the delivery services table.
    """
    query = get_queries(path + "create.sql")
    print(query)
    print(data)
    try:
        db.execute(query, data)
        return {"message": query, "data_added": data}
    except Exception as error:
        return {"message": error}


@router.get("/")
def read_all(db = Depends(get_session)):
    """
    fetches all rows from the delivery services table.
    """
    query = get_queries(path + "rread.sql")
    print(f"\nquery:\n{query}")
    db.execute(query)
    rows = db.fetchall()
    return {"message": rows}
    #except Exception as error:
    #return {"message": error}


@router.put("/{id}")
def update(id, data, db = Depends(get_session)):
    """
    updates a deleviry service row by id
    in the delivery services table.
    """
    query = get_queries(path + "update.sql")
    print(query)
    print(id)
    print(data)
    try:
        db.execute(query, data, id)
        return {"message": query, "id": id, "data": data}
    except Exception as error:
        return{"message": error}


@router.delete("/{id}")
def delete(id, db = Depends(get_session)):
    """
    deletes a delivery service row bu id
    from the delivery services table.
    """
    query = get_queries(path + "delete.sql")
    print(query)
    print(id)
    try:
        db.execute(query, id)
        return {"message": query, "id": id}
    except Exception as error:
        return{"message": error}
