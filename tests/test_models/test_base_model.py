"""
Unit tests for the BaseModel class.
"""

import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test__init(self):
        """Test the initialization of a BaseModel object."""
        a_model = BaseModel()
        self.assertIsInstance(a_model, BaseModel)
        self.assertEqual(len(a_model.id), 36)

    def test_save(self):
        """Test the save method of a BaseModel object."""
        b_model = BaseModel()
        b_model.save()
        self.assertNotEqual(b_model.created_at, b_model.updated_at)
