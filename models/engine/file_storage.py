#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class HBNBCommand:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

def reload(self):
        """Loads storage dictionary from file"""
        import unittest
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

class HBNBCommand(unittest.TestCase):
    def setUp(self):
        self.hbnb = HBNBCommand()
        self.storage = HBNBCommand()
        self.hbnb.storage = self.storage

    def tearDown(self):
        self.storage._FileStorage__objects = {}

    # Add your tests here
    
    def test_do_create_with_parameters(self):
        # Test with string and integer parameters
        self.assertFalse(self.storage.all())  # Ensure storage is empty

        # Create an object of the class with string and integer parameters
        self.hbnb.do_create("MyClass string_param=\"Hello\" int_param=123")

        # Check if the object was created and saved
        objects = self.storage.all()
        self.assertEqual(len(objects), 1)  # Expecting 1 object in storage
        obj = list(objects.values())[0]
        self.assertEqual(obj.__class__.__name__, "MyClass")  # Object class should match
        self.assertEqual(obj.string_param, "Hello")  # string_param should match
        self.assertEqual(obj.int_param, 123)  # int_param should match

    if __name__ == '__main__':
        unittest.main()
