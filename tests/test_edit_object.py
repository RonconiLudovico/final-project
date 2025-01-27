import unittest
from unittest.mock import patch

from utils.convert_json import locations, objects
from utils.edit_object import edit_object

class Test01(unittest.TestCase):
    @patch("builtins.input", side_effect=["name", "Oven"])
    def test_edit_object(self, mock_input):
        '''
        Here we'll test the edit_object function for the name attribute
        '''
        data = ["Microwave", "Kitchen", "Cooking"]
        edit_object(data)
        mock_input.assert_called()
        self.assertEqual(locations["Kitchen"], ["Oven"])

class Test02(unittest.TestCase):
    @patch("builtins.input", side_effect=["location", "Storage room"])
    def test_edit_object(self, mock_input):
        '''
        Here we'll test the edit_object function for the location attribute
        '''
        data = ["Microwave", "Kitchen", "Cooking"]
        edit_object(data)
        mock_input.assert_called()
        self.assertEqual(locations['Storage room'], ["Broom", "Mop", "Microwave"])

class Test03(unittest.TestCase):
    @patch("builtins.input", side_effect=["category", "Leisure"])
    def test_edit_object(self, mock_input):
        '''
        Here we'll test the edit_object function for the category attribute
        '''
        data = ["Microwave", "Kitchen", "Cooking"]
        edit_object(data)
        mock_input.assert_called()
        self.assertEqual(objects[data[0]][1], "Leisure")