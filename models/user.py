#!/usr/bin/python3
"""
user.py : Defines the class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new User instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
