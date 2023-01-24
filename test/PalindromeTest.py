import unittest

from src.Ohce import Ohce

class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        chaine = "Cameron"

        resultat = Ohce.miroir(chaine)

        self.assertIn(chaine[::-1], resultat)

    def test_palindrome(self):
        chaine = "kayak"
        retour = chaine + "Bien dit"

        resultat = Ohce.palindrome(chaine)

        self.assertEqual(retour, resultat)

if __name__ == '__main__':
    unittest.main()