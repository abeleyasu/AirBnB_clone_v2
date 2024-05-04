#!/usr/bin/python3
""" Module for FileStorage class """
import json
from models.base_model import BaseModel


class FileStorage:
    """ Serializes instances to a JSON file and deserializes JSON file to
    instances """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ Returns a dictionary of all objects
        If a class is specified, it returns a dictionary of objects of
        that type """

        if cls is None:
            return self.__objects

        obj_dict = {}
        for key, value in self.__objects.items():
            if isinstance(value, cls):
                obj_dict[key] = value
        return obj_dict

    def new(self, obj):
        """ Adds a new object to __objects """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to a JSON file """
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    obj = eval(class_name + "(**value)")
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Deletes obj from __objects if it's inside """
        if obj is None:
            return
        key = obj.__class__.__name__ + "." + obj.id
        if key in self.__objects:
            del self.__objects[key]
            self.save()
