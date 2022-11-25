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

    def save(self):
        """
        serializes __objects to the JSON file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        It deserializes the JSON file
        """
       try:
           with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
               new = json.load(f)
        for key, valu in new.items:
            FileStorage.__objects[key] = BaseModel(**v)
        except:
            pass
