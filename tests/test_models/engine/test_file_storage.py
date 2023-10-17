import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    __file_path = "file.json"

    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        if os.path.exists(self.__file_path):
            os.remove(self.__file_path)

    def test_file_path(self):
        self.assertEqual(self.__file_path, "file.json")

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        self.storage.new(self.model)
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.__file_path))

    def test_reload(self):
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(type(self.model).__name__, self.model.id)
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
