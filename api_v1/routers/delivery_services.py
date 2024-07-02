#!/usr/bin/python3
"""
delivery services table CRUD functions.
"""


from fastapi import Response, APIRouter, Depends, HTTPException
from helper_functions.get_queries_from_file import get_queries
from helper_functions.connect_to_database import get_session
import mysql.connector
import json


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
    print(f"\nquery:\n{query}")
    print(f"data:\n{data}\n")
    dict_data = json.loads(data)
    values = []
    values.append(dict_data.get("name"))
    values.append(dict_data.get("desc"))
    values.append(dict_data.get("note"))
    db.execute(query, tuple(values))
    print(db)
    print()
    return ({
        "message": query,
        "data_added": dict_data,
        "values": values
        })


@router.get("/")
def read(id: int = None, db = Depends(get_session)):
    """
    fetches from the delivery services table.
    """
    if id:
        query = get_queries(path + "read_one_by_id.sql")
        print(f"\nquery:\n{query}")
        db.execute(query, (id,))
        row = db.fetchall()
        if row:
            return {"message": row}
        else:
            return {"message": "404 not found"}
    else:
        query = get_queries(path + "read_all.sql")
        print(f"\nquery:\n{query}")
        db.execute(query)
        rows = db.fetchall()
        return {"message": rows}


@router.put("/{id}")
def update(id, data, db = Depends(get_session)):
    """
    updates a deleviry service row by id
    in the delivery services table.
    """
    query = get_queries(path + "update.sql")
    print(f"\nquery:\n{query}")
    print(f"id:\n{id}")
    print(f"\ndata:\n{data}\n")
    dict_data = json.loads(data)
    values = []
    values.append(dict_data.get("name"))
    values.append(dict_data.get("desc"))
    values.append(dict_data.get("note"))
    values.append(id)
    db.execute(query, tuple(values))
    print(db)
    print()
    return ({
        "message": query,
        "id": id,
        "data_updated": dict_data,
        "values": values
        })


@router.delete("/{id}")
def delete(id, db: int = Depends(get_session)):
    """
    deletes a delivery service row bu id
    from the delivery services table.
    """
    query = get_queries(path + "delete.sql")
    print(f"\nquery:\n{query}")
    print(f"id:\n{id}\n")
    db.execute(query, (id,))
    return {"message": query, "id": id}
