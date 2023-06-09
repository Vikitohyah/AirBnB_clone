#!/usr/bin/python3
'''Tests for User class'''
import models
from models.base_model import BaseModel
from models.place import Place
import os
import unittest


class TestPlace(unittest.TestCase):
    '''starts tests'''

    def test_docstring(self):
        '''tests if funcions, methods, classes
        and modules have docstring'''
        msj = "Módulo does not has docstring"
        self.assertIsNotNone(models.place.__doc__, msj)  # Modules
        msj = "Clase does not has docstring"
        self.assertIsNotNone(Place.__doc__, msj)  # Classes

    def test_executable_file(self):
        '''tests if a file has permissions u+x to execute'''
        # Check for read access
        is_read_true = os.access('models/place.py', os.R_OK)
        self.assertTrue(is_read_true)
        # Check for write access
        is_write_true = os.access('models/place.py', os.W_OK)
        self.assertTrue(is_write_true)
        # Check for execution access
        is_exec_true = os.access('models/place.py', os.X_OK)
        self.assertTrue(is_exec_true)

    def test_is_an_instance(self):
        '''checks if my_model is an instance of BaseModel'''
        my_place = Place()
        self.assertIsInstance(my_place, Place)
