import unittest
from contact import Contact

class TestContact(unittest.TestCase):


    """
    Test  class that defines the test cases
    args:
        unittest.TestCase helps in creating test cases
    """

    def setUp(self):
        self.new_contact=Contact("James", "Mwangi", "0718074934", "briememo95@gmail.com")

    def test_init(self):
        '''
        test init test case to test if the objects is initialized properly.
        '''
        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Mwangi")
        self.assertEqual(self.new_contact.phone_number, "0718074934")
        self.assertEqual(self.new_contact.email, "briememo95@gmail.com")

    def test_init(self):
        """
        test_save_contact test case to if the contact object is saved into the contact list
        """
if __name__=="_main_":
    unittest.main()
