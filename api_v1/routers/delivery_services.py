#!/usr/bin/python3
"""
delivery services table CRUD functions.
"""


from types import Union
from fastapi import Response, APIRouter, Depends, status, Response, HTTPException
from helper_functions.get_queries_from_file import get_queries
from helper_functions.connect_to_database import get_session
from pydantic_models.delivery_services import delivery_services_in
import mysql.connector
import json


router = APIRouter(
        prefix='/delivery_services',
        tags=['delivery_services']
        )

# delivery services file path
path = "delivery_services/"


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(data: delivery_services_in, db = Depends(get_session)):
    """
    creates deleviry service row in the delivery services table.
    """
    query = get_queries(path + "create.sql")
    print(f"\nquery:\n{query}")
    print(f"data:\n{data}\n")
    db.execute(query, data.model_dump())
    data.id = db.lastrowid
    print(db)
    print()
    return ({
        "message": query,
        "data_added": data,
        })


@router.get("/")
def read(id: Union[int, None], db = Depends(get_session)):
    """
    fetches from the delivery services table.
    """
    if id:
        query = get_queries(path + "read_one_by_id.sql")
        print(f"\nquery:\n{query}")
        db.execute(query, {"id": id})
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
def update(id: int, data: delivery_services_in, db = Depends(get_session)):
    """
    updates a deleviry service row by id
    in the delivery services table.
    """
    query = get_queries(path + "update.sql")
    print(f"\nquery:\n{query}")
    print(f"id:\n{id}")
    print(f"\ndata:\n{data}\n")
    data.id = id
    db.execute(query, data.model_dump())
    print(db)
    print()
    return ({
        "message": query,
        "id": id,
        "data_updated": data.model_dump(),
        "values": data.to_tuple()
        })


@router.delete("/{id}")
def delete(id: int, db = Depends(get_session)):
    """
    deletes a delivery service row bu id
    from the delivery services table.
    """
    query = get_queries(path + "delete.sql")
    print(f"\nquery:\n{query}")
    print(f"id:\n{id}\n")
    try:
        db.execute(query, {"id": id})
        db.execute("SELECT ROW_COUNT()")
        effected_tables = db.fetchone()
        return {"message": query, "id": id, "effected_tables": effected_tables}
    except Exception as error:
        print(error)
        return {"message": "404 not fount"}
