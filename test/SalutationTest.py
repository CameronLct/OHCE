import unittest

from parameterized import parameterized

from src.Langue.LangueEn import LangueEn
from src.Langue.LangueFr import LangueFr
from src.Periode import Periode
from src.Langue.Constantes import Constantes
from OhceBuilder import OhceBuilder


class SalutationTest(unittest.TestCase):
    @parameterized.expand(
        [
            [LangueEn(), Periode.DEFAULT, Constantes.English.HELLO],
            [LangueEn(), Periode.MATIN, Constantes.English.GOOD_MORNING],
            [LangueEn(), Periode.APRES_MIDI, Constantes.English.GOOD_AFTERNOON],
            [LangueEn(), Periode.SOIR, Constantes.English.GOOD_EVENING],
            [LangueEn(), Periode.NUIT, Constantes.English.GOOD_NIGHT],
            [LangueFr(), Periode.DEFAULT, Constantes.Francais.BONJOUR],
            [LangueFr(), Periode.MATIN, Constantes.Francais.BONJOUR],
            [LangueFr(), Periode.APRES_MIDI, Constantes.Francais.BONJOUR],
            [LangueFr(), Periode.SOIR, Constantes.Francais.BONSOIR],
            [LangueFr(), Periode.NUIT, Constantes.Francais.BONSOIR],
        ])
    def test_bonjour(self, langue, periode, retour):
        ohce = OhceBuilder().langue_defini(langue).periode_defini(periode).build()
        resultat = ohce.bonjour()

        self.assertEqual(retour, resultat)

    @parameterized.expand(
        [
            [LangueEn(), Periode.DEFAULT, Constantes.English.GOOD_BYE],
            [LangueFr(), Periode.DEFAULT, Constantes.Francais.AU_REVOIR],
        ])
    def test_au_revoir(self, langue, periode, retour):
        ohce = OhceBuilder().langue_defini(langue).periode_defini(periode).build()
        resultat = ohce.au_revoir()

        self.assertEqual(retour, resultat)

if __name__ == '__main__':
    unittest.main()