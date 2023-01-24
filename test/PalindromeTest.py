import unittest

from src.Ohce import Ohce

class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        chaine = "Cameron"

        ohce =Ohce()

        resultat = ohce.miroir(chaine)

        self.assertIn(chaine[::-1], resultat)

    def test_palindrome(self):
        palindrome = "kayak"
        retour = "Bonjour" + palindrome + "Bien dit" + "Au revoir"

        ohce = Ohce()
        resultat = ohce.palindrome(palindrome)

        self.assertIn(retour, resultat)

if __name__ == '__main__':
    unittest.main()