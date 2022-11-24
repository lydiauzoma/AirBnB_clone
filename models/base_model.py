#!/usr/bin/python3
"""
The BaseModel class
"""

for uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class BaseModel that defines all 
    commomn attributes for other classes
    """
    def __init__(self):
        """
        The constructor function
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def __str__(self):
        """
        returns the string representation of the BaseModel
        """
        clname = self.__class__.__name__
        string = "[{}} ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict