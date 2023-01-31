import unittest
import locale
import datetime

from parameterized import parameterized

from src.Langue.LangueEn import LangueEn
from src.Langue.LangueFr import LangueFr
from OhceBuilder import OhceBuilder
from LangueSpy import LangueSpy
from src.Periode import Periode
from src.Langue.Constantes import Constantes

class PalindromeTest(unittest.TestCase):

    @parameterized.expand([
        [LangueEn(), Periode.MATIN, Constantes.English.GOOD_EVENING, Constantes.English.GOOD_BYE,
         Constantes.English.WELL_DONE],
    ])
    def test_default(self, langue, periode, bonjour, au_revoir, bien_dit):
        palindrome = "kayak"

        ohce = OhceBuilder().langue_defini(langue).periode_defini(periode).build()

        resultat = ohce.palindrome(palindrome)

        self.assertIn(bonjour + palindrome + bien_dit + au_revoir, resultat)


        langue_spy = LangueSpy()
        ohce = OhceBuilder().langue_defini(langue_spy).build()

        ohce.palindrome("Cameron")

        self.assertEqual(0, langue_spy.nb_bien_dit)

        locale_language, locale_encoding = locale.getlocale()
        current_time = datetime.datetime.now().time()
        chaine = input('Veuillez entrer une chaine à tester : ')

        if locale_language == 'fr_FR':
            langue_locale = LangueFr()
            if current_time >= datetime.time(6) and current_time < datetime.time(18):
                periode_locale = Periode.MATIN
                bonjour_locale = "Bonjour"
            else:
                periode_locale = Periode.NUIT
                bonjour_locale = "Bonsoir"
            au_revoir_locale = "Au revoir"
            bien_dit_locale = "Bien dit"
        else:
            langue_locale = LangueEn()
            if current_time >= datetime.time(6) and current_time < datetime.time(12):
                periode_locale = Periode.MATIN
                bonjour_locale = "Good Morning"
            elif current_time >= datetime.time(12) and current_time < datetime.time(18):
                periode_locale = Periode.APRES_MIDI
                bonjour_locale = "Good Afternoon"
            elif current_time >= datetime.time(18) and current_time < datetime.time(22):
                periode_locale = Periode.SOIR
                bonjour_locale = "Good Evening"
            else:
                periode_locale = Periode.NUIT
                bonjour_locale = "Good Night"
            au_revoir_locale = "Good bye"
            bien_dit_locale = "Well done"

        ohcebuild = OhceBuilder().langue_defini(langue_locale).periode_defini(periode_locale).build()

        result = ohcebuild.palindrome(chaine)

        self.assertIn(bonjour_locale + chaine + bien_dit_locale + au_revoir_locale, result)


if __name__ == '__main__':
    unittest.main()