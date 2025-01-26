import unittest

from utils.convert_json import locations, objects
from utils.delete_object import del_object

class Test01(unittest.TestCase):
    def test_del_object(self):
        '''
        Here we'll test the del_object function for the location registry
        '''
        data = {"name":"Microwave", "location":"Kitchen", "category":"Cooking"}
        del_object(data)
        self.assertEqual(len(locations['Kitchen']), 0)


class Test02(unittest.TestCase):
    def test_del_object(self):
        '''
        Here we'll test the del_object function for the item registry
        '''
        data = {"name":"Microwave", "location":"Kitchen", "category":"Cooking"}
        del_object(data)
        self.assertEqual(len(objects), 3)