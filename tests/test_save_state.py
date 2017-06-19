import sqlite3
import unittest
from dojo_classes.Dojo import Dojo


class TestSaveState(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.offices = self.dojo.create_room("office", "Blue", "Black", "Brown")
        self.living_spaces = self.dojo.create_room("living_space", "Orange", "Yellow", "Purple")

    def test_save_state(self):
        self.dojo.save_state("test_db")
        self.assertTrue(sqlite3.connect('ExternalData/test_db.db'), msg="Can't connect to saved db")
