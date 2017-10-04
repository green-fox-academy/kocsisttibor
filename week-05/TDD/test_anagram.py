import unittest
import anagram

class TestExtend(unittest.TestCase):
    def test_angram_maker(self):
        self.assertTrue(anagram.decide_anagram("alma", "mala"))


    def test_one_letter_is_different(self):
         self.assertFalse(anagram.decide_anagram("alma", "almm"))

    def test_different_len_words(self):
        self.assertTrue(anagram.decide_anagram("alma", "alma "))

    def test_one_is_empty(self):
        self.assertFalse(anagram.decide_anagram('',"alma"))

    def test_one_is_none(self):
        self.assertFalse(anagram.decide_anagram(None, "alma"))


if __name__ == '__main__':
    unittest.main()