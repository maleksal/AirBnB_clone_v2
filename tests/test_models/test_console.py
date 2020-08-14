#!/usr/bin/python3
"""Unittests for console Module"""
import unittest
import os
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test console"""

    def setUp(self):
        """SetUp"""
        pass

    def tearDown(self):
        """TearDown"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_create_method_work_valid_args(self):
        """ test create method with valid args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, '\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')

    def test_create_method(self):
        """ test create method with parameter name"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place name=\"UK\"")
            HBNBCommand().onecmd("all Place")
        msg = f.getvalue()[:-1]
        self.assertRegex(msg, "'place': 'UK'")

    def test_create_method_without_args(self):
        """ test create method without args"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class name missing **")
