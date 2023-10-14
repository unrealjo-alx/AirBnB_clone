#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Base model with common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.
        """
        f_dict = self.__dict__.copy()
        f_created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        f_updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        f_dict["__class__"] = type(self).__name__
        f_dict["created_at"] = f_created_at
        f_dict["updated_at"] = f_updated_at
        return f_dict
