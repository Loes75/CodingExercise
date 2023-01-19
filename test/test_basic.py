import unittest
from src import exercise


class TestClass(unittest.TestCase):
    def test_success(self):
        list_values = [1, 9, 5, 0, 20, -4, 12, 16, 7]
        target = 12
        self.assertEqual(exercise.find_pairs_by_sum(list_values=list_values, target=target),
                         [[7, 5], [12, 0], [16, -4]])

    def test_empty_results(self):
        list_values = [3, 9, 4, 0, 20, -6, 12, 16, 7]
        target = 5
        self.assertEqual(exercise.find_pairs_by_sum(list_values=list_values, target=target),
                         [])
