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
