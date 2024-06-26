#!/usr/bin/python3
""" unittest file for base_model.py"""
import unittest
import os
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for base model"""

    def test_instance_creation(self):
        """tests instantiation with no arguments"""
        model = BaseModel()
        # check that model is an instance of BaseModel
        self.assertIsInstance(model, BaseModel)
        # check that id is string
        self.assertIsInstance(model.id, str)

    def test_save_method(self):
        """test the save method"""
        model = BaseModel()
        Update = model.updated_at
        model.save()
        self.assertNotEqual(Update, model.updated_at)

    def test_save_arg(self):
        """test save with an argument passed"""
        model = BaseModel()
        with self.assertRaises(TypeError):
            model.save(None)

    def test_save_json(self):
        """test save and read it"""
        model = BaseModel()
        model.save()
        modelid = "BaseModel." + model.id
        with open("file.json", "r") as f:
            self.assertIn(modelid, f.read())

    def test_to_dict_method(self):
        """test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        # check that id, created_at, and updated_at are set and are strings
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.updated_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
