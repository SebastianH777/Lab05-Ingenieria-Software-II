import unittest

from src.bubble_sort import BubbleSorter


class TestBubbleSorter(unittest.TestCase):

    def setUp(self):
        self.sorter = BubbleSorter()

    def test_cp1_single_element(self):
        # Arrange
        values = [5]
        expected = [5]

        # Act
        result = self.sorter.sort(values)

        # Assert
        self.assertEqual(expected, result)

    def test_cp2_two_elements_already_sorted(self):
        # Arrange
        values = [1, 2]
        expected = [1, 2]

        # Act
        result = self.sorter.sort(values)

        # Assert
        self.assertEqual(expected, result)

    def test_cp3_two_elements_unsorted(self):
        # Arrange
        values = [2, 1]
        expected = [1, 2]

        # Act
        result = self.sorter.sort(values)

        # Assert
        self.assertEqual(expected, result)

    def test_cp4_three_elements_already_sorted(self):
        # Arrange
        values = [1, 2, 3]
        expected = [1, 2, 3]

        # Act
        result = self.sorter.sort(values)

        # Assert
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()