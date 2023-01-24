import unittest

from src.Ohce import Ohce

class SalutationTest(unittest.TestCase):
    def test_bonjour(self):
        retour = "Bonjour"

        resultat = Ohce.bonjour()

        self.assertEqual(retour, resultat)

    def test_au_revoir(self):
        retour = "Au revoir"

        resultat = Ohce.au_revoir()

        self.assertEqual(retour, resultat)

if __name__ == '__main__':
    unittest.main()