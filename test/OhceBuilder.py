from src.Ohce import Ohce
from src.Periode import Periode
from LangueStub import LangueStub


class OhceBuilder():
    def __init__(self):
        self.langue = LangueStub()
        self.periode = Periode.DEFAULT

    def build(self):
        return Ohce(self.langue, self.periode)

    def default(self):
        return OhceBuilder.build(self)

    def langue_defini(self, langue):
        self.langue = langue
        return self

    def periode_defini(self, periode):
        self.periode = periode
        return self