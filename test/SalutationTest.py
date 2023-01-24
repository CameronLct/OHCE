import unittest

from src.Ohce import Ohce

class SalutationTest(unittest.TestCase):
    def test_bonjour(self):
        chaine = "Cameron"
        retour = "Bonjour" + chaine

        resultat = Ohce.bonjour(chaine)

        self.assertEqual(retour, resultat)

    def test_au_revoir(self):
        chaine = "Cameron"
        retour = chaine + "Au revoir"

        resultat = Ohce.bonjour()

        self.assertEqual(retour, resultat)

if __name__ == '__main__':
    unittest.main()