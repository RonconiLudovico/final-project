import unittest

import utils.convert_json

class TestConvertJson(unittest.TestCase):
    def test_convert_json(self):
        '''
        Here we are testing the output of the converting function to be a dictionary
        '''
        self.assertEqual(type(utils.convert_json.objects), dict)

class TestConvertJson2(unittest.TestCase):
    def test_convert_json_2(self):
        '''
        Here we are testing the output of the converting function to be a dictionary
        '''
        self.assertEqual(type(utils.convert_json.locations), dict)

class TestConvertJson3(unittest.TestCase):
    def test_convert_json_3(self):
        '''
        Here we are testing the output of the converting function to be a dictionary
        '''
        self.assertEqual(type(utils.convert_json.menu), dict)


class TestConvertJson4(unittest.TestCase):
    def test_convert_json(self):
        '''
        Here we are testing the output of the converting function to have maintained the same amount of elements
        '''
        self.assertEqual(len(utils.convert_json.objects), 4)


class TestConvertJson5(unittest.TestCase):
    def test_convert_json(self):
        '''
        Here we are testing the output of the converting function to have maintained the same amount of elements
        '''
        self.assertEqual(len(utils.convert_json.locations), 6)


class TestConvertJson6(unittest.TestCase):
    def test_convert_json(self):
        '''
        Here we are testing the output of the converting function to have maintained the same amount of elements
        '''
        self.assertEqual(len(utils.convert_json.menu), 4)