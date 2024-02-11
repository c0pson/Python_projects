import random
import time

def matrix_effect(rows: int, cols: int):
    """
    Function to generate a matrix effect animation.

    Parameters:
    - rows: int
        The number of rows in the matrix.
    - cols: int
        The number of columns in the matrix.

    Returns:
    - None

    Raises:
    - ValueError:
        Raises an error if either rows or cols is less than or equal to zero.
    """

    # Validating the input parameters
    if rows <= 0 or cols <= 0:
        raise ValueError("Number of rows and columns should be greater than zero.")

    # Creating an empty matrix
    matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

    # List of characters for the matrix effect
    characters = ['0', '1']

    # Loop to generate the matrix effect animation
    while True:
        # Clearing the console
        print("\033c", end='')

        # Updating the matrix with random characters
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = random.choice(characters)

        # Printing the matrix
        for row in matrix:
            print(' '.join(row))

        # Delaying the animation
        time.sleep(0.1)

# Unit tests for matrix_effect function.

import unittest
from io import StringIO
from unittest.mock import patch

class TestMatrixEffect(unittest.TestCase):

    def test_valid_matrix_effect(self):
        """
        Tests the matrix_effect function with valid input parameters.
        """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            matrix_effect(5, 10)
            output = fake_output.getvalue().strip()
            self.assertEqual(len(output.split('\n')), 5)

    def test_zero_rows_and_cols(self):
        """
        Tests if ValueError is raised when rows or cols is zero.
        """
        with self.assertRaises(ValueError):
            matrix_effect(0, 5)
        with self.assertRaises(ValueError):
            matrix_effect(5, 0)
        with self.assertRaises(ValueError):
            matrix_effect(0, 0)

    def test_negative_rows_and_cols(self):
        """
        Tests if ValueError is raised when rows or cols is negative.
        """
        with self.assertRaises(ValueError):
            matrix_effect(-5, 10)
        with self.assertRaises(ValueError):
            matrix_effect(5, -10)
        with self.assertRaises(ValueError):
            matrix_effect(-5, -10)

# Example usage of matrix_effect function:

matrix_effect(10, 20)
