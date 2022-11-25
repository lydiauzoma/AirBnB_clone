#!/usr/bin/python3
"""
The file storage class
"""
import json

class FileStorage:
    """
    The file storage class
    """

    __file_path = "file.json"
    __objects = dict()
    def __init__(self):
        """
        The constructor function
        """
        pass
    
    def all(self):
        """
        it returns all in the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in oobjects he obj 
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__object[key] = obj
