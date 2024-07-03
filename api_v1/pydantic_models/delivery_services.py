#!/usr/bin/python3
"""
"""
from typing import Union
from pydantic import BaseModel, Field


class delivery_services(BaseModel):

    def to_tuple(self):
        data = []
        for attr, value in self.__dict__.items():
            data.append(value)
        return tuple(data)


class delivery_services_in(delivery_services):
    id: int = Field(default=None)
    delivery_service_name: str
    description: str
    note: Union[str, None] = None
