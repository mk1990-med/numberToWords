import unittest
from numberToWord import *

class TestStringMethods(unittest.TestCase):

    def test_tens(self):
        self.assertEqual(number_to_words(70), 'soixante-dix')
        self.assertEqual(number_to_words(80), 'quatre-vingts')

    def test_numbers(self):
        self.assertEqual(number_to_words(22),"vingt-deux")
        self.assertEqual(number_to_words(17),"dix-sept")
        self.assertEqual(number_to_words(21),"vingt-et-un")
        self.assertEqual(number_to_words(74),"soixante-quatorze")
        self.assertEqual(number_to_words(77),"soixante-dix-sept")
        self.assertEqual(number_to_words(95),"quatre-vingt-quinze")
        self.assertEqual(number_to_words(99),"quatre-vingt-dix-neuf")
        self.assertEqual(number_to_words(82),"quatre-vingt-deux")
        self.assertEqual(number_to_words(71),"soixante-et-onze")
        self.assertEqual(number_to_words(81),"quatre-vingt-un")
        self.assertEqual(number_to_words(91),"quatre-vingt-onze")
        self.assertEqual(number_to_words(130),"cent-trente")
        self.assertEqual(number_to_words(1110),"mille-cent-dix")
        self.assertEqual(number_to_words(200),"deux-cents")
        self.assertEqual(number_to_words(252),"deux-cent-cinquante-deux")
        self.assertEqual(number_to_words(200000),"deux-cent-mille")
        self.assertEqual(number_to_words(180000),"cent-quatre-vingt-mille")


if __name__ == '__main__':
    unittest.main()