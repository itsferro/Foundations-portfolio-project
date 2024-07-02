#!/usr/bin/python3
"""
"""
from typing import Union
from pydantic import BaseModel


class delivery_services(BaseModel):
    id: int
    delivery_service_name: str
    description: str
    note: Union[str, None] = None
