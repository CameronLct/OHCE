from src.Langue.Constantes import Constantes
from src.Periode import Periode


class LangueEn:

    def bonjour(self, periode):
        match periode:
            case Periode.MATIN:
                return Constantes.English.GOOD_MORNING
            case Periode.APRES_MIDI:
                return Constantes.English.GOOD_AFTERNOON
            case Periode.SOIR:
                return Constantes.English.GOOD_EVENING
            case Periode.NUIT:
                return Constantes.English.GOOD_NIGHT

        return Constantes.English.HELLO

    def bien_dit(self):
        return Constantes.English.WELL_DONE

    def au_revoir(self):
        return Constantes.English.GOOD_BYE
