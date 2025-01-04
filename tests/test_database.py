import unittest
import MySQLdb
from io import StringIO
import sys
from your_console_file import HBNBCommand  # Update with the actual path

class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Set up the test case."""
        self.db = MySQLdb.connect(host="localhost", user="hbnb_test", passwd="hbnb_test_pwd", db="hbnb_test_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Tear down the test case."""
        self.cursor.close()
        self.db.close()

    def test_create_state(self):
        """Test to check if a new state is added to the database."""
        # Get the initial count of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        initial_count = self.cursor.fetchone()[0]

        # Call the console command to create a new state (make sure it's correct)
        console_output = StringIO()
        sys.stdout = console_output
        HBNBCommand().onecmd('create State name="California"')
        sys.stdout = sys.__stdout__

        # Get the count of records in the states table after insertion
        self.cursor.execute("SELECT COUNT(*) FROM states;")
        new_count = self.cursor.fetchone()[0]

        # Assert that the number of records has increased by 1
        self.assertEqual(new_count, initial_count + 1)

if __name__ == "__main__":
    unittest.main()

