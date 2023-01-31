import unittest

from parameterized import parameterized

from src.Langue.LangueEn import LangueEn
from src.Langue.LangueFr import LangueFr
from OhceBuilder import OhceBuilder
from LangueSpy import LangueSpy
from src.Periode import Periode
from src.Langue.Constantes import Constantes

class PalindromeTest(unittest.TestCase):
    def test_miroir(self):
        chaine = "Cameron"

        ohce = OhceBuilder().default()

        resultat = ohce.miroir(chaine)

        self.assertIn(chaine[::-1], resultat)

    @parameterized.expand([
        [LangueEn(), Periode.DEFAULT, Constantes.English.HELLO, Constantes.English.GOOD_BYE, Constantes.English.WELL_DONE],
        [LangueEn(), Periode.MATIN, Constantes.English.GOOD_MORNING, Constantes.English.GOOD_BYE, Constantes.English.WELL_DONE],
        [LangueEn(), Periode.APRES_MIDI, Constantes.English.GOOD_AFTERNOON, Constantes.English.GOOD_BYE, Constantes.English.WELL_DONE],
        [LangueEn(), Periode.SOIR, Constantes.English.GOOD_EVENING, Constantes.English.GOOD_BYE, Constantes.English.WELL_DONE],
        [LangueEn(), Periode.NUIT, Constantes.English.GOOD_NIGHT, Constantes.English.GOOD_BYE, Constantes.English.WELL_DONE],
        [LangueFr(), Periode.DEFAULT, Constantes.Francais.BONJOUR, Constantes.Francais.AU_REVOIR, Constantes.Francais.BIEN_DIT],
        [LangueFr(), Periode.MATIN, Constantes.Francais.BONJOUR, Constantes.Francais.AU_REVOIR, Constantes.Francais.BIEN_DIT],
        [LangueFr(), Periode.APRES_MIDI, Constantes.Francais.BONJOUR, Constantes.Francais.AU_REVOIR, Constantes.Francais.BIEN_DIT],
        [LangueFr(), Periode.SOIR, Constantes.Francais.BONSOIR, Constantes.Francais.AU_REVOIR, Constantes.Francais.BIEN_DIT],
        [LangueFr(), Periode.NUIT, Constantes.Francais.BONSOIR, Constantes.Francais.AU_REVOIR, Constantes.Francais.BIEN_DIT],
    ])
    def test_palindrome(self, langue, periode, bonjour, au_revoir, bien_dit):
        palindrome = "kayak"

        ohce = OhceBuilder().langue_defini(langue).periode_defini(periode).build()
        resultat = ohce.palindrome(palindrome)

        self.assertIn(bonjour + palindrome + bien_dit + au_revoir, resultat)

    def test_non_palindrome(self):
        langue = LangueSpy()
        ohce = OhceBuilder().langue_defini(langue).build()

        ohce.palindrome("Cameron")

        self.assertEqual(0, langue.nb_bien_dit)

if __name__ == '__main__':
    unittest.main()
