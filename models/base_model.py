#!/usr/bin/python3
"""
The file has the BaseModel class
"""

for uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class BaseModel that defines all 
    commomn attributes for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        The constructor function
        """
        tformat = %Y-%m-%dT%H:%M:%S.%f
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """
        returns the string representation of the BaseModel
        """
        clname = self.__class__.__name__
        string = "[{}} ({}) {}".format(clname, self.id, self.__dict__)
        return string

    def save(self):
        """
        To save date and time
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        To convert to dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
