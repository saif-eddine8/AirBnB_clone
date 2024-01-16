#!/usr/bin/python3
"""class of BaseModel"""               

from uuid import uuid4
import models
from datetime import datetime


class BaseModel:
    """The BaseModel"""              

    def __init__(self, *args, **kwargs):
        """to Initialise                         

        Args:
            *args (any): arg one
            **kwargs (dict): arg two
        """
        my_format = "%Y-%m-%dT%H:%M:%S.%f"          
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for i, v in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(v, my_format)
                else:
                    self.__dict__[i] = v
        else:
            models.storage.new(self)

    def save(self):
        """to up to date"""                               
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """method's dic                  
        """
        my_dic = self.__dict__.copy()                       
        my_dic["created_at"] = self.created_at.isoformat()
        my_dic["updated_at"] = self.updated_at.isoformat()
        my_dic["__class__"] = self.__class__.__name__
        return my_dic

    def __str__(self):
        """to represent the method               
        """
        my_name = self.__class__.__name__                    
        return "[{}] ({}) {}".format(my_name, self.id, self.__dict__)

