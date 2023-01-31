from src.Langue.Constantes import Constantes
from src.Periode import Periode


class LangueFr:

    def bonjour(self, periode):
        return Constantes.Francais.BONSOIR \
            if periode in (Periode.SOIR, Periode.NUIT) \
            else Constantes.Francais.BONJOUR

    def bien_dit(self):
        return Constantes.Francais.BIEN_DIT

    def au_revoir(self):
        return Constantes.Francais.AU_REVOIR
