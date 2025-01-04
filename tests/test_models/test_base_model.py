import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def test_instance(self):
        """Test if an object is an instance of BaseModel"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

if __name__ == '__main__':
    unittest.main()

