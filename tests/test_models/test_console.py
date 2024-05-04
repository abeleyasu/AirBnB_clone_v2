#!/usr/bin/python3
"""
Unittest for console.py
"""
import unittest
from unittest.mock import patch
import io
import os
from console import HBNBCommand
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Unittest class for the console
    """

    def setUp(self):
        """
        Set up test environment
        """
        self.console = HBNBCommand()
        self.test_attr = {'city_id': '0001', 'user_id': '0001',
                          'name': 'My little house', 'number_rooms': 4,
                          'number_bathrooms': 2, 'max_guest': 10,
                          'price_by_night': 300, 'latitude': 37.773972,
                          'longitude': -122.431297}

    def tearDown(self):
        """
        Clean test environment
        """
        del self.console

    def test_create(self):
        """
        Test create command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            state_id = f.getvalue().strip()
        state = storage.all()["State." + state_id]
        self.assertTrue(isinstance(state, State))
        self.assertEqual(state.name, "California")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create Place {}".format(
                                ' '.join(["{}=\"{}\"".format(k, v)
                                          for k, v in self.test_attr.items()])))
            place_id = f.getvalue().strip()
        place = storage.all()["Place." + place_id]
        self.assertTrue(isinstance(place, Place))
        for k, v in self.test_attr.items():
            self.assertEqual(getattr(place, k), v)

    def test_show(self):
        """
        Test show command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show State {}".format(state_id))
            output = f.getvalue().strip()
        self.assertTrue(output.startswith("[State] ({})".format(state_id)))
        self.assertIn("'name': 'California'", output)

    def test_destroy(self):
        """
        Test destroy command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            state_id = f.getvalue().strip()

        self.assertIn("State." + state_id, storage.all())
        self.console.onecmd("destroy State " + state_id)
        self.assertNotIn("State." + state_id, storage.all())

    def test_all(self):
        """
        Test all command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("all State")
            output = f.getvalue().strip()
        self.assertIn("State." + state_id, output)

    def test_count(self):
        """
        Test count command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("count State")
            output = f.getvalue().strip()
        self.assertEqual(output, "7")

    def test_update(self):
        """
        Test update command
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("update State {} name \"New California\"".format(
                state_id))
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show State " + state_id)
            output = f.getvalue().strip()
        self.assertIn("'name': 'New California'", output)

    def test_update_string(self):
        """
        Test update command with string
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create State name=\"California\"")
            state_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("update State {} name \"New California\"".format(
                state_id))
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show State " + state_id)
            output = f.getvalue().strip()
        self.assertIn("'name': 'New California'", output)

    def test_update_float(self):
        """
        Test update command with float
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create Place {}".format(
                                ' '.join(["{}=\"{}\"".format(k, v)
                                          for k, v in self.test_attr.items()])))
            place_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("update Place {} latitude 37.774".format(
                place_id))
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show Place " + place_id)
            output = f.getvalue().strip()
        self.assertIn("'latitude': 37.774", output)

    def test_update_integer(self):
        """
        Test update command with integer
        """
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("create Place {}".format(
                                ' '.join(["{}=\"{}\"".format(k, v)
                                          for k, v in self.test_attr.items()])))
            place_id = f.getvalue().strip()

        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("update Place {} max_guest 20".format(
                place_id))
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.console.onecmd("show Place " + place_id
