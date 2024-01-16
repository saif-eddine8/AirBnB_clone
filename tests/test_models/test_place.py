#!/usr/bin/python3
"""base_model unittests              

Unittest classes:
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
import models                       
from datetime import datetime 
from models.base_model import BaseModel


class TestBaseModel_save(unittest.TestCase):
    """method of saving unittests"""                 

    def test_updateF(self):                
        j = BaseModel()                 
        j.save()
        cI = "BaseModel." + j.id
        with open("file.json", "r") as f:
            self.assertIn(cI, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """ method of to_dict unittests"""                      
    
    def test_to_dict_date_attr_str(self):            
        j = BaseModel()                                 
        c_dic = j.to_dict()
        self.assertEqual(str, type(c_dic["created_at"]))
        self.assertEqual(str, type(c_dic["updated_at"]))


if __name__ == "__main__":
    unittest.main()

