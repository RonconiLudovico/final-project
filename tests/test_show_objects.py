import unittest
from utils.show_objects import show_objects

class Test_show_objects(unittest.TestCase):
    def test_show_objects(self):
        '''
        Here we'll test the function show_objects to return a string of all the objects
        '''
        self.assertEqual(show_objects(), "Storage room contains: Broom, Mop;\nEntrance contains: Batteries;\nKitchen contains: Microwave;\nLiving room contains: Air Conditioner;\n")