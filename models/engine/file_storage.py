#!/usr/bin/python3
"""
Module: file_storage
"""

import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, "r") as file:
            serialized_data = json.load(file)

        for object_key, object_value in serialized_data.items():
            class_name, object_id = object_key.split(".")
            object_class = globals().get(class_name)
            if object_class:
                object_instance = object_class(**object_value)
                self.__objects[object_key] = object_instance
