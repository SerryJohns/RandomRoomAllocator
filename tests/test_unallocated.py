import unittest
from dojo_classes.Dojo import Dojo


class TestUnallocatedPeople(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.add_person("Dominic Sanders", "Fellow", "Y")
        self.dojo.add_person("Jennifer Hopkins", "Staff")
        self.dojo.add_person("Jennifer Hopkins", "Staff")

    def test_unallocated(self):
        results = self.dojo.print_unallocated()
        num_unallocated_staff = results[0]
        num_unallocated_fellows = results[1]
        num_unallocated_living = results[2]

        self.assertEqual(num_unallocated_staff, 2, "2 Staff members should not be allocated offices")
        self.assertEqual(num_unallocated_fellows, 1, "1 Fellow should not be allocated an office")
        self.assertEqual(num_unallocated_living, 1, "1 Fellow should not be allocated living space")

    def test_print_unallocated(self):
        self.dojo.print_unallocated("un_allocated_tests")
        my_file = open("../ExternalData/un_allocated_tests.txt")
        self.assertTrue(my_file, msg="Should output a .txt file")
        my_file.close()