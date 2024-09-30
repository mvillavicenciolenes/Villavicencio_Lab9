import unittest
from unittest.mock import patch
import io
import studentgrade

class TestMainFunction(unittest.TestCase):

    # Test with valid inputs
    @patch('builtins.input', side_effect=['3', '85', '90', '75'])  # Mock user input
    @patch('sys.stdout', new_callable=io.StringIO)  # Capture printed output
    def test_valid_input(self, mock_stdout, mock_input):
        # Call the function 'main()' from 'studentGrade.py'
        studentgrade.main()

        # Retrieve the captured output
        output = mock_stdout.getvalue()

        # Check if the printed output is as expected
        self.assertIn("The class average is 83.33\n", output)

    # Test with invalid input first, then valid inputs
    @patch('builtins.input', side_effect=['2', '-1', '85', '72'])  # Mock user input
    @patch('sys.stdout', new_callable=io.StringIO)  # Capture printed output
    def test_invalid_input_then_valid(self, mock_stdout, mock_input):
        studentgrade.main()

        output = mock_stdout.getvalue()

        # Check for invalid input message and average
        self.assertIn("Invalid Input.\n", output)  # Match the actual printed message
        self.assertIn("The class average is 78.50", output)

    #test for invalid grade
    @patch('builtins.input', side_effect=['2', '102', '82', '-10', '70'])  # Mock user input
    @patch('sys.stdout', new_callable=io.StringIO)  # Capture printed output   

    def test_invalid_grade(self, mock_stdout, mock_input):
        #call the function main() from studentgrade.py
        studentgrade.main()

        #retrieve the capture output
        output = mock_stdout.getvalue()

        # Check if the printed output is as expected
        self.assertIn("Invalid Input. Grade must be between 0 and 100.")
        self.assertIn("The class average is 76.00", output)
        
    #test for invalid value of input number of students

    #test for invalid value of grades

    






if __name__ == "__main__":
    unittest.main()
