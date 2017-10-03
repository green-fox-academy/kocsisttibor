import unittest
from min_max_diff import min_max_difference

class MinMaxDiffTest(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_max_difference([]), "Add list of numbers as argument.")


    def test_one_element_in_list(self):
        self.assertEqual(min_max_difference([3]), 0)


    def test_two_positive_elements_in_list(self):
        self.assertEqual(min_max_difference([3, 6]), 3)


    def test_three_positive_elements_in_list(self):
        self.assertEqual(min_max_difference([18, 3, 6]), 15)


    def test_negative_elements_in_list(self):
        self.assertEqual(min_max_difference([-18, 3, 6]), 24)

if __name__ == '__main__':
    unittest.main()