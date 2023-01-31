import unittest

from parameterized import parameterized

from src.Langue.LangueEn import LangueEn
from src.Langue.LangueFr import LangueFr
from OhceBuilder import OhceBuilder
from LangueSpy import LangueSpy


class SalutationTest(unittest.TestCase):
    @parameterized.expand(
        [
            [LangueEn(), "Hello"],
            [LangueFr(), "Bonjour"],
        ])
    def test_bonjour(self, langue, retour):
        ohce = OhceBuilder().langue_defini(langue).build()
        resultat = ohce.bonjour()

        self.assertEqual(retour, resultat)

    @parameterized.expand(
        [
            [LangueEn(), "Goodbye"],
            [LangueFr(), "Au revoir"],
        ])
    def test_au_revoir(self, langue, retour):
        ohce = OhceBuilder().langue_defini(langue).build()
        resultat = ohce.au_revoir()

        self.assertEqual(retour, resultat)

if __name__ == '__main__':
    unittest.main()