class Ohce:
    def __init__(self, langue, periode):
        self.langue = langue
        self.periode = periode

    def bien_dit(self):
        return self.langue.bien_dit()

    def bonjour(self):
        return self.langue.bonjour(self.periode)

    def au_revoir(self):
        return self.langue.au_revoir()

    def miroir(self, chaine):
        return chaine[::-1]

    def palindrome(self, palindrome):
        miroir = self.miroir(palindrome)
        return self.bonjour() + miroir + (self.bien_dit() if miroir == palindrome else "") + self.au_revoir()