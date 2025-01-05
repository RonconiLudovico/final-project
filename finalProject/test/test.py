import unittest
from unittest.mock import patch

from src.utils.add_seat import ask_how_many_seats
from src.utils.add_seat import update_reservation

def add_one(param):
    return param + 1


class Test01(unittest.TestCase):
    def test_add_seat(self):
        '''
        This is the test for the add seat function
        '''
    @patch('builtins.input', return_value = 3)
    def test_ask_how_many(self):
        self.assertEqual(3, ask_how_many_seats())


class Test02(unittest.TestCase):
    def test_update_reservation(self):
        reservation_dict = {"a" : [1, 3], "b" : [2, 5], "c" : [3, 7]}
        update_reservation(reservation_dict, "b", 3)
        self.assertEqual(reservation_dict, {"a" : [1, 3], "b" : [2, 8], "c" : [3, 7]})
        