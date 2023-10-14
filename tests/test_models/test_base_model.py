"""
Unit tests for the BaseModel class.
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test the initialization of a BaseModel object."""
        a_model = BaseModel()
        self.assertIsInstance(a_model, BaseModel)
        self.assertEqual(len(a_model.id), 36)

    def test_save(self):
        """Test the save method of a BaseModel object."""
        b_model = BaseModel()
        initial_updated_at = b_model.updated_at
        b_model.save()
        self.assertNotEqual(b_model.updated_at, initial_updated_at)
        self.assertGreater(b_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of a BaseModel object."""
        c_model = BaseModel()
        d_model = BaseModel(**c_model.to_dict())
        self.assertEqual(c_model.id, d_model.id)
        self.assertEqual(c_model.created_at, d_model.created_at)
        self.assertEqual(c_model.updated_at, d_model.updated_at)
        self.assertEqual(c_model.to_dict(), d_model.to_dict())

    def test_str(self):
        """Test the __str__ method of a BaseModel object."""
        e_model = BaseModel()
        string_representation = f"[BaseModel] ({e_model.id}) {e_model.__dict__}"
        self.assertEqual(str(e_model), string_representation)


if __name__ == "__main__":
    unittest.main()
