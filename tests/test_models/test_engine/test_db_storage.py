#!/usr/bin/python3
"""
testing file storage module
"""
import unittest
from os import getenv

db = getenv('HBNB_TYPE_STORAGE')


class test_Db_Storage(unittest.TestCase):
    """
    Testing Db storage class
    """


if __name__ == '__main__':
    unittest.main()
