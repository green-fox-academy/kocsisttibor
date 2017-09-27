import unittest
from kt_work import Apple, Sum, Anagramma, CountLetter, Fibonacci

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

class TestAnagramma(unittest.TestCase):

    def test_anagramma_same_word(self):
        test_instance = Anagramma()
        self.assertTrue(test_instance.anagramma("alma", "alma"))


    def test_anagramma_letters_mixed(self):
        test_instance = Anagramma()
        self.assertTrue(test_instance.anagramma("alma", "lama"))


    def test_not_anagramma(self):
        test_instance = Anagramma()
        self.assertFalse(test_instance.anagramma("alma", "bela"))

    
    def test_not_same_length(self):
        test_instance = Anagramma()
        self.assertFalse(test_instance.anagramma("alma", "la"))

class TestCountLetter(unittest.TestCase):

    def test_single_letter(self):
        test_instance = CountLetter()
        self.assertEqual(test_instance.count_letter("apple")["a"], 1)


    def test_double_letter(self):
        test_instance = CountLetter()
        self.assertEqual(test_instance.count_letter("apple")["p"], 2)


    def test_one_letter(self):
        test_instance = CountLetter()
        self.assertEqual(test_instance.count_letter("a")["a"], 1)

    
    def test_no_letter(self):
        test_instance = CountLetter()
        self.assertEqual(test_instance.count_letter(""), {})

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_0(self):
        test_instance = Fibonacci()
        self.assertEqual(test_instance.fibonacci(0), 0)


    def test_fibonacci_2(self):
        test_instance = Fibonacci()
        self.assertEqual(test_instance.fibonacci(2), 1)


    def test_fibonacci_6(self):
        test_instance = Fibonacci()
        self.assertEqual(test_instance.fibonacci(6), 8)

if __name__ == "__main__":
    unittest.main()
