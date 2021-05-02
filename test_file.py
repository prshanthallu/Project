import unittest
from unittest.mock import *


class TestCase(unittest.TestCase):
    @patch('file.function')
    def test_function1(self):
        result = ""
        pass
