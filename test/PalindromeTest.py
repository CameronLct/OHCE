import unittest

from parameterized import parameterized

from src.Langue.LangueEn import LangueEn
from src.Langue.LangueFr import LangueFr
from OhceBuilder import OhceBuilder
from LangueSpy import LangueSpy


class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        chaine = "Cameron"

        ohce = OhceBuilder().default()

        resultat = ohce.miroir(chaine)

        self.assertIn(chaine[::-1], resultat)

    @parameterized.expand([
        [LangueEn(), "Hello", "Goodbye", "Well done"],
        [LangueFr(), "Bonjour", "Au revoir", "Bien dit"],
    ])
    def test_palindrome(self, langue, bonjour, au_revoir, bien_dit):
        palindrome = "kayak"
        retour = palindrome + "Bien dit"

        ohce = OhceBuilder().langue_defini(langue).build()
        resultat = ohce.palindrome(palindrome)

        self.assertIn(bonjour + palindrome + bien_dit + au_revoir, resultat)

    def test_non_palindrome(self):
        langue = LangueSpy()
        ohce = OhceBuilder().langue_defini(langue).build()

        ohce.palindrome("Cameron")

        self.assertEqual(0, langue.nb_bien_dit)

if __name__ == '__main__':
    unittest.main()
