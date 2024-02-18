#!/usr/bin/python3
"""this module  serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
import uuid
import datetime
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class FileStorage:
    """class to serialize and deserialize"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[obj.__class__.__name__+'.'+obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        transdict = {}
        for key, value in self.__objects.items():
            transdict[key] = value.to_dict()
        with open(self.__file_path, 'w') as tojsonfile:
            json.dump(transdict, tojsonfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as jfile:
                jdata = json.load(jfile)
                for k, v in jdata.items():
                    class_name, obj_id = k.split('.')
                    self.__objects[k] = eval(class_name)(**v)
        except FileNotFoundError:
            pass
