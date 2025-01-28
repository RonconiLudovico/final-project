import unittest
from unittest.mock import patch

from main import menu_engine


class Test01(unittest.TestCase):
    @patch("builtins.input", side_effect=['1'])
    def test_menu_1(self, mock_input):
        '''
        Here we will test the menu engine function to return the 1 choice result
        '''
        result = menu_engine()
        mock_input.assert_called()
        self.assertEqual(result, )