#!/usr/bin/python3
"""The storage file unittests         

Unittest classes:
    TestBaseModel_meth
    TestBaseModel_instansiation
"""

import unittest                                       
import models
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestBaseModel_instansiation(unittest.TestCase):
    """The storage file unittests"""                   

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_f_ins_n_arg(self):                      
        self.assertEqual(type(FileStorage()), FileStorage)
    
    def test_f_ins_with_arg(self):                        
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_f_p_str(self):                                 
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_f_l_ob_dic(self):                                     
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_str_inis(self):                        
        self.assertEqual(type(models.storage), FileStorage)


class TestBaseModel_meth(unittest.TestCase):
    """The storage file instance unittests"""                 
   
    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_args(self):                                
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):                 
        o = BaseModel()                             
        models.storage.new(o)           
        self.assertIn("BaseModel." + o.id, models.storage.all().keys())
        self.assertIn(o, models.storage.all().values())

    def test_save(self):
        o = BaseModel()                                 
        models.storage.new(o)
        models.storage.save()
        text = ""
        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + o.id, text)

    def test_reload(self):                                          
        j = BaseModel()                                                
        models.storage.new(j)
        a = FileStorage._FileStorage__objects    
        self.assertIn("BaseModel." + j.id, a)


if __name__ == "__main__":
    unittest.main()

