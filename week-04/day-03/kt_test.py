import unittest
from kt_work import Apple, Sum, Anagramma

class TestGetApple(unittest.TestCase):

    def test_apple_is_returned(self):
        test_apple = Apple()
        self.assertEqual(test_apple.get_apple(), "apple")

class TestSum(unittest.TestCase):

    def test_sum_with_three_items(self):
        test_list_of_ints = Sum()
        self.assertEqual(test_list_of_ints.sum_of_numbers([5, 6, 7]), 18)


    def test_sum_with_empty_list(self):
        test_list_of_ints = Sum()
        self.assertEqual(test_list_of_ints.sum_of_numbers([]), 0)


    def test_sum_with_one_element(self):
        test_list_of_ints = Sum()
        self.assertEqual(test_list_of_ints.sum_of_numbers([5]), 5)


    def test_sum_with_none_element(self):
        test_list_of_ints = Sum()
        self.assertEqual(test_list_of_ints.sum_of_numbers(None), None)

    # def test_sum_with_empty_list(self):                 #this is not running
    #     test_list_of_ints = Sum()
    #     with self.assertRaises(TypeError, ):
    #         test_list_of_ints.sum_of_numbers()

# class TestAnagrammaAskinput(unittest.TestCase):

#     def test_ask_input(self):
#         anagramma = Anagramma()
#         self.assertIsInstance(anagramma.ask_input[0], str)

if __name__ == "__main__":
    unittest.main()
