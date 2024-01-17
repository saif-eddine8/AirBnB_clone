#!/usr/bin/python3
"""Storage of a file class"""                    
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """to abstact engine of storage      

    Attributes:
    __file_pat (str): arg one
    __objects (dict): arg two
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """to dict"""                 
        return FileStorage.__objects

    def new(self, obj):
        """key object"""                             
        my_name = obj.__class__.__name__                    
        FileStorage.__objects["{}.{}".format(my_name, obj.id)] = obj

    def save(self):
        """to serialize"""                    
        my_dic = FileStorage.__objects                     
        my_ob_dic = {obj: my_dic[obj].to_dict() for obj in my_dic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_ob_dic, f)

    def reload(self):
        """to deserialize"""                  
        try:
            with open(FileStorage.__file_path) as f:
                my_ob_dic = json.load(f)                 
                for j in my_ob_dic.values():
                    className = j["__class__"]
                    del j["__class__"]
                    self.new(eval(className)(**j))
        except FileNotFoundError:
            return

