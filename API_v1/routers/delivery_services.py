#!/usr/bin/python3
"""
delivery services table CRUD functions.
"""


from fastapi import APIRouter
from helper_functions.get_queries_from_file import get_queries
import sqlite3


router = APIRouter(
        prefix='/delivery_services',
        tags=['delivery_services']
        )

# delivery services file path
path = "delivery_services/"

def delivery_service(conn, data):
    """
    creates deleviry service row in the delivery services table.
    """
    query = get_queries(path + "create.sql")
    print(query)


def read_all_delivery_services():
    """
    fetches all rows from the delivery services table.
    """
    pass


def update_delivery_service():
    """
    updates a deleviry service row by id
    in the delivery services table.
    """
    pass


def delete_delivery_service():
    """
    deletes a delivery service row bu id
    from the delivery services table.
    """
    pass
