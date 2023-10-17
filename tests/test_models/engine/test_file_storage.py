import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Unit tests for the FileStorage class.
    """

    __file_path = "file.json"

    @classmethod
    def setUpClass(cls):
        """
        Set up the FileStorage and BaseModel objects for testing.
        """
        cls.storage = FileStorage()
        cls.model = BaseModel()

    def tearDown(self):
        """
        Clean up the file created during testing, if it exists.
        """
        if os.path.exists(self.__file_path):
            os.remove(self.__file_path)

    def test_file_path(self):
        """
        Test the file path attribute of FileStorage.
        """
        self.assertEqual(self.__file_path, FileStorage._FileStorage__file_path)

    def test_all(self):
        """
        Test the all() method of FileStorage.
        """
        self.assertIsInstance(self.storage.all(), dict)
        self.assertGreaterEqual(len(self.storage.all()), 0)

    def test_new(self):
        """
        Test the new() method of FileStorage.
        """
        self.storage.new(self.model)
        key = f"{type(self.model).__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """
        Test the save() method of FileStorage.
        """
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.__file_path))

    def test_reload(self):
        """
        Test the reload() method of FileStorage.
        """
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        key = f"{type(self.model).__name__}.{self.model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
