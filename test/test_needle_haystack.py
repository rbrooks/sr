import unittest
from needle_haystack import is_found_in

class TestNeedleHaystack(unittest.TestCase):

    def test_positive_match(self):
        self.assertTrue(is_found_in('sent', 'This is a sentence.'))

    def test_positive_match_end(self):
        self.assertTrue(is_found_in('ence.', 'This is a sentence.'))

    def test_positive_match_beg(self):
        self.assertTrue(is_found_in('This', 'This is a sentence.'))

    def test_positive_match_single_word(self):
        self.assertTrue(is_found_in('Shop', 'Shoprunner'))

    def test_negative_match(self):
        self.assertFalse(is_found_in('asdf', 'This is a sentence.'))

    def test_negative_match_case(self):
        self.assertFalse(is_found_in('this', 'This is a sentence.'))

    def test_negative_match_num(self):
        self.assertFalse(is_found_in('1234', 'This is a sentence.'))

    def test_negative_match_single_word(self):
        self.assertFalse(is_found_in('Amazon', 'Shoprunner'))

if __name__ == '__main__':
    unittest.main()
