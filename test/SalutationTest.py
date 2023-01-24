import unittest

from src.Ohce import Ohce

class SalutationTest(unittest.TestCase):
    def test_bonjour(self):
        retour = "Bonjour"

        ohce = Ohce()
        resultat = ohce.bonjour()

        self.assertEqual(retour, resultat)

    def test_au_revoir(self):
        retour = "Au revoir"

        ohce = Ohce()
        resultat = ohce.au_revoir()

        self.assertEqual(retour, resultat)

if __name__ == '__main__':
    unittest.main()