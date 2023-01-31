from src.Ohce import Ohce
from LangueStub import LangueStub


class OhceBuilder():
    def __init__(self):
        self.langue = LangueStub()

    def build(self):
        return Ohce(self.langue)

    def default(self):
        return OhceBuilder.build(self)

    def langue_defini(self, langue):
        self.langue = langue
        return self