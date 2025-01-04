import MySQLdb
import unittest
from console import HBNBCommand  # Assuming this is your console file

class TestStateCreation(unittest.TestCase):
    def setUp(self):
        """Set up MySQL connection for tests"""
        self.db = MySQLdb.connect(user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Clean up after each test"""
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        """Test that a state is created and the record count increases by 1"""
        # Get the current number of states
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]

        # Execute the command to create a new state
        HBNBCommand().onecmd("create State name='California'")

        # Get the new number of states
        self.cursor.execute("SELECT COUNT(*) FROM states")
        new_count = self.cursor.fetchone()[0]

        # Assert that one record was added
        self.assertEqual(new_count, initial_count + 1)

