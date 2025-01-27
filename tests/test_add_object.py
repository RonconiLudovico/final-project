import unittest

from utils.convert_json import locations, objects
from utils.add_object import add_object


class Test01(unittest.TestCase):
    def test_add_object(self):
        '''
        Here we'll test the add_object function
        '''
        data = ["test", "Bathroom", "test"]
        add_object(data)
        self.assertEqual(len(locations['Bathroom']), 1)

class Test02(unittest.TestCase):
    def test_add_object(self):
        '''
        Here we'll test the add_object function
        '''
        data = ["test", "Bathroom", "test"]
        add_object(data)
        self.assertEqual(len(objects), 5)