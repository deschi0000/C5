import unittest

from palindrome import palindrome


class TestMain(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(palindrome(808), 818)
        self.assertEqual(palindrome(0), 11)
        # self.assertEqual(palindrome(0), 12)    # Will fail


        self.assertNotEqual(palindrome(808), 817)

        # palindrome(627)
        # palindrome(621)
        # palindrome(5324322)
        # palindrome(62347)
        # palindrome(4218)
        # palindrome(4128)
        # palindrome(422178)    
        # palindrome(2133)
        # palindrome(799)
        # palindrome(808)
        # palindrome(0)
        # palindrome(624443547)
        # palindrome(5324522)    
        # palindrome(3**39)