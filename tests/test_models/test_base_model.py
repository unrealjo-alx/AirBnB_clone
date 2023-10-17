import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(len(model.id), 36)

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_updated_at)
        self.assertGreater(model.updated_at, initial_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())

    def test_str(self):
        model = BaseModel()
        expected_string = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_string)


if __name__ == "__main__":
    unittest.main()
